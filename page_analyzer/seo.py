from bs4 import BeautifulSoup


def get_tag_text(tag):
    if tag is None:
        return None

    return tag.get_text(" ", strip=True)


def get_description(soup):
    tag = soup.find(
        "meta",
        attrs={"name": "description"},
    )

    if tag is None:
        return None

    content = tag.get("content")

    if not isinstance(content, str):
        return None

    return content.strip()


def parse_page(html):
    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    return {
        "h1": get_tag_text(soup.find("h1")),
        "title": get_tag_text(soup.find("title")),
        "description": get_description(soup),
    }
