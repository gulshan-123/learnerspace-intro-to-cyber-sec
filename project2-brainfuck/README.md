## Usage:
First compile the program with your favourite C compiler,
eg using gcc:
```shell
gcc brainfuck.c -o <OUTPUT PROGRAM NAME>
```
then run the final program interpreter using:
```shell
./brainfuck "<YOUR COMMANDS>"
```

Example Usage:
```bash
./brainfuck "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
```
This will output:
```
Hello World!
```

