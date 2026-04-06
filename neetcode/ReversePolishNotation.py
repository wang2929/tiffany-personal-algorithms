'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.
'''
type List = List[str]
class Solution:
    def evalRPN(self, tokens: List) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isnumeric():
                stack.append(int(tokens[i]))
            elif tokens[i][1:].isnumeric():
                stack.append(0 - int(tokens[i][1:]))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]

if __name__ == '__main__':
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22