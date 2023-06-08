import typing

import aiohttp
from pikanetwork.builders import build_player,build_player_leaderboard
from .exceptions import *
from .models import (Player, PlayerLeaderboard)
import logging
import json
import sys

ALLOWED_SERVERS = [
    "opfactions",
    "lifesteal",
    "oplifesteal",
    "classicskyblock",
    "opskyblock",
    "opprison",
    "survival",
    "kitpvp",
    "practice",
    "skywars",
    "bedwars"
]

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

    async def get_player(self, name: str) -> Player:
        """
        Returns a player object

        used to get all the data about a player in-game.
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

    async def get_player_leaderboard(
            self,
            name: str,
            server: str,
            interval: str,
            mode: typing.Optional[str] = None
    ) -> PlayerLeaderboard:
        """
        Returns a PlayerLeaderboard Object

        used to get data about a player's leaderboard stats.
        """

        if server not in ALLOWED_SERVERS:
            raise InvalidServerArgument(f"The server {server} does not exist!")

        self.logger.info("Starting get_player_leaderboard")
        if " " in name:
            raise InvalidName("The player name is Invalid")

        if mode is not None and server not in ["bedwars", "skywars"]:
            raise InvalidServerArgument(f"You cannot use the mode argument with the server {server}")

        if mode is None:
            url = f"https://stats.pika-network.net/api/profile/{name}/leaderboard?type={server}&interval={interval}"
        else:
            url = f"https://stats.pika-network.net/api/profile/{name}/leaderboard?type={server}&interval={interval}&mode={mode}"

        async with aiohttp.ClientSession() as session:

            data = await fetch(session, url)
            leaderboard_data = json.loads(data)

            leaderboard_object = await build_player_leaderboard(leaderboard_data)

            return leaderboard_object
