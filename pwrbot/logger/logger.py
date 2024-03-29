from __future__ import annotations
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import ConsoleLogger, DiscordLogger, PerformanceLogger
    from pwrbot import Config


class Logger(Protocol):
    def __init__(self, config: Config) -> None: ...
    def set_up(self) -> None: ...
    @property
    def console(self) -> ConsoleLogger: ...
    @property
    def discord(self) -> DiscordLogger: ...
    @property
    def performance(self) -> PerformanceLogger: ...
