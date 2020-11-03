import requests

class LocalImage:
    def __init__(self, path):
        self.path = path

    def get_image(self):
        return open(self._path, 'rb')
        