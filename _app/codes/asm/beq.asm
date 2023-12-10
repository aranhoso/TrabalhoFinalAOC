.data
ln: .asciiz "\n"

.text
.globl main
main:
	# vamos contar ateh 10
	li $t0, 0

loop:
	# Se t0 == 10, sai do loop
	beq $t0, 10, end

	add $t0, $t0, 1

	# imprime o valor de t0
	li $v0, 1
	move $a0, $t0
	syscall

	# imprime uma quebra de linha
	li $v0, 4
	la $a0, ln
	syscall

	# volta para o inicio do loop
	j loop

end:
	# termina o programa
	li $v0, 10
	syscall