import argparse
import json
import logging
import os
import sys
import traceback
import yaml
from collections import defaultdict
from nyko.grammar import program_grammar
from pyparsing import ParseException
from typing import List

logger = logging.getLogger (__name__)

class Parser:

    def __init__(self, grammar = program_grammar) -> None:
        self.program = grammar

    def parse (self, text: str) -> List:
        """ Parse a program, returning an abstract syntax tree. """
        result = None
        try:
            result = self.program.parseString (text)
        except ParseException as pEx:
            message = f"Parsing error at line {pEx.lineno}, col {pEx.col}."
            details = f'{pEx.line}'
            details += f"\n{' ' * (pEx.col -1)}^^^"
            details += f"\n{pEx.msg}"
            logger.error(message + '\n' + details)
            raise Exception(message, details)
        return result.asList ()

class TokenList:
    
    def __init__(self, raw:List) -> None:
        if isinstance(raw[0], str):
            self.key = raw[0]
        elif isinstance(raw[0], List) and isinstance(raw[0][0], str):
            self.key = raw[0][0]
        else:
            raise ValueError (f"invalid token: {raw}")
        self.value = raw
        
    def __repr__(self):
        return f"{self.key}->{self.value}"
