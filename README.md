# News Aggregator

The News Aggregator fetches the latest news articles from various categories such as World, Finance, Tech, Health, and Entertainment from CNN RSS feeds. It provides users with a concise summary of the article's content using advanced summarization techniques.

## Features

- **Fetch News**: Retrieves the latest news articles from CNN RSS feeds.
- **Summarization**: Generates concise summaries for news articles.
- **Category Filter**: Users can filter news articles by category.
- **Scrollable News List**: Displays a scrollable list of news articles.
- **Original Article Link**: Provides a link to the full article.

## How It Works

1. **Select a Category**: Choose a news category from the dropdown.
2. **View Articles**: A list of articles will be displayed on the left.
3. **Generate Summary**: Click on an article to view a summary on the right.
4. **Read Full Article**: Follow the link to read the original article if needed.

## Setup

1. **Clone the Repository**
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd news-aggregator-bot
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Data**
   ```python
   python -c "import nltk; nltk.download('punkt')"
   ```


5. **Run the Flask Application**
   ```bash
   export FLASK_APP=src.app
   flask run
   ```

## Contributing

Feel free to contribute by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License.

---

