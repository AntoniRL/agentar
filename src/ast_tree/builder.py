# src/ast_tree/builder.py

from ast_tree import nodes as ast
from antlr.AgentarVisitor import AgentarVisitor
from antlr.AgentarParser import AgentarParser

class AgentarToASTBuilder(AgentarVisitor):

    def node_meta(self, ctx):
        return {
            "_line": ctx.start.line,
            "_column": ctx.start.column
            #"_oryginal_text": ctx.getText() # Keep the original text if needed
        }

    def visitProgram(self, ctx:AgentarParser.ProgramContext):
        decls = [self.visit(child) for child in ctx.children if child.getText() != '<EOF>']
        mothers = [child for child in decls if isinstance(child, ast.MotherNode)]
        if len(mothers) > 1:
            raise ValueError("Only one mother declaration is allowed in the program.")
        elif len(mothers) < 1:
            raise ValueError("Mother declaration is required in the program.")
        return ast.ProgramNode(declarations=decls, **self.node_meta(ctx))


    def visitMotherDecl(self, ctx:AgentarParser.MotherDeclContext):
        return ast.MotherNode(body=self.visit(ctx.agentBody()), **self.node_meta(ctx))


    def visitAgentDecl(self, ctx:AgentarParser.AgentDeclContext):
        name = ctx.ID().getText()
        body = self.visit(ctx.agentBody())
        return ast.AgentNode(name=name, body=body, **self.node_meta(ctx))


    def visitAgentBody(self, ctx:AgentarParser.AgentBodyContext):
        if ctx.children is None:
            return []
        else:
            return [self.visit(child) for child in ctx.children ]


    def visitFieldSection(self, ctx:AgentarParser.FieldSectionContext):
        decls = [self.visit(decl) for decl in ctx.variableDecl()]
        return ast.FieldSectionNode(declarations=decls, **self.node_meta(ctx))


    def visitBeliefsSection(self, ctx:AgentarParser.BeliefsSectionContext):
        decls = [self.visit(decl) for decl in ctx.variableDecl()]
        return ast.BeliefSectionNode(declarations=decls, **self.node_meta(ctx))


    def visitInitialSection(self, ctx:AgentarParser.InitialSectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.InitSectionNode(statements=stats, **self.node_meta(ctx))


    def visitDestroySection(self, ctx:AgentarParser.DestroySectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.DestroySectionNode(statements=stats, **self.node_meta(ctx))


    def visitSenseSection(self, ctx:AgentarParser.SenseSectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.SeanseSectionNode(statements=stats, **self.node_meta(ctx))


    def visitGoalsSection(self, ctx:AgentarParser.GoalsSectionContext):
        goals = [self.visit(gole) for gole in ctx.goalBlock()]
        merge_condition = self.visit(ctx.expression()) if ctx.expression() else None
        return ast.GoalSectionNode(goals=goals, merge_condition=merge_condition, **self.node_meta(ctx))
    

    def visitGoalBlock(self, ctx:AgentarParser.GoalBlockContext):
        name = ctx.ID().getText()
        conditions = self.visit(ctx.expression()) if ctx.expression() else []
        return ast.GoalBlockNode(name=name, condition=conditions, **self.node_meta(ctx))


    def visitRulesSection(self, ctx:AgentarParser.RulesSectionContext):
        rules = [self.visit(rule) for rule in ctx.whenBlock()]
        return ast.RulesSectionNode(rules=rules, **self.node_meta(ctx))


    def visitReceiveSection(self, ctx:AgentarParser.ReceiveSectionContext):
        name = ctx.ID().getText()
        blocks = [self.visit(block) for block in ctx.whenBlock()]
        return ast.ReceiveSectionNode(name=name, blocks=blocks, **self.node_meta(ctx))


    def visitWhenBlock(self, ctx:AgentarParser.WhenBlockContext):
        conditions = self.visit(ctx.expression()) if ctx.expression() else []
        statements = [self.visit(stat) for stat in ctx.statement()]
        return ast.WhenBlockNode(conditions=conditions, statements=statements, **self.node_meta(ctx))


    def visitActionSection(self, ctx:AgentarParser.ActionSectionContext):
        name = ctx.ID().getText()
        parameters = self.visit(ctx.parameterList()) if ctx.parameterList() else []
        if ctx.type_() is None:
            raise ValueError("Return type is required for action section.")
        return_type = self.visit(ctx.type_())
        body = [self.visit(stat) for stat in ctx.statement()]
        return ast.ActionNode(name=name, parameters=parameters, return_type=return_type, body=body, **self.node_meta(ctx))


    def visitParameterList(self, ctx:AgentarParser.ParameterListContext):
        list_of_param = []
        value_for_param_required = False
        for param in ctx.parameter():
            parameter = self.visit(param)
            list_of_param.append(parameter)
            if parameter.value is not None:
                value_for_param_required = True
            if parameter.value is None and value_for_param_required:
                raise ValueError(f"Error in line {ctx.start.line}: Parameter '{parameter.name}' has no value. Parameter value is required for all parameters after the first one with a value.")
        return list_of_param


    def visitParameter(self, ctx:AgentarParser.ParameterContext):
        param_type = self.visit(ctx.type_()) if ctx.type_() else None
        name = ctx.ID().getText()
        value = self.visit(ctx.expression()) if ctx.expression() else None
        return ast.VariableDeclNode(var_type=param_type, name=name, value=value, **self.node_meta(ctx))


    def visitMessageDecl(self, ctx:AgentarParser.MessageDeclContext):
        name = ctx.ID().getText()
        fields = [self.visit(field) for field in ctx.variableDecl()]
        return ast.MessageDeclNode(name=name, fields=fields, **self.node_meta(ctx))
    

    def visitStatement(self, ctx:AgentarParser.StatementContext):
        return self.visit(ctx.getChild(0))


    def visitPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        return ast.PrintNode(values=[self.visit(expr) for expr in ctx.expression()], **self.node_meta(ctx))


    def visitLoggingStmt(self, ctx:AgentarParser.LoggingStmtContext):
        return ast.LoggingNode(values=[self.visit(expr) for expr in ctx.expression()], **self.node_meta(ctx))


    def visitSendStmt(self, ctx:AgentarParser.SendStmtContext):
        to = self.visit(ctx.expression(0))
        message = self.visit(ctx.expression(1))
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendNode(to=to, message=message, msg_type=msg_type, **self.node_meta(ctx))
    

    def visitSendParentStmt(self, ctx:AgentarParser.SendParentStmtContext):
        to = 'PARENT'  # Sending to parent agent
        message = self.visit(ctx.expression())
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendNode(to=to, message=message, msg_type=msg_type, **self.node_meta(ctx))


    def visitSendChildrenStmt(self, ctx:AgentarParser.SendChildrenStmtContext):
        agent_type = self.visit(ctx.expression(0))           # Sending to all children agents (when param _) or a specific child
        message = self.visit(ctx.expression(1))
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendToChildrenNode(agent_type=agent_type, message=message, msg_type=msg_type, **self.node_meta(ctx))


    def visitSendSiblingStmt(self, ctx:AgentarParser.SendSiblingStmtContext):
        agent_type = self.visit(ctx.expression(0))           # Sending to all siblings agents (when param _) or a specific child
        message = self.visit(ctx.expression(1))
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendToSiblingsNode(agent_type=agent_type, message=message, msg_type=msg_type, **self.node_meta(ctx))


    def visitSpawnStmt(self, ctx:AgentarParser.SpawnStmtContext):
        agent_type = ctx.ID().getText()
        if not agent_type:
            raise ValueError("Agent type is required for spawn statement.")
        args = [self.visit(arg) for arg in ctx.spawnFieldAssign()] if ctx.spawnFieldAssign() else []
        return ast.SpawnNode(agent_type=agent_type, args=args, **self.node_meta(ctx))


    def visitSpawnFieldAssign(self, ctx:AgentarParser.SpawnFieldAssignContext):
        key = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return key, value


    def visitKillStmt(self, ctx:AgentarParser.KillStmtContext):
        if ctx.expression() is None:
            agent_id = None
        else:
            agent_id = self.visit(ctx.expression())
        return ast.KillNode(agent_id=agent_id, **self.node_meta(ctx))
    

    def visitKillChildrenStmt(self, ctx:AgentarParser.KillChildrenStmtContext):
        if ctx.expression() is None:
            agent_type = None
        else:
            agent_type = self.visit(ctx.expression())
        return ast.KillChildrenNode(agent_type=agent_type, **self.node_meta(ctx))


    def visitSleepStmt(self, ctx:AgentarParser.SleepStmtContext):
        return ast.SleepNode(duration=self.visit(ctx.expression()), **self.node_meta(ctx))


    def visitReturnStmt(self, ctx:AgentarParser.ReturnStmtContext):
        return ast.ReturnNode(value=self.visit(ctx.expression()) if ctx.expression() else None, **self.node_meta(ctx))
    

    def visitSenseStmt(self, ctx:AgentarParser.SenseStmtContext):
        return ast.SenseNode(**self.node_meta(ctx))


    def visitGoalCheckStmt(self, ctx:AgentarParser.GoalCheckStmtContext):
        goal_name = ctx.ID().getText()
        return ast.GoalCheckNode(goal_name=goal_name, **self.node_meta(ctx))
    

    def visitGetTimeStmt(self, ctx:AgentarParser.GetTimeStmtContext):
        return ast.GetTimeNode(**self.node_meta(ctx))
    

    def visitDictDelStmt(self, ctx:AgentarParser.DictDelStmtContext):
        base = self.visit(ctx.expression(0)) 
        key = self.visit(ctx.expression(1))  
        return ast.DictDelNode(base=base, key=key, **self.node_meta(ctx))


    def visitListAddStmt(self, ctx:AgentarParser.ListAddStmtContext):
        base = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))
        return ast.ListAddNode(base=base, value=value, **self.node_meta(ctx))
    

    def visitIfStmt(self, ctx:AgentarParser.IfStmtContext):
        conditions = self.visit(ctx.expression()) if ctx.expression() else []
        statements = self.visit(ctx.ifBlock()) if ctx.ifBlock() else []
        elifBlocks = [self.visit(elif_block) for elif_block in ctx.elifBlock()] if ctx.elifBlock() else []
        elseStmt = self.visit(ctx.elseBlock()) if ctx.elseBlock() else None
        return ast.IfStmtNode(conditions=conditions, statements=statements, elifBlocks=elifBlocks, elseStmt=elseStmt, **self.node_meta(ctx))


    def visitIfBlock(self, ctx:AgentarParser.IfBlockContext):
        return [self.visit(stat) for stat in ctx.statement()]
    

    def visitElifBlock(self, ctx:AgentarParser.ElifBlockContext):
        condition = self.visit(ctx.expression()) if ctx.expression() else []
        statement = self.visit(ctx.ifBlock()) if ctx.ifBlock() else []
        return ast.ElifNode(condition=condition, statement=statement, **self.node_meta(ctx))


    def visitElseBlock(self, ctx:AgentarParser.ElseBlockContext):
        return [self.visit(stat) for stat in ctx.statement()]


    def visitForStmt(self, ctx:AgentarParser.ForStmtContext):
        initialize = self.visit(ctx.variableDecl())
        condition = self.visit(ctx.expression()) if ctx.expression() else None
        update = self.visit(ctx.forAssignExpr()) if ctx.forAssignExpr() else None
        body = self.visit(ctx.forBody()) if ctx.forBody() else []
        if not initialize or not condition or not update or not body:
            raise ValueError("For loop requires initialization, condition, update, and body.")
        return ast.ForLoopNode(initialize=initialize, condition=condition, update=update, body=body, **self.node_meta(ctx))
        

    def visitForBody(self, ctx:AgentarParser.ForBodyContext):
        return [self.visit(stat) for stat in ctx.statement()]


    def visitForAssignExpr(self, ctx:AgentarParser.ForAssignExprContext):
        target = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))
        return ast.AssignmentNode(target=target, value=value, **self.node_meta(ctx))


    def visitWhileStmt(self, ctx:AgentarParser.WhileStmtContext):
        condition = self.visit(ctx.expression()) if ctx.expression() else None
        body = [self.visit(stat) for stat in ctx.statement()]
        if not condition or not body:
            raise ValueError("While loop requires a condition and a body.")
        return ast.WhileLoopNode(condition=condition, body=body, **self.node_meta(ctx))


    def visitBreakStmt(self, ctx:AgentarParser.BreakStmtContext):
        return ast.BreakNode(**self.node_meta(ctx))
    

    def visitContinueStmt(self, ctx:AgentarParser.ContinueStmtContext):
        return ast.ContinueNode(**self.node_meta(ctx))
    

    def visitDoStmt(self, ctx:AgentarParser.DoStmtContext):
        name = ctx.ID().getText()
        variables = [self.visit(var) for var in ctx.expression()] if ctx.expression() else []
        return ast.DoNode(name=name, variables=variables, **self.node_meta(ctx))
    

    # TODO:  deal with parameters in declaration. What if there is the address of expression?
    def visitVarDecl(self, ctx:AgentarParser.VarDeclContext):
        var_type = self.visit(ctx.type_())
        name = ctx.ID().getText()
        value = self.visit(ctx.expression()) if ctx.expression() else None
        return ast.VariableDeclNode(var_type=var_type, name=name, value=value, **self.node_meta(ctx))


    def visitMessageVarDecl(self, ctx:AgentarParser.MessageVarDeclContext):
        message_type = ctx.ID(0).getText()
        name = ctx.ID(1).getText()
        message = self.visit(ctx.messageInit())
        return ast.MessageVarDeclNode(name=name, message_type=message_type, message=message, **self.node_meta(ctx))


    def visitAssignment(self, ctx:AgentarParser.AssignmentContext):
        target = self.visit(ctx.expression())
        value = self.visit(ctx.assignValue())
        return ast.AssignmentNode(target=target, value=value, **self.node_meta(ctx))


    def visitSimpleAssignValue(self, ctx:AgentarParser.SimpleAssignValueContext):
        return self.visit(ctx.expression())


    def visitGetTimeAssignValue(self, ctx:AgentarParser.GetTimeAssignValueContext):
        return self.visit(ctx.getTimeStmt())


    def visitSpawnAssignValue(self, ctx:AgentarParser.SpawnAssignValueContext):
        return self.visit(ctx.spawnStmt())


    def visitDoAssignValue(self, ctx:AgentarParser.DoAssignValueContext):
        return self.visit(ctx.doStmt())


    def visitGoalCheckAssignValue(self, ctx:AgentarParser.GoalCheckAssignValueContext):
        return self.visit(ctx.goalCheckStmt())


    def visitAndExpr(self, ctx:AgentarParser.AndExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='AND', left=left, right=right, **self.node_meta(ctx))


    def visitSelfAccessExpr(self, ctx: AgentarParser.SelfAccessExprContext):
        if type(ctx.ID()) is list:
            path = ["self"] + [id_.getText() for id_ in ctx.ID()]
        else: 
            path = ['self', ctx.ID().getText()]
        return ast.SelfAccessNode(path=path, **self.node_meta(ctx))


    def visitLeqExpr(self, ctx:AgentarParser.LeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='<=', left=left, right=right, **self.node_meta(ctx))


    def visitXorExpr(self, ctx:AgentarParser.XorExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='XOR', left=left, right=right, **self.node_meta(ctx))
    

    def visitAbsExpr(self, ctx:AgentarParser.AbsExprContext):
        base = self.visit(ctx.expression())
        return ast.AbsExprNode(base=base, **self.node_meta(ctx))
    

    def visitDerefExpr(self, ctx:AgentarParser.DerefExprContext):
        pointer = self.visit(ctx.expression())
        return ast.DerefExprNode(pointer=pointer, **self.node_meta(ctx))


    def visitGeqExpr(self, ctx:AgentarParser.GeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='>=', left=left, right=right, **self.node_meta(ctx))
    

    def visitNegExpr(self, ctx:AgentarParser.NegExprContext):
        base = self.visit(ctx.expression())
        return ast.NegExprNode(base=base, **self.node_meta(ctx))
    

    def visitLenExpr(self, ctx:AgentarParser.LenExprContext):
        base = self.visit(ctx.expression())
        return ast.LenNode(base=base, **self.node_meta(ctx))


    def visitMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        if type(ctx.ID()) is list:
            path = ['msg'] + [id_.getText() for id_ in ctx.ID()]
        else: 
            path = ['msg', ctx.ID().getText()]
        return ast.MsgAccessNode(path=path, **self.node_meta(ctx))


    def visitLtExpr(self, ctx:AgentarParser.LtExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='<', left=left, right=right, **self.node_meta(ctx))


    def visitGtExpr(self, ctx:AgentarParser.GtExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='>', left=left, right=right, **self.node_meta(ctx))
    

    def visitTypeExpr(self, ctx:AgentarParser.TypeExprContext):
        base = self.visit(ctx.expression())
        return ast.TypeExprNode(base=base, **self.node_meta(ctx))
    

    def visitTupleExpr(self, ctx:AgentarParser.TupleExprContext):
        elements = [self.visit(expr) for expr in ctx.tupleLiteral().expression()]
        return ast.TupleLiteralNode(elements=elements, **self.node_meta(ctx))


    def visitOrExpr(self, ctx:AgentarParser.OrExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='OR', left=left, right=right, **self.node_meta(ctx))


    def visitIndexExpr(self, ctx:AgentarParser.IndexExprContext):
        name = self.visit(ctx.expression(0))   # np. x
        index = self.visit(ctx.expression(1))  # np. 3
        return ast.IndexAccessNode(name=name, index=index, **self.node_meta(ctx))
    

    def visitSliceToExpr(self, ctx:AgentarParser.SliceToExprContext):
        name = self.visit(ctx.expression(0))
        start = None # means slice from the beginning
        end = self.visit(ctx.expression(1))
        return ast.SliceAccessNode(name=name, start=start, end=end, **self.node_meta(ctx))


    def visitSliceFromExpr(self, ctx:AgentarParser.SliceFromExprContext):
        name = self.visit(ctx.expression(0))
        start = self.visit(ctx.expression(1))
        end = None # means no end specified, slice to the end
        return ast.SliceAccessNode(name=name, start=start, end=end, **self.node_meta(ctx))


    def visitSliceRangeExpr(self, ctx:AgentarParser.SliceRangeExprContext):
        name = self.visit(ctx.expression(0))
        start = self.visit(ctx.expression(1))
        end = self.visit(ctx.expression(2))
        return ast.SliceAccessNode(name=name, start=start, end=end, **self.node_meta(ctx))


    def visitAgentIdExpr(self, ctx:AgentarParser.AgentIdExprContext):
        text = ctx.getText()
        return ast.AgentIdNode(path=text, **self.node_meta(ctx))
    

    def visitModuloExpr(self, ctx:AgentarParser.ModuloExprContext): 
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='%', left=left, right=right, **self.node_meta(ctx))


    def visitDictValuesExpr(self, ctx:AgentarParser.DictValuesExprContext):
        base = self.visit(ctx.expression())
        return ast.DictValuesNode(base=base, **self.node_meta(ctx))


    def visitBeliefAccessExpr(self, ctx:AgentarParser.BeliefAccessExprContext):
        if type(ctx.ID()) is list:
            path = ["bel"] + [id_.getText() for id_ in ctx.ID()]
        else: 
            path = ['bel', ctx.ID().getText()]
        return ast.BelAccessNode(path=path, **self.node_meta(ctx))


    def visitVarReference(self, ctx:AgentarParser.VarReferenceContext):
        name = ctx.getText()
        return ast.VarRefNode(name=name, **self.node_meta(ctx))


    def visitMulDivExpr(self, ctx:AgentarParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '*':
            op = '*'
        else:
            op = '/'
        return ast.BinaryOpNode(op=op, left=left, right=right, **self.node_meta(ctx))


    # def visitAddressOfExpr(self, ctx:AgentarParser.AddressOfExprContext):
    #     pass 
    # # TODO: implement address of expression


    def visitAddressOfExpr(self, ctx:AgentarParser.AddressOfExprContext):
        variable = self.visit(ctx.expression())
        return ast.AddressOfExprNode(variable=variable, **self.node_meta(ctx))
    

    # def visitDeepCopyExpr(self, ctx:AgentarParser.DeepCopyExprContext):
    #     return ast.DeepCopyNode(variable=self.visit(ctx.expression()), **self.node_meta(ctx))


    def visitEqExpr(self, ctx:AgentarParser.EqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='==', left=left, right=right, **self.node_meta(ctx))


    def visitNeqExpr(self, ctx:AgentarParser.NeqExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='!=', left=left, right=right, **self.node_meta(ctx))
    

    def visitRandomExpr(self, ctx:AgentarParser.RandomExprContext):
        start = self.visit(ctx.expression(0)) if ctx.expression(0) else None
        end = self.visit(ctx.expression(1)) if ctx.expression(1) else None
        return ast.RandomExprNode(start=start, end=end, **self.node_meta(ctx))


    def visitLiteralExpr(self, ctx:AgentarParser.LiteralExprContext):
        return self.visit(ctx.literal())
    

    def visitNoneExpr(self, ctx:AgentarParser.NoneExprContext):
        return ast.NoneExprNode(**self.node_meta(ctx))


    def visitMsgTypeValueExpr(self, ctx:AgentarParser.MsgTypeValueExprContext):
        return ast.LiteralNode(value=ctx.getText(), **self.node_meta(ctx))


    def visitNotExpr(self, ctx:AgentarParser.NotExprContext):
        left = self.visit(ctx.expression())
        return ast.BinaryOpNode(op='NOT', left=left, right=None, **self.node_meta(ctx))


    def visitListExpr(self, ctx:AgentarParser.ListExprContext):
        elements = [self.visit(expr) for expr in ctx.listLiteral().expression()]
        return ast.ListLiteralNode(elements=elements, **self.node_meta(ctx))


    def visitParenExpr(self, ctx:AgentarParser.ParenExprContext):
        return self.visit(ctx.expression())


    def visitParentAccessExpr(self, ctx:AgentarParser.ParentAccessExprContext):
        base = self.visit(ctx.expression())
        return ast.ParentShadowNode(base=base, **self.node_meta(ctx))
    

    def visitMessageInitExpr(self, ctx:AgentarParser.MessageInitExprContext):
        return self.visit(ctx.messageInit())
    

    def visitDictKeysExpr(self, ctx:AgentarParser.DictKeysExprContext):
        base = self.visit(ctx.expression())
        return ast.DictKeysNode(base=base, **self.node_meta(ctx))
    

    def visitDictGetExpr(self, ctx:AgentarParser.DictGetExprContext):
        base = self.visit(ctx.expression(0))
        key = self.visit(ctx.expression(1))
        return ast.DictGetNode(base=base, key=key, **self.node_meta(ctx))


    def visitAddSubExpr(self, ctx:AgentarParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.text == '+':
            op = '+'
        else:
            op = '-'
        return ast.BinaryOpNode(op=op, left=left, right=right, **self.node_meta(ctx))
    

    def visitMessageInit(self, ctx:AgentarParser.MessageInitContext):
        message_type = ctx.ID().getText()
        fields = {}
        for field_ctx in ctx.messageFieldAssign():
            key = field_ctx.ID().getText()  # nazwa pola, np. "task"
            value = self.visit(field_ctx.expression())  # wartość pola, np. LiteralNode("clean")
            fields[key] = value
        return ast.MessageInitNode(message_type=message_type, fields=fields, **self.node_meta(ctx))


    def visitDictLiteral(self, ctx:AgentarParser.DictLiteralContext):
        keys = []
        values = []
        for entry in ctx.dictEntry():
            keys.append(self.visit(entry.key))  # get the key expression
            values.append(self.visit(entry.value))
        return ast.DictLiteralNode(keys=keys, values=values, **self.node_meta(ctx))
    

    def visitBasicType(self, ctx:AgentarParser.BasicTypeContext):
        return ast.BaseTypeNode(name=ctx.bodyType().getText(), **self.node_meta(ctx))
    

    def visitPointerType(self, ctx:AgentarParser.PointerTypeContext):
        inner_type = self.visit(ctx.type_())
        return ast.PointerTypeNode(inner_type=inner_type, **self.node_meta(ctx))


    def visitListType(self, ctx:AgentarParser.ListTypeContext):
        inner_type = self.visit(ctx.type_())
        return ast.ListTypeNode(inner_type=inner_type, **self.node_meta(ctx))


    def visitDictType(self, ctx:AgentarParser.DictTypeContext):
        key_type = self.visit(ctx.key)
        value_type = self.visit(ctx.value)
        return ast.DictTypeNode(key_type=key_type, value_type=value_type, **self.node_meta(ctx))


    def visitTupleType(self, ctx:AgentarParser.TupleTypeContext):
        elements_type = [self.visit(type_ctx) for type_ctx in ctx.type_()]
        return ast.TupleTypeNode(elements_type=elements_type, **self.node_meta(ctx))
    

    def visitAnyType(self, ctx:AgentarParser.AnyTypeContext):
        return ast.AnyTypeNode(**self.node_meta(ctx))


    def visitIntLiteral(self, ctx:AgentarParser.IntLiteralContext):
        return ast.LiteralNode(value=int(ctx.getText()), **self.node_meta(ctx))


    def visitFloatLiteral(self, ctx:AgentarParser.FloatLiteralContext):
        return ast.LiteralNode(value=float(ctx.getText()), **self.node_meta(ctx))


    def visitStringLiteral(self, ctx:AgentarParser.StringLiteralContext):
        return ast.LiteralNode(value=ctx.getText()[1:-1], **self.node_meta(ctx))  # Remove quotes


    def visitBoolLiteral(self, ctx:AgentarParser.BoolLiteralContext):
        return ast.LiteralNode(value=ctx.getText() == 'True', **self.node_meta(ctx))  # Convert to boolean


    def visitMsgTypeValue(self, ctx:AgentarParser.MsgTypeValueContext):
        return ast.LiteralNode(value=ctx.getText(), **self.node_meta(ctx))  # Return the message type value as a literal
    