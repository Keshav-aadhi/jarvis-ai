import feedparser


def get_news(category="india"):

    try:

        feeds = {

            "india": "https://news.google.com/rss/search?q=India&hl=en-IN&gl=IN&ceid=IN:en",

            "tamilnadu": "https://news.google.com/rss/search?q=Tamil+Nadu&hl=en-IN&gl=IN&ceid=IN:en",

            "technology": "https://news.google.com/rss/search?q=Technology&hl=en-IN&gl=IN&ceid=IN:en",

            "ai": "https://news.google.com/rss/search?q=Artificial+Intelligence&hl=en-IN&gl=IN&ceid=IN:en",

            "sports": "https://news.google.com/rss/search?q=Sports&hl=en-IN&gl=IN&ceid=IN:en"
        }

        feed = feedparser.parse(
            feeds.get(category, feeds["india"])
        )

        headlines = []

        for entry in feed.entries[:5]:

            headlines.append(entry.title)

        if not headlines:

            return "No news found."

        return ". ".join(headlines)

    except Exception as e:

        print("NEWS ERROR:", e)

        return "Sorry boss, I could not fetch the news."