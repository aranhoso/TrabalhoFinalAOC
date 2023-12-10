.data
minus: .ascii " - "
iqual: .ascii " = "
nl: .ascii "\n"

.text
.global main
main:
	li $t0, 10
	li $t1, 5
	li $t2, 0

dim:
	sub $t2, $t0, $t1 # $t2 = $t0 - $t1

print:
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
	la $a0, minus
	syscall

	li $v0, 1
	move $a0, $t1
	syscall

	li $v0, 4
	la $a0, nl
	syscall

	li $v0, 10
	syscall