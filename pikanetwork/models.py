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