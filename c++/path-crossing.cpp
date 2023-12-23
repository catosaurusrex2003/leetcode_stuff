class Solution {
public:
    bool isPathCrossing(string path) {
        unordered_set< string > visited;
        int currX = 0, currY = 0;
        visited.insert(to_string(currX)+","+to_string(currY));
        for( auto direction : path) {
            if(direction == 'N') currY++;
            if(direction == 'S') currY--;
            if(direction == 'E') currX++;
            if(direction == 'W') currX--;

            if( visited.count(to_string(currX)+","+to_string(currY))) return true;
            visited.insert(to_string(currX)+","+to_string(currY));
        }
        return false;
    }
};