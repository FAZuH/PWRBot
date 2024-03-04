from __future__ import annotations
from enum import Enum
import traceback
from typing import TYPE_CHECKING

from aiohttp import ClientSession
import discord

from . import ConsoleLogger

if TYPE_CHECKING:
    from pwrbot import Config


class DiscordLogger:  # NOTE: i hate how this class looks
    """For exceptions needed to be sent to discord to be logged and reported to the developer."""

    def __init__(self, config: Config, console_logger: ConsoleLogger) -> None:
        self._config = config
        self._console_logger = console_logger

    async def issues(self, message: str, exception: None | BaseException = None) -> None:
        self._console_logger.warning(message)
        await self._send_to_discord(message, self.DiscordLoggerType.ISSUES, exception)

    async def report(self, message: str) -> None:
        self._console_logger.info(message)
        await self._send_to_discord(message, self.DiscordLoggerType.REPORT)

    async def error(self, message: str, exception: None | BaseException = None) -> None:
        await self._send_to_discord(message, self.DiscordLoggerType.ERROR, exception)

    async def _send_to_discord(self, message: str, type_: DiscordLogger.DiscordLoggerType, exc: None | BaseException = None) -> None:
        if type_ is self.DiscordLoggerType.ISSUES:
            url = self._config.issues_webhook
        elif type_ is self.DiscordLoggerType.REPORT:
            url = self._config.report_webhook
        else:
            raise ValueError(f"Invalid type: {type_}")

        async with ClientSession() as s:
            hook = discord.Webhook.from_url(url, session=s)
            if exc is None:
                await hook.send(message)
            else:
                await hook.send(embed=self._get_embed(message, exc))

    def _get_embed(self, message: str, exc: BaseException) -> discord.Embed:
        tb = f"`{exc}` ```{''.join(traceback.format_exception(type(exc), exc, exc.__traceback__))}```"
        tb = tb[:1024]
        return discord.Embed(
                title="Caught exception",
                description=message,
                color=discord.Colour.red()
        ).add_field(name="Traceback", value=tb)


    class DiscordLoggerType(Enum):
        ISSUES = "ISSUES"
        REPORT = "REPORT"
        ERROR = "ERROR"
