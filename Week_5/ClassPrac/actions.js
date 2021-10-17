console.log("JavaScript file connected");

function message() {
    alert("Test")
}

let accept= document.querySelector('#cookie_policy')
function acceptCookies(){
    accept.remove()
}

setTimeout(function() {
    alert("This is a timed message")
}, 4s)


function searchBox(); {
    let inputVal = document.querySelector('#myInput').Value
    alert('Why did you select? ' + inputVal)
}

let numCount = 0;
let count = document.querySelector("#count") 
fucntion addFavorite(); {
    numCount++
    count.innerText = numCount
}