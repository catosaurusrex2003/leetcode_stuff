class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int,int> track;
        for(auto &i : nums){
            track[i]++;
        }
        vector<vector<int>>finalArr;
        while(!track.empty()){
            vector<int> temporary, eraser;
            for(auto &[k, v]: track){
                temporary.emplace_back(k);
                v--;
                if(v==0) eraser.emplace_back(k);
            }
            finalArr.emplace_back(temporary);
            for(auto &i : eraser){
                track.erase(i);
            }
        }
        return finalArr;
    }
};