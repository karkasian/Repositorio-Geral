;ARQUITETURA: Soma de Vetores
;Desenvolvido por:     Jhordan Silveira de Borba
;E-mail:               jhordandecacapava@gmail.com
;Website:              https://sapogithub.github.io
;Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/tree/master/Arquitetura
;2018

;Versão comentada

.org 0x000                    ;A partir da posição 0
    loop:                     ;Vamos guardar o endereço do primeiro comando
        LOAD M(i)             ;Carregamos o endereço do elemento do vetor A
        STA M(0x003,8:19)     ;Alteramos no comando que vai carregar o valor de A (1)

        LOAD M(j)             ;Carregamos o endereço do elemento do vetor B
        STA M(0x003,28:39)    ;Alteramos no comando que vai somar o valor de B(2)

        LOAD M(k)             ;Carregamos o endereço do elemento do vetor C
        STA M(0x004,8:19)     ;Alteramos no comando que vai salvar a soma (3)

        LOAD M(A)             ;(1) - Carregamos A
        ADD M(B)              ;(2) - Somamos B
        STOR M(C)             ;(3) - Salvamos em C

        LOAD M(i)             ;Carregamos o endereço de A
        ADD M(unidade)        ;Vamos pro próximo elemento
        STOR M(i)             ;Salvamos o novo endereço

        LOAD M(j)             ;Carregamos o endereço de B
        ADD M(unidade)        ;Vamos pro próximo elemento
        STOR M(j)             ;Salvamos o novo endereço

        LOAD M(k)             ;Carregamos o endereço de C
        ADD M(unidade)        ;Vamos pro próximo elemento
        STOR M(k)             ;Salvamos o novo endereço

        LOAD M(contador)      ;Carregamos o nosso contador do loop
        ADD M(unidade)        ;Registramos +1 volta
        STOR M(contador)      ;Salvamos

        SUB M(tamanho)        ;Fazemos (contador-tamanho)
        JUMP+ M(1024,0:19)    ;Se fizemos o ultimo loop, temos 3-3=0, então
                              ;Pulamos para um endereço inexistente e encerramos
        JUMP M(loop)          ;Entramos novamente no loop

.org 100                      ;A partir da posição 100
    A:                        ;Vamos registrar onde começa nosso vetor A
        .word 1               ;E declarar os elementos
        .word 2
        .word 3
    B:                        ;Vamos registrar onde começa nosso vetor B
        .word 4               ;E declarar os elementos
        .word 5
        .word 6
    C:
        .word 0               ;Vamos registrar onde começa nosso vetor B
        .word 0               ;E declarar os elementos
        .word 0
    i:                        ;Endereço do primeiro elemento do vetor A
        .word 100
    j:                        ;Endereço do primeiro elemento do vetor B
        .word 103
    k:                        ;Endereço do primeiro elemento do vetor C
        .word 106
    unidade:                  ;Para somarmos 1
        .word 1
    contador:                 ;Contador do nosso loop
        .word 0
    tamanho:                  ;Quantidade de loops que vamos fazer
        .word 3

;Versão sem comentário

.org 0x000
    loop:
        LOAD M(i)
        STA M(0x003,8:19)

        LOAD M(j)
        STA M(0x003,28:39)

        LOAD M(k)
        STA M(0x004,8:19)

        LOAD M(A)
        ADD M(B)
        STOR M(C)

        LOAD M(i)
        ADD M(unidade)
        STOR M(i)

        LOAD M(j)
        ADD M(unidade)
        STOR M(j)

        LOAD M(k)
        ADD M(unidade)
        STOR M(k)

        LOAD M(contador)
        ADD M(unidade)
        STOR M(contador)

        SUB M(tamanho)
        JUMP+ M(1024,0:19)

        JUMP M(loop)

.org 100
    A:
        .word 1
        .word 2
        .word 3
    B:
        .word 4
        .word 5
        .word 6
    C:
        .word 0
        .word 0
        .word 0
    i:
        .word 100
    j:
        .word 103
    k:
        .word 106
    unidade:
        .word 1
    contador:
        .word 0
    tamanho:
        .word 3
