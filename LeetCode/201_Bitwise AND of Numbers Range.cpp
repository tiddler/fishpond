class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int diff = n - m;
        int i = 0;
        while (diff > 0) {
            diff /= 2;
            i++;
        }
        return n & ((m >> i ) << i);
    }
};