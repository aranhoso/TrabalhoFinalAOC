// Para esse exemplo, vamos utilizar a instrução goto para parar um loop de repetição.
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	printf("Hello! I'm here to count to 10!\n");
	int i = 0;
	while (1) {
		printf("%d\n", i);
		i++;
		if (i >= 10) goto label_to_leave;
	}

	label_to_leave:

	printf("We are done! Bye!\n");
	return 0;
}