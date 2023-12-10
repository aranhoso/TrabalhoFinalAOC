.text
.data
plus: .asciiz " + "
nl: .asciiz "\n"
equals: .asciiz " = "

.globl main
main:
	li $t0, 3 # a = 3

	li $t1, 4 # b = 4

sum:
	add $t2, $t0, $t1 # t2 = t0 + t1

print:
	li $v0, 1
	move $a0, $t0
	syscall
	
	la $a0, plus
	li $v0, 4
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	la $a0, equals
	li $v0, 4
	syscall

	li $v0, 1
	move $a0, $t2
	syscall

	la $a0, nl
	li $v0, 4
	syscall

	li $v0, 10
	syscall # system call to exit