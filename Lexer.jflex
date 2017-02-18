import java_cup.runtime.*;
%%
%class Lexer
%unicode
%cup
%line
%column
%{
 private Symbol symbol(int type)
 {
  return new Symbol(type, yyline, yycolumn);
 }

 private Symbol symbol(int type, Object value)
 {
  return new Symbol(type, yyline, yycolumn, value);
 }
%}

LT            = \r|\n|\r\n  /* Line Terminator */
WS            = {LT} |" "|"\t" /* White Space */
Digit         = [0-9]
Letter        = [a-z]|[A-Z]
Character     = .
Int           = 0 | -?[1-9]{Digit}*
Float         = {Int}\.{Digit}+ | \.{Digit}+
Rational      = {Int}\/{Int} | {Int}_{Int}\/{Int}
Number        = {Int} | {Rational} | {Float}
Bool          = [T] | [F]
Identifier    = {Letter}[a-zA-Z0-9_]*
Comment       = #.*\n | \/#(.*[\n]*)*#\/
%%
    
<YYINITIAL>{

    /* comments */
    {Comment}                      { /* ignore */ }

    /* whitespace */
    {WS}                   { /* ignore */ }

    /* Reserved words */
    "main"             { return symbol(sym.MAIN);           }
    "bool"             { return symbol(sym.BOOLEAN);        }
    "char"             { return symbol(sym.ICHARACTER);     }
    "dict"             { return symbol(sym.DICTIONARY);     }
    "rat"              { return symbol(sym.XRATIONAL);      }
    "int"              { return symbol(sym.XINTEGER);       }
    "float"            { return symbol(sym.IFLOAT);         }
    "top"              { return symbol(sym.TOP);            }
    "seq"              { return symbol(sym.SEQ);            }
    "in"               { return symbol(sym.IN);             }
    "T"                { return symbol(sym.TRUE);           }
    "F"                { return symbol(sym.FALSE);          }
    "tdef"             { return symbol(sym.TYPEDEF);        }
    "fdef"             { return symbol(sym.FUNCDEF);        }
    "void"             { return symbol(sym.VOID);           }
    "alias"            { return symbol(sym.ALIAS);          }
    "if"               { return symbol(sym.IF);             }
    "elif"             { return symbol(sym.ELIF);           }
    "else"             { return symbol(sym.ELSE);           }
    "forall"           { return symbol(sym.FORALL);         }
    "while"            { return symbol(sym.WHILE);          }
    "read"             { return symbol(sym.READ);           }
    "print"            { return symbol(sym.PRINT);          }
    "return"           { return symbol(sym.RETURN);         }
    "od"               { return symbol(sym.OD);             }
    "do"               { return symbol(sym.DO);             }
    "fi"               { return symbol(sym.FI);             }
    "len"              { return symbol(sym.LEN);            }
    "then"             { return symbol(sym.THEN);           }
            
    /* Brackets, operators, etc. */     
    "<="               { return symbol(sym.LESSEQUAL);      }
    ">="               { return symbol(sym.MOREEQUAL);      }
    "=="               { return symbol(sym.ISEQUAL);        }
    "!="               { return symbol(sym.NOTEQUAL);       }
    "{"                { return symbol(sym.LCURLY);         }
    "}"                { return symbol(sym.RCURLY);         }
    "["                { return symbol(sym.LSQUARE);        }
    "]"                { return symbol(sym.RSQUARE);        }
    "="                { return symbol(sym.EQUAL);          }
    ";"                { return symbol(sym.SEMICOL);        }
    "+"                { return symbol(sym.PLUS);           }
    "-"                { return symbol(sym.MINUS);          }
    "*"                { return symbol(sym.MULT);           }
    "/"                { return symbol(sym.DIV);            }
    "("                { return symbol(sym.LPAREN);         }
    ")"                { return symbol(sym.RPAREN);         }
    "<"                { return symbol(sym.LESSTHAN);       }
    ">"                { return symbol(sym.MORETHAN);       }
    "!"                { return symbol(sym.NOT);            }
    "&&"               { return symbol(sym.AND);            }
    "||"               { return symbol(sym.OR);             }
    "^"                { return symbol(sym.POWER);          }
    "::"               { return symbol(sym.DCOLON);         }
    ":"                { return symbol(sym.COLON);          }
    ","                { return symbol(sym.COMMA);          }
    "."                { return symbol(sym.DOT);            }
    
    /* Declarations */
    {Rational}         { return symbol(sym.RATIONAL, yytext());                     }
    {Float}            { return symbol(sym.FLOAT, Float.parseFloat(yytext()));      }
    {Int}              { return symbol(sym.INTEGER, Integer.parseInt(yytext()));    }
    {Number}           { return symbol(sym.NUMBER, yytext());                       }
    "'"{Character}"'"  { return symbol(sym.CHARACTER, yytext());                    }
    {Identifier}       { return symbol(sym.IDENTIFIER, yytext());                   }
    {WS}               { /* do nothing */ }

}

[^]  {
  System.out.println("file:" + (yyline+1) +
    ":0: Error: Invalid input '" + yytext()+"'");
  return symbol(sym.ERRORFLAG);
}
