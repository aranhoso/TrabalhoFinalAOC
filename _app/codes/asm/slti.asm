.data
lt: .ascii " < "
ln: .ascii "\n"
equal: .ascii " = "

.text
.globl main
main:
	li $t0, 60
	li $t1, 50 # usado para a impressao apenas.

check:
	slti $t2, $t0, 50

	li $v0, 1
	move $a0, $t2
	syscall

	li $v0, 4
	la $a0, igual
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