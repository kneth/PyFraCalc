# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker

from calculatorLexer import calculatorLexer
from calculatorListener import calculatorListener
from calculatorParser import calculatorParser
from Fraction import Fraction


class CalculatorEvaluator(calculatorListener):
    def __init__(self):
        self.stack = []

    def exitExpr(self, ctx: calculatorParser.ExprContext):
        self.stack.append(self.stack.pop())

    def exitProduct(self, ctx: calculatorParser.ProductContext):
        if ctx.getChildCount() != 1:
            a = self.stack.pop()
            b = self.stack.pop()
            if ctx.getChild(1).getText() == "*":
                self.stack.append(a * b)
            else:
                self.stack.append(a / b)

    def exitSum_(self, ctx: calculatorParser.Sum_Context):
        if ctx.getChildCount() != 1:
            a = self.stack.pop()
            b = self.stack.pop()
            if ctx.getChild(1).getText() == "+":
                self.stack.append(a + b)
            else:
                self.stack.append(a - b)

    def exitValue(self, ctx: calculatorParser.ValueContext):
        self.stack.append(self.stack.pop())

    def exitFraction(self, ctx: calculatorParser.FractionContext):
        if ctx.getChildCount() == 1:
            self.stack.append(Fraction(int(ctx.getChild(0).getText()), 1))
        else:
            self.stack.append(
                Fraction(int(ctx.getChild(0).getText()), int(ctx.getChild(2).getText()))
            )

    def exitMain(self, ctx: calculatorParser.MainContext):
        self.stack.append(self.stack.pop())

    def getResult(self):
        return self.stack[0]


def main():
    if len(sys.argv) == 2:
        lexer = calculatorLexer(InputStream(sys.argv[1]))
        stream = CommonTokenStream(lexer)
        parser = calculatorParser(stream)
        tree = parser.main()
        evaluator = CalculatorEvaluator()
        walker = ParseTreeWalker()
        walker.walk(evaluator, tree)
        print(evaluator.getResult())
    else:
        print("Error: one argument required")


if __name__ == "__main__":
    main()
