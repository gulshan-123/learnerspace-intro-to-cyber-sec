#include <stdio.h>
#include <stdlib.h>

#define TAPE_SIZE 30000
#define STACK_SIZE 1000

void execute_brainfuck(const char *code) {
    char tape[TAPE_SIZE] = {0};
    char *ptr = tape;
    const char *pc = code;

    int stack[STACK_SIZE];
    int stack_ptr=-1;

    while (*pc) {
        switch (*pc) {
            case '>':
                ptr++;
                break;
            case '<':
                ptr--;
                break;
            case '+':
                (*ptr)++;
                break;
            case '-':
                (*ptr)--;
                break;
            case '.':
                putchar(*ptr);
                break;
            case ',':
                *ptr = getchar();
                break;
            case '[':
                if (*ptr == 0) {
                    int depth_gul=1;
                    while(depth_gul!=0){
                        pc++;
                        if (*pc == '[') {
                            depth_gul++;
                        }
                        else if (*pc==']') {
                            depth_gul--;
                        }
                    }
                }
                else {
                    stack_ptr++;
                    stack[stack_ptr]=pc-code;
                }
                break;
            case ']':
                if (*ptr == 0) {
                    stack_ptr--;
                }
                else {
                    pc=code+stack[stack_ptr];
                }
                break;
            default:
				
                break;
        }
        ++pc;
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s \"<brainfuck code>\"\n", argv[0]);
        return 1;
    }

    execute_brainfuck(argv[1]);

    return 0;
}