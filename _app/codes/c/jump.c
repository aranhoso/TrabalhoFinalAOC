// Para esse exemplo, vamos fazer um loop de contagem, mas não vamos utilizar nenhum laço de repetição. (for, while, do-while)
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	printf("Hello! I'm here to count to 10!\n");
	int i = 0;
	// introduzindo a label da repetição:
	label_loop:
	printf("%d\n", i);
	i++;
	if (i < 10) goto label_loop;

	printf("We are done! Bye!\n");

	return 0;
}