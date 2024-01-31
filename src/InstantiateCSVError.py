class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = f"Файл {args[0]} поврежден"

    def __str__(self):
        return self.message
