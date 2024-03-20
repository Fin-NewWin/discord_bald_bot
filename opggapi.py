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
        print(pic)

        level = soup.find("div", {"class": "level"})
        if level:
            level = level.text
        print(level)

        rank_solo_duo = soup.find("div", {"class": "css-1kw4425 ecc8cxr0"})
        rank_solo_duo_lp = None
        rank_solo_duo_wl = None
        if rank_solo_duo:
            rank_solo_duo_lp = rank_solo_duo.find("div", {"class": "lp"})
            rank_solo_duo_wl = rank_solo_duo.find("div", {"class": "win-lose"})
            rank_solo_duo = rank_solo_duo.find("div", {"class": "tier"})
            if rank_solo_duo and rank_solo_duo_lp and rank_solo_duo_wl:
                rank_solo_duo = rank_solo_duo.text.title()
                rank_solo_duo_lp = rank_solo_duo_lp.text
                rank_solo_duo_wl = rank_solo_duo_wl.text
            else:
                rank_solo_duo = "Unranked"
        print(rank_solo_duo)
        print(rank_solo_duo_lp)
        print(rank_solo_duo_wl)

        rank_flex = soup.find("div", {"class": "css-1ialdhq ecc8cxr0"})
        rank_flex_lp = None
        rank_flex_wl = None
        if rank_flex:
            rank_flex_lp = rank_flex.find("div", {"class": "lp"})
            rank_flex_wl = rank_flex.find("div", {"class": "win-lose"})
            rank_flex = rank_flex.find("div", {"class": "tier"})
            if rank_flex and rank_flex_lp and rank_flex_wl:
                rank_flex = rank_flex.text.title()
                rank_flex_lp = rank_flex_lp.text
                rank_flex_wl = rank_flex_wl.text
            else:
                rank_flex = "Unranked"
        print(rank_flex)
        print(rank_flex_lp)
        print(rank_flex_wl)

        return [
            pic,
            url,
            level,
            rank_solo_duo,
            rank_solo_duo_lp,
            rank_solo_duo_wl,
            rank_flex,
            rank_flex_lp,
            rank_flex_wl,
        ]
        # return [pic, url, level]
    except AttributeError:
        return None


# example usage
retrieve_rank("na", "Pho King-eboy")
retrieve_rank("na", "yeefide-NA1")
retrieve_rank("na", "Not Relapse-NA1")
