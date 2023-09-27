function isUpperCase(letter: string): boolean {
  return letter === letter.toUpperCase() && letter !== letter.toLowerCase();
}

function detectCapitalUse(word: string): boolean {
  let nol: number = 0;
  for (let i = 0; i < word.length; i++) {
    if (isUpperCase(word[i])) {
        nol++;
    }
  }
  if(nol==word.length){
    return true;
  }
  else if (nol == 0){
    return true;
  }
  else if (nol==1 && isUpperCase(word[0])){
    return true
  }
  else return false;
}

// const word = "USA"; //true
const word = "leetcode"; //false

console.log(`final : ${detectCapitalUse(word)}`);
