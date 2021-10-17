var animalImg = document.querySelector("#fav-animal");

console.log(animalImg);

function pickCat(element) {
    // console.log(element.style);
    element.style.backgroundColor = "goldenrod";
    // element.remove();
    animalImg.src = "cat.jpeg";
    // console.log("animalImg.src");
}

function pickDog(element) {
    console.log(element.classList);
    element.classList.add("btn");
    animalImg.src = "dog.jpeg";
    // console.log("animalImg.src");
}

// var h3 = document.querySelector("h3");
// h3.innerText = "New Title";


// var petImg = document.querySelector("#pet-img");
    
// function switchImg() {
//     petImg.src = "dog.jpeg";  
// }

function setActive(element) {
    element.style.backgroundColor = "#222222";
    element.style.color = "#ffffff";
}
// this below would do the same as right above//
function setActive(element) {
    element.classList.add("dark-mode");
}

function setActive(element) {
    if(element.classList.includes("dark-mode")) {
        element.innerText = "Switch to light mode";
        element.classList.remove("dark-mode");
    } else {
        element.innerText = "Switch to dark mode";
        element.classList.add("dark-mode");
    }
}
