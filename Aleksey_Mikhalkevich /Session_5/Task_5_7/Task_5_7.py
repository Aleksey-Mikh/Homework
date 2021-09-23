"""
1)Run the module modules/mod_a.py. Check its result. Explain why does this happen.

When we launch mod_a.py the file is executed line by line.
In the first line, mod_c is imported, after that the file mod_c.py will be executed.

In this file, the variable x is declared and the value 5 is assigned to it.
Line 1 has been executed and starts executing line 2 - import mod_b.

In the mod_b.py in the first line is the import of mod_c, but the execution of mod_c.py
does not happen again because this file has already been executed and the
data from it is already in the global namespace.
In line 4 of the mod_b file, the variable x is redefined from the mod_c file.

The execution of line 2 in the mod_a.py ends and line 5 is executed with output
to the console the values of the variable x from mod_c.
The console prints 5, but this is the value that was obtained from the mod_b file,
and not the original value of the variable x that was declared in mod_c.


2)Try to change x to a list [1,2,3]. Explain the result.

The number 5 was output to the console, since in the mod_b file
we redefine x and the list is replaced with the value 5


3)Try to change import to from x import * where x - module names. Explain the result.

Nothing has changed
"""
