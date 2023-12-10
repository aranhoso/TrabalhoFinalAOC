#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int a, b;
	a = 10;
	b = 20;
	printf("a is ");
	if (a > b) { // equivalente ao bgt do MIPS
		printf("grather than ");
	} else {
		printf("less than or equal to ");
	}
	printf("b\n");
	return 0;
}