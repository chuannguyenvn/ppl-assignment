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
    : identifier_list ':' type_specifier '=' expression_list ';'
    ;

parameter_declaration_list
    : parameter_declaration (',' parameter_declaration)*
    ;

parameter_declaration
    : INHERIT? OUT? IDENTIFIER ':' type_specifier ';'
    ;
    
identifier_list
    : IDENTIFIER (',' IDENTIFIER)*
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
    : IDENTIFIER ':' FUNCTION type_specifier OPEN_PAREN parameter_declaration_list CLOSE_PAREN (INHERIT IDENTIFIER)?
    ;

function_body
    : block_statement
    ;
    
block_statement
    : OPEN_BRACE statement* CLOSE_BRACE

statement
    :
    ;
    
expression_list
    : expression (',' expression)*
    ;

expression
    : IDENTIFIER
    | literal
    ;
    
sign_expression
    : MINUS 
    ;
    
logic_flip_expression
    :
    ;
    
multiplying_expression
    :
    ;

adding_expression
    :
    ;
    
logic_expression
    :
    ;

relational_expression
    :
    ;

string_expression
    :
    ;
    
literal
    : IDENTIFIER
    | INTEGER_LIT
    | FLOAT_LIT
    | BOOLEAN_LIT
    | STRING_LIT
    | ARRAY_LIT
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
OROR : '||';
EQUAL : '==';
NOT_EQUAL : '!=';
LESS : '<';
LESS_EQUAL : '<=';
GREATER : '>';
GREATER_EQUAL : '>=';
DOUBLE_COLON : '::';

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