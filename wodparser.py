import urllib.request
from html.parser import HTMLParser

class WODParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.tag = ''
        self.attrs = []
        self.wod = None


    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tag = tag
        self.attrs = attrs

    def handle_endtag(self, tag: str) -> None:
        self.tag = ''

    def has_class(self, attrs, clazz) -> bool:
        for attr in attrs:
            if attr[0] == 'class' and attr[1] == clazz:
                return True
        return False

    def handle_data(self, data: str) -> None:
        if self.wod:
            return

        if self.tag == 'h2' and self.has_class(self.attrs, 'word-header-txt'):
            self.wod = data

    def get_wod(self):
        return self.wod


def get_wod(date: str) -> str | None:
    try:
        url = "https://www.merriam-webster.com/word-of-the-day/" + date
        text = urllib.request.urlopen(url).read().decode('utf8')
    except Exception as e:
        print("Unable to retrieve page: ", str(e))
        return None

    parser = WODParser()
    parser.feed(text)
    return parser.get_wod()
