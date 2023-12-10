.data
or_str: .asciiz " || "
equal: .asciiz " = "
true: .asciiz "(true)"
false: .asciiz "(false)"
ln: .asciiz "\n"
.text

.globl main
main:
	li $t0, 0
	li $t1, 1

or_check:
	or $t2, $t0, $t1

	li $v0, 1
	move $a0, $t0
	syscall

	la $a0, or_str
	li $v0, 4
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, equal
	syscall

	beq $t2, $zero, false_or

	li $v0, 4
	la $a0, true
	syscall

	j end

false_or:
	li $v0, 4
	la $a0, false
	syscall

end:
	li $v0, 4
	la $a0, ln
	syscall

	li $v0, 10
	syscall