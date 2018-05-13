from lxml import html
import requests

print('Counting...')

URL = 'https://madakikoeru.tumblr.com/page/'

total_posts = 0
total_notes = 0
max_notes = 0

reached_end = False
current_page = 0

while (not reached_end):
    current_page += 1

    page = requests.get(URL + str(current_page))
    tree = html.fromstring(page.content)

    # ignore the reblogged posts
    notes = tree.xpath("//*[contains(@class, 'post') and not(contains(@class, 'reblogged'))]//li[contains(@class, 'notes')]/a/text()")

    if (not notes):
        reached_end = True
        break

    total_posts += len(notes)
    for note in notes:
        note = int(note)
        total_notes += note

    if (max_notes < note):
        max_notes = note

print('Number of pages:', current_page)
print('Number of posts:', total_posts)
print('Total notes:', total_notes)
print('Max number of notes of one post:', max_notes)
print('Average number of notes per post:', round(total_notes / total_posts))
