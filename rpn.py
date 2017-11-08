#!/usr/bin/env python3

import operator
import readline
#from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def foo(bar):
    return 1

def bar(foo):
    hello = foo + 6
    return hello -3
def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)
        #print(colored('Result: ', 'green'), colored(result, 'blue')
if __name__ == '__main__':
    main()

