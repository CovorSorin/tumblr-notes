from lxml import html
import requests

URL = 'http://madakikoeru.tumblr.com/archive'

page = requests.get(URL)
tree = html.fromstring(page.content)

notes = tree.xpath("//span[contains(@class, 'post_notes')]/text()")

total_notes = 0
max_notes = 0

for note in notes:
    note = int(note.strip()[:-6])
    total_notes += note

    if (max_notes < note):
        max_notes = note

print('Number of posts:', len(notes))
print('Total notes:', total_notes)
print('Max number of notes of one post:', max_notes)
print('Average number of notes per post:', total_notes / len(notes))
