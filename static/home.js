
// Side-Bar
const menuItems = document.querySelectorAll(".menu-item");

// remove class active from all items
const changeActiveItem = () => {
	menuItems.forEach(item => {
		item.classList.remove("active");
	})
}

// Add active class in item clicked
menuItems.forEach(item => {
	item.addEventListener("click", () => {
		changeActiveItem();
		item.classList.add("active");
		if(item.id != "notifications"){
			document.querySelector('.notifications-popup').style.display = 'none';
		} else {
			document.querySelector('.notifications-popup').style.display = 'block';
			document.querySelector('#notifications .notifications-count').style.display = 'none';
		}
	})
})