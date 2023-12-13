.data
    buffer: .word 20

.text
.globl main
    li $v0,8
    la $a0,buffer
    li $a1,20
    syscall
    li $v0,4
    la $a0,buffer
    syscall