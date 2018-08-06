#Assembly

sudo apt-get install nasm

sudo apt-get install binutils

git clone link
gir add *
git commit -m 'comentario'
git push origin master
git pull

nasm -f elf codigo.asm -o objeto.o
ld objeto.o -o executavel
./executavel