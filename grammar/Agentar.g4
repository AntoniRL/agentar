grammar Agentar;

// Parser rules
program: statement+ EOF;
statement: printStmt ';';
printStmt: 'print' '(' STRING ')';

// Lexer rules
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;