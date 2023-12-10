.text
.data
nl: .asciz "\n"
plus: .asciz " + "
equals: .asciz " = "

.globl main
main:
	li $t0, 3
	li $t1, 10 # Utilizaremos apenas $t0 e $t2 para fazer a soma, $t1 sera o valor a ser impresso

sumi:
	addi $t2, $t0, 10

print:
	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, plus
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, equals
	syscall

	li $v0, 1
	move $a0, $t2
	syscall

	li $v0, 4
	la $a0, nl
	syscall

	li $v0, 10
	syscall