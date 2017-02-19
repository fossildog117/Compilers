import java_cup.runtime.*;
import java.util.ArrayList;

parser code {:

    public boolean syntaxErrors = false;

    private Lexer lexer;

    public Parser(Lexer input) {
        super(input);
        lexer = input;
    }

    public void syntax_errors(Symbol symbol) {
        report_error("Syntax error at line " + (symbol.left+1) + " , column " + symbol.right);
        syntaxErrors = true;
    }


:};

scan with {:
    return lexer.next_token();
:};

// ------- Grammar Values ------- START -------

// Reserved words
terminal MAIN, BOOLEAN, ICHARACTER, DICTIONARY, XRATIONAL, XINTEGER, IFLOAT, TOP, SEQ, IN, TRUE, FALSE, TYPEDEF, FUNCDEF, VOID, ALIAS, IF, ELIF, ELSE, FORALL, WHILE, READ, PRINT, RETURN, OD, DO, FI, LEN, THEN;

// Brackets, operators, etc.
terminal LESSEQUAL, MOREEQUAL, ISEQUAL, NOTEQUAL, LCURLY, RCURLY, LSQUARE, RSQUARE, EQUAL, SEMICOL, PLUS, MINUS, MULT, DIV, LPAREN, RPAREN, LESSTHAN, MORETHAN, NOT, AND, OR, POWER, DCOLON, COLON, COMMA, DOT;

// Declarations
terminal RATIONAL, FLOAT, INTEGER, NUMBER, CHARACTER, IDENTIFIER;

// Error flag
terminal ERRORFLAG;

// ------- Grammar Values ------- END -------

// Precedence
// Values with lowest line number have lowest precedence
precedence left AND, OR, NOT;
precedence left LESSEQUAL, MOREEQUAL, ISEQUAL, NOTEQUAL, MORETHAN, LESSTHAN;
precedence left DCOLON;
precedence left PLUS, MINUS;
precedence left MULT, DIV;
precedence left POWER;
precedence left LPAREN, RPAREN;

// Non terminals
nonterminals main, function_body

// Grammar
main ::= MAIN LCURLY function_body RCURLY SEMICOL;








