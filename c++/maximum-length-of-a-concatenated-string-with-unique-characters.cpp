class Solution {
public:
    int maxLength(vector<string>& arr) {
        sort(arr.begin(),arr.end(),[](const string&a,const string& b){
            return a.size() > b.size();
        });
        for(int i = 0 ; i < arr.size() ; i++){
            cout<<arr[i]<<endl;
        }
    }
};