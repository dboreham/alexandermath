
"""
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
"""

import random

debug = False
verbose = False

# The set of numbers to use in expressions
#numbers = [4,11,12,19,20]
numbers = [8,5,6,7]
# Target expression value
target = 13

# The set of arithmetic operations to use
#operators = ['+','-','*','/','**']
operators = ['+','-','*','/','**']

expressions_tested = 0
solutions_found = []
results_found = []

class Leaf:
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return self.__str__()

class Node:
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
    def __str__(self):
        # Special case for commutative operators
        if self.op == '+' or self.op == '*':
            operands = [str(self.left),str(self.right)]
            # Sort (lexical sort is ok)
            operands.sort()
            return '({}{}{})'.format(operands[0],self.op,operands[1])
        else:
            return '({}{}{})'.format(self.left,self.op,self.right)

def MakeLeafNodes():
    new_nodes = []
    # Randomly shuffle the numbers
    shuffled_numbers = numbers
    random.shuffle(shuffled_numbers)
    if debug:
        print('Shuffled numbers: ' + str(shuffled_numbers))
    # Generate leaf nodes
    for number in shuffled_numbers:
        new_leaf_node = Leaf(number)
        new_nodes.append(new_leaf_node)
    return new_nodes

def OneIteration(target):
    global expressions_tested
    foundit = False
    available_nodes = MakeLeafNodes()

    if debug:
        print('Initial Nodes: ' + str(available_nodes))

    while len(available_nodes) > 1:
        # Insert a new node using two of the available nodes
        my_left_operand = available_nodes.pop(random.randrange(len(available_nodes)))
        my_right_operand = available_nodes.pop(random.randrange(len(available_nodes)))
        my_operator = random.choice(operators)
        my_new_node = Node(my_left_operand,my_right_operand,my_operator)
        if debug:
            print('New Node: ' + str(my_new_node))
        # Add the new node into the available list
        available_nodes.append(my_new_node)

    # When we exit the loop we have one node left which is the root
    expression = str(available_nodes[0])
    # Execute the expression
    if debug:
        print('Evaluating: ' + expression)
    try:
        result = eval(expression)
        expressions_tested = expressions_tested + 1
        if debug:
            print('Result = ' + str(result))
        # Alternate tests for different forms of the puzzle:
        #if result == target and not expression in solutions_found:
        if result >= 0 and int(result) == result and not expression in solutions_found and not result in results_found:
            if verbose:
                print('Found it! ' + expression)
            print('{} = {}'.format(expression,result))
            solutions_found.append(expression)
            results_found.append(result)
            if debug:
                print('Found {} solutions after trying {}'.format(len(solutions_found),expressions_tested))
            foundit = True
    except ZeroDivisionError :
        pass
    return foundit


# Start here
while True:
    OneIteration(target)
