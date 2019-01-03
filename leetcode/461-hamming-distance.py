https://leetcode.com/problems/hamming-distance/description/
class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x ^ y;
        int counter = 0;
        for (int i=0; i<32; i++) 
        {
            counter += (z & 1);
            z = (z >> 1);
        }
        return counter;
    }
};
