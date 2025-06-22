# src/ast_tree/builder.py

from ast_tree import nodes as ast
from antlr.AgentarVisitor import AgentarVisitor
from antlr.AgentarParser import AgentarParser

class AgentarToASTBuilder(AgentarVisitor):

    def visitProgram(self, ctx:AgentarParser.ProgramContext):
        decls = [self.visit(child) for child in ctx.children if child.getText() != '<EOF>']
        mothers = [child for child in decls if isinstance(child, ast.MotherNode)]
        if len(mothers) > 1:
            raise ValueError("Only one mother declaration is allowed in the program.")
        elif len(mothers) < 1:
            raise ValueError("Mother declaration is required in the program.")
        return ast.ProgramNode(declarations=decls)


    def visitStatement(self, ctx:AgentarParser.StatementContext):
        return self.visit(ctx.getChild(0))


    def visitMotherDecl(self, ctx:AgentarParser.MotherDeclContext):
        return ast.MotherNode(body=self.visit(ctx.agentBody()))


    def visitAgentDecl(self, ctx:AgentarParser.AgentDeclContext):
        name = ctx.ID().getText()
        body = self.visit(ctx.agentBody())
        return ast.AgentNode(name=name, body=body)


    def visitAgentBody(self, ctx:AgentarParser.AgentBodyContext):
        if ctx.children is None:
            return []
        else:
            return [self.visit(child) for child in ctx.children ]


    def visitFieldSection(self, ctx:AgentarParser.FieldSectionContext):
        decls = [self.visit(decl) for decl in ctx.variableDecl()]
        return ast.FieldSectionNode(declarations=decls)


    def visitInitialSection(self, ctx:AgentarParser.InitialSectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.InitSectionNode(statements=stats)


    def visitDestroySection(self, ctx:AgentarParser.DestroySectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.DestroySectionNode(statements=stats)


    def visitBeliefsSection(self, ctx:AgentarParser.BeliefsSectionContext):
        decls = [self.visit(decl) for decl in ctx.variableDecl()]
        return ast.BeliefSectionNode(declarations=decls)


    def visitSenseSection(self, ctx:AgentarParser.SenseSectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.SeanseSectionNode(statements=stats)


    def visitGoalsSection(self, ctx:AgentarParser.GoalsSectionContext):
        goals = [self.visit(gole) for gole in ctx.goalBlock()]
        merge_condition = self.visit(ctx.expression()) if ctx.expression() else None
        return ast.GoalSectionNode(goals=goals, merge_condition=merge_condition)
    

    def visitGoalBlock(self, ctx:AgentarParser.GoalBlockContext):
        name = ctx.ID().getText()
        conditions = self.visit(ctx.expression()) if ctx.expression() else []
        return ast.GoalBlockNode(name=name, condition=conditions)


    def visitRulesSection(self, ctx:AgentarParser.RulesSectionContext):
        rules = [self.visit(rule) for rule in ctx.whenBlock()]
        return ast.RulesSectionNode(rules=rules)


    def visitReceiveSection(self, ctx:AgentarParser.ReceiveSectionContext):
        name = ctx.ID().getText()
        blocks = [self.visit(block) for block in ctx.whenBlock()]
        return ast.ReceiveSectionNode(name=name, blocks=blocks)


    def visitWhenBlock(self, ctx:AgentarParser.WhenBlockContext):
        conditions = self.visit(ctx.expression()) if ctx.expression() else []
        statements = [self.visit(stat) for stat in ctx.statement()]
        return ast.WhenBlockNode(conditions=conditions, statements=statements)


    def visitActionSection(self, ctx:AgentarParser.ActionSectionContext):
        name = ctx.ID().getText()
        parameters = [self.visit(param) for param in ctx.parameterList().parameter()] if ctx.parameterList() else []
        if ctx.type_() is None:
            raise ValueError("Return type is required for action section.")
        return_type = self.visit(ctx.type_())
        body = [self.visit(stat) for stat in ctx.statement()]
        return ast.ActionNode(name=name, parameters=parameters, return_type=return_type, body=body)


    def visitParameter(self, ctx:AgentarParser.ParameterContext):
        param_type = self.visit(ctx.type_()) if ctx.type_() else None
        name = ctx.ID().getText()
        if not param_type or not name:
            raise ValueError("Parameter type and name are required.")
        return ast.ParameterNode(param_type=param_type, name=name)


    def visitMessageDecl(self, ctx:AgentarParser.MessageDeclContext):
        name = ctx.ID().getText()
        fields = [self.visit(field) for field in ctx.variableDecl()]
        return ast.MessageDeclNode(name=name, fields=fields)


    def visitSendStmt(self, ctx:AgentarParser.SendStmtContext):
        to = self.visit(ctx.expression(0))
        message = self.visit(ctx.expression(1))
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendNode(to=to, message=message, msg_type=msg_type)
    

    def visitSendParentStmt(self, ctx:AgentarParser.SendParentStmtContext):
        to = 'PARENT'  # Sending to parent agent
        message = self.visit(ctx.expression())
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendNode(to=to, message=message, msg_type=msg_type)


    def visitSendChildrenStmt(self, ctx:AgentarParser.SendChildrenStmtContext):
        agent_type = self.visit(ctx.expression(0))           # Sending to all children agents (when param _) or a specific child
        message = self.visit(ctx.expression(1))
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendToChildrenNode(agent_type=agent_type, message=message, msg_type=msg_type)


    def visitSendSiblingStmt(self, ctx:AgentarParser.SendSiblingStmtContext):
        agent_type = self.visit(ctx.expression(0))           # Sending to all siblings agents (when param _) or a specific child
        message = self.visit(ctx.expression(1))
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendToSiblingsNode(agent_type=agent_type, message=message, msg_type=msg_type)


    def visitSpawnStmt(self, ctx:AgentarParser.SpawnStmtContext):
        agent_type = ctx.ID().getText()
        if not agent_type:
            raise ValueError("Agent type is required for spawn statement.")
        args = [self.visit(arg) for arg in ctx.expression()]
        return ast.SpawnNode(agent_type=agent_type, args=args)


    def visitKillStmt(self, ctx:AgentarParser.KillStmtContext):
        if ctx.expression() is None:
            agent_id = None
        else:
            agent_id = self.visit(ctx.expression())
        return ast.KillNode(agent_id=agent_id)
    

    def visitKillchildrenStmt(self, ctx:AgentarParser.KillchildrenStmtContext):
        if ctx.expression() is None:
            agent_type = None
        else:
            agent_type = self.visit(ctx.expression())
        return ast.KillChildrenNode(agent_type=agent_type)


    def visitSleepStmt(self, ctx:AgentarParser.SleepStmtContext):
        return ast.SleepNode(duration=self.visit(ctx.expression()))


    def visitReturnStmt(self, ctx:AgentarParser.ReturnStmtContext):
        return ast.ReturnNode(value=self.visit(ctx.expression()) if ctx.expression() else None)
    

    def visitSenseStmt(self, ctx:AgentarParser.SenseStmtContext):
        return ast.SenseNode()


    def visitGoalCheckStmt(self, ctx:AgentarParser.GoalCheckStmtContext):
        goal_name = ctx.ID().getText()
        return ast.GoalCheckNode(goal_name=goal_name)
    

    def visitGetTimeStmt(self, ctx:AgentarParser.GetTimeStmtContext):
        return ast.GetTimeNode()


    def visitMessageInit(self, ctx:AgentarParser.MessageInitContext):
        message_type = ctx.ID().getText()
        fields = {}
        for field_ctx in ctx.messageFieldAssign():
            key = field_ctx.ID().getText()  # nazwa pola, np. "task"
            value = self.visit(field_ctx.expression())  # wartość pola, np. LiteralNode("clean")
            fields[key] = value
        return ast.MessageInitNode(message_type=message_type, fields=fields)


    def visitMessageFieldAssign(self, ctx:AgentarParser.MessageFieldAssignContext):
        pass # TODO: Handle message field assignment if needed


    def visitPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        return ast.PrintNode(values=[self.visit(expr) for expr in ctx.expression()])


    def visitIfStmt(self, ctx:AgentarParser.IfStmtContext):
        conditions = self.visit(ctx.expression()) if ctx.expression() else []
        statements = self.visit(ctx.blockOrStmt()) if ctx.blockOrStmt() else []
        elseStmt = self.visit(ctx.elseStmt()) if ctx.elseStmt() else None
        return ast.IfStmtNode(conditions=conditions, statements=statements, elseStmt=elseStmt)


    def visitBlockOrStmt(self, ctx:AgentarParser.BlockOrStmtContext):
        return [self.visit(stat) for stat in ctx.statement()]


    def visitElseStmt(self, ctx:AgentarParser.ElseStmtContext):
        statements = [self.visit(stat) for stat in ctx.statement()]
        return ast.ElseStmtNode(statements=statements)


    def visitForStmt(self, ctx:AgentarParser.ForStmtContext):
        initialize = self.visit(ctx.variableDecl())
        condition = self.visit(ctx.expression()) if ctx.expression() else None
        update = self.visit(ctx.forAssignExpr()) if ctx.forAssignExpr() else None
        body = self.visit(ctx.forBody()) if ctx.forBody() else []
        if not initialize or not condition or not update or not body:
            raise ValueError("For loop requires initialization, condition, update, and body.")
        return ast.ForLoopNode(initialize=initialize, condition=condition, update=update, body=body)
        

    def visitForBody(self, ctx:AgentarParser.ForBodyContext):
        return [self.visit(stat) for stat in ctx.statement()]


    def visitForAssignExpr(self, ctx:AgentarParser.ForAssignExprContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return ast.AssignmentNode(target=target, value=value)


    def visitWhileStmt(self, ctx:AgentarParser.WhileStmtContext):
        condition = self.visit(ctx.expression()) if ctx.expression() else None
        body = [self.visit(stat) for stat in ctx.statement()]
        if not condition or not body:
            raise ValueError("While loop requires a condition and a body.")
        return ast.WhileLoopNode(condition=condition, body=body)


    def visitBreakStmt(self, ctx:AgentarParser.BreakStmtContext):
        return ast.BreakNode()
    

    def visitVarDecl(self, ctx:AgentarParser.VarDeclContext):
        if ctx.type_() is None:
            raise ValueError("Variable type is required for declaration.")
        var_type = self.visit(ctx.type_())
        name = ctx.ID().getText()
        value = self.visit(ctx.expression()) if ctx.expression() else None
        return ast.VariableDeclNode(var_type=var_type, name=name, value=value)


    def visitSimpleAssign(self, ctx: AgentarParser.SimpleAssignContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return ast.AssignmentNode(target=target, value=value)


    def visitIndexAssign(self, ctx: AgentarParser.IndexAssignContext):
        target = ctx.ID().getText()    # np. x
        index = self.visit(ctx.expression(0))   # np. 3
        value = self.visit(ctx.expression(1))   # np. 10
        return ast.AssignmentNode(target=target, index=index, value=value)


    def visitListAddAssign(self, ctx:AgentarParser.ListAddAssignContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.expression())
        index = "add"
        return ast.AssignmentNode(target=target, index=index, value=value)


    def visitSpawnAssign(self, ctx: AgentarParser.SpawnAssignContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.spawnStmt())
        return ast.AssignmentNode(target=target, value=value)
    
       
    def visitDoAssign(self, ctx:AgentarParser.DoAssignContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.doStmt())
        return ast.AssignmentNode(target=target, value=value)


    def visitGoalCheckAssign(self, ctx:AgentarParser.GoalCheckAssignContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.goalCheckStmt())
        return ast.AssignmentNode(target=target, value=value)


    def visitGetTimeAssign(self, ctx:AgentarParser.GetTimeAssignContext):
        target = self.visit(ctx.expression())
        value = self.visit(ctx.getTimeStmt())
        return ast.AssignmentNode(target=target, value=value)


    def visitDoSelfAssign(self, ctx:AgentarParser.DoSelfAssignContext):
        target = self.visit(ctx.expression())
        value = self.visit(ctx.doStmt())
        return ast.AssignmentNode(target=target, value=value)


    def visitSelfAssign(self, ctx:AgentarParser.SelfAssignContext):
        target = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))
        return ast.AssignmentNode(target=target, value=value)


    def visitSelfIndexAssign(self, ctx:AgentarParser.SelfIndexAssignContext):
        target = self.visit(ctx.expression(0))
        index = self.visit(ctx.expression(1))
        value = self.visit(ctx.expression(2))
        return ast.AssignmentNode(target=target, index=index, value=value)


    def visitSelfListAddAssign(self, ctx:AgentarParser.SelfListAddAssignContext):
        target = self.visit(ctx.expression(0))
        index = "add"
        value = self.visit(ctx.expression(1))
        return ast.AssignmentNode(target=target, index=index, value=value)


    def visitSelfGoalCheckAssign(self, ctx:AgentarParser.SelfGoalCheckAssignContext):
        target = self.visit(ctx.expression())
        value = self.visit(ctx.goalCheckStmt())
        return ast.AssignmentNode(target=target, value=value)


    def visitDoStmt(self, ctx:AgentarParser.DoStmtContext):
        name = ctx.ID().getText()
        variables = [self.visit(var) for var in ctx.expression()] if ctx.expression() else []
        return ast.DoNode(name=name, variables=variables)


    def visitBacisType(self, ctx:AgentarParser.BacisTypeContext):
        return ast.BaseTypeNode(name=ctx.bodyType().getText())
    

    def visitPointerType(self, ctx:AgentarParser.PointerTypeContext):
            inner = self.visit(ctx.type_())
            return ast.PointerTypeNode(inner=inner)


    def visitMapExpr(self, ctx:AgentarParser.MapExprContext):
        entries = {}
        ids = ctx.ID()
        exprs = ctx.expression()
        for i in range(len(ids)):
            key = ids[i].getText()
            value = self.visit(exprs[i])
            entries[key] = value
        return ast.MapLiteralNode(entries=entries)


    def visitAndExpr(self, ctx:AgentarParser.AndExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='AND', left=left, right=right)


    def visitSelfAccessExpr(self, ctx: AgentarParser.SelfAccessExprContext):
        if type(ctx.ID()) is list:
            path = ["self"] + [id_.getText() for id_ in ctx.ID()]
        else: 
            path = ['self', ctx.ID().getText()]
        return ast.SelfAccessNode(path=path)


    def visitLeqExpr(self, ctx:AgentarParser.LeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='<=', left=left, right=right)


    def visitXorExpr(self, ctx:AgentarParser.XorExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='XOR', left=left, right=right)


    def visitGeqExpr(self, ctx:AgentarParser.GeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='>=', left=left, right=right)
    

    def visitLenExpr(self, ctx:AgentarParser.LenExprContext):
        base = self.visit(ctx.expression())
        return ast.LenNode(base=base)


    def visitMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        if type(ctx.ID()) is list:
            path = ['msg'] + [id_.getText() for id_ in ctx.ID()]
        else: 
            path = ['msg', ctx.ID().getText()]
        return ast.MsgAccessNode(path=path)


    def visitLtExpr(self, ctx:AgentarParser.LtExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='<', left=left, right=right)


    def visitGtExpr(self, ctx:AgentarParser.GtExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='>', left=left, right=right)
    

    def visitTypeExpr(self, ctx:AgentarParser.TypeExprContext):
        base = self.visit(ctx.expression())
        return ast.TypeExprNode(base=base)


    def visitOrExpr(self, ctx:AgentarParser.OrExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='OR', left=left, right=right)


    def visitIndexExpr(self, ctx:AgentarParser.IndexExprContext):
        base = self.visit(ctx.expression(0))   # np. x
        index = self.visit(ctx.expression(1))  # np. 3
        return ast.IndexAccessNode(base=base, index=index)
    

    def visitSliceToExpr(self, ctx:AgentarParser.SliceToExprContext):
        base = self.visit(ctx.expression(0))
        start = None # means slice from the beginning
        end = self.visit(ctx.expression(1))
        return ast.SliceAccessNode(base=base, start=start, end=end)


    def visitSliceFromExpr(self, ctx:AgentarParser.SliceFromExprContext):
        base = self.visit(ctx.expression(0))
        start = self.visit(ctx.expression(1))
        end = None # means no end specified, slice to the end
        return ast.SliceAccessNode(base=base, start=start, end=end)


    def visitSliceRangeExpr(self, ctx:AgentarParser.SliceRangeExprContext):
        base = self.visit(ctx.expression(0))
        start = self.visit(ctx.expression(1))
        end = self.visit(ctx.expression(2))
        return ast.SliceAccessNode(base=base, start=start, end=end)


    def visitAgentIdExpr(self, ctx:AgentarParser.AgentIdExprContext):
        text = ctx.getText()
        return ast.AgentIdNode(path=text)
    

    def visitModuloExpr(self, ctx:AgentarParser.ModuloExprContext): 
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='%', left=left, right=right)


    def visitBeliefAccessExpr(self, ctx:AgentarParser.BeliefAccessExprContext):
        if type(ctx.ID()) is list:
            path = ["bel"] + [id_.getText() for id_ in ctx.ID()]
        else: 
            path = ['bel', ctx.ID().getText()]
        return ast.BelAccessNode(path=path)


    def visitVarReference(self, ctx:AgentarParser.VarReferenceContext):
        name = ctx.getText()
        return ast.VarRefNode(name=name)


    def visitMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '*':
            op = '*'
        else:
            op = '/'
        return ast.BinaryOpNode(op=op, left=left, right=right)


    def visitAddressOfExpr(self, ctx:AgentarParser.AddressOfExprContext):
        variable = self.visit(ctx.expression())
        return ast.AddressOfExprNode(variable=variable)


    def visitEqExpr(self, ctx:AgentarParser.EqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='==', left=left, right=right)


    def visitNeqExpr(self, ctx:AgentarParser.NeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='!=', left=left, right=right)


    def visitLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        return self.visit(ctx.literal())


    def visitMsgTypeValueExpr(self, ctx:AgentarParser.MsgTypeValueExprContext):
        return ast.LiteralNode(value=ctx.getText())


    def visitNotExpr(self, ctx:AgentarParser.NotExprContext):
        left = self.visit(ctx.expression(0))
        return ast.BinaryOpNode(op='NOT', left=left, right=None)


    def visitListExpr(self, ctx:AgentarParser.ListExprContext):
        elements = [self.visit(expr) for expr in ctx.listLiteral().expression()]
        return ast.ListLiteralNode(elements=elements)


    def visitParenExpr(self, ctx:AgentarParser.ParenExprContext):
        return self.visit(ctx.expression())


    def visitMessageInitExpr(self, ctx:AgentarParser.MessageInitExprContext):
        return self.visit(ctx.messageInit())


    def visitAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '+':
            op = '+'
        else:
            op = '-'
        return ast.BinaryOpNode(op=op, left=left, right=right)


    def visitListLiteral(self, ctx:AgentarParser.ListLiteralContext):
        pass # TODO: Handle list literal if needed, currently not used in the grammar


    def visitMapLiteral(self, ctx:AgentarParser.MapLiteralContext):
        pass # TODO: Handle map literal if needed, currently not used in the grammar


    def visitIntLiteral(self, ctx:AgentarParser.IntLiteralContext):
        return ast.LiteralNode(value=int(ctx.getText()))


    def visitFloatLiteral(self, ctx:AgentarParser.FloatLiteralContext):
        return ast.LiteralNode(value=float(ctx.getText()))


    def visitStringLiteral(self, ctx:AgentarParser.StringLiteralContext):
        return ast.LiteralNode(value=ctx.getText()[1:-1])  # Remove quotes


    def visitBoolLiteral(self, ctx:AgentarParser.BoolLiteralContext):
        return ast.LiteralNode(value=ctx.getText() == 'true')  # Convert to boolean


    def visitMsgTypeValue(self, ctx:AgentarParser.MsgTypeValueContext):
        return ast.LiteralNode(value=ctx.getText())  # Return the message type value as a literal
    