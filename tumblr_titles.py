from lxml import html
import requests

URL = "http://madakikoeru.tumblr.com/"

page = requests.get(URL)
tree = html.fromstring(page.content)

titles = tree.xpath("//div[contains(@class, 'copy')]/h2/text()")

for title in titles:
    print(title.strip())
