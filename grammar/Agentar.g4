grammar Agentar;

program: statement+ EOF;

statement: 
    printStmt ';' 
    | variableDecl ';'
    | assignment ';';

printStmt: 'print' '(' expression ')';
variableDecl: type ID ('=' expression)?;
assignment: ID '=' expression;

type: 'int' | 'float' | 'string' | 'bool';

expression:
    expression op=('*'|'/') expression # MulDivExpr
    | expression op=('+'|'-') expression # AddSubExpr
    | expression op=('=='|'!='|'<'|'>') expression # CompareExpr
    | literal                           # LiteralExpr
    | ID                                # VarReference
    | '(' expression ')'                # ParenExpr
    ;

literal: 
    INT     # IntLiteral
    | FLOAT # FloatLiteral
    | STRING # StringLiteral
    | BOOL   # BoolLiteral
    ;

// Lexer rules
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
WS: [ \t\r\n]+ -> skip;