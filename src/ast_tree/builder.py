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
        return [self.visit(child) for child in ctx.children]


    def visitFieldSection(self, ctx:AgentarParser.FieldSectionContext):
        decls = [self.visit(decl) for decl in ctx.variableDecl()]
        return ast.FieldSectionNode(declarations=decls)


    def visitInitialSection(self, ctx:AgentarParser.InitialSectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.InitSectionNode(statements=stats)

 
    def visitDestroySection(self, ctx:AgentarParser.DestroySectionContext):
        stats = [self.visit(stat) for stat in ctx.statement()]
        return ast.DestroySectionNode(statements=stats)


    def visitReceiveSection(self, ctx:AgentarParser.ReceiveSectionContext):
        name = ctx.ID().getText()
        blocks = [self.visit(block) for block in ctx.whenBlock()]
        return ast.ReceiveSectionNode(name=name, blocks=blocks)


    def visitWhenBlock(self, ctx:AgentarParser.WhenBlockContext):
        conditions = [self.visit(cond) for cond in ctx.expression()]
        statements = [self.visit(stat) for stat in ctx.statement()]
        return ast.WhenBlockNode(conditions=conditions, statements=statements)


    def visitActionSection(self, ctx:AgentarParser.ActionSectionContext):
        name = ctx.ID().getText()
        parameters = [self.visit(param) for param in ctx.parameterList().parameter()] if ctx.parameterList() else []
        if ctx.type_() is None:
            raise ValueError("Return type is required for action section.")
        return_type = ctx.type_().getText() 
        body = [self.visit(stat) for stat in ctx.statement()]
        return ast.ActionNode(name=name, parameters=parameters, return_type=return_type, body=body)


    def visitParameter(self, ctx:AgentarParser.ParameterContext):
        param_type = ctx.type_().getText() if ctx.type_() else None
        name = ctx.ID().getText()
        if not param_type or not name:
            raise ValueError("Parameter type and name are required.")
        return ast.ParameterNode(param_type=param_type, name=name)
    

    def visitSelfAccessExpr(self, ctx: AgentarParser.SelfAccessExprContext):
        return ast.SelfAccessNode(path=["self"] + [id_.getText() for id_ in ctx.ID()])


    def visitMessageDecl(self, ctx:AgentarParser.MessageDeclContext):
        name = ctx.ID().getText()
        fields = [self.visit(field) for field in ctx.variableDecl()]
        return ast.MessageDeclNode(name=name, fields=fields)


    def visitSendStmt(self, ctx:AgentarParser.SendStmtContext):
        to = self.visit(ctx.expression(0))
        message = self.visit(ctx.expression(1))
        msg_type = ctx.msgTypeValue().getText() if ctx.msgTypeValue() else None
        return ast.SendNode(to=to, message=message, msg_type=msg_type)


    def visitSpawnStmt(self, ctx:AgentarParser.SpawnStmtContext):
        agent_type = ctx.ID().getText()
        if not agent_type:
            raise ValueError("Agent type is required for spawn statement.")
        args = [self.visit(arg) for arg in ctx.expression()]
        return ast.SpawnNode(agent_type=agent_type, args=args)
    
    def visitKillStmt(self, ctx:AgentarParser.KillStmtContext):
        return ast.KillNode()


    def visitDoStmt(self, ctx:AgentarParser.DoStmtContext):
        name = ctx.ID().getText()
        variables = [self.visit(var) for var in ctx.expression()] if ctx.expression() else []
        return ast.DoNode(name=name, variables=variables)


    def visitMessageInit(self, ctx:AgentarParser.MessageInitContext):
        message_type = ctx.ID().getText()
        fields = {}
        for field_ctx in ctx.messageFieldAssign():
            key = field_ctx.ID().getText()  # nazwa pola, np. "task"
            value = self.visit(field_ctx.expression())  # wartość pola, np. LiteralNode("clean")
            fields[key] = value
        return ast.MessageInitNode(message_type=message_type, fields=fields)


    def visitPrintStmt(self, ctx:AgentarParser.PrintStmtContext):
        return ast.PrintNode(values=[self.visit(expr) for expr in ctx.expression()])


    def visitVariableDecl(self, ctx:AgentarParser.VariableDeclContext):
        var_type = ctx.type_().getText()
        name = ctx.ID().getText()
        value = self.visit(ctx.expression()) if ctx.expression() else None
        return ast.VariableDeclNode(var_type=var_type, name=name, value=value)


    def visitSimpleAssign(self, ctx: AgentarParser.SimpleAssignContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return ast.AssignmentNode(target=target, value=value)

    def visitIndexAssign(self, ctx: AgentarParser.IndexAssignContext):
        base = ctx.ID().getText()    # np. x
        index = self.visit(ctx.expression(0))   # np. 3
        value = self.visit(ctx.expression(1))   # np. 10
        return ast.AssignmentNode(target=base, index=index, value=value)
    
    def visitSpawnAssign(self, ctx: AgentarParser.SpawnAssignContext):
        target = ctx.ID().getText()
        value = self.visit(ctx.spawnStmt())
        return ast.AssignmentNode(target=target, value=value)
    

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


    def visitMessageAccessExpr(self, ctx:AgentarParser.MessageAccessExprContext):
        path = ['msg'] + [id_.getText() for id_ in ctx.ID()]
        return ast.MsgAccessNode(path=path)


    def visitLtExpr(self, ctx:AgentarParser.LtExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='<', left=left, right=right)


    def visitGtExpr(self, ctx:AgentarParser.GtExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='>', left=left, right=right)


    def visitOrExpr(self, ctx:AgentarParser.OrExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return ast.BinaryOpNode(op='OR', left=left, right=right)


    def visitIndexExpr(self, ctx:AgentarParser.IndexExprContext):
        base = self.visit(ctx.expression(0))   # np. x
        index = self.visit(ctx.expression(1))  # np. 3
        return ast.IndexAccessNode(base=base, index=index)


    def visitAgentIdExpr(self, ctx:AgentarParser.AgentIdExprContext):
        text = ctx.getText()
        return ast.AgentIdNode(path=text)


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


    def visitMessageInit(self, ctx:AgentarParser.MessageInitContext):
        message_type = ctx.ID().getText()
        fields = {}
        for field_assign in ctx.messageFieldAssign():
            key = field_assign.ID().getText()
            value = self.visit(field_assign.expression())
            fields[key] = value
        return ast.MessageInitNode(message_type=message_type, fields=fields)


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