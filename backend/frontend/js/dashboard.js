const API_BASE_URL = "http://127.0.0.1:8000";

const accessToken = sessionStorage.getItem("access_token");
const userEmail = sessionStorage.getItem("user_email");

const accountsContainer = document.getElementById("accounts-container");
const dashboardMessage = document.getElementById("dashboard-message");
const userEmailElement = document.getElementById("user-email");
const logoutButton = document.getElementById("logout-button");

const transferForm = document.getElementById("transfer-form");
const sourceAccountSelect = document.getElementById("source-account");
const destinationAccountInput = document.getElementById("destination-account");
const transferAmountInput = document.getElementById("transfer-amount");
const requestReferenceInput = document.getElementById("request-reference");
const transferButton = document.getElementById("transfer-button");
const transferMessage = document.getElementById("transfer-message");

let currentAccounts = [];

function showDashboardMessage(message, type = "error") {
    dashboardMessage.textContent = message;
    dashboardMessage.className = `message ${type}`;
    dashboardMessage.hidden = false;
}

function showTransferMessage(message, type = "error") {
    transferMessage.textContent = message;
    transferMessage.className = `message ${type}`;
    transferMessage.hidden = false;
}

function hideTransferMessage() {
    transferMessage.textContent = "";
    transferMessage.className = "message";
    transferMessage.hidden = true;
}

function clearSession() {
    sessionStorage.removeItem("access_token");
    sessionStorage.removeItem("user_id");
    sessionStorage.removeItem("user_email");
}

function logout() {
    clearSession();
    window.location.replace("/");
}

function formatBalance(balance) {
    const amount = Number(balance);

    if (!Number.isFinite(amount)) {
        return String(balance);
    }

    return new Intl.NumberFormat("en-US", {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(amount);
}

function createAccountCard(account) {
    const card = document.createElement("article");
    card.className = "account-card";

    const title = document.createElement("h3");
    title.textContent = "Account number";

    const number = document.createElement("p");
    number.className = "account-number";
    number.textContent = account.account_number;

    const balance = document.createElement("p");
    balance.className = "account-balance";
    balance.textContent = formatBalance(account.balance);

    const status = document.createElement("span");
    status.className = "account-status";

    const normalizedStatus = String(account.status).toLowerCase();

    if (normalizedStatus !== "active") {
        status.classList.add("inactive");
    }

    status.textContent = account.status;

    card.append(title, number, balance, status);

    return card;
}

function populateSourceAccounts(accounts) {
    sourceAccountSelect.replaceChildren();

    const defaultOption = document.createElement("option");
    defaultOption.value = "";
    defaultOption.textContent = "Select source account";
    sourceAccountSelect.appendChild(defaultOption);

    accounts.forEach((account) => {
        const option = document.createElement("option");
        option.value = account.account_number;
        option.textContent =
            `${account.account_number} — Balance: ${formatBalance(account.balance)}`;

        sourceAccountSelect.appendChild(option);
    });
}

async function loadAccounts() {
    if (!accessToken) {
        window.location.replace("/");
        return;
    }

    userEmailElement.textContent = userEmail || "";

    try {
        const response = await fetch(`${API_BASE_URL}/api/v1/accounts`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${accessToken}`
            }
        });

        if (response.status === 401) {
            logout();
            return;
        }

        if (!response.ok) {
            showDashboardMessage("Unable to load your accounts.");
            return;
        }

        const accounts = await response.json();

        currentAccounts = accounts;
        accountsContainer.replaceChildren();

        populateSourceAccounts(currentAccounts);

        if (currentAccounts.length === 0) {
            showDashboardMessage("No accounts were found.");
            return;
        }

        currentAccounts.forEach((account) => {
            accountsContainer.appendChild(createAccountCard(account));
        });
    } catch (error) {
        showDashboardMessage(
            "Unable to connect to BlueBank. Please try again."
        );

        console.error("Account request failed:", error);
    }
}

async function submitTransfer(event) {
    event.preventDefault();
    hideTransferMessage();

    if (!accessToken) {
        logout();
        return;
    }

    const sourceAccountNumber = sourceAccountSelect.value;
    const destinationAccountNumber = destinationAccountInput.value.trim();
    const amount = transferAmountInput.value;
    const requestReference = requestReferenceInput.value.trim();

    if (!sourceAccountNumber) {
        showTransferMessage("Please select a source account.");
        return;
    }

    if (!destinationAccountNumber || !amount || !requestReference) {
        showTransferMessage("Please complete all fields.");
        return;
    }

    if (sourceAccountNumber === destinationAccountNumber) {
        showTransferMessage(
            "Source and destination accounts must be different."
        );
        return;
    }

    transferButton.disabled = true;
    transferButton.textContent = "Processing...";

    try {
        const response = await fetch(`${API_BASE_URL}/api/v1/transfers`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${accessToken}`
            },
            body: JSON.stringify({
                source_account_number: sourceAccountNumber,
                destination_account_number: destinationAccountNumber,
                amount: amount,
                request_reference: requestReference
            })
        });

        const data = await response.json();

        if (response.status === 401) {
            logout();
            return;
        }

        if (!response.ok) {
            const detail = data.detail;
            const message = typeof detail === "string"
                ? detail
                : "Transfer failed. Please check your input.";

            showTransferMessage(message);
            return;
        }

        showTransferMessage(
            `Transfer successful. Transaction ID: ${data.transaction_id}`,
            "success"
        );

        transferForm.reset();

        await loadAccounts();
    } catch (error) {
        showTransferMessage(
            "Unable to connect to BlueBank. Please try again."
        );

        console.error("Transfer request failed:", error);
    } finally {
        transferButton.disabled = false;
        transferButton.textContent = "Transfer Money";
    }
}

logoutButton.addEventListener("click", logout);
transferForm.addEventListener("submit", submitTransfer);

loadAccounts();