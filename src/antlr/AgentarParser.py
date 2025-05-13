# Generated from /home/toni/mgr/agentar/grammar/Agentar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        3,3,44,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,59,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,70,8,6,10,6,12,
        6,73,9,6,1,7,1,7,1,7,1,7,3,7,79,8,7,1,7,0,1,12,8,0,2,4,6,8,10,12,
        14,0,4,1,0,6,9,1,0,10,11,1,0,12,13,1,0,14,17,84,0,17,1,0,0,0,2,32,
        1,0,0,0,4,34,1,0,0,0,6,39,1,0,0,0,8,45,1,0,0,0,10,49,1,0,0,0,12,
        58,1,0,0,0,14,78,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,
        0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,
        0,0,0,23,24,3,4,2,0,24,25,5,1,0,0,25,33,1,0,0,0,26,27,3,6,3,0,27,
        28,5,1,0,0,28,33,1,0,0,0,29,30,3,8,4,0,30,31,5,1,0,0,31,33,1,0,0,
        0,32,23,1,0,0,0,32,26,1,0,0,0,32,29,1,0,0,0,33,3,1,0,0,0,34,35,5,
        2,0,0,35,36,5,3,0,0,36,37,3,12,6,0,37,38,5,4,0,0,38,5,1,0,0,0,39,
        40,3,10,5,0,40,43,5,18,0,0,41,42,5,5,0,0,42,44,3,12,6,0,43,41,1,
        0,0,0,43,44,1,0,0,0,44,7,1,0,0,0,45,46,5,18,0,0,46,47,5,5,0,0,47,
        48,3,12,6,0,48,9,1,0,0,0,49,50,7,0,0,0,50,11,1,0,0,0,51,52,6,6,-1,
        0,52,59,3,14,7,0,53,59,5,18,0,0,54,55,5,3,0,0,55,56,3,12,6,0,56,
        57,5,4,0,0,57,59,1,0,0,0,58,51,1,0,0,0,58,53,1,0,0,0,58,54,1,0,0,
        0,59,71,1,0,0,0,60,61,10,6,0,0,61,62,7,1,0,0,62,70,3,12,6,7,63,64,
        10,5,0,0,64,65,7,2,0,0,65,70,3,12,6,6,66,67,10,4,0,0,67,68,7,3,0,
        0,68,70,3,12,6,5,69,60,1,0,0,0,69,63,1,0,0,0,69,66,1,0,0,0,70,73,
        1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,13,1,0,0,0,73,71,1,0,0,0,
        74,79,5,19,0,0,75,79,5,20,0,0,76,79,5,21,0,0,77,79,5,22,0,0,78,74,
        1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,15,1,0,0,0,
        7,19,32,43,58,69,71,78
    ]

class AgentarParser ( Parser ):

    grammarFileName = "Agentar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'print'", "'('", "')'", "'='", 
                     "'int'", "'float'", "'string'", "'bool'", "'*'", "'/'", 
                     "'+'", "'-'", "'=='", "'!='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "FLOAT", "STRING", 
                      "BOOL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_printStmt = 2
    RULE_variableDecl = 3
    RULE_assignment = 4
    RULE_type = 5
    RULE_expression = 6
    RULE_literal = 7

    ruleNames =  [ "program", "statement", "printStmt", "variableDecl", 
                   "assignment", "type", "expression", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ID=18
    INT=19
    FLOAT=20
    STRING=21
    BOOL=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AgentarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.StatementContext)
            else:
                return self.getTypedRuleContext(AgentarParser.StatementContext,i)


        def getRuleIndex(self):
            return AgentarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AgentarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.statement()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 263108) != 0)):
                    break

            self.state = 21
            self.match(AgentarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printStmt(self):
            return self.getTypedRuleContext(AgentarParser.PrintStmtContext,0)


        def variableDecl(self):
            return self.getTypedRuleContext(AgentarParser.VariableDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(AgentarParser.AssignmentContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = AgentarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.printStmt()
                self.state = 24
                self.match(AgentarParser.T__0)
                pass
            elif token in [6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.variableDecl()
                self.state = 27
                self.match(AgentarParser.T__0)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.assignment()
                self.state = 30
                self.match(AgentarParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = AgentarParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(AgentarParser.T__1)
            self.state = 35
            self.match(AgentarParser.T__2)
            self.state = 36
            self.expression(0)
            self.state = 37
            self.match(AgentarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(AgentarParser.TypeContext,0)


        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_variableDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDecl" ):
                listener.enterVariableDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDecl" ):
                listener.exitVariableDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl" ):
                return visitor.visitVariableDecl(self)
            else:
                return visitor.visitChildren(self)




    def variableDecl(self):

        localctx = AgentarParser.VariableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.type_()
            self.state = 40
            self.match(AgentarParser.ID)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 41
                self.match(AgentarParser.T__4)
                self.state = 42
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return AgentarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = AgentarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(AgentarParser.ID)
            self.state = 46
            self.match(AgentarParser.T__4)
            self.state = 47
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AgentarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = AgentarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AgentarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VarReferenceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AgentarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarReference" ):
                listener.enterVarReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarReference" ):
                listener.exitVarReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarReference" ):
                return visitor.visitVarReference(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class CompareExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareExpr" ):
                return visitor.visitCompareExpr(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(AgentarParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralExpr" ):
                return visitor.visitLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(AgentarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AgentarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(AgentarParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AgentarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 22]:
                localctx = AgentarParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                self.literal()
                pass
            elif token in [18]:
                localctx = AgentarParser.VarReferenceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(AgentarParser.ID)
                pass
            elif token in [3]:
                localctx = AgentarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(AgentarParser.T__2)
                self.state = 55
                self.expression(0)
                self.state = 56
                self.match(AgentarParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = AgentarParser.MulDivExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = AgentarParser.AddSubExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = AgentarParser.CompareExprContext(self, AgentarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 66
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        self.expression(5)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AgentarParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(AgentarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class BoolLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(AgentarParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolLiteral" ):
                listener.enterBoolLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolLiteral" ):
                listener.exitBoolLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolLiteral" ):
                return visitor.visitBoolLiteral(self)
            else:
                return visitor.visitChildren(self)


    class FloatLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AgentarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AgentarParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AgentarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = AgentarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = AgentarParser.IntLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(AgentarParser.INT)
                pass
            elif token in [20]:
                localctx = AgentarParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(AgentarParser.FLOAT)
                pass
            elif token in [21]:
                localctx = AgentarParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(AgentarParser.STRING)
                pass
            elif token in [22]:
                localctx = AgentarParser.BoolLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.match(AgentarParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




