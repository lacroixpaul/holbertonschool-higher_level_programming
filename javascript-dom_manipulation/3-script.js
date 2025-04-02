document.addEventListener("DOMContentLoaded", function () {
	const toggleHeader = document.querySelector("#toggle_header");
	const header = document.querySelector("header");
  
	if (toggleHeader && header) {
	  toggleHeader.addEventListener("click", function () {
		if (header.classList.contains("red")) {
		  header.classList.replace("red", "green");
		} else {
		  header.classList.replace("green", "red");
		}
	  });
	}
  });
  