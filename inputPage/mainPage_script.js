"use strict";
let loader = document.querySelector(".loader-wrapper");

window.addEventListener("load", function () {
  this.setTimeout('loader.style.display = "none";', 100000);
});
