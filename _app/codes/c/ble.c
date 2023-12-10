#include <stdio.h>
#include <string.h>

int main(void) {
	int a, b;
	a = 10;
	b = 20;
	printf("a is ");
	if (a <= b) { // equivalente ao ble do MIPS
		printf("less than or equal to ");
	} else {
		printf("grather than ");
	}
	printf("b\n");
	return 0;
}