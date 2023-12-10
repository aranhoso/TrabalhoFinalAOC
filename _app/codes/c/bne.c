#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	int a, b;
	a = 10;
	b = 20;
	printf("a is ");
	if (a != b) { // equivalente ao bne do MIPS
		printf("not ");
	}
	printf("equal to b\n");
	return 0;
}