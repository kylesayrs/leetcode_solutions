#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char * get_subsequence(char *s, int period) {
    int string_len = strlen(s);
    int subsequence_len = string_len / period + 1;
    char *subsequence = malloc(string_len * sizeof(int) + 1);
    
    int subsequence_index = 0;
    int string_index = 0;
    while(string_index < string_len) {
        subsequence[subsequence_index] = s[string_index];
        subsequence_index += 1;
        string_index += period;
    }

    return subsequence;
}

int main() {
    char string[] = "abcde";

    char *subsequence = get_subsequence(string, 2);

    printf("%s", subsequence);
}
