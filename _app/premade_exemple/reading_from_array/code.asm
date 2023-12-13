.data
    array: .word 20

.text
.globl main
    li $t0,8
    lw $s0,($t0)array