grammar Agentar;

// PARSER RULES ---------------------------------------

program 
    : (motherDecl | agentDecl)* EOF
    ;

statement: 
    printStmt ';' 
    | variableDecl ';'
    | assignment ';'
    ;

// === Mother declaration
motherDecl
    : 'agent' 'mother' '{' agentBody '}'
    ;


// === Agent declaration
agentDecl
    : 'agent' ID '{' agentBody '}'
    ;

agentBody
    : fieldSection actionSection*
    ;

fieldSection
    : 'fields' '{' fieldDecl* '}'
    ;

fieldDecl
    : type ID ('=' literal)? ';'
    ;

actionSection
    : 'action' ID '(' ')' ':' type block
    ;

block
    : '{' statement* '}'
    ;
// === End agent declaration

printStmt: 'print' '(' expression ')';

variableDecl: type ID ('=' expression)?;

assignment
    : ID '=' expression                                # SimpleAssign
    | expression '[' expression ']' '=' expression     # IndexAssign
    ;

type: 'int' | 'float' | 'string' | 'bool' | 'void' | 'list' | 'map';

expression
    : NOT expression                         # NotExpr
    | expression AND expression              # AndExpr
    | expression OR expression               # OrExpr
    | expression XOR expression              # XorExpr
    | expression op=('*'|'/') expression    # MulDivExpr
    | expression op=('+'|'-') expression    # AddSubExpr
    | listLiteral                           # ListExpr
    | mapLiteral                            # MapExpr
    | literal                               # LiteralExpr
    | ID                                    # VarReference
    | '(' expression ')'                    # ParenExpr
    | expression '[' expression ']'         # IndexExpr
    ;

listLiteral
    : '[' (expression (',' expression)*)? ']'
    ;

mapLiteral
    : '{' (ID ':' expression (',' ID ':' expression)*)? '}'
    ;

literal
    : INT       # IntLiteral
    | FLOAT     # FloatLiteral
    | STRING    # StringLiteral
    | BOOL      # BoolLiteral
    ;

// === End of parser rules


// LEXER RULES ---------------------------------------
ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';

// Symbols
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
COLON: ':';
SEMI: ';';
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
NOT: 'NOT';
AND: 'AND';
OR: 'OR';
XOR: 'XOR';

// Whitespace and comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;