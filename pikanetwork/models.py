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

from typing import (Optional, Union)


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
    members: Union[list[ClanMember], list]
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
    season: Optional[str]


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
    clan: Optional[Clan]
    rank: Rank
    friends: list[Friend]


@dataclass
class PlayerLeaderboardBase:
    total_players: int
    place: Union[int, None]
    value: Union[str, None]
    username: Union[str, None]


@dataclass
class PlayerLeaderboard:
    """
    A PlayerLeaderboard object

    It contains details about a player's leaderboard stats.
    """
    mobs_killed: Optional[PlayerLeaderboardBase] = None
    player_level: Optional[PlayerLeaderboardBase] = None
    deaths: Optional[PlayerLeaderboardBase] = None
    kills: Optional[PlayerLeaderboardBase] = None
    losses: Optional[PlayerLeaderboardBase] = None
    wins: Optional[PlayerLeaderboardBase] = None

    highest_killstreak: Optional[PlayerLeaderboardBase] = None
    current_killstreak: Optional[PlayerLeaderboardBase] = None
    highest_winstreak_reached: Optional[PlayerLeaderboardBase] = None

    balance: Optional[PlayerLeaderboardBase] = None

    blocks_placed: Optional[PlayerLeaderboardBase] = None
    blocks_broken: Optional[PlayerLeaderboardBase] = None

    gambling_skill_level: Optional[PlayerLeaderboardBase] = None
    swords_skill_level: Optional[PlayerLeaderboardBase] = None

    harvest_sugar_cane: Optional[PlayerLeaderboardBase] = None
    total_koths_won: Optional[PlayerLeaderboardBase] = None

    souls: Optional[PlayerLeaderboardBase] = None
    tokens: Optional[PlayerLeaderboardBase] = None
    tokens_obtained: Optional[PlayerLeaderboardBase] = None
    gems_obtained: Optional[PlayerLeaderboardBase] = None
    tokens_spent: Optional[PlayerLeaderboardBase] = None
    prestige: Optional[PlayerLeaderboardBase] = None
    exp_collected: Optional[PlayerLeaderboardBase] = None

    bow_kills: Optional[PlayerLeaderboardBase] = None
    arrow_kills: Optional[PlayerLeaderboardBase] = None
    melee_kills: Optional[PlayerLeaderboardBase] = None
    void_kills: Optional[PlayerLeaderboardBase] = None
    games_played: Optional[PlayerLeaderboardBase] = None
    arrows_shot: Optional[PlayerLeaderboardBase] = None
    arrows_hit: Optional[PlayerLeaderboardBase] = None
    beds_destroyed: Optional[PlayerLeaderboardBase] = None
    final_kills: Optional[PlayerLeaderboardBase] = None

    lumberjack_skill_level: Optional[PlayerLeaderboardBase] = None
    adventurer_skill_level: Optional[PlayerLeaderboardBase] = None
    farmer_skill_level: Optional[PlayerLeaderboardBase] = None
    archery_skill_level: Optional[PlayerLeaderboardBase] = None
    axes_skill_level: Optional[PlayerLeaderboardBase] = None
    special_ores_mined: Optional[PlayerLeaderboardBase] = None
    miner_skill_level: Optional[PlayerLeaderboardBase] = None
    wizard_skill_level: Optional[PlayerLeaderboardBase] = None
    banker_skill_level: Optional[PlayerLeaderboardBase] = None
    alchemist_skill_level: Optional[PlayerLeaderboardBase] = None
    lucky_skill_level: Optional[PlayerLeaderboardBase] = None
    drugs_skill_level: Optional[PlayerLeaderboardBase] = None
