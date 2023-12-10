.data
ln: .asciiz "\n"

.text
.globl main
main:
	li $t0, 0

loop:
	# novamente fazendo um loop para imprimir os 10 primeiros números
	# mas utilizando o bgt para comparar os valores [>], devido ao bgt, o loop imprime de 0 a 10
	bgt $t0, 10, end
	li $v0, 1
	move $a0, $t0
	syscall

	# imprimindo o \n
	li $v0, 4
	la $a0, ln
	syscall

	add $t0, $t0, 1
	j loop

end:
	li $v0, 10
	syscall