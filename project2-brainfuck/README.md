## Usage:
First compile the program with your favourite C compiler,

**Example using gcc:**
```shell
gcc brainfuck.c -o <OUTPUT PROGRAM NAME>
```
then run the final program interpreter using:
```shell
./brainfuck "<YOUR COMMANDS>"
```

**Example Usage:** (Assuming output program name to be brainfuck)
```bash
./brainfuck "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
```
This will **output:**
```
Hello World!
```

