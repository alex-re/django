$(document).ready ( function(){
    var navbar, div_navbar_bug;
    navbar = document.getElementById('top_navbar');
    div_navbar_bug = document.getElementById("navbar_bug");

    div_navbar_bug.style.height = navbar.offsetHeight+'px';
    div_navbar_bug.style.width = navbar.offsetWidth+'px';
});