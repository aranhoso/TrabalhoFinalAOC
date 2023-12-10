#include <stdio.h>
#include <stdlib.h>

int add(int a, int b) {
	return a + b;
}

int main(void) {
	int a, b;
	a = 3;
	b = 4;
	printf("%d + %d = ", a, b);
	printf("%d\n", add(a, b));
	return 0;
}