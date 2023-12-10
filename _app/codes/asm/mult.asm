.text
.data
astr: .ascii " * "
iqual: .ascii " = "

.globl main

main:
	li $t0, 2 # Esse eh nosso X
	li $t1, 3 # Esse eh nosso Y
	li $t2, 0 # Esse eh nosso Z

# Multiplicacao
multiply:
	mult $t0, $t1
	mfhi $t2

exit:
	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, astr
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, iqual
	syscall

	li $v0, 1
	move $a0, $t2
	syscall

	li $v0, 10
	syscall