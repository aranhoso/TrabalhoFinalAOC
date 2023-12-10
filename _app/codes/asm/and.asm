.data
and_str: .asciiz " & "
equal: .asciiz " = "
true: .asciiz " (true)"
false: .asciiz " (false)"
ln: .asciiz "\n"

.text
.globl main
main:
	li $t0, 0
	li $t1, 1

and_check:
	and $t2, $t0, $t1

	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, and_str
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

	beq $t2, $zero, and_false

	li $v0, 4
	la $a0, true
	syscall

	li $v0, 4
	la $a0, ln
	syscall
	
	j end

and_false:
	li $v0, 4
	la $a0, false
	syscall

	li $v0, 4
	la $a0, ln
	syscall
	
	j end

end:
	li $v0, 10
	syscall