//Switch Light/Dark Mode
let stylemode = document.cookie;
let stylelink = document.getElementById('style');

toolbar = document.getElementById('toolbar')
menuButton = document.getElementById('menuButton')

let pets = document.getElementById('pets')

if (stylemode === 'dark') {
    stylelink.href = 'css/dark.css';
    pets.src = 'img/pets_dark.png';
} else {
    stylelink.href = 'css/light.css';
    pets.src = 'img/pets_light.png';
    document.cookie = 'light';
}

function switchmode() {
    if (stylemode === 'light') {
        stylemode = 'dark';
        stylelink.href = 'css/dark.css';
        document.cookie = 'dark';
        pets.src = 'img/pets_dark.png';
        toolbar.style.backgroundColor = '#ffffff';
        menuButton.style.backgroundColor = '#ffffff';
    } else {
        stylemode = 'light';
        stylelink.href = 'css/light.css';
        document.cookie = 'light';
        pets.src = 'img/pets_light.png';
        toolbar.style.backgroundColor = '#333333';
        menuButton.style.backgroundColor = '#333333';
    }
}

//Show/Hide Toolbar
function showhide() {
    let toolbarbuttons = document.getElementById('buttons');

    if (document.cookie === 'light') {
        if (toolbarbuttons.style.display === 'none') {
            toolbarbuttons.style.display = 'block';
            toolbar.style.backgroundColor = '#333333';
            menuButton.style.backgroundColor = '#333333';
        } else {
            toolbarbuttons.style.display = 'none';
            toolbar.style.backgroundColor = '#ffffff';
            menuButton.style.backgroundColor = '#333333';
        }
    } else if (document.cookie === 'dark') {
        if (toolbarbuttons.style.display === 'none') {
            toolbarbuttons.style.display = 'block';
            toolbar.style.backgroundColor = '#ffffff';
            menuButton.style.backgroundColor = '#ffffff';
        } else {
            toolbarbuttons.style.display = 'none';
            toolbar.style.backgroundColor = '#333333';
            menuButton.style.backgroundColor = '#ffffff';
        }
    }
}

function coin() {
    const randomNumber = Math.floor(Math.random() * 2);
    if (randomNumber === 0) {
        document.getElementById('coinImg').src = 'img/coin_top.png';
    } else {
        document.getElementById('coinImg').src = 'img/coin_bottom.png';
    }
}