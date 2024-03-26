import random

import requests
from bs4 import BeautifulSoup


def retrieve_rank(server, username):

    try:
        url = f"https://www.op.gg/summoners/{server.lower()}/{username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Alt-Used": "www.op.gg",
            "Cookie": "_hackle_last_event_ts_3Gj3LiFYk3tUL82EOTg7sKdb=1711419968931; _hackle_hid=f168a3ad-86b5-4b83-948c-90ea0013e23e; _hackle_did_XYnC2Y883Gj3LiFYk3tUL82EOTg7sKdb=f168a3ad-86b5-4b83-948c-90ea0013e23e; _hackle_session_id_3Gj3LiFYk3tUL82EOTg7sKdb=1711406346309.58afd5ab; _hackle_mkt_XYnC2Y88=%7B%7D; _rs=%5B%5D; cf_clearance=6m4Y80V06SSQGolfzRiI_QzueN8nvJh9AAmmoZ0KUwQ-1711418227-1.0.1.1-cIRagHadTs94byuJL_CXUxCireYULaXthMfMYmc4YY_0E8KBrVs3Y7MsdfGIlTYkujuUe0Pmotrz5RVIzDvaVQ; _dd_s=rum=0&expire=1711420950016; __cf_bm=jUPxCxbRNPOCrnQKHlyYIR2achn5vz.d6AbloFp7l84-1711419833-1.0.1.1-RSY2FdGRtLAw0_ZxpUVlDlqyi_3I2argEehgrGYP4mn4vnZnQF3E7FrLEHlZc.wP51emvdGMjEkTIpRxifnN4A",
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

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
# retrieve_rank("na", "yeefide-NA1")
# retrieve_rank("na", "Not Relapse-NA1")
