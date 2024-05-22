from flask import Flask, jsonify, request, render_template
from .scraper import aggregate_news
from .analyzer import summarize_article

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/news', methods=['GET'])
def get_news():
    category = request.args.get('category', 'world')
    news_data = aggregate_news(category)
    print(f"News data: {news_data}")
    return jsonify(news_data)

@app.route('/api/analyze', methods=['GET'])
def analyze_article():
    url = request.args.get('url')
    summary, image_url = summarize_article(url)
    if not summary:
        summary = "Sorry, we couldn't generate a summary at this time. Read the full article below:"
    print(f"Summary: {summary}")
    return jsonify({'summary': summary, 'image_url': image_url})
