console.log("page loaded...");

function changeText(){
    document.getElementById("profilename").innerText= 'Amy Othername';

}

//first attempts at getting buttons to remove items, figured it out starting line 42//

// function accept() {
//     var myobj = document.getElementsByClassName("card-list-item");
//     myobj.remove("card-list-item");
// }

// function accept(elementClass) {
//     var element = document.getElementsByClassName("card-list-item");
//     element.parentNode.removeChild("card-list-item");
// }


// function accept(element) {
//     var element = document. getElementsByClassName("card-list-item");
//     element. parentNode. remove("card-list-item");
//     }

// function accept(element) {
//     element.remove("card-list-item");
// }


// function accept() {
//     var myobj = document.getElementById("ToddE");
//     myobj.remove("ToddE");
// }

// function accept(elementId) {
//     var element = document.getElementById(ToddE);
//     element. parentNode. removeChild();
// }


let accept= document.querySelector('#toddE')
function acceptFriend(){
    accept.remove()
}


let decline= document.querySelector('#toddE')
function declineFriend(){
    accept.remove()
}

let accept2= document.querySelector('#philE')
function acceptFriend2(){
    accept2.remove()
}


let decline2= document.querySelector('#philE')
function declineFriend2(){
    accept2.remove()
}

//trying to get numnbers to change on connections when button accepted. //

var connectCount= 2;
var connectSpan1 = document.querySelector("#connection-requests");

function connectCount1() {
    // when accept();
    connectCount1--;
    connectSpan1.innerText = connectCount;
}