from os import path
from discord.ext import commands

import confighandler as _configHandler
import eventhandler as _eventHandler
import coghandler as _cogHandler


class Hinata:
    def __init__(self):
        self.config_path = path.join(path.dirname(path.abspath(__file__)), 'assets/config.json')
        self.config = _configHandler.ConfigHandler(self.config_path).load_config()

        self.dev_environment = bool(self.config['dev_environment'])
        print(f"[>] Running in dev environment? {'yes' if self.dev_environment else 'no'}")

        self.prefix = self.config['prefixing']['dev'] if self.dev_environment else self.config['prefixing']['release']
        self.token = self.config['discord']['dev'] if self.dev_environment else self.config['discord']['release']

        self.owner_id = self.config['owner_id']

        self.bot = commands.Bot(command_prefix=self.prefix, owner_id=self.owner_id, case_insensitive=True)
        self.bot.remove_command("help")

        self.event_handler = _eventHandler.EventHandler(self)
        self.cog_handler = _cogHandler.CogHandler(self)

    def load_bot(self):
        self.cog_handler.load_all_cogs()
        self.bot.run(self.token)


hinata = Hinata()
if __name__ == '__main__':
    hinata.load_bot()