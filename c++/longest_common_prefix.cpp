class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        sort(strs.begin(),strs.end());
        int n = strs.size();
        string firstString = strs[0], lastString = strs[n-1];
        for(int i = 0 ; i < min(firstString.size(),lastString.size());i++){
            if(firstString[i] != lastString[i]){
                return ans;
            }
            ans+=firstString[i];
        }
        return ans;
    }
};