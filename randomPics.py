from httpx import get
from random import randint


def getGoats():
    res = "http://placegoat.com/200/200"
    return res

def getPoke():
    r =randint(1, 893)
    res = f"https://pokeres.bastionbot.org/images/pokemon/{r}.png"
    return res

def getCats():
    res = get("https://aws.random.cat/meow").json()
    return res['file']

def getDogs():
    res = get("https://random.dog/woof.json").json()
    return res['url']
def getFox():
    res = get("https://randomfox.ca/floof/").json()
    return res['image']

