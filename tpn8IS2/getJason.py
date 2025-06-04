import json


class SiteData:
    _instance = None
    _data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SiteData, cls).__new__(cls)
            with open("sitedata.json", encoding="utf-8") as f:
                cls._data = json.load(f)
        return cls._instance

    def get_key(self, token_name):
        return self._data.get(token_name)
