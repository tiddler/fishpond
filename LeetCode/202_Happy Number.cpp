class Solution {
public:
    bool isHappy(int n) {
        int temp = n;
        set<int> mem;

        while (mem.find(temp) == mem.end()) {
            mem.insert(temp);
            temp = 0;
            while (n != 0) {
                temp += (n % 10) * (n % 10);
                n = n / 10;
            }
            if (temp == 1) {
                return true;
            }
            n = temp;
        }
        return false;
    }
};