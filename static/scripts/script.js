let next = document.querySelector(".toggle-next");

let firstform = document.querySelector(".firstform");
let secondform = document.querySelector(".secondform");
let back = document.querySelector(".back");


next.onclick = () => {
    firstform.classList.remove("active");
    secondform.classList.add("active");
    back.classList.add("active");
}

/*
let loginForm = document.querySelector('.login-wrap');
let signupForm = document.querySelector('.signup-wrap');
let title = document.querySelector('title');

let signupToggleBtn = document.querySelector('#toggle-signup');
let loginToggleBtn = document.querySelector('#toggle-login');


loginToggleBtn.onclick = () => {
    signupForm.classList.remove('active');
    loginForm.classList.add('active');
    title.textContent = 'Login form';
}

signupToggleBtn.onclick = () => {
    loginForm.classList.remove('active');
    signupForm.classList.add('active');
    title.textContent = 'Signup form';
}
*/

//
