var modalZakaz = document.getElementById("myZakazModal");
var zakazBtn = document.getElementById("zakaz-button");
var span3 = document.getElementsByClassName("close-zakaz")[0];

// Open modal for Orders after selecting
zakazBtn.onclick = function () {
    modalZakaz.style.display = "block"
}
span3.onclick = function () {
    modalZakaz.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modalZakaz) {
        modalZakaz.style.display = "none";
    }
}
