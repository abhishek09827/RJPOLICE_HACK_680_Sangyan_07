"use strict";
//elements
let btn = document.querySelector(".submit-btn");
let usernameInput = document.querySelector(".login--username");
let passwordInput = document.getElementById("exampleInputPassword1");
let wrongPassDiv = document.getElementById("wrong-pass-text");

btn.addEventListener("click", function () {
  if (usernameInput.value === "user" && passwordInput.value === "1111") {
    window.open("inputPage/mainPage.html", "_top");
  } else {
    wrongPassDiv.classList.remove("opacity-0");
  }
});
