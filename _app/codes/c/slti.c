#include <stdio.h>
#include <stdlib.h>

int slti(int rs, int immediate) {
	if (rs < immediate) {
		return 1;
	} else {
		return 0;
	}
}

int main(int argc, char *argv[]) {
	int rs,  immediate;
	rs = 60;
	immediate = 10;
	printf("slt %d, %d = %d\n", rs, immediate, slti(rs, immediate));
	return 0;
}