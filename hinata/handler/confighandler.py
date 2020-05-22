import os, json

class ConfigHandler:
    def __init__(self, path):
        self.path = path

        if not os.path.isfile(path):
            print("[!] Could not find config path, maybe invalid specification?")
            exit()

    def load_config(self):
        try:
            with open(self.path, 'r+') as readable:
                print("[>] Found config.")
                return json.loads(readable.read())
        except Exception as err:
            print(f"[!] Error loading config. {type(err).__name__} - {err}")
            exit()
