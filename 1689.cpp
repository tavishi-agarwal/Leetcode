class Solution {
public:
    int minPartitions(string n) {
        int maxDigit = 0;

        for (char digit : n) {
            maxDigit = max(maxDigit, digit - '0');

            if (maxDigit == 9)
                return 9;
        }

        return maxDigit;
    }
};
