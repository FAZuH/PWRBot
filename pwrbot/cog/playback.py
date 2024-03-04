from __future__ import annotations
from typing import TYPE_CHECKING

from discord import app_commands

from . import CogBase

if TYPE_CHECKING:
    from discord import Interaction


class Playback(CogBase):

    def setup(self) -> None:
        self._commands.extend([
                self.play,
                self.search,
                self.skip,
                self.skipto,
                self.previous
        ])

    @app_commands.command()
    async def play(self, interation: Interaction) -> None:
        return

    @app_commands.command()
    async def search(self, interation: Interaction) -> None:
        return

    @app_commands.command()
    async def skip(self, interation: Interaction) -> None:
        return

    @app_commands.command()
    async def skipto(self, interation: Interaction) -> None:
        return

    @app_commands.command()
    async def previous(self, interation: Interaction) -> None:
        return
