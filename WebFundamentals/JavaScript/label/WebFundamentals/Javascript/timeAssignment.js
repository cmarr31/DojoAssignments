

function time() {
    var HOUR = 8;
    var MINUTE = 50;
    var PERIOD = "AM";

        if (MINUTE < 30 && PERIOD === "AM") {
            console.log("Its just after " + HOUR + " in the morning");
        } else if (MINUTE >= 30 && PERIOD === "AM") {
            console.log("Its almost " + (HOUR+1) + " in the morning");
        } else if (MINUTE >= 30 && PERIOD === "PM") {
            console.log("Its almost " + (HOUR+1) + " in the evening");
        } else if (MINUTE < 30 && PERIOD === "PM") {
            console.log("Its just after " + HOUR + " in the evening");
    }
}

time();