const gridTraveller = (m: number, n: number, memo: any = {}) => {
  const key = `${Math.min(m, n)},${Math.max(m, n)}`;
  if (key in memo) return memo[key];
  if (m == 1 && n == 1) {
    return 1;
  }
  if (m == 0 || n == 0) {
    return 0;
  }
  memo[key] = gridTraveller(m - 1, n) + gridTraveller(m, n - 1);
  return memo[key];
};

console.log(gridTraveller(18,18));
