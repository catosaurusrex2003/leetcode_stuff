function mergeAlternately(word1: string, word2: string): string {
    let final: string = "";
    let i = 0;
    const n = Math.min(word1.length, word2.length);
    for (; i <n ; i++) {
        final += word1[i];
        final += word2[i];
    }
    if (n == word1.length) {
        final += word2.slice(i,word2.length)
    }
    else{
        final += word1.slice(i,word1.length)
    }
    return final
};
