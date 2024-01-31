class InstantiateCSVError(Exception):
    def __init__(self, path_to_file):
        self.message = f"Файл {path_to_file} поврежден"

    def __str__(self):
        return self.message
