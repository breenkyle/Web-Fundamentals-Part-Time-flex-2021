var count = 1;
var countElement = document.querySelector("#count");

console.log(countElement);

function add1() {
    count++;
    countElement.innerText = "The Count is " + count;
    console.log(count);
}

function subtract() {
    count--;
    countElement.innerText = "The Count is " + count;
    console.log(count);
}