import asyncio
from time import sleep

from pwrbot.app import PwrBot


class Main:

    def __init__(self) -> None:
        self._app = PwrBot()

    def main(self) -> None:
        self._app.start()

        while True:
            inpt = input()
            if inpt == "exit":
                self._app.logger.console.info("Exiting...")
                exit(0)
            sleep(1)

    @property
    def app(self) -> PwrBot:
        return self._app


if __name__ == "__main__":
    main = Main()
    try:
        main.main()
    except Exception as e:
        asyncio.run(main.app.logger.discord.error("Fatal Error Occured", e))
