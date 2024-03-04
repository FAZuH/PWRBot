from __future__ import annotations
from typing import TYPE_CHECKING

from discord import Client
from discord.app_commands import CommandTree

from pwrbot import Config
from pwrbot.cog import (
    Admin,
    Help,
    Info,
    Playback,
    Playlist,
    Queue,
    Song
)

if TYPE_CHECKING:
    from pwrbot import Logger


class Cogs:

    def __init__(self, client: Client, command_tree: CommandTree, config: Config, logger: Logger) -> None:
        cog_args = (client, command_tree, config, logger)
        self.admin = Admin(*cog_args)
        self.help = Help(*cog_args)
        self.info = Info(*cog_args)
        self.playback = Playback(*cog_args)
        self.playlist = Playlist(*cog_args)
        self.queue = Queue(*cog_args)
        self.song = Song(*cog_args)

    def setup(self) -> None:
        self.admin.setup()
        self.help.setup()
        self.info.setup()
        self.playback.setup()
        self.playlist.setup()
        self.queue.setup()
        self.song.setup()
