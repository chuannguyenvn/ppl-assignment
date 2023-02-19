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
    : identifier_list COLON type_specifier ASSIGN expression_list SEMI_COLON
    ;

parameter_declaration_list
    : parameter_declaration (COMMA parameter_declaration)*
    ;

parameter_declaration
    : INHERIT? OUT? IDENTIFIER COLON type_specifier SEMI_COLON
    ;
    
identifier_list
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

// BUG: This may cause variable of type void to exist.
type_specifier
    : INTEGER
    | FLOAT
    | BOOLEAN
    | STRING
    | ARRAY
    | VOID
    ;

function_declaration
    : IDENTIFIER COLON FUNCTION type_specifier OPEN_PAREN parameter_declaration_list CLOSE_PAREN (INHERIT IDENTIFIER)?
    ;

function_body
    : block_statement
    ;
    
statement
    : assignment_statement
    | assignment_statement
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
    : DO block_statement WHILE OPEN_PAREN statement CLOSE_PAREN SEMI_COLON
    ;
    
break_statement
    : BREAK SEMI_COLON
    ;
    
continue_statement
    : CONTINUE SEMI_COLON
    ;
    
return_statement
    : RETURN expression SEMI_COLON
    ;
    
call_statement
    : IDENTIFIER OPEN_PAREN expression_list? CLOSE_PAREN SEMI_COLON
    ;
 
block_statement
    : OPEN_BRACE statement* CLOSE_BRACE
    ;
       
expression_list
    : expression (COMMA expression)*
    ;

expression
    : IDENTIFIER
    | literal
    | string_expression
    ;

string_expression
    : string_expression DOUBLE_COLON relational_expression
    | relational_expression
    ;
    
relational_expression
    : relational_expression (EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREATER | GREATER_EQUAL) logical_expression
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
    : multiplying_expression (STAR | DIV) negate_expression
    | negate_expression
    ;
    
negate_expression
    : NOT negate_expression
    | sign_expression
    ;
    
sign_expression
    : MINUS sign_expression
    | operands
    ;
    
    
operands
    : literal
    | function_call
    ;
    
literal
    : IDENTIFIER
    | INTEGER_LIT
    | FLOAT_LIT
    | BOOLEAN_LIT
    | STRING_LIT
    | ARRAY_LIT
    ;
    
function_call
    :
    ;

// Keywords
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

// Operators
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
ASSIGN : '=';
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';

// Separators
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';

// Identifiers
fragment IDENTIFIER_START : [a-zA-Z_];
fragment IDENTIFIER_CONTINUE : [a-zA-Z0-9_];
IDENTIFIER : IDENTIFIER_START IDENTIFIER_CONTINUE*;

// Literals
fragment NON_ZERO_DIGIT 
    : [1-9]
    ;
    
fragment DIGIT 
    : [0-9]
    ;
    
fragment INTEGER_PART
    : '0' 
    | NON_ZERO_DIGIT DIGIT*
    ;
    
fragment DECIMAL_PART
    : '.' DIGIT*
    ;

fragment EXPONENT_PART
    : [eE] [+-]? DIGIT+
    ;
    
    
INTEGER_LIT 
    : INTEGER_PART
    {self.text = self.text.replace('_','')}
    ;

FLOAT_LIT
    : INTEGER_PART DECIMAL_PART EXPONENT_PART?
    | INTEGER_PART DECIMAL_PART
    | INTEGER_PART EXPONENT_PART
    ;

BOOLEAN_LIT
    : TRUE
    | FALSE
    ;
    
fragment ESCAPE_SEQUENCE
    : '\\\''
    | '\\"'
    | '\\?'
    | '\\\\'
    | '\\a'
    | '\\b'
    | '\\f'
    | '\\n'
    | '\\r'
    | ('\\' ('\r' '\n'? | '\n'))
    | '\\t'
    | '\\v';

STRING_LIT
    : '"' ( ESCAPE_SEQUENCE | ~[\\\r\n\f] )* '"'
    ;

fragment ARRAY_ELEMENT
    : INTEGER_LIT
    | FLOAT_LIT
    | BOOLEAN_LIT
    | STRING_LIT
    ;
    
ARRAY_LIT
    : OPEN_BRACE ARRAY_ELEMENT (',' ARRAY_ELEMENT)* CLOSE_BRACE
    ;
    

 



























WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;