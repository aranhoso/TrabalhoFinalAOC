#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	int a = 0, b = 1;
	int c = a || b;
	printf("%d = %d || %d", c, a, b);
	if (c) {
		printf("(true)\n");
	} else {
		printf("(false)\n");
	}
	return 0;
}