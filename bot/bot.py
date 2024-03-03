import os

from discord import Bot

from bot.slash_commands import commands


class DiscordBot(Bot):
    """
    The interface for user interaction with the Discord bot
    """

    def __init__(self):
        super(Bot, self).__init__()

        # Register slash commands
        for command in commands:
            self.add_application_command(command)

    async def on_ready(self):
        print(f"Ready! Logged in as {self.user.name} ({self.user.id})")

    _instance = None

    @classmethod
    def initialize(cls):
        assert cls._instance is None, "Initializer called more than once"
        cls._instance = DiscordBot()
        cls._instance.run(os.environ.get("TOKEN"))

    @classmethod
    def get_instance(cls) -> "DiscordBot":
        assert cls._instance is not None, "Instance not yet initialized"
        return cls._instance