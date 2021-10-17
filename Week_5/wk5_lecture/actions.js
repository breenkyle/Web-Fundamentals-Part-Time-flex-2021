console.log("JavaScript file connected");

function message() {
    alert(`Test`)
}

function showText(element) {
    alert(element.innerText)
}

setTimeout(function() {
    alert("This is a time message")
}, 6000)

function temp(element) {
    console.log(element.value);
    if (element.value == "Hot") {
        alert("You prefer a hot coffee")
    }
    if (element.value == "Cold") {
        alert("You prefer a cold coffee")
    }
    if (element.value == "Iced Coffee") {
        alert("You prefer a Iced Coffee")
    }
    if (element.value == "Scolding") {
        alert("You prefer a Scolding Hot Coffee")
    }
    else {
        alert("You prefer a Room Temp Coffee")
    }
}

let accept = document.querySelector('#cookie-policy')
function acceptCookies() {
    accept.remove()
}

function searchBox() {
    let inputVal = document.querySelector('#myInput').value
    alert('Why did you select ' + inputVal + ' ?')
}

let numCount = 0
let count = document.querySelector("#count")
function addFavorite() {
    numCount++
    count.innerText = numCount
}

let lap = 0
function addLaps(element) {
    lap++
    element.innerText = lap
}