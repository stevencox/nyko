import logging
import yaml
from nyko.parser import TokenList

logger = logging.getLogger (__name__)

class Actor:

    def __init__(self, tokens: TokenList) -> None:
        self.tokens = tokens
        
    def act (self, conf:dict) -> bool:
        logger.debug (f"{self.__class__.__name__}.act<base>")
        return self._act (conf)

class NullActor(Actor):

    def __init__(self, tokens:TokenList) -> None:
        super().__init__(tokens)
    
    def _act (self, conf: dict) -> bool:
        pass
        
class IncludeActor(Actor):

    def __init__(self, tokens: TokenList) -> None:
        super().__init__(tokens)
        logger.debug (f"include {self.tokens}")
        
    def _act (self, conf: dict) -> bool:
        includes = conf.get("include", [])
        included = self.tokens.value[1]
        if not included in includes:
            includes.append (included)
            conf["include"] = includes
            logger.debug (
                f"{__class__.__name__} added {included} to include list.")
        return True

class VLANActor(Actor):

    def __init__(self, tokens: TokenList) -> None:
        super().__init__(tokens)
        
    def _act (self, conf: dict) -> bool:
        vlans = conf.get ("vlans", {})
        self.tokens.value = [ e  for e in self.tokens.value if len(e) == 2]
        for e in self.tokens.value:
            if len(e) != 2:
                raise ValueError (f"syntax error parsing vlans {e}")
        inputs = { element[0] : element[1] for element in self.tokens.value }
        vlan_key = inputs.get ("vlan")
        vid = inputs.get ("vid")
        logger.debug (f"vid --> {vid}")
        description = inputs.get ("description")
        the_vlan = vlans.get (vlan_key, {})
        if vid:
            the_vlan['vid'] = vid
        if description:
            the_vlan['description'] = description
        conf['vlans'] = vlans
        logger.debug (
            f"{__class__.__name__} vlans: {yaml.dump(vlans)}")
