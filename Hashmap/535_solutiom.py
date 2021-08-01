class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        enc = ""
        for i in longUrl:
            enc += str(ord(i)) + "+"
        print(enc)
        return enc

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        dec = ""
        shortUrl = shortUrl.split("+")
        print(shortUrl)
        for i in shortUrl:
            if i.isdigit():
                dec += chr(int(i))
        return dec
