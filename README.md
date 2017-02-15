# alexandermath
Python program for solving my sons' math homework puzzles

Program for solving math problems where you are asked
to find all the expressions involving all of some set of integers
and some subset of a given set of operators that evaluate to some
target value, or are greater then some value etc.

To do this we:
Build a tree that has the 5 given numbers as leaf nodes
The tree structure is randomly generated, bottom-up
by adding new nodes that reference a) two operands and
b) an operator (that can be +, -, *, /, ^
Operands can be either leaf nodes or non-leaf nodes
Eventually over time we will generate every possible
unique expression. We sort the operands and operators
in order to make a canonical form for the purpose of
eliminating duplicates.
