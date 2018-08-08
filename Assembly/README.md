# Assembly

## Terminal

Comandos no terminal para instalar o necessário:
- <code> sudo apt-get install nasm</code>
- <code>sudo apt-get install binutils</code>
- <code>sudo apt-get install git</code>

Comandos no GitHub:
- Para baixar o repositório:
  - <code>git add remote link</code>
- Para enviar alterações pro repositório:
  - <code>gir add .</code>
  - <code>git commit -m 'comentario'</code>
  - <code>git push origin master</code>
- Para baixar alterações:
  - <code>git pull</code>

Para compilar o código assembly:
- <code> nasm -f elf codigo.asm -o objeto.o</code>
- <code>ld objeto.o -o executavel </code>
