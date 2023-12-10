#include <stdio.h>
#include <stdlib.h>

int div(int a, int b) {
	return a / b;
}

int mod(int a, int b) {
	return a % b;
}

int main(int argc, char *argv[]) {
	int x, y, z;
	x = 10;
	y = 3;
	z = div(x, y);
	printf("%d / %d = %d\n", x, y, z);
	z = mod(x, y);
	printf("%d %% %d = %d\n", x, y, z);
	return 0;
}