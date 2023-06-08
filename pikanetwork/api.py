import aiohttp
from pikanetwork.builders import build_player
from .exceptions import *
import logging
import json
import sys


async def fetch(client, url):
    async with client.get(url) as resp:
        if resp.status == 400:
            raise PlayerNotFound(f"The player {name} does not exist in the database.")

        return await resp.text()


class PikaAPI:
    """
    The base class of the pikanetwork api wrapper
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def get_player(self, name: str):
        """
        Returns a player object
        """
        self.logger.info("Starting get_player")
        if " " in name:
            raise InvalidName("The player name is Invalid")

        url = f"https://stats.pika-network.net/api/profile/{name}"

        async with aiohttp.ClientSession() as session:

            data = await fetch(session, url)
            player_data = json.loads(data)

            player_object = await build_player(player_data)

            return player_object
