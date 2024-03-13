import urllib3
from bs4 import BeautifulSoup

"""
        Parameters
        ----------
        server : str
            The server abreviation as used in the op gg url -> "euw", "na", "kr" etc.
        username : str
            The username and the Riot tag seperated by a "-" -> "your_name-Riot_tag"
"""


def retrieve_rank(server, username):

    url = f"https://www.op.gg/summoners/{server.lower()}/{username}"
    http = urllib3.PoolManager()
    response = http.request("GET", url, decode_content=True)
    reply = response.data

    soup = BeautifulSoup(reply, "html.parser")
    pic = soup.find("div", {"class": "profile-icon"}).contents[0].attrs["src"]
    try:
        tier = soup.find("div", {"class": "tier"}).contents[0]
        lp = soup.find("div", {"class": "lp"}).contents[0]
    except AttributeError:
        tier = "Unranked"
        lp = ""

    # print(pic)
    # print(url)
    # print(tier)
    # print(f"{lp} lp")

    return [pic, tier, lp, url]


# example usage
# retrieve_rank("na", "Not Relapse-NA1")
