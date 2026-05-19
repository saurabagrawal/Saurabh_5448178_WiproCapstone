class ConfigReader:

    def __init__(self):

        self.configs = {}

        with open("config/config.properties") as file:

            for line in file:

                if "=" in line:

                    key, value = line.strip().split("=", 1)

                    self.configs[key] = value

    def get(self, key):

        return self.configs.get(key)