from pyparsing import (
    Combine, Word, White, Literal, delimitedList, Optional, Empty, Suppress,
    Group, alphas, alphanums, printables, Forward, oneOf, quotedString,
    QuotedString, ZeroOrMore, restOfLine, CaselessKeyword, ParserElement,
    LineEnd, removeQuotes, Regex, nestedExpr, pyparsing_common as ppc
)

""" A program is a list of statements. """
optWhite = ZeroOrMore(LineEnd() | White())
string = Word(alphas, alphanums + '.')
quotedName = QuotedString(quoteChar='"', unquoteResults=True)

SEMI,COLON,LPAR,RPAR,LBRACE,RBRACE,LBRACK,RBRACK,DOT,COMMA,EQ = map(
    Literal,
    ";:(){}[].,=")

""" Tokens. """
INCLUDE, VLAN, VID, DESCRIPTION = map(
    CaselessKeyword,
    "include vlan vid description".split())
vlan_name = Word(alphas, alphanums)
vlan_vid = ppc.integer("vid")

""" Grammar productions. """
statement = Forward()
statement <<= (
    Group(
        Group(VLAN + vlan_name) + optWhite +
        Group(VID + vlan_vid) + optWhite +
        Group(Optional(DESCRIPTION + quotedName)) + optWhite
    ) |
    Group (
        INCLUDE + string
    )
)("statement")

""" Make a program a series of statements. """
program_grammar = statement + ZeroOrMore(statement)

""" Make rest-of-line comments. """
comment = "--" + restOfLine
program_grammar.ignore (comment)
