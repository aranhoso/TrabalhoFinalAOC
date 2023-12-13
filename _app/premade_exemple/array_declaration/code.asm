.data
    array: .word 20
    ...
.text
.globl main
    li $s0,10
    li $t0,4
    sw $s0, ($t0)array
...