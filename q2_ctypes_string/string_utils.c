#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to reverse a string in place
// Note: In C, modifying a string literal is undefined behavior, so we expect a
// mutable buffer. Returns the reversed string for convenience.
char *reverse_string(char *str) {
  if (str == NULL)
    return NULL;
  int len = strlen(str);
  int start = 0;
  int end = len - 1;
  char temp;

  while (start < end) {
    temp = str[start];
    str[start] = str[end];
    str[end] = temp;
    start++;
    end--;
  }
  return str;
}
