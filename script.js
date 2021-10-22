//if statement

// if ( 3 < 1) {
//     console.log('Link');
// } 
// else if ( 2 == 2) {
//     console.log('Gannon');
// }      
// else {
//     console.log("Zelda");
// }

// Equal Sign 

// =   =>  value or assignment  x = 5
// ==   => comparison ( 2 == "2")  - integer can equal a string
// ===   => Must Equal   ( 2 === "2") NO   can only both be string or integers. STRICT ( 2 === 2 )   most liekly wont use this in lerning stuff. Robert has seen some in his work. 


// FUNctions are FUN
//function is a block of Code   something we do over and over.  tying shoes. do over and over. 


// function add(number1, number2) {
//     // let number1 = 5
//     // let number2 = 7
//     // console.log(number1 + number2);
//     return number1 + number2
// }

// // console.log(add(5, 7))
// let result = add(5, 7)
// console.log(result);


//Undefined or NULL

// let x;
// // let x = null
// x = 'Coding is Fun;
// console.log(x);

//-----------------------------

//Print odds 1-20
//using a loop write code that will console.log all of the odd valuesfrom 1 to 20

//SudoCode
//allows us to break down something. 

//Print 1-20
//we need a loop. 
//console.log
//we need odd values

// for (i = 0; i < 20; i++ ) {
//     if ( i % 5 == 0 ) (
//         console.log(i)
//     )
// }
// % is modulous. divisible by

//   !=  does not equal

//--------------------------------------

// Sigma LOOP CHALLENGE. 
//write a code that will add all the values from 1 to 100 onto some variable sum and at the end console.log the result of 1+2+3+... 98+99+100.  We should get 5050 at the end. 

//sum 1 - 100  - Done (ran properties with for)
//variable - Done (variable has been declared  with (let sum = 0))
//console.log each value - done
//sum == 5050

// let sum = 0
// // for ( i = 0; 1 <= 100; i++)
// for ( i = 0; i < 101; i++) {
//     console.log(i);
//     // sum = sum + i
//     sum += i
// }
// console.log(sum);

//-----------------------------

//ARRAY REVERSE
//write a function that will reverse the values of an array and return them. 

// var arr = [ "a", "b", "c", "d", "e",]

// write a function - done
// Reverse the Array
// console.log

function reverseArr(arr) {
    for ( i = 0; i < arr.length/2; i++) {
        temp = arr[i]
        arr[i] = arr[arr.length-1-i]
        arr[arr.length-1-i] = temp
    }
    return arr
}
let result = reverseArr([ "a", "b", "c", "d", "e",])
console.log(result);