import feedparser

RSS_FEEDS = {
    "world": "http://rss.cnn.com/rss/cnn_world.rss",
    "finance": "http://rss.cnn.com/rss/money_latest.rss",
    "tech": "http://rss.cnn.com/rss/cnn_tech.rss",
    "health": "http://rss.cnn.com/rss/cnn_health.rss",
    "entertainment": "http://rss.cnn.com/rss/cnn_showbiz.rss"
}

def aggregate_news(category):
    feed_url = RSS_FEEDS.get(category, RSS_FEEDS["world"])
    feed = feedparser.parse(feed_url)
    news_items = []

    for entry in feed.entries:
        media_content = entry.media_content[0]['url'] if 'media_content' in entry and entry.media_content else None
        news_items.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary if 'summary' in entry else 'No summary available.',
            "media_content": media_content
        })

    return {"news": news_items}
