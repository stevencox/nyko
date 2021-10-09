import argparse
import logging
from nyko.util import LoggingUtil, Resource
from nyko.parser import Parser, TokenList
from nyko.syntaxtree import *
from typing import List, Dict

LoggingUtil.setup_logging ()

logger = logging.getLogger ("nyko.compiler")

class Compiler:

    def __init__(self, dry_run:bool, faucet_config:str) -> None:
        self.dry_run = dry_run
        self.faucet_config = faucet_config
        message = ", ".join ([
            f"dry_run={self.dry_run}",
            f"faucet_config={self.faucet_config}"
        ])
        logger.debug (f"{message}")
        self.parser = Parser ()

    def _parse (self, source: str) -> None:
        text = Resource.load_file (source)
        return self.parser.parse (text)
        
    def _emit (self, ast:List[Actor]) -> None:
        self._emit_faucet_config (ast)
        
    def _emit_faucet_config (self, ast:List[Actor]) -> None:
        conf = Resource.read_yaml (self.faucet_config)
        status = [ a.act(conf) for a in ast ]
        if not self.dry_run:
            logger.debug (f"writing config {self.faucet_config}")
            Resource.write_yaml (self.faucet_config, conf)
        
    def process (self, source: str) -> None:
        """ Parse, model, and execute a program, soup to nuts. """
        ast_table = {
            "include" : lambda p: IncludeActor (p),
            "vlan"    : lambda p: VLANActor (p)
        }
        parse_tree = [ TokenList(p) for p in self._parse (source) ]
        logger.debug (parse_tree)
        ast : List[Actor] = [
            ast_table[token.key](token)
            for token in parse_tree
        ]
        self._emit (ast)
        
def main ():
    
    """ Process arguments. """
    arg_parser = argparse.ArgumentParser(
        description='Nyko',
        formatter_class=lambda prog: argparse.ArgumentDefaultsHelpFormatter(
            prog,
            max_help_position=180))
    
    arg_parser.add_argument('-s', '--source',
                            help="The program's source file")
    arg_parser.add_argument('--faucet-config',
                            help="Path to Faucet's config",
                            default="etc/faucet/faucet.yaml")
    arg_parser.add_argument('--dry-run',
                             help="Don't write any output.",
                             action="store_true",
                             default=False)
    
    args = arg_parser.parse_args ()
    if args.source:
        compiler = Compiler (
            dry_run=args.dry_run,
            faucet_config=args.faucet_config)
        compiler.process (args.source)

if __name__ == '__main__':
    main ()
