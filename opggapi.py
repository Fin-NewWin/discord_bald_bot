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

    try:
        url = f"https://www.op.gg/summoners/{server.lower()}/{username}"
        http = urllib3.PoolManager()
        response = http.request("GET", url, decode_content=True)
        reply = response.data

        soup = BeautifulSoup(reply, "html.parser")
        pic = soup.find("div", {"class": "profile-icon"}).contents[0].attrs["src"]
        print(pic)
        level = soup.find("div", {"class": "level"}).text
        print(soup.find("div", {"class": "win-lose"}).text)

        try:
            rank_solo_duo = (
                soup.find("div", {"class": "css-1kw4425 ecc8cxr0"})
                .find("div", {"class": "tier"})
                .text
            )
            rank_flex = (
                soup.find("div", {"class": "css-1ialdhq ecc8cxr0"})
                .find("div", {"class": "tier"})
                .text
            ) or "Unranked"
            print(rank_flex)
            # find win and lose in rank
            solo_lp = soup.find("div", {"class": "lp"}).text
        except AttributeError:
            rank_solo_duo = "Unranked"
            tier = None
            solo_lp = ""

        # print(pic)
        # print(url)
        # print(tier)
        # print(f"{lp} lp")

        return [pic, url, level, rank_solo_duo, solo_lp]
    except AttributeError:
        return None


# example usage
retrieve_rank("na", "Pho King-eboy")
retrieve_rank("na", "yeefide-NA1")
retrieve_rank("na", "Not Relapse-NA1")
