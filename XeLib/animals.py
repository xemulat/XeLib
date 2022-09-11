from json import load
from urllib.request import urlopen

def dl(base, defi, add):
    if base == "animal" and add == "img":
        with urlopen("https://some-random-api.ml/" + base + "/" + defi) as l:
            return(load(l)["image"])
    if base == "animal" and add == "fact":
        with urlopen("https://some-random-api.ml/" + base + "/" + defi) as l:
            return(load(l)["fact"])
    if base == "img":
        with urlopen("https://some-random-api.ml/" + base + "/" + defi) as l:
            return(load(l)["link"])
    if base == "facts":
        with urlopen("https://some-random-api.ml/" + base + "/" + defi) as l:
            return(load(l)["fact"])

class image():
    def dog():
        return dl("img", "dog", 0)
    def cat():
        return dl("img", "cat", 0)
    def panda():
        return dl("img", "panda", 0)
    def fox():
        return dl("img", "fox", 0)
    def bird():
        return dl("img", "bird", 0)
    def koala():
        return dl("img", "koala", 0)
    def raccoon():
        return dl("animal", "raccoon", "img")
    def kangaroo():
        return dl("animal", "dog", "img")
    def redpanda():
        return dl("animal", "red_panda", "img")
    
class facts():
    def dog():
        return dl("facts", "dog", 0)
    def cat():
        return dl("facts", "cat", 0)
    def panda():
        return dl("facts", "panda", 0)
    def fox():
        return dl("facts", "fox", 0)
    def bird():
        return dl("facts", "birb", 0)
    def koala():
        return dl("facts", "koala", 0)
    def raccoon():
        return dl("animal", "raccoon", "fact")
    def kangaroo():
        return dl("animal", "kangaroo", "fact")
    def redpanda():
        return dl("animal", "red_panda", "fact")