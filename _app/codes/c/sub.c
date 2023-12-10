#include <stdio.h>
#include <stdlib.h>

int sub(int a, int b) {
	return a - b;
}

int main(void) {
	int a, b;
	a = 10;
	b = 5;
	printf("%d = ", sub(a, b));
	printf("%d - %d\n", a, b);
	return 0;
}