document.addEventListener("DOMContentLoaded", function () {
	const updateHeaderButton = document.querySelector("#update_header");
	const header = document.querySelector("header");
	if (updateHeaderButton && header) {
	  updateHeaderButton.addEventListener("click", function () {
		header.textContent = "New Header!!!";
	  });
	}
  });
  