let next = document.querySelector(".toggle-next");

let firstform = document.querySelector(".firstform");
let secondform = document.querySelector(".secondform");
let back = document.querySelector(".back");


next.onclick = () => {
    firstform.classList.remove("active");
    secondform.classList.add("active");
    back.classList.add("active");
}

back.onclick = () => {
    firstform.classList.add("active");
    secondform.classList.remove("active");
    back.classList.remove("active");
}