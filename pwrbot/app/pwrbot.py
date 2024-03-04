import asyncio

from . import DiscordBot
from pwrbot import Config
from pwrbot.logger import PwrbotLogger


class PwrBot:

    def __init__(self) -> None:
        self._config = Config()
        self._logger = PwrbotLogger(self._config)
        self._bot = DiscordBot(self._config, self._logger)

    def start(self) -> None:
        asyncio.run(self.bot.start())

    def stop(self) -> None:
        return

    @property
    def bot(self) -> DiscordBot:
        return self._bot

    @property
    def config(self) -> Config:
        return self._config

    @property
    def logger(self) -> PwrbotLogger:
        return self._logger
