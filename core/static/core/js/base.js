const toggleBtn = document.getElementById("toggle-sidebar");
const sidebar = document.querySelector(".sidebar");
const mainWrapper = document.querySelector(".main-wrapper");

toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");

    if (sidebar.classList.contains("collapsed")) {
        mainWrapper.style.marginLeft = "80px";
    } else {
        mainWrapper.style.marginLeft = "230px";
    }
});
