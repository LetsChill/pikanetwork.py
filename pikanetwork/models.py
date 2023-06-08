"""
MIT License

Copyright (c) 2023 LetsChill

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from dataclasses import dataclass


@dataclass
class ClanOwner:
    """
        A child object of Clan

        It contains information about the Owner of the clan.
        """
    username: str
    last_seen: int
    online: bool


@dataclass
class ClanMember:
    """
    A child object of Clan

    It contains information about a member in a clan.
    """
    username: str
    last_seen: int
    online: bool
    join_date: str


@dataclass
class Clan:
    """
    A child object of Player.

    It contains information about the Player's clan.
    """
    name: str
    tag: str
    current_trophies: str
    creation_time: str
    members: list[ClanMember] | list
    owner: ClanOwner
    level: int
    experience: int
    total_experience: int


@dataclass
class Rank:
    """
    A child object of Player.

    It contains the information of the player's level, experience and the Rank Display of the minigames gamemode.
    """

    level: int
    experience: int
    percentage: float
    rank_display: str


@dataclass
class GameRank:
    """
    A child object of Player.

    It contains the information of the player's rank.
    """
    name: str
    display_name: str
    server: str
    season: str | None


@dataclass
class Friend:
    """
    A child object of Player.

    It contains the information of a player's friend.
    """
    username: str
    last_seen: int
    online: bool


@dataclass
class Player:
    """
    A Player object.

    It contains the whole information of the player.
    """
    username: str
    friend_status: str
    discord_verified: bool
    last_seen: int
    ranks: list[GameRank]
    email_verified: bool
    discord_boosting: bool
    clan: Clan | None
    rank: Rank
    friends: list[Friend]

    def get_leaderboard(self):
        leaderboard = build_player_leaderboard(self.username)


@dataclass
class LeaderboardData:
    total_entries: int

    place: int | None
    value: str | None
    username: str | None


@dataclass
class LeaderboardBase:
    """
    LeaderboardBase

    An object that initiates any type of leaderboard.
    """
    data: dict
    total_entries: int


class Leaderboards:
    """
    A class that contains a set of dataclasses for leaderboards.
    """
    pass