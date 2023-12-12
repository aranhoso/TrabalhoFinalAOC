.data
texto: .asciiz "Loren ipsum dolor sit amet, consectetur adipiscing elit."

.text
.globl print
print:
	li $v0, 4
	la $a0, texto
	syscall