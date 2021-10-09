import json
import logging
import logging.config
import os
import yaml
from jinja2 import Template

logger = logging.getLogger(__name__)

class LoggingUtil(object):

    @staticmethod
    def setup_logging ():
        config_path = os.path.join (
            os.path.dirname(__file__),
            "logging.yaml")
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    
class Resource:

    @staticmethod
    def load_file (path:str) -> object:
        result = None
        with open (path, 'r') as stream:
            result = stream.read ()
        return result

    @staticmethod
    def load_json (path:str) -> object:
        result = None
        with open (path, 'r') as stream:
            result = json.loads (stream.read ())
        return result

    @staticmethod
    def read_yaml (path:str) -> object:
        result = None
        with open (path, 'r') as stream:
            result = yaml.safe_load (stream.read ())
        return result

    @staticmethod
    def write_yaml (path:str, obj:object) -> None:
        result = None
        with open (path, 'w') as stream:
            result = yaml.dump (obj, stream)
        return result
