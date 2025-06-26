grammar Agentar;

// PARSER RULES ---------------------------------------

program 
    : (motherDecl | agentDecl | messageDecl)* EOF
    ;

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
    | sendStmt
    | sendParentStmt
    | sendChildrenStmt
    | sendSiblingStmt
    | spawnStmt
    | killStmt
    | killchildrenStmt
    | doStmt
    | sleepStmt
    | returnStmt
    | senseStmt
    | goalCheckStmt
    | getTimeStmt
    | dictDelStmt
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
    : 'goals' '{' goalBlock* '}' ( 'merge' '(' expression')' )?
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


sendParentStmt
    : 'send2parent' '(' expression (',' ('msg_type=' msgTypeValue | msgTypeValue))? ')' ';'
    ;


sendChildrenStmt
    : 'send2children' '(' expression ',' expression (',' ('msg_type=' msgTypeValue | msgTypeValue))? ')' ';'
    ;


sendSiblingStmt
    : 'send2siblings' '(' expression ',' expression (',' ('msg_type=' msgTypeValue | msgTypeValue))? ')' ';'
    ;


spawnStmt
    : 'spawn' '(' ID (',' '['expression (',' expression)*']')? ')' ';'
    ;

killStmt  
    : 'kill' '(' expression? ')' ';'
    ;


killchildrenStmt
    : 'kill_children' '(' expression? ')' ';'
    ;


sleepStmt  
    : 'sleep' '('expression')' ';'
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

// === End_of_statements


messageInit
    : ID '(' (messageFieldAssign (',' messageFieldAssign)*)? ')'
    ;

messageFieldAssign
    : ID '=' expression
    ;

printStmt
    : 'print' '(' expression (',' expression)* ')' ';'
    ;

loggingStmt
    : 'logging' '(' expression (',' expression)* ')' ';'
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

continueStmt
    : 'continue' ';'
    ;
    

doStmt
    : 'do(' ID (',' '['expression (',' expression)*']')? ')' ';' 
    ;


variableDecl
    : type ID ('=' expression)? ';'                       # VarDecl
    ;

assignment
    : expression '=' getTimeStmt                          # GetTimeAssign
    | ID '=' expression ';'                               # SimpleAssign
    | ID '['']' '=' expression ';'                        # ListAddAssign
    | ID '[' expression ']' '=' expression ';'            # IndexAssign
    | ID '=' spawnStmt                                    # SpawnAssign
    | ID '=' doStmt                                       # DoAssign
    | ID '=' goalCheckStmt                                # GoalCheckAssign
    | expression '=' doStmt                               # DoSelfAssign
    | expression'['']' '=' expression ';'                 # SelfListAddAssign
    | expression'[' expression ']' '=' expression ';'     # SelfIndexAssign
    | expression '=' expression ';'                       # SelfAssign
    | expression '=' goalCheckStmt                        # SelfGoalCheckAssign
    ;

type
    :  bodyType                 # BacisType
    | 'pointer<'type'>'         # PointerType
    ;

bodyType: 'int' | 'float' | 'string' | 'bool' | 'void' | 'tuple' | 'list' | 'dict' | 'agentid';


expression
    : '(' expression ')'                    # ParenExpr
    | '-' expression                        # NegExpr
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
    | '&' expression                        # AddressOfExpr
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
    | doExpr                                # DoExpression
    ;


doExpr
    : 'do(' ID (',' '['expression (',' expression)*']')?  ')'
    ;


listLiteral
    : '[' (expression (',' expression)*)? ']'
    ;

dictLiteral
    : '{' dictEntry (',' dictEntry)* '}'
    ;

dictEntry
  : key=expression '=' value=expression
  ;

tupleLiteral
    : '(' expression ',' expression (',' expression)* ')'
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
BELIEF: 'bel';
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