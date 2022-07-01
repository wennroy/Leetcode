class Codec:
    def __init__(self):
        self.record = {}
        self.n = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.n += 1
        shortUrl = "http://tinyurl.com/" + str(self.n)
        self.record[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.record[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))