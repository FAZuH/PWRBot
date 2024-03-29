from . import (
    ConsoleLogger,
    DiscordLogger,
    Logger,
    PerformanceLogger
)
from pwrbot import Config


class PwrbotLogger(Logger):

    def __init__(self, config: Config) -> None:
        self._console_logger = ConsoleLogger()
        self._discord_logger = DiscordLogger(config, self._console_logger)
        self._performance_logger = PerformanceLogger()

    def set_up(self) -> None:
        return

    @property
    def console(self) -> ConsoleLogger:
        return self._console_logger

    @property
    def discord(self) -> DiscordLogger:
        return self._discord_logger

    @property
    def performance(self) -> PerformanceLogger:
        return self._performance_logger
