import hashlib

class Codec:
    def __init__(self):
        self.mapping = {}

    def encode(self, longUrl: str) -> str:
        d = hashlib.md5(longUrl.encode('utf8')).digest()
        tiny = f"http://tinyurl.com/{d}"
        
        self.mapping[tiny] = longUrl
        return tiny
        
    def decode(self, shortUrl: str) -> str:
        return self.mapping[shortUrl]
