.text
.data
mod_text: .asciiz " % "
iqual: .asciiz " = "
div_text: .asciiz " / "
nl: .asciiz "\n"

.globl main
main:
	li $t0, 5 # i = 5
	li $t1, 2 # j = 2

	li $t2, 0
	li $t3, 0

do_div:
	div $t0, $t1 # i / j
	mflo $t2 # t2 = i / j
	mfhi $t3 # t3 = i % j

print_exit:
	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, div_text
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, equal
	syscall

	li $v0, 1
	move $a0, $t2
	syscall

	li $v0, 4
	la $a0, nl
	syscall

	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, mod_text
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