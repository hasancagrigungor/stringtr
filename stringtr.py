class StringTR:
    _kucukharfler = "abcçdefgğhıijklmnoöprsştuüvyz"
    _buyukharfler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    _rakamlar = "0123456789"
    _semboller = "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    @classmethod
    def kucukharfler(cls):
        return cls._kucukharfler

    @classmethod
    def buyukharfler(cls):
        return cls._buyukharfler

    @classmethod
    def harfler(cls):
        return cls._kucukharfler + cls._buyukharfler

    @classmethod
    def rakamlar(cls):
        return cls._rakamlar

    @classmethod
    def semboller(cls):
        return cls._semboller