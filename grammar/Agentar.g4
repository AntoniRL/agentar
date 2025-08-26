grammar Agentar;

// PARSER RULES ---------------------------------------

program 
    : (motherDecl | agentDecl | messageDecl)* EOF
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
    beliefsSection?
    goalsSection?
    initialSection?
    senseSection?
    rulesSection?
    destroySection?
    receiveSection*
    actionSection*
    ;

fieldSection
    : 'fields' '{' variableDecl* '}'
    ;

beliefsSection
    : 'beliefs' '{' variableDecl* '}'
    ;

initialSection
    : 'initialize' '{' statement* '}'
    ;

senseSection
    : 'sense' '{' statement* '}'
    ;

goalsSection
    : 'goals' '{' goalBlock* '}' ( 'merge' '(' expression')' )?
    ;

goalBlock
    : ID ':' expression ';'
    ;

rulesSection
    : 'rules' '{' whenBlock* '}'
    ;

destroySection
    : 'destroy' '{' statement* '}'
    ;

receiveSection
    : 'receive' ID '{' whenBlock* '}'
    ;

whenBlock
    : 'when' '(' expression* ')' 'then' '{' statement* '}'
    ;

actionSection
    : 'action' ID '(' parameterList? ')' ':' type '{' statement* '}'
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : type ID ('=' expression)?
    | type star=STAR ID ('=' expression)?
    ;
// === End agent declaration

// === Message declaration
messageDecl
    : MESSAGE ID '{' variableDecl* '}'
    ;
// === end of message declaration


// === Statements
statement
    : printStmt
    | loggingStmt
    | ifStmt
    | forStmt
    | whileStmt
    | breakStmt
    | continueStmt
    | variableDecl
    | assignment
    | listAddStmt
    | sendStmt
    | sendParentStmt
    | sendChildrenStmt
    | sendSiblingStmt
    | spawnStmt
    | killStmt
    | killChildrenStmt
    | doStmt
    | sleepStmt
    | returnStmt
    | senseStmt
    | goalCheckStmt
    | getTimeStmt
    | dictDelStmt
    ;


printStmt
    : 'print' '(' expression (',' expression)* ')' ';'
    ;

loggingStmt
    : 'logging' '(' expression (',' expression)* ')' ';'
    ;

sendStmt
    : 'send' '(' expression ',' expression (','  msgTypeValue)? ')' ';'  
    ;

sendParentStmt
    : 'send2parent' '(' expression (',' msgTypeValue)? ')' ';'
    ;

sendChildrenStmt
    : 'send2children' '(' expression ',' expression (',' msgTypeValue)? ')' ';'
    ;

sendSiblingStmt
    : 'send2siblings' '(' expression ',' expression (',' msgTypeValue)? ')' ';'
    ;

spawnStmt
    : 'spawn' '(' ID (',' '{'spawnFieldAssign (',' spawnFieldAssign)*'}')? ')' ';'
    ;

spawnFieldAssign
    : ID ':' expression
    ;

killStmt  
    : 'kill' '(' expression? ')' ';'
    ;

killChildrenStmt
    : 'killChildren' '(' expression? ')' ';'
    ;

sleepStmt  
    : 'sleep' '(' expression ')' ';'
    ;

returnStmt
    : 'return' expression? ';'
    ;

senseStmt
    : 'sense' '('')' ';'
    ;

goalCheckStmt
    : 'goal_check' '(' ID ')' ';'
    ;

getTimeStmt
    : 'getTime' '('')' ';'
    ;    

dictDelStmt
    : 'del' expression '[' expression ']' ';'
    ;

listAddStmt
    : expression '.add(' expression ')' ';'
    ;


ifStmt
    : 'if' '(' expression ')' ifBlock (elseBlock)?
    ;   

ifBlock
    : '{' statement* '}'
    | statement 
    ;

elseBlock
    : 'else' '{' statement* '}'
    | 'else' statement
    ;

forStmt
    : 'for' '(' variableDecl expression ';' forAssignExpr ')' '{' forBody '}'
    ;

forAssignExpr
    : expression '=' expression
    ;

forBody
    : statement*
    ;


whileStmt
    : 'while' '(' expression ')' '{' statement* '}'
    ;

breakStmt
    : 'break' ';'
    ;

continueStmt
    : 'continue' ';'
    ;

doStmt
    : 'do' ID '(' (expression (',' expression)*)? ')' ';' 
    ;


variableDecl
    : type ID ('=' expression)? ';'   # VarDecl      
    | ID ID '=' messageInit ';'       # MessageVarDecl    
    ;


assignment
    : expression '=' assignValue
    ;

assignValue
    : expression ';'             # SimpleAssignValue
    | getTimeStmt                # GetTimeAssignValue 
    | spawnStmt                  # SpawnAssignValue
    | doStmt                     # DoAssignValue
    | goalCheckStmt              # GoalCheckAssignValue
    ;


expression
    : '(' expression ')'                    # ParenExpr
    | MINUS expression                      # NegExpr
    | MSG '.' ID                            # MessageAccessExpr
    | SELF '.' ID                           # SelfAccessExpr
    | BELIEF '.' ID                         # BeliefAccessExpr
    | expression '[' expression ']'         # IndexExpr
    | expression '[' ':' expression ']'     # SliceToExpr
    | expression '[' expression ':' ']'     # SliceFromExpr
    | expression '[' expression ':' expression ']' # SliceRangeExpr
    | expression '.keys()'                  # DictKeysExpr   
    | expression '.values()'                # DictValuesExpr  
    | expression '.get('expression')'       # DictGetExpr
    | 'len' '(' expression ')'              # LenExpr
    | 'type' '(' expression ')'             # TypeExpr
    | 'abs' '(' expression ')'              # AbsExpr  
    | 'random' '(' expression ',' expression ')' # RandomExpr
    | 'deepcopy' '(' expression ')'         # DeepCopyExpr
    | NOT expression                        # NotExpr 
    | AMPERSAND expression                  # AddressOfExpr
    | STAR expression                       # DerefExpr
    | expression op=('*'|'/') expression    # MulDivExpr
    | expression op=('+'|'-') expression    # AddSubExpr
    | expression op=MODULO expression       # ModuloExpr
    | expression op=EQ expression           # EqExpr
    | expression op=NEQ expression          # NeqExpr
    | expression op=LT expression           # LtExpr
    | expression op=GT expression           # GtExpr
    | expression op=LEQ expression          # LeqExpr
    | expression op=GEQ expression          # GeqExpr
    | expression op=AND expression          # AndExpr
    | expression op=OR expression           # OrExpr
    | expression op=XOR expression          # XorExpr
    | NONE                                  # NoneExpr
    | ID                                    # VarReference
    | AGENTID                               # AgentIdExpr
    | messageInit                           # MessageInitExpr
    | msgTypeValue                          # MsgTypeValueExpr
    | tupleLiteral                          # TupleExpr
    | listLiteral                           # ListExpr
    | dictLiteral                           # DictExpr
    | literal                               # LiteralExpr
    ;



messageInit
    : ID '{' (messageFieldAssign (',' messageFieldAssign)*)? '}'
    ;


messageFieldAssign
    : ID ':' expression
    ;


listLiteral
    : '[' (expression (',' expression)*)? ']'
    ;


dictLiteral
    : '{' dictEntry (',' dictEntry)* '}'
    ;


dictEntry
    : key=expression ':' value=expression
    ;


tupleLiteral
    : '(' expression ',' expression (',' expression)* ')'
    ;


type
    :  bodyType                         # BasicType
    | 'pointer' '<' type '>'            # PointerType
    | 'list' '<' type '>'               # ListType
    | 'dict' '<' key=type ',' value=type '>'      # DictType
    | 'tuple' '<' type (',' type)* '>'  # TupleType
    | 'any'                               # AnyType
    ;
    
bodyType : 'int' | 'float' | 'str' | 'bool' | 'void' | 'agentid';


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
BELIEF: 'bel';
MSGTYPE_INFORM:  'msgType_inform';
MSGTYPE_ASK:     'msgType_ask';
MSGTYPE_REQUEST: 'msgType_request';
MSGTYPE_CONFIRM: 'msgType_confirm';
MSGTYPE_DENY:    'msgType_deny';


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
MODULO: '%';
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
AMPERSAND: '&';
NONE: 'None';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
BREAK: 'break';
PRINT: 'print';
LOGGING: 'logging';
AGENT: 'agent';
VOID: 'void';
KILL: 'kill';
SEND: 'send';
SPAWN: 'spawn';
DO: 'do';
SLEEP: 'sleep';
RETURN: 'return';



INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
AGENTID: '.' [0-9]+ ('.' [0-9]+)*;
BOOL: 'True' | 'False';
STRING: '"' .*? '"';
// function and variables names 
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Whitespace and comments
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;