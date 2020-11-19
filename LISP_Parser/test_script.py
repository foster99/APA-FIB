import sys
from antlr4 import *
from myLispGrammarLexer import myLispGrammarLexer as mylexer
from myLispGrammarParser import myLispGrammarParser as myparser
from myLispGrammarVisitor import myLispGrammarVisitor as myvisitor

input_stream = InputStream(input('? '))

lexer = mylexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = myparser(token_stream)
tree = parser.root() 

visitor = myvisitor()
visitor.visit(tree)