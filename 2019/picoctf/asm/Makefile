
all:
	gcc -m32 -c decode.c
	nasm -f elf asm1.S -o asm1.o
	nasm -f elf asm4.S -o asm4.o
	gcc -m32 asm1.o asm4.o decode.o -o out

clean:
	rm *.o out

