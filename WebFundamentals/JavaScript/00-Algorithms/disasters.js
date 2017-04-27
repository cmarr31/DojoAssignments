function whatReallyHappened(){
  var disaster = ["volcano", "tsunami", "earthquake", "blizzard", "meteor"];
  var probability = [10,15,20,25,30];
  var amount = 0;
  var day = Math.floor((Math.random() * 100) + 1);

  for (var i = 0; i<probability.length; i++){
    if (day < probability[i]){
      amount++;
      console.log(disaster[i]);
      day = Math.floor((Math.random() * 100) + 1);
    }
  }
  console.log(amount);
  return true;
}
for (var i = 0; i < 200; i++){
  whatReallyHappened();
}