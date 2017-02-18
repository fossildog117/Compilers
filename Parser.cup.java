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

// Reserved words
terminal MAIN, BOOLEAN, ICHARACTER, DICTIONARY, XRATIONAL, XINTEGER, IFLOAT, TOP, SEQ, IN, TRUE, FALSE, TYPEDEF, FUNCDEF, VOID, ALIAS, IF, ELIF, ELSE, FORALL, WHILE, READ, PRINT, RETURN, OD, DO, FI, LEN, THEN

// Brackets, operators, etc.
terminal LESSEQUAL, MOREEQUAL, ISEQUAL, NOTEQUAL, LCURLY, RCURLY, LSQUARE, RSQUARE, EQUAL, SEMICOL, PLUS, MINUS, MULT, DIV, LPAREN, RPAREN, LESSTHAN, MORETHAN, NOT, AND, OR, POWER, DCOLON, COLON, COMMA, DOT

// Declarations
terminal RATIONAL, FLOAT, INTEGER, NUMBER, CHARACTER, IDENTIFIER

// Error flag
terminal ERRORFLAG







