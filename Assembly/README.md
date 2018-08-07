# Assembly

Comandos no terminal para instalar o necessário:
- <code> sudo apt-get install nasm</code>
- <code>sudo apt-get install binutils</code>
- <code>sudo apt-get install git</code>

Para baixar o repositório:
- <code>git add remote link</code>
- <code>gir add .</code>
- <code>git commit -m 'comentario'</code>
- <code>git push origin master</code>
- <code>git pull</code>

Para compilar o código assembly:
- <code> nasm -f elf codigo.asm -o objeto.o</code>
- <code>ld objeto.o -o executavel </code>
