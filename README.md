# lalg
a tiny linear algebra compiler.

Takes a vector addition or subtraction expression or a matrix addition or subtraction and generates the corresponding C code.

E.g.,

```
>>> create_c_file("[[3 4 4 5 6][5 6 7 8 8]] + [[5 6 7 8 9][6 7 8 9 0]]", "computem.c")
```
