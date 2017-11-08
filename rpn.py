#!/usr/bin/env python3

def calculate(string):
	stack = list()
	for token in string.split():
		if token == '+':
			ar1 = stack.pop()
			ar2 = stack.pop()

			result =  ar1 + ar2
			stack.append(result)
		else:
			stack.append(int(token))
	

	return stack.pop()
def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()


