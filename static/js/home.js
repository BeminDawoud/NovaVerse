

const menuItems = document.querySelectorAll(".menu-item");
const theme = document.querySelector('#theme');
const themeModel = document.querySelector('.customized-theme');
const fontSizes = document.querySelectorAll('.choose-size span');
const colorPalette = document.querySelectorAll('.choose-color span');
const root = document.querySelector(':root');
const bg1 = document.querySelector('.bg-1');
const bg2 = document.querySelector('.bg-2');
const bg3 = document.querySelector('.bg-3');
const contacts = document.querySelectorAll(".contact");
const noMessage = document.querySelector(".no-messages");
const inputBar = document.querySelector(".input-bar");


// *******************Side-Bar*************************
// remove class active from all items
const removeActiveItem = (items) => {
	items.forEach(item => {
		item.classList.remove("active");
	})
}

// Add active class in menu-item clicked
menuItems.forEach(item => {
	item.addEventListener("click", () => {
		removeActiveItem(menuItems);
		item.classList.add("active");
		if(item.id != "notifications"){
			document.querySelector('.notifications-popup').style.display = 'none';
		} else {
			document.querySelector('.notifications-popup').style.display = 'block';
			document.querySelector('#notifications .notifications-count').style.display = 'none';
		}
	})
})


// **************** messages ********************
// Add active class in messages clicked
contacts.forEach(item => {
	item.addEventListener("click", () => {
		noMessage.style.display = 'none';
		inputBar.style.display = "block"
	})
})

/* no-message icon visibility */
contacts.forEach(item => {
	item.addEventListener("click", () => {
		removeActiveItem(contacts);
		item.classList.add("active");
	})
})

// **************** theme customization ********************
// open and close theme card
const openThemeModel = () => {
	themeModel.style.display='grid';
}
const closeThemeModel = (e) => {
	if(e.target.classList.contains('customized-theme')){
		themeModel.style.display='none';
	}
}
theme.addEventListener('click', openThemeModel);
themeModel.addEventListener('click', closeThemeModel);



// ************************ change font ********************
// remove active class
const removeFontActiveClass = () => {
	fontSizes.forEach(size => {
		size.classList.remove('active');
	})
}


fontSizes.forEach(size => {
	size.addEventListener('click', () => {
		let fontSize;
		removeFontActiveClass();
		size.classList.toggle('active');
		if(size.classList.contains('font-size-1')){
			fontSize = '10px';
			root.style.setProperty('--sticky-top-left', '5.4rem');
			root.style.setProperty('--sticky-top-right', '5.4rem');
		} else if(size.classList.contains('font-size-2')){
			fontSize = '13px';
			root.style.setProperty('--sticky-top-left', '5.4rem');
			root.style.setProperty('--sticky-top-right', '-7rem');
		} else if(size.classList.contains('font-size-3')){
			fontSize = '16px';
			root.style.setProperty('--sticky-top-left', '-2rem');
			root.style.setProperty('--sticky-top-right', '-17rem');
		} else if(size.classList.contains('font-size-4')){
			fontSize = '19px';
			root.style.setProperty('--sticky-top-left', '-5rem');
			root.style.setProperty('--sticky-top-right', '-25rem');
		} else if(size.classList.contains('font-size-5')){
			fontSize = '22px';
			root.style.setProperty('--sticky-top-left', '-10rem');
			root.style.setProperty('--sticky-top-right', '-33rem');
		}
		document.querySelector('html').style.fontSize = fontSize;
	})
})


// ************************ change color ********************
const removeActiveColorClass = () => {
	colorPalette.forEach( color => {
		color.classList.remove('active');
	})
}

colorPalette.forEach(color => {
	color.addEventListener('click', () => {
		let primaryHue;
		removeActiveColorClass();
		color.classList.toggle('active');
		if(color.classList.contains('color-1')){
			primaryHue = 210;
		} else if(color.classList.contains('color-2')){
			primaryHue = 310;
		} else if(color.classList.contains('color-3')){
			primaryHue = 620;
		} else if(color.classList.contains('color-4')){
			primaryHue = 840;
		} else if(color.classList.contains('color-5')){
			primaryHue = 6500;
		}

		root.style.setProperty('--primary-color-hue', primaryHue)
	})
})


// ************************ change background ********************

bg1.addEventListener('click', () => {
	bg2.classList.remove('active');
	bg3.classList.remove('active');
	bg1.classList.add('active');
	root.style.setProperty('--colour-primary', 'hsl(252, 30%, 100%)');
	root.style.setProperty('--colour-primary-theme', '10, 41, 73');
	root.style.setProperty('--colour-secondary', 'hsl(252, 30%, 95%)');
	document.querySelector('body').style.color = 'black';

})

bg2.addEventListener('click', () => {
	bg1.classList.remove('active');
	bg3.classList.remove('active');
	bg2.classList.add('active');
	root.style.setProperty('--colour-primary', 'hsl(213, 89%, 12%)');
	root.style.setProperty('--colour-primary-theme', '10, 41, 73');
	root.style.setProperty('--colour-secondary', 'hsl(210, 75%, 16%)');
	document.querySelector('body').style.color = 'white';

})

bg3.addEventListener('click', () => {
	bg1.classList.remove('active');
	bg2.classList.remove('active');
	bg3.classList.add('active');
	root.style.setProperty('--colour-primary', 'hsl(270, 89%, 12%)');
	root.style.setProperty('--colour-primary-theme', '32, 0, 32');
	root.style.setProperty('--colour-secondary', 'hsl(270, 89%, 16%)');
	document.querySelector('body').style.color = 'white';

	
})


/* no-message icon visibility */
