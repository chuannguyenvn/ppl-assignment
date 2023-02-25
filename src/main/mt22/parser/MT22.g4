// 2052046
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program
    : declaration+ EOF
    ;

declaration
    : variable_declaration
    | function_declaration
    ;
    
variable_declaration
    : short_variable_declaration SEMI_COLON
    | long_variable_declaration SEMI_COLON
    ;
    
short_variable_declaration
    : identifier_list COLON type_specifier 
    ;
    
long_variable_declaration
    : IDENTIFIER COLON type_specifier ASSIGN expression 
    | IDENTIFIER COMMA long_variable_declaration COMMA expression 
    ;

parameter_declaration_list
    : parameter_declaration (COMMA parameter_declaration)*
    ;

parameter_declaration
    : INHERIT? OUT? IDENTIFIER COLON type_specifier
    ;
    
identifier_list
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

type_specifier
    : array_type_specifier
    | AUTO
    | INTEGER
    | FLOAT
    | BOOLEAN
    | STRING
    | VOID
    ;

array_type_specifier
    : ARRAY OPEN_BRACK dimension_list CLOSE_BRACK OF (INTEGER | FLOAT | BOOLEAN | STRING)
    ;
    
dimension_list
    : INTEGER_LIT (COMMA INTEGER_LIT)*
    ;

function_declaration
    : IDENTIFIER COLON FUNCTION type_specifier OPEN_PAREN parameter_declaration_list? CLOSE_PAREN (INHERIT IDENTIFIER)? function_body
    ;

function_body
    : block_statement
    ;
    
statement
    : assignment_statement
    | if_statement
    | for_statement
    | while_statement
    | do_while_statement
    | break_statement
    | continue_statement
    | return_statement
    | call_statement
    | block_statement
    ;
 
assignment_statement
    : IDENTIFIER ASSIGN expression SEMI_COLON
    ;
    
if_statement
    : IF OPEN_PAREN expression CLOSE_PAREN statement (ELSE statement)?
    ;
    
for_statement
    : FOR OPEN_PAREN IDENTIFIER ASSIGN expression COMMA expression COMMA expression CLOSE_PAREN statement
    ;
    
while_statement
    : WHILE OPEN_PAREN expression CLOSE_PAREN statement
    ;
    
do_while_statement
    : DO block_statement WHILE OPEN_PAREN expression CLOSE_PAREN SEMI_COLON
    ;
    
break_statement
    : BREAK SEMI_COLON
    ;
    
continue_statement
    : CONTINUE SEMI_COLON
    ;
    
return_statement
    : RETURN expression? SEMI_COLON
    ;
    
call_statement
    : IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN SEMI_COLON
    ;
 
block_statement
    : OPEN_BRACE (statement | variable_declaration)* CLOSE_BRACE
    ;
       
expression_list
    : expression (COMMA expression)*
    ;

expression
    : string_expression
    ;

string_expression
    : relational_expression DOUBLE_COLON relational_expression
    | relational_expression
    ;
    
relational_expression
    : relational_expression (EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) relational_expression
    | logical_expression
    ;

logical_expression
    : logical_expression (AND_AND | OR_OR) adding_expression
    | adding_expression
    ;
    
adding_expression
    : adding_expression (ADD | MINUS) multiplying_expression
    | multiplying_expression
    ;

multiplying_expression
    : multiplying_expression (STAR | DIV | MOD) unary_expression
    | unary_expression
    ;
    
unary_expression
    : (MINUS | NOT) unary_expression
    | indexing_expression
    ;
    
indexing_expression
    : IDENTIFIER indexing_expression_continue OPEN_BRACK expression_list CLOSE_BRACK
    | braced_expression
    ;
    
indexing_expression_continue
    : indexing_expression_continue OPEN_BRACK expression_list CLOSE_BRACK
    | OPEN_BRACK expression_list CLOSE_BRACK
    ;
    
braced_expression
    : OPEN_PAREN expression CLOSE_PAREN
    | operand
    ;
    
operand
    : literal
    | function_call
    | IDENTIFIER
    ;
    
literal
    : INTEGER_LIT
    | FLOAT_LIT
    | BOOLEAN_LIT
    | STRING_LIT
    | indexed_array_lit
    ;
    
indexed_array_lit
    : OPEN_BRACE expression_list CLOSE_BRACE
    ;    
    
function_call
    : IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN
    ;

fragment INTEGER_START
    : [1-9]
    ;  

fragment DIGIT
    : [0-9]
    ;
    
fragment UNDERSCORE
    : '_'
    ;
    
fragment INTEGER_CONTINUE
    : UNDERSCORE? DIGIT
    ;
    
fragment INTEGER_PART
    : '0' 
    | INTEGER_START INTEGER_CONTINUE*
    ;
    
fragment DECIMAL_PART
    : '.' DIGIT*
    ;

fragment EXPONENT_PART
    : [eE] [+-]? DIGIT+
    ;
    
    
INTEGER_LIT 
    : INTEGER_PART {self.text = self.text.replace('_','')}
    ;

FLOAT_LIT
    : INTEGER_PART DECIMAL_PART EXPONENT_PART? {self.text = self.text.replace('_','')}
    | INTEGER_PART DECIMAL_PART {self.text = self.text.replace('_','')}
    | INTEGER_PART EXPONENT_PART {self.text = self.text.replace('_','')}
    ;

BOOLEAN_LIT
    : TRUE
    | FALSE
    ;
    
fragment ESCAPE: '\\' [bfrnt'"\\];

STRING_LIT
    : '"' ( ESCAPE | ~[\\\r\n\f] )*? '"' {self.text = self.text[1:-1]}
    ;

//fragment ARRAY_ELEMENT
//    : INTEGER_LIT
//    | FLOAT_LIT
//    | BOOLEAN_LIT
//    | STRING_LIT
//    ;
    
//ARRAY_LIT
//    : OPEN_BRACE ARRAY_ELEMENT (',' ARRAY_ELEMENT)* CLOSE_BRACE
//    ;

AUTO : 'auto';
BREAK : 'break';
BOOLEAN : 'boolean';
DO : 'do';
ELSE : 'else';
FALSE : 'false';
FLOAT : 'float';
FOR : 'for';
FUNCTION : 'function';
IF : 'if';
INTEGER : 'integer';
RETURN : 'return';
STRING : 'string';
TRUE : 'true';
WHILE : 'while';
VOID : 'void';
OUT : 'out';
CONTINUE : 'continue';
OF : 'of';
INHERIT : 'inherit';
ARRAY : 'array';

ADD : '+';
MINUS : '-';
STAR : '*';
DIV : '/';
MOD : '%';
NOT : '!';
AND_AND : '&&';
OR_OR : '||';
EQUAL : '==';
NOT_EQUAL : '!=';
LESS : '<';
LESS_EQUAL : '<=';
GREATER : '>';
GREATER_EQUAL : '>=';
DOUBLE_COLON : '::';

OPEN_PAREN : '(';
CLOSE_PAREN : ')';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';
DOT : '.';
ASSIGN : '=';
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';

fragment IDENTIFIER_START : [a-zA-Z_];
fragment IDENTIFIER_CONTINUE : [a-zA-Z0-9_];
IDENTIFIER : IDENTIFIER_START IDENTIFIER_CONTINUE*;

COMMENT_LINE
    : '//' ~[\n\r\f]* -> skip
    ;
    
COMMENT_BLOCK
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip 
    ;

fragment CHARACTER: ~[\b\f\r\n\t'"\\] | ESCAPE;
fragment NOT_ESCAPE: '\\' ~[bfrnt'"\\] ;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' CHARACTER* ([\b\f\r\n\t\\] | EOF) {
    esc = ['\b', '\t', '\n', '\f', '\r', '\\']
    temp = str(self.text)
    if temp[-1] in esc:
        raise UncloseString(temp[1:-1])
    else :
        raise UncloseString(temp[1:])
};
ILLEGAL_ESCAPE:'"' CHARACTER* NOT_ESCAPE {
    temp = str(self.text)
    raise IllegalEscape(temp[1:])
};