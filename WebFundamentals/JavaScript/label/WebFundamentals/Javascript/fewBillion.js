var sum = 0.01;
var is10000= false;

for (var index = 1; index < 30; index++) {
  
  if (sum >= 10000.00 && is10000 === false) {
      console.log("Day " + index + " - " + sum);
      is10000 = true;
      sum*=2;
  } else {
      console.log(sum);
      sum*=2;
  }
  
}
console.log(sum);

