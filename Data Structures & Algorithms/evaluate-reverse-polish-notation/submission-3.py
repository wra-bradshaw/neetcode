class Solution:
    stack: list[int]

    def __init__(self) -> None:
        self.stack = []

    def addition(self) -> None:
        x1 = self.stack.pop()
        x2 = self.stack.pop()
        self.stack.append(x2 + x1)

    def subtraction(self) -> None:
        x1 = self.stack.pop()
        x2 = self.stack.pop()
        self.stack.append(x2 - x1)

    def multiplication(self) -> None:
        x1 = self.stack.pop()
        x2 = self.stack.pop()
        self.stack.append(x2 * x1)

    def division(self) -> None:
        x1 = self.stack.pop()
        x2 = self.stack.pop()
        self.stack.append(math.trunc(x2 / x1))

    def evalRPN(self, tokens: List[str]) -> int:
        for token in tokens:
            match token:
                case "+":
                    self.addition()
                case "-":
                    self.subtraction()
                case "*":
                    self.multiplication()
                case "/":
                    self.division()
                case _:
                    self.stack.append(int(token))
        return self.stack.pop()