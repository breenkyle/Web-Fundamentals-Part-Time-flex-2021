console.log("page loading...");

// index     0  1   2
var likes = [9, 12, 9];
var spans = [
    document.querySelector("#post-1"),
    document.querySelector("#post-2"),
    document.querySelector("#post-3")
];

function like(id) {
    likes[id]++;
    spans[id].innerHTML = likes[id] + "like(s)";
}

// OR this//

var likeCount1 = 9;
var likeSpan1 = document.querySelector("#post-1");

function likeCount1() {
    likeCount1++;
    likeSpan1.innerText = likeCount + " like(s)";
}


var likeCount2 = 12;
var likeSpan2 = document.querySelector("#post-2");

function likeCount2() {
    likeCount2++;
    likeSpan2.innerText = likeCount2 + " like(s)";
}


var likeCount3 = 9;
var likeSpan = document.querySelector("#post-3");

function likeCount3() {
    likeCount3++;
    likeSpan3.innerText = likeCount3 + " like(s)";
}