import java_cup.runtime.*;

%%
%class Lexer
%unicode
%cup
%line
%column

%{
  
  private Symbol symbol(int type) {
    return new Symbol(type, yyline, yycolumn);
  }
  
  private Symbol symbol(int type, Object value) {
    return new Symbol(type, yyline, yycolumn, value);
  }

%}

Whitespace = \r|\n|\r\n|\s|"\t"
Letter = [a-zA-Z]
Digit = [0-9]
Char = .
String = [^\"]*
IdChar = {Letter} | {Digit} | _
Identifier = {Letter}{IdChar}*
PosInteger = [1-9]{Digit}*
Integer = 0 | {PosInteger}
Float = {Integer}\.{Digit}{Digit}* | \.{Digit}{Digit}*
Rational = {Integer}\/{PosInteger} | {Integer}_{PosInteger}\/{PosInteger}
Comment = #.*\n|\/#(.*[\n]*)*#\/

%%
<YYINITIAL> {
    {Comment}       { /*return nothing*/ }

    "main"          { return symbol(sym.MAIN);      }
    "bool"          { return symbol(sym.KBOOL);     }
    "char"          { return symbol(sym.KCHAR);     }
    "dict"          { return symbol(sym.DICT);      }
    "string"        { return symbol(sym.STRING);    }
    "int"           { return symbol(sym.KINT);      }
    "rat"           { return symbol(sym.KRAT);      }
    "float"         { return symbol(sym.KFLOAT);    }
    "top"           { return symbol(sym.TOP);       }
    "seq"           { return symbol(sym.SEQ);       }
    "in"            { return symbol(sym.IN);        }
    "T"             { return symbol(sym.TRUE);      }
    "F"             { return symbol(sym.FALSE);     }
    "tdef"          { return symbol(sym.TDEF);      }
    "fdef"          { return symbol(sym.FDEF);      }
    "void"          { return symbol(sym.VOID);      }
    "alias"         { return symbol(sym.ALIAS);     }
    "if"            { return symbol(sym.IF);        }
    "elif"          { return symbol(sym.ELIF);      }
    "else"          { return symbol(sym.ELSE);      }
    "forall"        { return symbol(sym.FORALL);    }
    "loop"          { return symbol(sym.LOOP);      }
    "pool"          { return symbol(sym.POOL);      }
    "read"          { return symbol(sym.READ);      }
    "print"         { return symbol(sym.PRINT);     }
    "return"        { return symbol(sym.RETURN);    }
    "od"            { return symbol(sym.OD);        }
    "do"            { return symbol(sym.DO);        }
    "fi"            { return symbol(sym.FI);        }
    "len"           { return symbol(sym.LEN);       }
    "then"          { return symbol(sym.THEN);      }
    "break"         { return symbol(sym.BREAK);     }
    
    {Rational}      { return symbol(sym.RATIONAL, yytext());    }
    {Float}         { return symbol(sym.FLOAT, Float.parseFloat(yytext()));    }
    {Integer}       { return symbol(sym.INTEGER, Integer.parseInt(yytext()));    }
    "'"{Char}"'"    { return symbol(sym.CHARACTER, yytext());   }
    "\""{String}"\"" { return symbol(sym.CHARACTER, yytext());  }
    {Identifier}    { return symbol(sym.IDENTIFIER, yytext());  }
    {Whitespace}    { /* do nothing */              }

    "<="            { return symbol(sym.LESSEQUAL); }
    "=>"            { return symbol(sym.MIMP);      }
    ">="            { return symbol(sym.MOREEQUAL); }
    "="             { return symbol(sym.ISEQUAL);   }
    "!="            { return symbol(sym.NOTEQUAL);  }
    "{"             { return symbol(sym.LCURLY);    }
    "}"             { return symbol(sym.RCURLY);    }
    "["             { return symbol(sym.LSQUARE);   }
    "]"             { return symbol(sym.RSQUARE);   }
    ":="            { return symbol(sym.EQUAL);     }
    ";"             { return symbol(sym.SEMICOL);   }
    "+"             { return symbol(sym.PLUS);      }
    "-"             { return symbol(sym.MINUS);     }
    "*"             { return symbol(sym.MULT);      }
    "/"             { return symbol(sym.DIV);       }
    "("             { return symbol(sym.LPAREN);    }
    ")"             { return symbol(sym.RPAREN);    }
    "<"             { return symbol(sym.LESSTHAN);  }
    ">"             { return symbol(sym.MORETHAN);  }
    "!"             { return symbol(sym.NOT);       }
    "&&"            { return symbol(sym.AND);       }
    "||"            { return symbol(sym.OR);        }
    "^"             { return symbol(sym.POWER);     }
    "::"            { return symbol(sym.DCOLON);    }
    ":"             { return symbol(sym.COLON);     }
    ","             { return symbol(sym.COMMA);     }
    "."             { return symbol(sym.DOT);       }
    "?"             { return symbol(sym.QUEST);     }
}

[^]  {
  System.out.println("file:" + (yyline+1) +
    ":0: Error: Invalid input '" + yytext()+"'");
  return symbol(sym.BADCHAR);
}

