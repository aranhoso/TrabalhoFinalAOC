#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int a, b;
	a = 10;
	b = 20;
	printf("a is ");
	if (a >= b) { // equivalente ao bge do MIPS
		printf("grather than or equal to ");
	} else {
		printf("less than ");
	}
	printf("b\n");
	return 0;
}