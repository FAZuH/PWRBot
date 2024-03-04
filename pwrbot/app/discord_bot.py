from __future__ import annotations
from typing import TYPE_CHECKING

from discord import Client, Intents
from discord.app_commands import CommandTree

from . import Cogs
from pwrbot import Config

if TYPE_CHECKING:
    from pwrbot import Logger


class DiscordBot:

    def __init__(self, config: Config, logger: Logger) -> None:
        self._logger = logger
        self._bot_token = config.discord_bot_token
        self._intents = Intents.default()
        self._intents.message_content = True
        self._intents.members = True
        self._intents.presences = True

        self._client = Client(intents=self._intents)
        self._command_tree = CommandTree(self.client)
        self._cogs = Cogs(self.client, self._command_tree, config, logger)

    async def setup(self) -> None:
        @self.client.event
        async def on_ready() -> None:  # type: ignore
            if self.client.user is not None:
                await self._logger.discord.report(f"<@{self.client.user.id}> has successfully started.")

        self._cogs.setup()

    async def start(self) -> None:
        await self.setup()
        await self.client.start(self._bot_token)
        await self._command_tree.sync()

    @property
    def client(self) -> Client:
        return self._client
