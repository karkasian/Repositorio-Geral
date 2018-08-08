.org 0x0FA
    .word 0x25

.org 0x000
    LOAD M(0x0FA)
    STOR M(0x0FB)
    LOAD M(0x0FA)
    JUMP+ M(0x08D,0:19)

.org 0x08D
    LOAD -M(0x0FA)
    STOR M(0x0FB)
    JUMP M(0x400,0:19)

#DESCRIÇÃO

1. Salvamos o número 19 (Decimal) no endereço 0FA
2. Copiamos o conteúdo de 0FA para AC
3. Copiamos o conteúdo de AC para 0FB
4. Copiamos o conteúdo de 0FA para AC
5. Se o número for não negativo apanha a próxima instrução da metade esquerda de 08D
6. Transferimos o valor contido em 0FA com sinal trocado para o AC.
7. Copiamos o conteúdo do AC para 0FB
8. Saltamos para uma posição inexistente para encerrar o programa
