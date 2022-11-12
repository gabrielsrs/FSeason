const navTopToggler = document.querySelector(".nav-top-toggler");
const navTop = document.querySelector(".nav-top");
const navItem = document.querySelectorAll(".nav-item")
const btnGame = document.querySelector("#submit")

function checkItem() {
    if(navItem[0].classList.contains("active")) {
        sessionStorage.lol = "active"
        sessionStorage.tft = ""
    } else if(navItem[1].classList.contains("active")) {
        sessionStorage.tft = "active"
        sessionStorage.lol = ""
    } else {
        checkSession()
    }
}

function checkSession() {
    if(sessionStorage.lol) {
        navItem[0].classList.add("active")
    } else if(sessionStorage.tft) {
        navItem[1].classList.add("active")
    } else {
        navItem[0].classList.add("active")
    }

    btnCurrentGame()
}


function changeStatus(element) {
    for(itemCount=0; itemCount < navItem.length; itemCount++){
        navItem[itemCount].classList.remove("active")
        sessionStorage.setItem(`${navItem[itemCount].children[0].children[0].title}`, "")
    }
    element.parentElement.classList.add("active")

    sessionStorage.setItem(`${element.children[0].title}`, "active")

    btnCurrentGame()
}

function btnCurrentGame() {
    if(sessionStorage.lol || navItem[0].classList.contains("active")) {
        btnGame.value = 'lol'
    } else {
        btnGame.value = 'tft'
    }
}

navTopToggler.onclick = function() {
    navTop.classList.toggle("active");
}

checkItem()
