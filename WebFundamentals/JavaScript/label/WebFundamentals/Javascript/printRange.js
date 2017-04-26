function printRange(start, end, skip){
    var counter = start;
    while (counter < end) {
        console.log(counter);
        counter +=skip;
    }

}


printRange(2, 10, 2);