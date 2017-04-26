
function randomChance(tokens){
  var winningNum = Math.floor(Math.random() * 100);
  var randomNum = Math.floor(Math.random() * 100);
  var quartersWon = Math.floor(Math.random() * 50)+51;
  
  while(tokens > 0){
   
    if(randomNum === winningNum){
      tokens += quartersWon;
      return tokens;
    } else {
      tokens--;
      winningNum = Math.floor(Math.random() * 100);
      randomNum = Math.floor(Math.random() * 100);
      console.log("winning Number picked: " + winningNum);
      console.log("random Number picked: " + randomNum);
      console.log("Jackpot of quarters: " + quartersWon);
      console.log("quarters remaining: " + tokens);
    }
  }
  return 0;
}



randomChance(10);