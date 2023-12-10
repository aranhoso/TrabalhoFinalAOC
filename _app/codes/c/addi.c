#include <stdio.h>
#include <stdlib.h>

int add10(int a) { // Para diferenciar o addi do add (em C), utilizaremos o nome add10
	return a + 10;
}

int main(void) {
	int a;
	a = 3;
	printf("%d + 10 = ", a);
	printf("%d\n", add10(a));
	// Para diferenciar o addi do add (em C), utilizaremos o nome add10
	return 0;
}