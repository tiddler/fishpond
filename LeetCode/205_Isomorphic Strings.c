bool isIsomorphic(char* s, char* t) {
    char origin[256] = {0};
    bool trans[256] = {true};
    while (*s != '\0') {
        if (origin[*s]) {
            if (origin[*s] != *t)
                return false;
        }
        else {
            if (trans[*t] == true)
                return false;
            else {
                origin[*s] = *t;
                trans[*t] = true;
            }
        }
        s++;
        t++;
    }
    return true;
}