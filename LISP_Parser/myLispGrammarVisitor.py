# Generated from myLispGrammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .myLispGrammarParser import myLispGrammarParser
else:
    from myLispGrammarParser import myLispGrammarParser

# This class defines a complete generic visitor for a parse tree produced by myLispGrammarParser.

class myLispGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by myLispGrammarParser#root.
    def visitRoot(self, ctx:myLispGrammarParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#instance.
    def visitInstance(self, ctx:myLispGrammarParser.InstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#items_list.
    def visitItems_list(self, ctx:myLispGrammarParser.Items_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#value_type.
    def visitValue_type(self, ctx:myLispGrammarParser.Value_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#value.
    def visitValue(self, ctx:myLispGrammarParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#typed_value.
    def visitTyped_value(self, ctx:myLispGrammarParser.Typed_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#ratio.
    def visitRatio(self, ctx:myLispGrammarParser.RatioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#interval.
    def visitInterval(self, ctx:myLispGrammarParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#single.
    def visitSingle(self, ctx:myLispGrammarParser.SingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#dual.
    def visitDual(self, ctx:myLispGrammarParser.DualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#column_name.
    def visitColumn_name(self, ctx:myLispGrammarParser.Column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#def_instance.
    def visitDef_instance(self, ctx:myLispGrammarParser.Def_instanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#uni_name.
    def visitUni_name(self, ctx:myLispGrammarParser.Uni_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#ratio_.
    def visitRatio_(self, ctx:myLispGrammarParser.Ratio_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#thous.
    def visitThous(self, ctx:myLispGrammarParser.ThousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#money.
    def visitMoney(self, ctx:myLispGrammarParser.MoneyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#scale.
    def visitScale(self, ctx:myLispGrammarParser.ScaleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#this_state.
    def visitThis_state(self, ctx:myLispGrammarParser.This_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#location.
    def visitLocation(self, ctx:myLispGrammarParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#control.
    def visitControl(self, ctx:myLispGrammarParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#num_students.
    def visitNum_students(self, ctx:myLispGrammarParser.Num_studentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#gender.
    def visitGender(self, ctx:myLispGrammarParser.GenderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#student_faculty.
    def visitStudent_faculty(self, ctx:myLispGrammarParser.Student_facultyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#sat_verbal.
    def visitSat_verbal(self, ctx:myLispGrammarParser.Sat_verbalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#sat_maths.
    def visitSat_maths(self, ctx:myLispGrammarParser.Sat_mathsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#expenses.
    def visitExpenses(self, ctx:myLispGrammarParser.ExpensesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#finantial_aid.
    def visitFinantial_aid(self, ctx:myLispGrammarParser.Finantial_aidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#number_appli.
    def visitNumber_appli(self, ctx:myLispGrammarParser.Number_appliContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#perc_admitance.
    def visitPerc_admitance(self, ctx:myLispGrammarParser.Perc_admitanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#perc_enrolled.
    def visitPerc_enrolled(self, ctx:myLispGrammarParser.Perc_enrolledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#academics.
    def visitAcademics(self, ctx:myLispGrammarParser.AcademicsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#social_scale.
    def visitSocial_scale(self, ctx:myLispGrammarParser.Social_scaleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#quality_of_life.
    def visitQuality_of_life(self, ctx:myLispGrammarParser.Quality_of_lifeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by myLispGrammarParser#academic_emphasis.
    def visitAcademic_emphasis(self, ctx:myLispGrammarParser.Academic_emphasisContext):
        return self.visitChildren(ctx)



del myLispGrammarParser