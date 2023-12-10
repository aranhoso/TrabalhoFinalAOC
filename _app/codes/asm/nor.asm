# Considera-se qualquer valor maior que 0 como true, caso contrário, false.
.data
not_str: .asciiz "! "
or_str: .asciiz " || "
equal: .asciiz " = "
true: .asciiz "(true)\n"
false: .asciiz "(false)\n"

.text
.globl main
main:
	li $t0, 0
	li $t1, 1
	li $t2, 1

check_01:
	nor $t3, $t0, $t1

	li $v0, 4
	la $a0, not_str
	syscall

	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, or_str
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, equal
	syscall

	li $v0, 1
	move $a0, $t3
	syscall

	ble $t3, $zero, false_01
	li $v0, 4
	la $a0, true
	syscall

	j check_12

false_01:
	li $v0, 4
	la $a0, false
	syscall

check_12:
	nor $t3, $t1, $t2

	li $v0, 4
	la $a0, not_str
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, or_str
	syscall

	li $v0, 1
	move $a0, $t2
	syscall

	li $v0, 4
	la $a0, equal
	syscall

	li $v0, 1
	move $a0, $t3
	syscall

	ble $t3, $zero, false_12
	li $v0, 4
	la $a0, true
	syscall

	j end

false_12:
	li $v0, 4
	la $a0, false
	syscall

end:
	li $v0, 10
	syscall