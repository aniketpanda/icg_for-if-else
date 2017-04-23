INTERMEDIATE CODE GENERATOR FOR IF-ELSE in C

Team Members:
Aarthi Vishwanathan 
Akshata R
Aniket Panda

This project generates Intermediate Code for if-else in C. The project is written in python with implementation of the ply module.

The project consists of the following modules:-
1)Lexer - "lexer.py"
2)Parser - "syntax_phase.py"
3)Abstract_Syntax_Tree - creation of node classes in a seprate module folder "AST"
4)Intermediate_Code_Generator - integrated as semantic rules within the productions of "syntax_phase.py"

Execution:
the code in question is present in "test.c".
->	python syntax_phase.py 
->	This generates the tokens for lexer, symbol table and Intermediate Code.

for AST switch to AST directory :
the code for which AST is generated is present in "foo.c".
->	python c.py foo.c -ast
->	foo.ast will have the output of the AST in terms of nodes 

