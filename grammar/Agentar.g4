grammar Agentar;

// PARSER RULES ---------------------------------------

program 
    : (motherDecl | agentDecl | messageDecl)* EOF
    ;

statement
    : printStmt
    | variableDecl
    | assignment
    | sendStmt
    | spawnStmt
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
    : fieldSection? 
    initialSection?
    destroySection?
    receiveSection*
    actionSection*
    ;

fieldSection
    : 'fields' '{' variableDecl* '}'
    ;

initialSection
    : 'initialize' '{' statement* '}'
    ;

destroySection
    : 'destroy' '{' statement* '}'
    ;

receiveSection
    : 'receive' ID '{' (whenBlock+ | statement*) '}'
    ;

whenBlock
    : 'when' '(' expression* ')' 'then' '{' statement* '}'
    ;

actionSection
    : 'action' ID '(' parameterList* ')' ':' type '{' statement* '}'
    ;
// === End agent declaration

// === Message declaration
messageDecl
    : MESSAGE ID '{' variableDecl? '}'
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : type ID
    ;

// === end of message declaration

// === Statements
sendStmt
    : 'send' '(' expression ',' expression (',' ('msg_type=' msgTypeValue | msgTypeValue))? ')' ';'  
    ;

spawnStmt
    : 'spawn' '(' ID (',' expression)* ')' ';'
    ;


messageInit
    : ID '(' messageFieldAssign (',' messageFieldAssign)* ')'
    ;

messageFieldAssign
    : ID '=' expression
    ;

printStmt
    : 'print' '(' expression (',' expression)* ')' ';'
    ;

variableDecl
    : type ID ('=' expression)? ';'
    ;

assignment
    : ID '=' expression ';'                               # SimpleAssign
    | expression '[' expression ']' '=' expression ';'    # IndexAssign
    ;

type: 'int' | 'float' | 'string' | 'bool' | 'void' | 'list' | 'map' ;

expression
    : NOT expression                         # NotExpr
    | expression AND expression              # AndExpr
    | expression OR expression               # OrExpr
    | expression XOR expression              # XorExpr
    | expression op=('*'|'/') expression     # MulDivExpr
    | expression op=('+'|'-') expression     # AddSubExpr
    | expression EQ expression               # EqExpr
    | 'msg' ('.' ID)+                        # MessageAccessExpr
    | listLiteral                            # ListExpr
    | mapLiteral                             # MapExpr
    | literal                                # LiteralExpr
    | ID                                     # VarReference
    | '(' expression ')'                     # ParenExpr
    | expression '[' expression ']'          # IndexExpr
    | AGENTID                                # AgentIdExpr
    | messageInit                            # MessageInitExpr
    | msgTypeValue                           # MsgTypeValueExpr
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

msgTypeValue
    : MSGTYPE_INFORM
    | MSGTYPE_ASK
    | MSGTYPE_REQUEST
    | MSGTYPE_CONFIRM
    | MSGTYPE_DENY
    ;

// === End of parser rules


// LEXER RULES --------------------------------------
MESSAGE: 'message';
MSGTYPE_INFORM:  'inform';
MSGTYPE_ASK:     'ask';
MSGTYPE_REQUEST: 'request';
MSGTYPE_CONFIRM: 'confirm';
MSGTYPE_DENY:    'deny';

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
AGENTID: '.' [0-9]+ ('.' [0-9]+)*;

// function and variables names 
ID: [a-zA-Z_][a-zA-Z0-9_]*;

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