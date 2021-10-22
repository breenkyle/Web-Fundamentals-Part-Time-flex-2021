// Write code that will go through each number from 1 to 100  - DONE!
// For each number that is a multiple of 3, print "Fizz" - DONE
// For each number that is a multiple of 5, print "Buzz" - DONE
// (SHOULD BE 2ND THING, MORE SPECFIC) For numbers which are a multiple of both 3 and 5, print "FizzBuzz" - PHEW DONE. duh math....
// All other numbers should just print normally - DONE

for (i = 1; i < 101; i++ ) 
    if ( i % 15 == 0 ) {
            console.log("Fizzbuzz")
}  else if ( i % 3 == 0 ) {
            console.log("Fizz")
    }

    else if ( i % 5 == 0 ) {
        console.log("Buzz");
}
    else {
        (console.log(i)
        )
    }  
    
    
