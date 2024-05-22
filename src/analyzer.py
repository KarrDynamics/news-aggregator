from newspaper import Article
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import sys

LANGUAGE = "english"
SENTENCES_COUNT = 5

def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        top_image = article.top_image

        if not text.strip():
            raise ValueError("Document is empty")

        parser = HtmlParser.from_string(text, url, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)
        summarizer = LsaSummarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        summary = summarizer(parser.document, SENTENCES_COUNT)
        summary_sentences = [str(sentence) for sentence in summary]

        return ' '.join(summary_sentences), top_image
    except Exception as e:
        print(f"Error summarizing article: {e}", file=sys.stderr)
        return None, None
