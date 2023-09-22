/*
done using dynamic programming.
hint: 1 2 4 8 16 32
the sum of 1's in the binary numbers are repeating and so is the pattern of placement of the 1's
*/


class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> dp(n + 1, 0);
        int sub = 1;

        for(int i = 1  ; i <= n ; i++){
            if(sub * 2 == i){
                sub = i;
            }
            dp[i] = dp[i - sub] + 1;
        }
        return dp;
    }
};