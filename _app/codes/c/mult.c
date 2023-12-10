#include <stdio.h>
#include <stdlib.h>

int mult(int a, int b) {
	return a * b;
}

int main(int argc, char *argv[]) {
	int x, y, z;
	x = 2;
	y = 3;
	z = mult(x, y);
	printf("%d * %d = %d\n", x, y, z);
	return 0;
}