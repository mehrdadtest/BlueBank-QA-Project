const API_BASE_URL = "http://127.0.0.1:8000";

const loginForm = document.getElementById("login-form");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const loginButton = document.getElementById("login-button");
const loginMessage = document.getElementById("login-message");

function showMessage(message, type = "error") {
    loginMessage.textContent = message;
    loginMessage.className = `message ${type}`;
    loginMessage.hidden = false;
}

function hideMessage() {
    loginMessage.textContent = "";
    loginMessage.className = "message";
    loginMessage.hidden = true;
}

loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    hideMessage();

    const email = emailInput.value.trim();
    const password = passwordInput.value;

    loginButton.disabled = true;
    loginButton.textContent = "Signing in...";

    try {
        const response = await fetch(`${API_BASE_URL}/api/v1/auth/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            showMessage(
                data.detail || "Login failed. Please check your credentials."
            );
            return;
        }

        sessionStorage.setItem("access_token", data.access_token);
        sessionStorage.setItem("user_id", String(data.user_id));
        sessionStorage.setItem("user_email", data.email);

        window.location.replace("/dashboard.html");
    } catch (error) {
        showMessage(
            "Unable to connect to BlueBank. Please make sure the server is running."
        );
        console.error("Login request failed:", error);
    } finally {
        loginButton.disabled = false;
        loginButton.textContent = "Sign in";
    }
});