nasm -f elf codigo.asm -o objeto.o
ld objeto.o -o executavel
./executavel