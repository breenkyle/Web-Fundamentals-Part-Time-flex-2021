console.log("page loaded...");

function addShadow(element) {
    element.classList.add("shadow");
}

function removeShadow(element) {
    element.classList.remove("shadow");
}

// function over(element) {
//     alert("mouseover");    
// }
    
// function out(element) {
//     alert("mouseout");    
// }

function over(element) {
    element.style.backgroundColor = "lime";    
}
    
function out(element) {
    element.style.backgroundColor = "silver";   
}

