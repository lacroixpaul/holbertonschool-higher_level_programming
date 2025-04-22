document.addEventListener("DOMContentLoaded", function () {
	const addItemButton = document.querySelector("#add_item");
	const myList = document.querySelector(".my_list");
  
	if (addItemButton && myList) {
	  addItemButton.addEventListener("click", function () {
		const newItem = document.createElement("li");
		newItem.textContent = "Item";
		myList.appendChild(newItem);
	  });
	}
  });
