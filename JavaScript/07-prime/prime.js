"use strict";
function isPrime(num)
    {
        for (var i = 2; i < num; i ++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }
    function helloWorld(num)
    {
        if(isPrime(num))
        {
            console.log("it's prime!");
        }
        else
        {
            console.log("it's not prime");
        }
    } 