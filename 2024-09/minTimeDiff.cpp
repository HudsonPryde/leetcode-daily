#include <string>
#include <vector>
#include <algorithm>
using std::vector;
using std::string;
using std::stoi;
using std::sort;

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int n = timePoints.size();
        vector<int> mins(n);
        
        for (int i=0; i<n; i++) {
            mins[i] = (stoi(timePoints[i].substr(0,2))*60) + stoi(timePoints[i].substr(3,5));
        }

        sort(timePoints.begin(), timePoints.end());
        
        int res = 1000000;
        for (int i = 0; i < n; i++) {
            int d1 = abs(mins[i] - mins[(i+1)%n]);
            int d2 = 24*60-d1;
            int d;
            if (d1 >= d2) {
                d = d2;
            } else {
                d = d1;
            }
            
            if (res > d) {
                res = d;
            }
        }

        return res;
    }
};