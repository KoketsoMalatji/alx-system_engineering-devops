#!/usr/bin/python3
""" prints the titles of the first 10 hot posts"""


def top_ten(subreddit):

    from requests import get

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    headers = {'user-agent': 'my-app1'}

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print(None)
        return None

    try:
        js = r.json()

    except ValueError:
        print(None)
        return None

    try:

        data = js.get("data")
        children = data.get("children")
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))

    except:
        print(None)
