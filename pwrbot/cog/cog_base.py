from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING, Any

from discord import Client
from discord.ext.commands import Cog

from pwrbot import Config

if TYPE_CHECKING:
    from discord.app_commands import Command, CommandTree
    from pwrbot import Logger


class CogBase(Cog):

    def __init__(self, client: Client, command_tree: CommandTree, config: Config, logger: Logger) -> None:
        self._client = client
        self._command_tree = command_tree
        self._config = config
        self._logger = logger

        self._commands: list[Command[Any, ..., Any]] = []

    def setup(self) -> None:
        """
        Setup method to be called after instantiation.
        Adds commands to self._command_tree.
        """
        for cmd in self._commands:
            self._command_tree.add_command(cmd)
            self._logger.console.success(f"Added command: {cmd.name}")
        self._logger.console.success(f"Added cog: {self.__class__.__name__}")

    @abstractmethod
    def _setup(self) -> None:
        """For subclasses to add commands into self._commands."""
        pass
