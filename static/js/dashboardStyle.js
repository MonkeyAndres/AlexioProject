var menuBtn = document.getElementById("menu");
var menu = document.getElementById("sidebar");
var shadow = document.getElementById("shadow")

function hideMenu() {
    shadow.style.pointerEvents = "none";
    shadow.style.display = "none";
    menu.style.left = "-360px";
}

function showMenu() {
    shadow.style.pointerEvents = "all";
    shadow.style.display = "block";
    menu.style.left = "0";
}

menuBtn.addEventListener("click", showMenu);
shadow.addEventListener("click", hideMenu);