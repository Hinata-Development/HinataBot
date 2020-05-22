import os

class CogHandler():
    def __init__(self, hinata):
        self.hinata = hinata

    def load_all_cogs(self):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                cog_name = file[:-3]
                try:
                    self.hinata.bot.load_extension(f"cogs.{cog_name}")
                    print(f"[>] Loaded Cog: {cog_name}")
                except Exception as err:
                    print(f"[!] Error loading cog {cog_name}, {type(err).__name__} - {err}")
        print("[>] Finished loading cogs.")