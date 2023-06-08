# pikanetwork.py

A unique API wrapper for **PikaNetwork API**.

It provides ready-to-use objects from the api to python for optimization and durability of data.

It also makes accessing data an easy thing to do.

# Basic Examples:
## Fetching a player's information.
```py
from pikanetwork import PikaAPI
import asyncio

app = PikaAPI()


async def print_player_data(name: str):
    player = await app.get_player(name)

    print(player)


async def print_player_clan(name: str):
    player = await app.get_player(name)

    # Sometimes the Player has a Nullified clan Attribute. you can use an if statement on the clan object
    # for easier handling.
    try:
        print(player.clan)
    except AttributeError:
        print("This player does not have a clan!")
        
    # or
    if player.clan is None:
        print("This player does not have a clan.")
        return
    
    print(player.clan.owner)


async def print_player_clan_owner(name: str):
    player = await app.get_player(name)

    try:
        print(player.clan.owner)
    except AttributeError:
        print("This player does not have a clan!")

    # or
    if player.clan is None:
        print("This player does not have a clan.")
        return
    
    print(player.clan.owner)


asyncio.run(print_player_data("LetsChill"))
# Player(...)
asyncio.run(print_player_clan("MrEpiko"))
# Clan(...)
# or
# This player does not have a clan.
asyncio.run(print_player_clan_owner("Arrly"))
# ClanOwner(...)
# or
# This player does not have a clan.
```
## Fetching a player's leaderboard statistics.
```python
from pikanetwork import PikaAPI
import asyncio

app = PikaAPI()

async def get_player_bedwars_leaderboard(name: str):
    
    leaderboard = await app.get_player_leaderboard(name, "bedwars", "total", "solo")
    
    print(leaderboard)

asyncio.run(get_player_bedwars_leaderboard("Wondermine"))
# PlayerLeaderboard(...)
```

# Installation

to install pikanetwork.py, you can use:
```shell
$ pip install pikanetwork.py
```

# Contribution
You can open an issue to state your concerns or feature you want to implement.

We can make a deal and arrange how tasks should be assigned.

**ALWAYS OPEN AN ISSUE BEFORE MAKING A PULL REQUEST.**

# License

Copyright (c) 2023 LetsChill.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.