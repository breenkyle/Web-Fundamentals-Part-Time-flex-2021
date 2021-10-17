function displayName(elementName) {
    console.log(elementName);
}

function example(element) {
    console.log("element clicked", element);
}

function turnOff(element) {
    element.innerText = "Off";
}

function hide(element) {
    element.remove();
}
