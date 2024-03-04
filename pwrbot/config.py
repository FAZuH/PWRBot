from typing import Any

from dotenv import dotenv_values


class Config:

    # def __init__(self, config: dict[str, str | None]) -> None:
    def __init__(self) -> None:
        self._config = dotenv_values(".env")
        self._admin_discord_id = int(self._must_get(self._config, "ADMIN_DISCORD_ID"))
        self._discord_bot_token = self._must_get(self._config, "DISCORD_BOT_TOKEN")
        self._discord_bot_client_id = int(self._must_get(self._config, "DISCORD_BOT_CLIENT_ID"))
        self._issues_webhook = self._must_get(self._config, "ISSUES_WEBHOOK")
        self._report_webhook = self._must_get(self._config, "REPORT_WEBHOOK")

    def _must_get(self, dict_: dict[str, str | None], key: str) -> Any:
        value = dict_.get(key)
        if value is None:
            raise ValueError(f"Missing required config key: {key}")
        return value

    @property
    def admin_discord_id(self) -> int:
        return self._admin_discord_id

    @property
    def discord_bot_token(self) -> str:
        return self._discord_bot_token

    @property
    def discord_bot_client_id(self) -> int:
        return self._discord_bot_client_id

    @property
    def issues_webhook(self) -> str:
        return self._issues_webhook

    @property
    def report_webhook(self) -> str:
        return self._report_webhook
