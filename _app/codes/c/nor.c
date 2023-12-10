#include <stdio.h>
#include <stdlib.h>

void nor(int a, int b) {
	int c = !(a | b);
	printf("%d = !(%d | %d)", c, a, b);
	if (c) {
		printf("(true)\n");
	} else {
		printf("(false)\n");
	}
}

int main(int argc, char *argv[]) {
	int a = 0, b = 1, c = 1;
	nor(a, b);
	nor(b, c);
	return 0;
}