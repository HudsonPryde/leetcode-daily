#include <vector>
#include <string>
#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        map<string, int> words;
        int pos = 0;
        while ((pos = s1.find(' ')) != string::npos) {
            string token = s1.substr(0, pos);
            words[token]++;
            s1.erase(0, pos+1);
        }
        words[s1]++;
        pos = 0;
        while ((pos = s2.find(' ')) != string::npos) {
            string token = s2.substr(0, pos);
            words[token]++;
            s2.erase(0, pos+1);
        }
        words[s2]++;
        vector<string> res;
        for (auto const& [key, val]: words) { 
            if (val == 1) {
                res.push_back(key);
            }
        }
        return res;
    }
};

int main(void) {
    cout << "hello" << endl;
    Solution s = Solution();
    vector<string> res = s.uncommonFromSentences("apple apple", "orange");
    for (const string& f: res) {
        cout << f << " " << flush;
    }
    return 0;
}