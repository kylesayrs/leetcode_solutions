from typing import List

import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluation_stack = []
        
        for token in tokens:
            if token == "+":
                operand_one = evaluation_stack.pop()
                operand_two = evaluation_stack.pop()

                evaluation_stack.append(operand_one + operand_two)

            elif token == "-":
                operand_one = evaluation_stack.pop()
                operand_two = evaluation_stack.pop()

                evaluation_stack.append(operand_two - operand_one)

            elif token == "*":
                operand_one = evaluation_stack.pop()
                operand_two = evaluation_stack.pop()

                evaluation_stack.append(operand_one * operand_two)

            elif token == "/":
                operand_one = evaluation_stack.pop()
                operand_two = evaluation_stack.pop()

                partial_dividend = operand_two / operand_one
                if partial_dividend < 0:
                    evaluation_stack.append(math.ceil(partial_dividend))
                else:
                    evaluation_stack.append(math.floor(partial_dividend))

            else:
                evaluation_stack.append(int(token))

        return evaluation_stack.pop()
    

if __name__ == "__main__":
    #assert Solution().evalRPN(["2","1","+","3","*"]) == 9
    #assert Solution().evalRPN(["4","13","5","/","+"]) == 6
    assert Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
