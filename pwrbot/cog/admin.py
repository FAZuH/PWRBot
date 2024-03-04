from __future__ import annotations
from typing import TYPE_CHECKING

from discord import app_commands

from . import CogBase

if TYPE_CHECKING:
    from discord import Interaction



class Admin(CogBase):

    def setup(self) -> None:
        self._commands.extend([
                self.echo
        ])

    @app_commands.command()
    async def echo(self, interaction: Interaction, message: str) -> None:
        await interaction.response.send_message(message)
