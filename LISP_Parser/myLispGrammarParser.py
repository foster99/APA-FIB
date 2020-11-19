# Generated from myLispGrammar.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u00c1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\7\2H\n\2\f\2")
        buf.write("\16\2K\13\2\3\2\3\2\3\3\3\3\3\3\3\3\6\3S\n\3\r\3\16\3")
        buf.write("T\3\3\3\3\3\4\3\4\3\4\3\4\5\4]\n\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5e\n\5\3\6\3\6\3\6\3\6\5\6k\n\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\5\tv\n\t\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0091\n\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\2\2$\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BD\2\30\3\2\7\b\3\2\t\n\3\2\13\f\3\2\r\16\3\2\17\20")
        buf.write("\3\2\21\22\3\2\23\24\3\2\25\26\3\2\27\30\3\2\31\32\3\2")
        buf.write("\33\34\3\2\35\36\3\2\37 \3\2!\"\3\2#$\3\2%&\3\2\'(\3\2")
        buf.write(")*\3\2+,\3\2-.\3\2/\60\3\2\61\62\2\u00b9\2I\3\2\2\2\4")
        buf.write("N\3\2\2\2\6X\3\2\2\2\bd\3\2\2\2\nj\3\2\2\2\fl\3\2\2\2")
        buf.write("\16o\3\2\2\2\20u\3\2\2\2\22w\3\2\2\2\24z\3\2\2\2\26\u0090")
        buf.write("\3\2\2\2\30\u0092\3\2\2\2\32\u0094\3\2\2\2\34\u0096\3")
        buf.write("\2\2\2\36\u0098\3\2\2\2 \u009a\3\2\2\2\"\u009c\3\2\2\2")
        buf.write("$\u009e\3\2\2\2&\u00a0\3\2\2\2(\u00a2\3\2\2\2*\u00a4\3")
        buf.write("\2\2\2,\u00a6\3\2\2\2.\u00a8\3\2\2\2\60\u00aa\3\2\2\2")
        buf.write("\62\u00ac\3\2\2\2\64\u00ae\3\2\2\2\66\u00b0\3\2\2\28\u00b2")
        buf.write("\3\2\2\2:\u00b4\3\2\2\2<\u00b6\3\2\2\2>\u00b8\3\2\2\2")
        buf.write("@\u00ba\3\2\2\2B\u00bc\3\2\2\2D\u00be\3\2\2\2FH\5\4\3")
        buf.write("\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2K")
        buf.write("I\3\2\2\2LM\7\2\2\3M\3\3\2\2\2NO\7\3\2\2OP\5\30\r\2PR")
        buf.write("\5\32\16\2QS\5\6\4\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3")
        buf.write("\2\2\2UV\3\2\2\2VW\7\4\2\2W\5\3\2\2\2XY\7\3\2\2Y\\\5\26")
        buf.write("\f\2Z]\5\n\6\2[]\5\f\7\2\\Z\3\2\2\2\\[\3\2\2\2]^\3\2\2")
        buf.write("\2^_\7\4\2\2_\7\3\2\2\2`e\5\34\17\2ae\5\36\20\2be\5 \21")
        buf.write("\2ce\5\"\22\2d`\3\2\2\2da\3\2\2\2db\3\2\2\2dc\3\2\2\2")
        buf.write("e\t\3\2\2\2fk\5\16\b\2gk\5\20\t\2hk\7\63\2\2ik\7\64\2")
        buf.write("\2jf\3\2\2\2jg\3\2\2\2jh\3\2\2\2ji\3\2\2\2k\13\3\2\2\2")
        buf.write("lm\5\b\5\2mn\5\n\6\2n\r\3\2\2\2op\7\64\2\2pq\7\5\2\2q")
        buf.write("r\7\64\2\2r\17\3\2\2\2sv\5\24\13\2tv\5\22\n\2us\3\2\2")
        buf.write("\2ut\3\2\2\2v\21\3\2\2\2wx\7\64\2\2xy\7\6\2\2y\23\3\2")
        buf.write("\2\2z{\7\64\2\2{|\7\6\2\2|}\7\64\2\2}\25\3\2\2\2~\u0091")
        buf.write("\5$\23\2\177\u0091\5&\24\2\u0080\u0091\5(\25\2\u0081\u0091")
        buf.write("\5*\26\2\u0082\u0091\5,\27\2\u0083\u0091\5*\26\2\u0084")
        buf.write("\u0091\5.\30\2\u0085\u0091\5\60\31\2\u0086\u0091\5\62")
        buf.write("\32\2\u0087\u0091\5\64\33\2\u0088\u0091\5\66\34\2\u0089")
        buf.write("\u0091\58\35\2\u008a\u0091\5:\36\2\u008b\u0091\5<\37\2")
        buf.write("\u008c\u0091\5> \2\u008d\u0091\5@!\2\u008e\u0091\5B\"")
        buf.write("\2\u008f\u0091\5D#\2\u0090~\3\2\2\2\u0090\177\3\2\2\2")
        buf.write("\u0090\u0080\3\2\2\2\u0090\u0081\3\2\2\2\u0090\u0082\3")
        buf.write("\2\2\2\u0090\u0083\3\2\2\2\u0090\u0084\3\2\2\2\u0090\u0085")
        buf.write("\3\2\2\2\u0090\u0086\3\2\2\2\u0090\u0087\3\2\2\2\u0090")
        buf.write("\u0088\3\2\2\2\u0090\u0089\3\2\2\2\u0090\u008a\3\2\2\2")
        buf.write("\u0090\u008b\3\2\2\2\u0090\u008c\3\2\2\2\u0090\u008d\3")
        buf.write("\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091\27")
        buf.write("\3\2\2\2\u0092\u0093\t\2\2\2\u0093\31\3\2\2\2\u0094\u0095")
        buf.write("\7\63\2\2\u0095\33\3\2\2\2\u0096\u0097\t\3\2\2\u0097\35")
        buf.write("\3\2\2\2\u0098\u0099\t\4\2\2\u0099\37\3\2\2\2\u009a\u009b")
        buf.write("\t\5\2\2\u009b!\3\2\2\2\u009c\u009d\t\6\2\2\u009d#\3\2")
        buf.write("\2\2\u009e\u009f\t\7\2\2\u009f%\3\2\2\2\u00a0\u00a1\t")
        buf.write("\b\2\2\u00a1\'\3\2\2\2\u00a2\u00a3\t\t\2\2\u00a3)\3\2")
        buf.write("\2\2\u00a4\u00a5\t\n\2\2\u00a5+\3\2\2\2\u00a6\u00a7\t")
        buf.write("\13\2\2\u00a7-\3\2\2\2\u00a8\u00a9\t\f\2\2\u00a9/\3\2")
        buf.write("\2\2\u00aa\u00ab\t\r\2\2\u00ab\61\3\2\2\2\u00ac\u00ad")
        buf.write("\t\16\2\2\u00ad\63\3\2\2\2\u00ae\u00af\t\17\2\2\u00af")
        buf.write("\65\3\2\2\2\u00b0\u00b1\t\20\2\2\u00b1\67\3\2\2\2\u00b2")
        buf.write("\u00b3\t\21\2\2\u00b39\3\2\2\2\u00b4\u00b5\t\22\2\2\u00b5")
        buf.write(";\3\2\2\2\u00b6\u00b7\t\23\2\2\u00b7=\3\2\2\2\u00b8\u00b9")
        buf.write("\t\24\2\2\u00b9?\3\2\2\2\u00ba\u00bb\t\25\2\2\u00bbA\3")
        buf.write("\2\2\2\u00bc\u00bd\t\26\2\2\u00bdC\3\2\2\2\u00be\u00bf")
        buf.write("\t\27\2\2\u00bfE\3\2\2\2\tIT\\dju\u0090")
        return buf.getvalue()


class myLispGrammarParser ( Parser ):

    grammarFileName = "myLispGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':'", "'-'", "'DEF-INSTANCE'", 
                     "'def-instance'", "'RATIO:'", "'ratio:'", "'THOUS:'", 
                     "'thous:'", "'THOUS$:'", "'thous$:'", "'SCALE:'", "'scale:'", 
                     "'STATE'", "'state'", "'LOCATION'", "'location'", "'CONTROL'", 
                     "'control'", "'NO-OF-STUDENTS'", "'no-of-students'", 
                     "'MALE:FEMALE'", "'male:female'", "'STUDENT:FACULTY'", 
                     "'student:faculty'", "'SAT VERBAL'", "'sat verbal'", 
                     "'SAT MATH'", "'sat math'", "'EXPENSES'", "'expenses'", 
                     "'PERCENT-FINANCIAL-AID'", "'percent-financial-aid'", 
                     "'NO-APPLICANTS'", "'no-applicants'", "'PERCENT-ADMITTANCE'", 
                     "'percent-admittance'", "'PERCENT-ENROLLED'", "'percent-enrolled'", 
                     "'ACADEMICS'", "'academics'", "'SOCIAL'", "'social'", 
                     "'QUALITY-OF-LIFE'", "'quality-of-life'", "'ACADEMIC-EMPHASIS'", 
                     "'academic-emphasis'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WORD", "NUMBER", "WS" ]

    RULE_root = 0
    RULE_instance = 1
    RULE_items_list = 2
    RULE_value_type = 3
    RULE_value = 4
    RULE_typed_value = 5
    RULE_ratio = 6
    RULE_interval = 7
    RULE_single = 8
    RULE_dual = 9
    RULE_column_name = 10
    RULE_def_instance = 11
    RULE_uni_name = 12
    RULE_ratio_ = 13
    RULE_thous = 14
    RULE_money = 15
    RULE_scale = 16
    RULE_this_state = 17
    RULE_location = 18
    RULE_control = 19
    RULE_num_students = 20
    RULE_gender = 21
    RULE_student_faculty = 22
    RULE_sat_verbal = 23
    RULE_sat_maths = 24
    RULE_expenses = 25
    RULE_finantial_aid = 26
    RULE_number_appli = 27
    RULE_perc_admitance = 28
    RULE_perc_enrolled = 29
    RULE_academics = 30
    RULE_social_scale = 31
    RULE_quality_of_life = 32
    RULE_academic_emphasis = 33

    ruleNames =  [ "root", "instance", "items_list", "value_type", "value", 
                   "typed_value", "ratio", "interval", "single", "dual", 
                   "column_name", "def_instance", "uni_name", "ratio_", 
                   "thous", "money", "scale", "this_state", "location", 
                   "control", "num_students", "gender", "student_faculty", 
                   "sat_verbal", "sat_maths", "expenses", "finantial_aid", 
                   "number_appli", "perc_admitance", "perc_enrolled", "academics", 
                   "social_scale", "quality_of_life", "academic_emphasis" ]

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
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    WORD=49
    NUMBER=50
    WS=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(myLispGrammarParser.EOF, 0)

        def instance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myLispGrammarParser.InstanceContext)
            else:
                return self.getTypedRuleContext(myLispGrammarParser.InstanceContext,i)


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = myLispGrammarParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==myLispGrammarParser.T__0:
                self.state = 68
                self.instance()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(myLispGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def def_instance(self):
            return self.getTypedRuleContext(myLispGrammarParser.Def_instanceContext,0)


        def uni_name(self):
            return self.getTypedRuleContext(myLispGrammarParser.Uni_nameContext,0)


        def items_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(myLispGrammarParser.Items_listContext)
            else:
                return self.getTypedRuleContext(myLispGrammarParser.Items_listContext,i)


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance" ):
                return visitor.visitInstance(self)
            else:
                return visitor.visitChildren(self)




    def instance(self):

        localctx = myLispGrammarParser.InstanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(myLispGrammarParser.T__0)
            self.state = 77
            self.def_instance()
            self.state = 78
            self.uni_name()
            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.items_list()
                self.state = 82 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==myLispGrammarParser.T__0):
                    break

            self.state = 84
            self.match(myLispGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Items_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_name(self):
            return self.getTypedRuleContext(myLispGrammarParser.Column_nameContext,0)


        def value(self):
            return self.getTypedRuleContext(myLispGrammarParser.ValueContext,0)


        def typed_value(self):
            return self.getTypedRuleContext(myLispGrammarParser.Typed_valueContext,0)


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_items_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItems_list" ):
                return visitor.visitItems_list(self)
            else:
                return visitor.visitChildren(self)




    def items_list(self):

        localctx = myLispGrammarParser.Items_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_items_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(myLispGrammarParser.T__0)
            self.state = 87
            self.column_name()
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [myLispGrammarParser.WORD, myLispGrammarParser.NUMBER]:
                self.state = 88
                self.value()
                pass
            elif token in [myLispGrammarParser.T__6, myLispGrammarParser.T__7, myLispGrammarParser.T__8, myLispGrammarParser.T__9, myLispGrammarParser.T__10, myLispGrammarParser.T__11, myLispGrammarParser.T__12, myLispGrammarParser.T__13]:
                self.state = 89
                self.typed_value()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 92
            self.match(myLispGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ratio_(self):
            return self.getTypedRuleContext(myLispGrammarParser.Ratio_Context,0)


        def thous(self):
            return self.getTypedRuleContext(myLispGrammarParser.ThousContext,0)


        def money(self):
            return self.getTypedRuleContext(myLispGrammarParser.MoneyContext,0)


        def scale(self):
            return self.getTypedRuleContext(myLispGrammarParser.ScaleContext,0)


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_value_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_type" ):
                return visitor.visitValue_type(self)
            else:
                return visitor.visitChildren(self)




    def value_type(self):

        localctx = myLispGrammarParser.Value_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value_type)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [myLispGrammarParser.T__6, myLispGrammarParser.T__7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.ratio_()
                pass
            elif token in [myLispGrammarParser.T__8, myLispGrammarParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.thous()
                pass
            elif token in [myLispGrammarParser.T__10, myLispGrammarParser.T__11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.money()
                pass
            elif token in [myLispGrammarParser.T__12, myLispGrammarParser.T__13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.scale()
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


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ratio(self):
            return self.getTypedRuleContext(myLispGrammarParser.RatioContext,0)


        def interval(self):
            return self.getTypedRuleContext(myLispGrammarParser.IntervalContext,0)


        def WORD(self):
            return self.getToken(myLispGrammarParser.WORD, 0)

        def NUMBER(self):
            return self.getToken(myLispGrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return myLispGrammarParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = myLispGrammarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.ratio()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.interval()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.match(myLispGrammarParser.WORD)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self.match(myLispGrammarParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typed_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value_type(self):
            return self.getTypedRuleContext(myLispGrammarParser.Value_typeContext,0)


        def value(self):
            return self.getTypedRuleContext(myLispGrammarParser.ValueContext,0)


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_typed_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyped_value" ):
                return visitor.visitTyped_value(self)
            else:
                return visitor.visitChildren(self)




    def typed_value(self):

        localctx = myLispGrammarParser.Typed_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typed_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.value_type()
            self.state = 107
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RatioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(myLispGrammarParser.NUMBER)
            else:
                return self.getToken(myLispGrammarParser.NUMBER, i)

        def getRuleIndex(self):
            return myLispGrammarParser.RULE_ratio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRatio" ):
                return visitor.visitRatio(self)
            else:
                return visitor.visitChildren(self)




    def ratio(self):

        localctx = myLispGrammarParser.RatioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ratio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(myLispGrammarParser.NUMBER)
            self.state = 110
            self.match(myLispGrammarParser.T__2)
            self.state = 111
            self.match(myLispGrammarParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dual(self):
            return self.getTypedRuleContext(myLispGrammarParser.DualContext,0)


        def single(self):
            return self.getTypedRuleContext(myLispGrammarParser.SingleContext,0)


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_interval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterval" ):
                return visitor.visitInterval(self)
            else:
                return visitor.visitChildren(self)




    def interval(self):

        localctx = myLispGrammarParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_interval)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.dual()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.single()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(myLispGrammarParser.NUMBER, 0)

        def getRuleIndex(self):
            return myLispGrammarParser.RULE_single

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle" ):
                return visitor.visitSingle(self)
            else:
                return visitor.visitChildren(self)




    def single(self):

        localctx = myLispGrammarParser.SingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_single)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(myLispGrammarParser.NUMBER)
            self.state = 118
            self.match(myLispGrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DualContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(myLispGrammarParser.NUMBER)
            else:
                return self.getToken(myLispGrammarParser.NUMBER, i)

        def getRuleIndex(self):
            return myLispGrammarParser.RULE_dual

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDual" ):
                return visitor.visitDual(self)
            else:
                return visitor.visitChildren(self)




    def dual(self):

        localctx = myLispGrammarParser.DualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dual)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(myLispGrammarParser.NUMBER)
            self.state = 121
            self.match(myLispGrammarParser.T__3)
            self.state = 122
            self.match(myLispGrammarParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def this_state(self):
            return self.getTypedRuleContext(myLispGrammarParser.This_stateContext,0)


        def location(self):
            return self.getTypedRuleContext(myLispGrammarParser.LocationContext,0)


        def control(self):
            return self.getTypedRuleContext(myLispGrammarParser.ControlContext,0)


        def num_students(self):
            return self.getTypedRuleContext(myLispGrammarParser.Num_studentsContext,0)


        def gender(self):
            return self.getTypedRuleContext(myLispGrammarParser.GenderContext,0)


        def student_faculty(self):
            return self.getTypedRuleContext(myLispGrammarParser.Student_facultyContext,0)


        def sat_verbal(self):
            return self.getTypedRuleContext(myLispGrammarParser.Sat_verbalContext,0)


        def sat_maths(self):
            return self.getTypedRuleContext(myLispGrammarParser.Sat_mathsContext,0)


        def expenses(self):
            return self.getTypedRuleContext(myLispGrammarParser.ExpensesContext,0)


        def finantial_aid(self):
            return self.getTypedRuleContext(myLispGrammarParser.Finantial_aidContext,0)


        def number_appli(self):
            return self.getTypedRuleContext(myLispGrammarParser.Number_appliContext,0)


        def perc_admitance(self):
            return self.getTypedRuleContext(myLispGrammarParser.Perc_admitanceContext,0)


        def perc_enrolled(self):
            return self.getTypedRuleContext(myLispGrammarParser.Perc_enrolledContext,0)


        def academics(self):
            return self.getTypedRuleContext(myLispGrammarParser.AcademicsContext,0)


        def social_scale(self):
            return self.getTypedRuleContext(myLispGrammarParser.Social_scaleContext,0)


        def quality_of_life(self):
            return self.getTypedRuleContext(myLispGrammarParser.Quality_of_lifeContext,0)


        def academic_emphasis(self):
            return self.getTypedRuleContext(myLispGrammarParser.Academic_emphasisContext,0)


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_column_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_name" ):
                return visitor.visitColumn_name(self)
            else:
                return visitor.visitChildren(self)




    def column_name(self):

        localctx = myLispGrammarParser.Column_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_column_name)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.this_state()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.location()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.control()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.num_students()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.gender()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.num_students()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.student_faculty()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.sat_verbal()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 132
                self.sat_maths()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.expenses()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 134
                self.finantial_aid()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 135
                self.number_appli()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 136
                self.perc_admitance()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 137
                self.perc_enrolled()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 138
                self.academics()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 139
                self.social_scale()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 140
                self.quality_of_life()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 141
                self.academic_emphasis()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Def_instanceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_def_instance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDef_instance" ):
                return visitor.visitDef_instance(self)
            else:
                return visitor.visitChildren(self)




    def def_instance(self):

        localctx = myLispGrammarParser.Def_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_def_instance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__4 or _la==myLispGrammarParser.T__5):
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


    class Uni_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(myLispGrammarParser.WORD, 0)

        def getRuleIndex(self):
            return myLispGrammarParser.RULE_uni_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUni_name" ):
                return visitor.visitUni_name(self)
            else:
                return visitor.visitChildren(self)




    def uni_name(self):

        localctx = myLispGrammarParser.Uni_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_uni_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(myLispGrammarParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ratio_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_ratio_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRatio_" ):
                return visitor.visitRatio_(self)
            else:
                return visitor.visitChildren(self)




    def ratio_(self):

        localctx = myLispGrammarParser.Ratio_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ratio_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__6 or _la==myLispGrammarParser.T__7):
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


    class ThousContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_thous

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThous" ):
                return visitor.visitThous(self)
            else:
                return visitor.visitChildren(self)




    def thous(self):

        localctx = myLispGrammarParser.ThousContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_thous)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__8 or _la==myLispGrammarParser.T__9):
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


    class MoneyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_money

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoney" ):
                return visitor.visitMoney(self)
            else:
                return visitor.visitChildren(self)




    def money(self):

        localctx = myLispGrammarParser.MoneyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_money)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__10 or _la==myLispGrammarParser.T__11):
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


    class ScaleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_scale

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScale" ):
                return visitor.visitScale(self)
            else:
                return visitor.visitChildren(self)




    def scale(self):

        localctx = myLispGrammarParser.ScaleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_scale)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__12 or _la==myLispGrammarParser.T__13):
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


    class This_stateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_this_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThis_state" ):
                return visitor.visitThis_state(self)
            else:
                return visitor.visitChildren(self)




    def this_state(self):

        localctx = myLispGrammarParser.This_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_this_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__14 or _la==myLispGrammarParser.T__15):
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


    class LocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_location

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocation" ):
                return visitor.visitLocation(self)
            else:
                return visitor.visitChildren(self)




    def location(self):

        localctx = myLispGrammarParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_location)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__16 or _la==myLispGrammarParser.T__17):
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


    class ControlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_control

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl" ):
                return visitor.visitControl(self)
            else:
                return visitor.visitChildren(self)




    def control(self):

        localctx = myLispGrammarParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_control)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__18 or _la==myLispGrammarParser.T__19):
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


    class Num_studentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_num_students

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_students" ):
                return visitor.visitNum_students(self)
            else:
                return visitor.visitChildren(self)




    def num_students(self):

        localctx = myLispGrammarParser.Num_studentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_num_students)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__20 or _la==myLispGrammarParser.T__21):
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


    class GenderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_gender

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGender" ):
                return visitor.visitGender(self)
            else:
                return visitor.visitChildren(self)




    def gender(self):

        localctx = myLispGrammarParser.GenderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_gender)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__22 or _la==myLispGrammarParser.T__23):
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


    class Student_facultyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_student_faculty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStudent_faculty" ):
                return visitor.visitStudent_faculty(self)
            else:
                return visitor.visitChildren(self)




    def student_faculty(self):

        localctx = myLispGrammarParser.Student_facultyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_student_faculty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__24 or _la==myLispGrammarParser.T__25):
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


    class Sat_verbalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_sat_verbal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSat_verbal" ):
                return visitor.visitSat_verbal(self)
            else:
                return visitor.visitChildren(self)




    def sat_verbal(self):

        localctx = myLispGrammarParser.Sat_verbalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sat_verbal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__26 or _la==myLispGrammarParser.T__27):
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


    class Sat_mathsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_sat_maths

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSat_maths" ):
                return visitor.visitSat_maths(self)
            else:
                return visitor.visitChildren(self)




    def sat_maths(self):

        localctx = myLispGrammarParser.Sat_mathsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sat_maths)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__28 or _la==myLispGrammarParser.T__29):
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


    class ExpensesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_expenses

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpenses" ):
                return visitor.visitExpenses(self)
            else:
                return visitor.visitChildren(self)




    def expenses(self):

        localctx = myLispGrammarParser.ExpensesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expenses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__30 or _la==myLispGrammarParser.T__31):
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


    class Finantial_aidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_finantial_aid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinantial_aid" ):
                return visitor.visitFinantial_aid(self)
            else:
                return visitor.visitChildren(self)




    def finantial_aid(self):

        localctx = myLispGrammarParser.Finantial_aidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_finantial_aid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__32 or _la==myLispGrammarParser.T__33):
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


    class Number_appliContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_number_appli

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_appli" ):
                return visitor.visitNumber_appli(self)
            else:
                return visitor.visitChildren(self)




    def number_appli(self):

        localctx = myLispGrammarParser.Number_appliContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_number_appli)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__34 or _la==myLispGrammarParser.T__35):
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


    class Perc_admitanceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_perc_admitance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPerc_admitance" ):
                return visitor.visitPerc_admitance(self)
            else:
                return visitor.visitChildren(self)




    def perc_admitance(self):

        localctx = myLispGrammarParser.Perc_admitanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_perc_admitance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__36 or _la==myLispGrammarParser.T__37):
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


    class Perc_enrolledContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_perc_enrolled

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPerc_enrolled" ):
                return visitor.visitPerc_enrolled(self)
            else:
                return visitor.visitChildren(self)




    def perc_enrolled(self):

        localctx = myLispGrammarParser.Perc_enrolledContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_perc_enrolled)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__38 or _la==myLispGrammarParser.T__39):
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


    class AcademicsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_academics

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcademics" ):
                return visitor.visitAcademics(self)
            else:
                return visitor.visitChildren(self)




    def academics(self):

        localctx = myLispGrammarParser.AcademicsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_academics)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__40 or _la==myLispGrammarParser.T__41):
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


    class Social_scaleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_social_scale

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSocial_scale" ):
                return visitor.visitSocial_scale(self)
            else:
                return visitor.visitChildren(self)




    def social_scale(self):

        localctx = myLispGrammarParser.Social_scaleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_social_scale)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__42 or _la==myLispGrammarParser.T__43):
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


    class Quality_of_lifeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_quality_of_life

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuality_of_life" ):
                return visitor.visitQuality_of_life(self)
            else:
                return visitor.visitChildren(self)




    def quality_of_life(self):

        localctx = myLispGrammarParser.Quality_of_lifeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_quality_of_life)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__44 or _la==myLispGrammarParser.T__45):
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


    class Academic_emphasisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return myLispGrammarParser.RULE_academic_emphasis

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcademic_emphasis" ):
                return visitor.visitAcademic_emphasis(self)
            else:
                return visitor.visitChildren(self)




    def academic_emphasis(self):

        localctx = myLispGrammarParser.Academic_emphasisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_academic_emphasis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==myLispGrammarParser.T__46 or _la==myLispGrammarParser.T__47):
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





