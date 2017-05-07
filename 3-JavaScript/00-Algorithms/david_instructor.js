function greater (x, y, fn) {
    if (x > y) {
        fn(x);
    } else {
        fn(y);
    }
}

greater(12, 14, function (num) {
    console.log("`num` should be 14");
    console.log("num:", num);
});

function ask (question, yes, no) {
    if (question()) {
        yes();
    } else {
        no();
    }
}

ask(function () {
    return true;
}, function () {
    console.log("WORKED!");
}, function () {
    console.log("BROKE!");
});

function runDangerousFunction (dangerousFunction, callback) {
    var x = null;
    try {
        x = dangerousFunction();
        callback(null, x);
    } catch (error) {
        callback(error, null);
    }
}
runDangerousFunction(function () {
    var num = Math.random();
    if (num < 0.2) {
        throw "********* NUM CAN'T BE LESS THAN 0.2 **********";
    }
    return num;
}, function (error, num) {
    if (error) {
        console.log(error);
    } else {
        console.log("NUM:", num);
    }
});