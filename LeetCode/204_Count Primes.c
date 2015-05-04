int countPrimes(int n) {
    bool *flag = (bool *)calloc(n + 1, sizeof(bool));
    int count = 0;
    int i, j;
    int limit = sqrt(n);
    for (i = 2; i < n; i++) {
        if (!*(flag + i)) {
            count++;
            j = i;
            while ( i <= limit && j * i <= n) {
                *(flag + j * i) = true;
                j++;
            }
        }
    }
    return count;
}
