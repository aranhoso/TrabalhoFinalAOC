#include <stdio.h>
#include <stdlib.h>

int slt(int a, int b) {
	return (a < b) ? 1 : 0;
}

int main(int argc, char *argv[]) {
	int a, b;
	a = 5;
	b = 10;
	printf("%d = %d < %d\n", slt(a, b), a, b);
	return 0;
}