#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int a, b;
	a = 10;
	b = 20;
	printf("a is ");
	if (a < b) {
		printf("less than ");
	} else {
		printf("greater than or equal to ");
	}
	printf("b\n");
	return 0;
}