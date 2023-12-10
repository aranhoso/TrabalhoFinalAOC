.data
ln: .asciiz "\n"

.text
.globl main
main:
	li $t0, 0

loop:
	# Fazendo o mesmo loop de contagem ateh 10
	# Agora, ao inves de usar beq, usamos bge
	# (branch if greater than or equal) [>=]
	bge $t0, 10, end

	li $v0, 1
	move $a0, $t0
	syscall

	li $v0, 4
	la $a0, ln
	syscall

	addi $t0, $t0, 1
	j loop

end:
	li $v0, 10
	syscall