//Switch Light/Dark Mode
let stylemode = document.cookie;
let stylelink = document.getElementById('style');

let toolbar = document.getElementById('toolbar')
let menuButton = document.getElementById('menuButton')

if (stylemode === 'dark') {
    stylelink.href = '../css/dark.css';
} else {
    stylelink.href = '../css/light.css';
    document.cookie = 'light;path=/';
}

function switchmode() {
    if (stylemode === 'light') {
        stylemode = 'dark';
        stylelink.href = '../css/dark.css';
        document.cookie = 'dark;path=/';
        toolbar.style.backgroundColor = '#ffffff';
        menuButton.style.backgroundColor = '#ffffff';
    } else {
        stylemode = 'light';
        stylelink.href = '../css/light.css';
        document.cookie = 'light;path=/';
        toolbar.style.backgroundColor = '#333333';
        menuButton.style.backgroundColor = '#333333';

    }
}

//Show/Hide Toolbar
function showhide() {
    let toolbarbuttons = document.getElementById('buttons');

    if (stylemode === 'light') {
        if (toolbarbuttons.style.display === 'none') {
            toolbarbuttons.style.display = 'block';
            toolbar.style.backgroundColor = '#333333';
            menuButton.style.backgroundColor = '#333333';
        } else {
            toolbarbuttons.style.display = 'none';
            toolbar.style.backgroundColor = '#ffffff';
            menuButton.style.backgroundColor = '#333333';
        }
    } else if (stylemode === 'dark') {
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