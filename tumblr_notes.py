from lxml import html
import requests

print('Counting...')

USERNAME = 'madakikoeru'
URL = 'https://' + USERNAME + '.tumblr.com/page/'

total_posts = 0
total_reblogs = 0
total_notes = 0
total_reblog_notes = 0
max_notes = 0

reached_end = False
current_page = 0

while (not reached_end):
    current_page += 1

    page = requests.get(URL + str(current_page))
    tree = html.fromstring(page.content)

    posts = tree.xpath("//*[contains(@class, 'post')]//li[contains(@class, 'notes')]/a/text()")
    reblogs = tree.xpath("//*[contains(@class, 'reblogged')]//li[contains(@class, 'notes')]/a/text()")

    if (not posts):
        reached_end = True
        break

    total_posts += len(posts)
    for post in posts:
        post = int(post)
        total_notes += post

        if (max_notes < post):
            max_notes = post

    total_reblogs += len(reblogs)
    for reblog in reblogs:
        total_reblog_notes += int(reblog)

print('Stats for ' + USERNAME + ':')
print('Number of pages:', current_page)
print('Number of posts:', total_posts - total_reblogs, '/', total_posts, '(' + str(total_reblogs) + ' reblogs ignored))')
print('Total notes:', total_notes - total_reblog_notes, '(ignoring', total_reblog_notes, 'reblogs)')
print('Best post:', max_notes, 'notes')
print('Average:', round(total_notes / total_posts), 'notes / post')
