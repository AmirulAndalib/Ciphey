from typing import Dict, Optional

from ciphey.iface import Checker, Config, ParamSpec, T, registry
import logging
from pywhat import identifier


@registry.register
class What(Checker[str]):

    """
    Uses PyWhat to determine plaintext with regexes
    """

    def check(self, ctext: T) -> Optional[str]:
        logging.debug("Trying PyWhat checker")
        returned_regexes = self.id.identify(ctext, api=True)
        if len(returned_regexes["Regexes"]) > 0:
            return returned_regexes["Regexes"][0]["Regex Pattern"]["Name"]
        return None

    def getExpectedRuntime(self, text: T) -> float:
        # TODO: actually bench this
        return 2e-7 * len(text)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        return None

    def __init__(self, config: Config):
        super().__init__(config)
        self.id = identifier.Identifier()