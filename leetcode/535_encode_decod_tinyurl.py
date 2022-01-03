class Codec:
    def __init__(self):
        self.buckets = [None] * 10_000
        self.length = 10_000

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        url_hash = abs(hash(longUrl))
        url_bucket = url_hash % self.length
        if self.buckets[url_bucket] is None:
            self.buckets[url_bucket] = [(url_hash, longUrl)]
        else:
            self.buckets[url_bucket].append((url_hash, longUrl))
        return str(url_hash)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        bucket = int(shortUrl) % self.length
        found_bucket = self.buckets[bucket]
        if len(found_bucket) == 1:
            return found_bucket[0][1]
        for b in found_bucket:
            obj_hash, url = b
            if obj_hash == shortUrl:
                return url


if __name__ == "__main__":
    codec = Codec()
    res = codec.encode("https://edmundmartin.com")
    print(res)
    res = codec.decode(res)
    print(res)
