
#include <stdio.h>

unsigned int asm1(unsigned int input);
unsigned int asm4(const char* input);

int main() {
  printf("asm lol\n");
  printf("asm1 %p\n", (void*)asm1(0x1b4));
  char* input = "picoCTF_fdb55";
  printf("asm4 %p\n", (void*)asm4(input));

  /*char* input = "picoCTF_fdb55";*/
  /*char* output = asm4(input);*/
  /*printf("did asm lol\n");*/
  /*printf("output: %slol\n", output);*/
  
  return 0;
}
