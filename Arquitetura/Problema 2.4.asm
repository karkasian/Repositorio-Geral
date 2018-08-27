;ARQUITETURA: Problema 2.4
;Desenvolvido por:     Jhordan Silveira de Borba
;E-mail:               jhordandecacapava@gmail.com
;Website:              https://sapogithub.github.io
;Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/tree/master/Arquitetura
;2018

;Com comentários
.org 0x0FA
    .word 0x19		;Guardamos o valor 25 (decimal) em 0FA

.org 0x000
    LOAD M(0x0FA)	;Copiamos o conteúdo de 0FA para AC
    STOR M(0x0FB)	;Passamos o conteúdo de AC para 0FB
    LOAD M(0x0FA)	;Copiamos o conteúdo de 0FA para AC
    JUMP+ M(0x08D,0:19) ;Se o conteúdo em AC é positivo, vamos para a metade esquerda de 08D

.org 0x08D		;Começamos a guardar em 08D
    LOAD -M(0x0FA)	;Carregamos o conteúdo de 0FA com sinal invertido
    STOR M(0x0FB)	;Guardamos o conteúdo de AC em 0FB
    JUMP M(0x400,0:19)	;Pulamos para o endereço 1024

;Sem comentários
.org 0x0FA
    .word 0x19		

.org 0x000
    LOAD M(0x0FA)
    STOR M(0x0FB)
    LOAD M(0x0FA)
    JUMP+ M(0x08D,0:19)

.org 0x08D
    LOAD -M(0x0FA)
    STOR M(0x0FB)
    JUMP M(0x400,0:19)
