.data
equals: .asciiz " = "
lt: .asciiz " < "
ln: .asciiz "\n"

.text
.globl main
main:
	li $t0, 5 # a = 5
	li $t1, 10 # b = 10

do_slt:
	slt $t2, $t0, $t1 # t2 = a < b

	li $v0, 1
	move $a0, $t2
	syscall

	li $v0, 4
	la $a0, equals
	syscall

	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, lt
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, ln
	syscall

end:
	li $v0, 10
	syscall