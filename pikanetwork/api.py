import requests
from pikanetwork.builders import build_player
import logging
import json
import sys


class InvalidName(ValueError):
    """Raised when the name given is invalid"""
    pass


class PlayerNotFound(Exception):
    pass


class PikaAPI:
    """
    The base class of the pikanetwork api wrapper
    """
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})
        self.logger = logging.getLogger(__name__)

    def get_player(self, name: str):
        """
        Returns a player object
        """
        self.logger.info("Starting get_player")
        if " " in name:
            raise InvalidName("The player name is Invalid")

        data = self.session.get(f"https://stats.pika-network.net/api/profile/{name}")

        if data.status_code == 200:
            player_data = json.loads(data.text)

            player_object = build_player(player_data)

            return player_object

        if data.status_code == 400:
            raise PlayerNotFound(f"The player {name} does not exist in the database.")
