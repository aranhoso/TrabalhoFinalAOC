.data
ln: .asciiz "\n"

.text
.globl main
main:
	# Iniciando t0 com 0
	li $t0, 0

loop:
	addi $t0, $t0, 1

	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, ln
	syscall

	# Pula para o início do loop se t0 != 10
	bne $t0, 10, loop

end:
	# Termina o programa
	li $v0, 10
	syscall