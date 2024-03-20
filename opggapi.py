import urllib3
from bs4 import BeautifulSoup


def retrieve_rank(server, username):

    try:
        url = f"https://www.op.gg/summoners/{server.lower()}/{username}"
        http = urllib3.PoolManager()
        response = http.request("GET", url, decode_content=True)
        reply = response.data

        soup = BeautifulSoup(reply, "html.parser")

        pic = soup.find("img", {"alt": "profile image"})
        if pic:
            pic = pic["src"]

        # level = soup.find("div", {"class": "level"}).text
        # print(soup.find("div", {"class": "win-lose"}).text)

        # try:
        #     rank_solo_duo = (
        #         soup.find("div", {"class": "css-1kw4425 ecc8cxr0"})
        #         .find("div", {"class": "tier"})
        #         .text
        #     )
        #     rank_flex = (
        #         soup.find("div", {"class": "css-1ialdhq ecc8cxr0"})
        #         .find("div", {"class": "tier"})
        #         .text
        #     ) or "Unranked"
        #     print(rank_flex)
        #     # find win and lose in rank
        #     solo_lp = soup.find("div", {"class": "lp"}).text
        # except AttributeError:
        #     rank_solo_duo = "Unranked"
        #     tier = None
        #     solo_lp = ""

        # print(pic)
        # print(url)
        # print(tier)
        # print(f"{lp} lp")

        # return [pic, url, level, rank_solo_duo, solo_lp]
        # return [pic, url, level]
    except AttributeError:
        return None


# example usage
retrieve_rank("na", "Pho King-eboy")
retrieve_rank("na", "yeefide-NA1")
retrieve_rank("na", "Not Relapse-NA1")
