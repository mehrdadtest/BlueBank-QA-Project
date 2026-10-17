import pytest
from playwright.sync_api import sync_playwright, expect

BASE_URL = "http://127.0.0.1:8000"
LOGIN_EMAIL = "john.doe@bluebank.test"
LOGIN_PASSWORD = "BlueBank@123"


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        browser_page = browser.new_page()

        try:
            yield browser_page
        finally:
            browser.close()


@pytest.fixture
def authenticated_page(page):
    login(page)
    return page


def login(page):
    page.goto(BASE_URL)
    page.locator("#email").fill(LOGIN_EMAIL)
    page.locator("#password").fill(LOGIN_PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url(f"{BASE_URL}/dashboard.html")


def select_source_account(page):
    source_account = page.locator("#source-account")
    expect(source_account).to_be_visible()
    expect(source_account.locator("option")).to_have_count(4)
    source_account.select_option(index=1)
    return source_account


def fill_transfer_form(page, reference="PW-TEST"):
    select_source_account(page)
    page.locator("#destination-account").fill("10009999")
    page.locator("#transfer-amount").fill("10")
    page.locator("#request-reference").fill(reference)


def mock_transfer_response(page, status, body):
    page.route(
        "**/api/v1/transfers",
        lambda route: route.fulfill(
            status=status,
            content_type="application/json",
            body=body,
        ),
    )


def test_login_page_displays_required_elements(page):
    page.goto(BASE_URL)

    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#login-button")).to_be_visible()
    expect(page.locator("#login-form")).to_be_visible()


def test_login_with_invalid_password_shows_error(page):
    page.goto(BASE_URL)

    page.locator("#email").fill(LOGIN_EMAIL)
    page.locator("#password").fill("WrongPassword123!")
    page.locator("#login-button").click()

    expect(page.locator("#login-message")).to_be_visible()
    expect(page.locator("#login-message")).to_contain_text("Invalid email or password")


def test_login_with_valid_credentials_opens_dashboard(page):
    login(page)

    expect(page.locator("#accounts-container")).to_be_visible()


def test_dashboard_redirects_to_login_without_token(page):
    page.goto(f"{BASE_URL}/dashboard.html")

    expect(page).to_have_url(f"{BASE_URL}/")
    expect(page.locator("#login-form")).to_be_visible()


def test_dashboard_displays_user_accounts(authenticated_page):
    accounts_container = authenticated_page.locator("#accounts-container")
    expect(accounts_container).to_be_visible()
    expect(accounts_container.locator(".account-card").first).to_be_visible()


def test_logout_redirects_to_login_and_protects_dashboard(authenticated_page):
    authenticated_page.locator("#logout-button").click()

    expect(authenticated_page).to_have_url(f"{BASE_URL}/")
    expect(authenticated_page.locator("#login-form")).to_be_visible()

    authenticated_page.goto(f"{BASE_URL}/dashboard.html")

    expect(authenticated_page).to_have_url(f"{BASE_URL}/")
    expect(authenticated_page.locator("#login-form")).to_be_visible()


def test_account_card_displays_required_information(authenticated_page):
    account_card = authenticated_page.locator(".account-card").first

    expect(account_card).to_be_visible()
    expect(account_card.locator(".account-number")).to_be_visible()
    expect(account_card.locator(".account-number")).not_to_be_empty()
    expect(account_card.locator(".account-balance")).to_be_visible()
    expect(account_card.locator(".account-balance")).not_to_be_empty()
    expect(account_card.locator(".account-status")).to_be_visible()
    expect(account_card.locator(".account-status")).not_to_be_empty()


def test_dashboard_displays_message_when_user_has_no_accounts(page):
    page.route(
        "**/api/v1/accounts",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body="[]",
        ),
    )

    login(page)

    expect(page.locator(".account-card")).to_have_count(0)
    expect(page.locator("#dashboard-message")).to_be_visible()
    expect(page.locator("#dashboard-message")).to_contain_text(
        "No accounts were found."
    )


def test_source_account_dropdown_contains_account_numbers(authenticated_page):
    source_account = authenticated_page.locator("#source-account")

    expect(source_account).to_be_visible()

    options = source_account.locator("option")
    expect(options).to_have_count(4)

    for index in range(1, 4):
        expect(options.nth(index)).not_to_be_empty()


def test_dashboard_displays_error_when_accounts_request_fails_on_initial_load(page):
    page.route(
        "**/api/v1/accounts",
        lambda route: route.fulfill(
            status=500,
            content_type="application/json",
            body='{"detail": "Internal Server Error"}',
        ),
    )

    login(page)

    expect(page).to_have_url("http://127.0.0.1:8000/dashboard.html")
    expect(page.get_by_text("Unable to load your accounts.")).to_be_visible()


def test_dashboard_displays_error_when_accounts_server_fails(
    authenticated_page,
):
    authenticated_page.route(
        "**/api/v1/accounts",
        lambda route: route.fulfill(
            status=500,
            content_type="application/json",
            body='{"detail":"Internal server error"}',
        ),
    )

    authenticated_page.reload()

    expect(authenticated_page.locator("#dashboard-message")).to_be_visible()
    expect(authenticated_page.locator("#dashboard-message")).to_have_text(
        "Unable to load your accounts."
    )


def test_dashboard_displays_error_when_accounts_network_fails(
    authenticated_page,
):
    authenticated_page.route(
        "**/api/v1/accounts",
        lambda route: route.abort(),
    )

    authenticated_page.reload()

    expect(authenticated_page.locator("#dashboard-message")).to_be_visible()
    expect(authenticated_page.locator("#dashboard-message")).to_have_text(
        "Unable to connect to BlueBank. Please try again."
    )


def test_dashboard_redirects_to_login_when_accounts_token_is_expired(
    authenticated_page,
):
    authenticated_page.route(
        "**/api/v1/accounts",
        lambda route: route.fulfill(
            status=401,
            content_type="application/json",
            body='{"detail":"Not authenticated"}',
        ),
    )

    authenticated_page.reload()

    expect(authenticated_page).to_have_url(f"{BASE_URL}/", timeout=10000)


def test_transfer_form_displays_required_elements(authenticated_page):
    page = authenticated_page

    expect(page.locator("#transfer-form")).to_be_visible()
    expect(page.locator("#source-account")).to_be_visible()
    expect(page.locator("#destination-account")).to_be_visible()
    expect(page.locator("#transfer-amount")).to_be_visible()
    expect(page.locator("#request-reference")).to_be_visible()
    expect(page.locator("#transfer-button")).to_be_visible()
    expect(page.locator("#transfer-message")).to_be_attached()


def test_transfer_rejects_same_source_and_destination_account(
    authenticated_page,
):
    page = authenticated_page
    source_account = select_source_account(page)
    source_account_number = source_account.input_value()

    page.locator("#destination-account").fill(source_account_number)
    page.locator("#transfer-amount").fill("10")
    page.locator("#request-reference").fill("PW-TEST-015")

    transfer_requests = []
    page.on(
        "request",
        lambda request: (
            transfer_requests.append(request)
            if request.url.endswith("/api/v1/transfers") and request.method == "POST"
            else None
        ),
    )

    page.locator("#transfer-button").click()

    expect(page.locator("#transfer-message")).to_be_visible()
    expect(page.locator("#transfer-message")).to_contain_text(
        "Source and destination accounts must be different."
    )
    assert transfer_requests == []


def test_transfer_displays_error_when_required_fields_are_missing(
    authenticated_page,
):
    page = authenticated_page
    select_source_account(page)

    page.locator("#transfer-form").evaluate("(form) => form.noValidate = true")
    page.locator("#transfer-button").click()

    expect(page.locator("#transfer-message")).to_be_visible()
    expect(page.locator("#transfer-message")).to_contain_text(
        "Please complete all fields."
    )


def test_transfer_requires_source_account(authenticated_page):
    page = authenticated_page
    source_account = page.locator("#source-account")
    expect(source_account.locator("option")).to_have_count(4)
    source_account.select_option("")

    page.locator("#destination-account").fill("10009999")
    page.locator("#transfer-amount").fill("10")
    page.locator("#request-reference").fill("PW-TEST-024")

    transfer_requests = []
    page.on(
        "request",
        lambda request: (
            transfer_requests.append(request)
            if request.url.endswith("/api/v1/transfers") and request.method == "POST"
            else None
        ),
    )

    page.locator("#transfer-form").evaluate("(form) => form.noValidate = true")
    page.locator("#transfer-button").click()

    expect(page.locator("#transfer-message")).to_contain_text(
        "Please select a source account."
    )
    assert transfer_requests == []


def test_transfer_displays_api_error_and_restores_button(
    authenticated_page,
):
    page = authenticated_page
    fill_transfer_form(page, "PW-TEST-017")

    mock_transfer_response(
        page,
        400,
        '{"detail":"Insufficient funds"}',
    )

    transfer_button = page.locator("#transfer-button")
    transfer_button.click()

    expect(page.locator("#transfer-message")).to_be_visible()
    expect(page.locator("#transfer-message")).to_have_text("Insufficient funds")
    expect(transfer_button).to_be_enabled()
    expect(transfer_button).to_have_text("Transfer Money")


def test_transfer_displays_success_message_and_resets_form(
    authenticated_page,
):
    page = authenticated_page
    fill_transfer_form(page, "PW-TEST-018")

    page.route(
        "**/api/v1/transfers",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"transaction_id":98765}',
        ),
    )

    page.route(
        "**/api/v1/accounts",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=(
                '[{"account_number":"10001234","balance":880,"status":"Active"},'
                '{"account_number":"10005678","balance":500,"status":"Closed"},'
                '{"account_number":"10009012","balance":750,"status":"Blocked"}]'
            ),
        ),
    )

    page.locator("#transfer-button").click()

    expect(page.locator("#transfer-message")).to_be_visible()
    expect(page.locator("#transfer-message")).to_contain_text(
        "Transfer successful. Transaction ID: 98765"
    )

    expect(page.locator("#source-account")).to_have_value("")
    expect(page.locator("#destination-account")).to_have_value("")
    expect(page.locator("#transfer-amount")).to_have_value("")
    expect(page.locator("#request-reference")).to_have_value("")


def test_transfer_button_shows_processing_state(authenticated_page):
    page = authenticated_page

    page.evaluate("""
        () => {
            const originalFetch = window.fetch;

            window.fetch = async (url, options = {}) => {
                if (String(url).includes("/api/v1/transfers")) {
                    await new Promise(resolve => setTimeout(resolve, 1000));

                    return new Response(
                        JSON.stringify({"message": "Transfer successful"}),
                        {
                            status: 200,
                            headers: {"Content-Type": "application/json"}
                        }
                    );
                }

                return originalFetch(url, options);
            };
        }
    """)

    select_source_account(page)
    fill_transfer_form(page)

    page.get_by_role("button", name="Transfer").click()

    expect(page.get_by_role("button", name="Processing...")).to_be_disabled()


def test_transfer_displays_network_error(authenticated_page):
    page = authenticated_page
    fill_transfer_form(page, "PW-TEST-020")

    page.route("**/api/v1/transfers", lambda route: route.abort())

    transfer_button = page.locator("#transfer-button")
    transfer_button.click()

    expect(page.locator("#transfer-message")).to_contain_text(
        "Unable to connect to BlueBank. Please try again."
    )
    expect(transfer_button).to_be_enabled()
    expect(transfer_button).to_have_text("Transfer Money")


def test_transfer_redirects_to_login_when_token_is_expired(
    authenticated_page,
):
    page = authenticated_page
    fill_transfer_form(page, "PW-TEST-021")

    mock_transfer_response(
        page,
        401,
        '{"detail":"Not authenticated"}',
    )

    page.locator("#transfer-button").click()

    expect(page).to_have_url(f"{BASE_URL}/", timeout=10000)


def test_transfer_button_prevents_duplicate_submissions(authenticated_page):
    page = authenticated_page

    page.evaluate("""
        () => {
            window.__transferRequestCount = 0;
            const originalFetch = window.fetch.bind(window);

            window.fetch = async (...args) => {
                const requestUrl =
                    typeof args[0] === "string" ? args[0] : args[0].url;

                if (requestUrl.endsWith("/api/v1/transfers")) {
                    window.__transferRequestCount += 1;
                    await new Promise(resolve => setTimeout(resolve, 1500));

                    return new Response(
                        JSON.stringify({ transaction_id: 98767 }),
                        {
                            status: 200,
                            headers: { "Content-Type": "application/json" }
                        }
                    );
                }

                return originalFetch(...args);
            };
        }
    """)

    fill_transfer_form(page, "PW-TEST-022")

    transfer_button = page.locator("#transfer-button")
    transfer_button.click()

    expect(transfer_button).to_be_disabled()
    expect(transfer_button).to_have_text("Processing...")

    transfer_button.click(force=True)

    assert page.evaluate("window.__transferRequestCount") == 1


def test_transfer_clears_previous_message_on_new_submission(
    authenticated_page,
):
    page = authenticated_page

    page.evaluate("""
        () => {
            window.__transferRequestCount = 0;
            const originalFetch = window.fetch.bind(window);

            window.fetch = async (...args) => {
                const requestUrl =
                    typeof args[0] === "string" ? args[0] : args[0].url;

                if (requestUrl.endsWith("/api/v1/transfers")) {
                    window.__transferRequestCount += 1;

                    if (window.__transferRequestCount === 1) {
                        return new Response(
                            JSON.stringify({ detail: "Insufficient funds" }),
                            {
                                status: 400,
                                headers: { "Content-Type": "application/json" }
                            }
                        );
                    }

                    await new Promise(resolve => setTimeout(resolve, 1500));

                    return new Response(
                        JSON.stringify({ detail: "Insufficient funds" }),
                        {
                            status: 400,
                            headers: { "Content-Type": "application/json" }
                        }
                    );
                }

                return originalFetch(...args);
            };
        }
    """)

    fill_transfer_form(page, "PW-TEST-023")

    transfer_message = page.locator("#transfer-message")
    transfer_button = page.locator("#transfer-button")

    transfer_button.click()
    expect(transfer_message).to_contain_text("Insufficient funds")

    transfer_button.click()

    expect(transfer_message).to_be_hidden()
    expect(transfer_button).to_be_disabled()

    expect(transfer_message).to_contain_text(
        "Insufficient funds",
        timeout=5000,
    )


def test_transfer_form_accepts_zero_amount_input(authenticated_page):
    select_source_account(authenticated_page)

    amount_input = authenticated_page.locator("#transfer-amount")
    amount_input.fill("0")

    expect(amount_input).to_have_value("0")


def test_transfer_button_is_enabled_after_api_error(authenticated_page):
    page = authenticated_page
    fill_transfer_form(page, "PW-TEST-029")

    mock_transfer_response(
        page,
        400,
        '{"detail":"Insufficient funds"}',
    )

    transfer_button = page.locator("#transfer-button")
    transfer_button.click()

    expect(page.locator("#transfer-message")).to_have_text("Insufficient funds")
    expect(transfer_button).to_be_enabled()
    expect(transfer_button).to_have_text("Transfer Money")
