/*
Filename: Assignment 1
Student Name: Jonathan Au
Student ID: 300827701
Date: 09/10/2023
*/

let toggleState = 0;
function toggle() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    let darkBtn = document.getElementById("darkMode");
    if (toggleState == 0) {
        darkBtn.innerHTML = "Let there be light!";
        toggleState = 1;
        console.log(to)
    } else if (toggleState == 1) {
        darkBtn.innerHTML = "Too Bright!";
        toggleState = 0;
    }
}