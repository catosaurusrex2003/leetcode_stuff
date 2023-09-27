function calculateSubstrings(n: number): number {
    return (n * (n + 1)) / 2;
}

function countVowelSubstrings(word: string): number {
    const vowels = new Set(["a", "e", "i", "o", "u"]);
    let final = 0;
    
    return final;
};

// const str = "aeiouu"; // 2
// const str = "unicornarihan"; // 0
// const str = "cuaieuouac"; // 7
const str = "poazaeuioauoiioaouuouaui"; // 31

console.log(str)

console.log(`final answer is : ${countVowelSubstrings(str)}`)

// console.log(calculateSubstrings());