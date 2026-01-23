document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.querySelector(".toggle-password");
    const passwordInput = document.getElementById("senha");
    const icon = toggleButton.querySelector("i");

    toggleButton.addEventListener("click", () => {
        passwordInput.type =
            passwordInput.type === "password" ? "text" : "password";

        icon.classList.toggle("fa-eye");
        icon.classList.toggle("fa-eye-slash");
    });
});
