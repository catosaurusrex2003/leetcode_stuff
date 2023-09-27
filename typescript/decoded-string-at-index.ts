function isNumericString(value: string) {
    return /^[0-9]$/.test(value);
}
function decodeAtIndex(s: string, k: number): string {
    let st = '';
    let i = 0;
    while (i < s.length && st.length <= k) {
        if (isNumericString(s[i])) {
            const temp = st;
            for (let j = 0; j < parseFloat(s[i]) -1; j++) {
                st += temp;
            }
        }
        else {
            st += s[i];
        }
        // console.log(`element is ${s[i]} , st is ${st}`)
        i++;
    }
    return st[k-1];
};


// console.log(`final is ${decodeAtIndex("leet2code3",10)}`) //o
// console.log(`final is ${decodeAtIndex("ha22",5)}`) //h
// console.log(`final is ${decodeAtIndex("a2345678999999999999999",1)}`) //a
// console.log(`final is ${decodeAtIndex("y959q969u3hb22odq595",222280369)}`) //a