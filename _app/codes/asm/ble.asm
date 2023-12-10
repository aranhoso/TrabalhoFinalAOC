.data
ln: .asciiz "\n"

.text
.globl main
main:
	li $t0, 0

loop:
	# Agora, um loop para imprimir os números de 0 a 10
	# Utilizando o ble (branch less or equal) para se manter no loop
	
	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, ln
	syscall

	add $t0, $t0, 1
	ble $t0, 10, loop # if $t0 <= 10, goto loop

	li $v0, 10
	syscall # exit