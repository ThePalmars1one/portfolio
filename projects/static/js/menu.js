var btn = document.getElementsByClassName('menu_button')[0];
var options = document.getElementsByClassName('menu_options')[0];
var icons = document.getElementsByClassName('menu_icons')[0];
var container = document.getElementsByClassName('menu_container')[0];
var logo = document.getElementsByClassName('menu_logo')[0]


btn.addEventListener('click', function(){
    options.classList.toggle('active')
    icons.classList.toggle('active')
    container.classList.toggle('active')
    container.style.transition = "top 0.1s ease-in-out";

    if (!options.classList.contains('active')) {
        btn.setAttribute('src', './static/images/menu.svg');
        logo.setAttribute('src', './static/images/logo.svg');
    } else {
        btn.setAttribute('src', './static/images/menu_deploy.svg');
        logo.setAttribute('src', './static/images/logo_deploy.svg');
    }
})
