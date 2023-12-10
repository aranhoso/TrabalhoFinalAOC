# Vamos fazer a contagem de 0 a 10, utilizando jumps!
.data
ln: .asciiz "\n"
contado: .asciiz "We are done! Bye!\n"

.text
.globl main
main:
	li $t0, 0 # i = 0 (para o contador)

label_loop:
	li $v0, 1
	move $a0, $t0
	syscall # print i

	li $v0, 4
	la $a0, ln
	syscall # print \n (pula linha)

	addi $t0, $t0, 1 # i = i + 1

	bgt $t0, 10, end # se i != 11, vai para label_loop
	j label_loop

end:
	li $v0, 4
	la $a0, contado
	syscall # print "We are done! Bye!"

	li $v0, 10
	syscall