grammar Agentar;

// PARSER RULES ---------------------------------------

program 
    : (motherDecl | agentDecl | messageDecl)* EOF
    ;

statement
    : printStmt
    | ifStmt
    | forStmt
    | whileStmt
    | breakStmt
    | variableDecl
    | assignment
    | sendStmt
    | spawnStmt
    | killStmt
    | doStmt
    | sleepStmt
    | returnStmt
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
    beliefsSection?
    senseSection?
    goalsSection?
    rulesSection?
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

beliefsSection
    : 'beliefs' '{' variableDecl* '}'
    ;

senseSection
    : 'sense' '{' statement* '}'
    ;

goalsSection
    : 'goals' '{' goalBlock* '}'
    ;

goalBlock
    : ID ':' expression ';'
    ;

rulesSection
    : 'rules' '{' whenBlock* '}'
    ;

receiveSection
    : 'receive' ID '{' whenBlock* '}'
    ;

whenBlock
    : 'when' '(' expression ')' 'then' '{' statement* '}'
    | 'when' '(' ')' 'then' '{' statement* '}'
    ;

actionSection
    : 'action' ID '(' parameterList? ')' ':' type '{' statement* '}'
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : type ID
    ;
// === End agent declaration

// === Message declaration
messageDecl
    : MESSAGE ID '{' variableDecl* '}'
    ;
// === end of message declaration

// === Statements
sendStmt
    : 'send' '(' expression ',' expression (',' ('msg_type=' msgTypeValue | msgTypeValue))? ')' ';'  
    ;

spawnStmt
    : 'spawn' '(' ID (',' '['expression (',' expression)*']')? ')' ';'
    ;

killStmt  
    : 'kill' '(' expression? ')' ';'
    ;

sleepStmt  
    : 'sleep' '('expression')' ';'
    ;

returnStmt
    : 'return' expression ';'
    ;


messageInit
    : ID '(' (messageFieldAssign (',' messageFieldAssign)*)? ')'
    ;

messageFieldAssign
    : ID '=' expression
    ;

printStmt
    : 'print' '(' expression (',' expression)* ')' ';'
    ;

ifStmt
    : 'if' '(' expression ')' blockOrStmt (elseStmt)?
    ;   


blockOrStmt 
    : '{' statement* '}'
    | statement
    ;


elseStmt
    : 'else' '{' statement* '}'
    ;


forStmt
    : 'for' '(' variableDecl expression ';' forAssignExpr ')' '{' forBody '}'
    ;

forBody
    : statement*
    ;

forAssignExpr
    : ID '=' expression
    ;

whileStmt
    : 'while' '(' expression ')' '{' statement* '}'
    ;

breakStmt
    : 'break' ';'
    ;
    

variableDecl
    : type ID ('=' expression)? ';'                       # VarDecl
    ;

assignment
    : ID '=' expression ';'                               # SimpleAssign
    | ID '[' expression ']' '=' expression ';'            # IndexAssign
    | ID '['']' '=' expression ';'                        # ListAddAssign
    | ID '=' spawnStmt                                    # SpawnAssign
    | ID '=' doStmt                                       # DoAssign
    | expression '=' doStmt                               # DoSelfAssign
    | expression'[' expression ']' '=' expression ';'     # SelfIndexAssign
    | expression'['']' '=' expression ';'                 # SelfListAddAssign
    | expression '=' expression ';'                       # SelfAssign
 
    ;

doStmt
    : 'do(' ID (',' '['expression (',' expression)*']')? ')' ';' 
    ;

type: 'int' | 'float' | 'string' | 'bool' | 'void' | 'list' | 'map' | 'agentid';

expression
    : expression op=OR expression     # OrExpr
    | expression op=AND expression    # AndExpr
    | expression op=XOR expression    # XorExpr
    | expression op=EQ expression     # EqExpr
    | expression op=NEQ expression    # NeqExpr
    | expression op=LT expression     # LtExpr
    | expression op=GT expression     # GtExpr
    | expression op=LEQ expression    # LeqExpr
    | expression op=GEQ expression    # GeqExpr
    | expression op=('+'|'-') expression # AddSubExpr
    | expression op=('*'|'/') expression # MulDivExpr
    | NOT expression                 # NotExpr
    | '(' expression ')'             # ParenExpr
    | MSG '.' ID                     # MessageAccessExpr
    | SELF '.' ID                    # SelfAccessExpr
    | expression '[' expression ']'  # IndexExpr
    | messageInit                    # MessageInitExpr
    | msgTypeValue                   # MsgTypeValueExpr
    | listLiteral                    # ListExpr
    | mapLiteral                     # MapExpr
    | literal                        # LiteralExpr
    | ID                             # VarReference
    | AGENTID                        # AgentIdExpr
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
MSG: 'msg';
SELF: 'self';
MSGTYPE_INFORM:  'inform';
MSGTYPE_ASK:     'ask';
MSGTYPE_REQUEST: 'request';
MSGTYPE_CONFIRM: 'confirm';
MSGTYPE_DENY:    'deny';


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
LEQ: '<=';
GEQ: '>=';
NOT: '!';
AND: '&&';
OR: '||';
XOR: '^';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
BREAK: 'break';
PRINT: 'print';
AGENT: 'agent';
VOID: 'void';
KILL: 'kill';
SEND: 'send';
SPAWN: 'spawn';
DO: 'do';
SLEEP: 'sleep';
RETURN: 'return';



INT: '-'? [0-9]+;
FLOAT: '-'? [0-9]+ '.' [0-9]+;
AGENTID: '.' [0-9]+ ('.' [0-9]+)*;
BOOL: 'true' | 'false';
STRING: '"' .*? '"';
// function and variables names 
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Whitespace and comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;