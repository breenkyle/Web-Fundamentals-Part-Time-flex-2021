// Print ODDS 1-20
// Using a loop write code that will console.log all of the odd values from 1 up to 20. - DONE 

// for (i = 0; i < 20; i++ ) {
//         if ( i % 2 != 0 ) (
//             console.log(i)
//         )
//     }

//------------------------------------------------------

// Decreasing Multiples of 3 
// Using a loop write code that will console.log all of the values that are evenly divisible by 3 from 100 down to 0. - DONE

// for (i = 101; i > -1; i-- ) 
//     if ( i % 3 == 0 ) {
//         console.log(i);
//     }

//----------------------------------------------------------

// Print the sequence
// Using a loop write code that will console.log the values in this sequence 4, 2.5, 1, -0.5, -2, -3.5. - DONE

// for (var i = 4; i>-5; i-=1.5){
//     console.log(i);
// }





//----------------------------------------------------------
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


//-----------------------------------------------------------------

// Factorial
// Write code that will multiply all of the values from 1-12 onto some variable product and at the end console.log the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end.

//FINAL ANSWER 
function factorial(n){
    let answer = 1;
    if (n == 0 || n == 1){
    return answer;
    }else{
    for(var i = n; i >= 1; i--){
        answer = answer * i;
    }
    return answer;
    }  
}
let n = 12;
answer = factorial(n)
console.log(answer);
