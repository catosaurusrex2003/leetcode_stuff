function countPrimes(n: number): number {
  if (n <= 2) return 0;
  const isPrime: Boolean[] = new Array(n).fill(true);
  isPrime[0] = isPrime[1] = false;
  for (let i = 2; i * i < n; i++) {
    if (isPrime[i]) {
      for (let j = i * i; j < n; j += i) {
        isPrime[j] = false;
      }
    }
  }
  return isPrime.filter((val) => val).length;
}

function factorial(n: number): number {
  let fact = 1;
  for (let i = n; i > 0; i--) {
    fact *= i;
  }
  return fact;
}

const MOD = 1e9 + 7;

function numPrimeArrangements(n: number): number {
  const numPrimes = countPrimes(n);
  console.log(numPrimes);
  return (factorial(n - numPrimes) * factorial(numPrimes))%MOD;
}

const meow = numPrimeArrangements(15);
console.log(meow);

// [ ,-,-, ,-, ,-, , ,  ,--,  ,--,  ,  ]
// [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
// [1,2,5,4,3]
// [ ,2,3, ,5]
// [ , , , , ]