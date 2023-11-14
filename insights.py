
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk



def perform_sentiment_analysis(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def extract_keywords(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_features=10)  # Extract the top 10 keywords
    tfidf_vectorizer.fit(words)

    # Get the feature names (keywords)
    keywords = tfidf_vectorizer.get_feature_names_out()

    return keywords



def insight_sent():
    with open('reviews.txt', 'r', encoding='utf-8') as file:
        reviews_text = file.read()
    
    sentiment_score = perform_sentiment_analysis(reviews_text)
    keywords = extract_keywords(reviews_text)
    
    return "Sentiment Score: {}\n".format(sentiment_score) + "Keywords: {}\n".format(keywords)

# with open('insights.txt', 'w', encoding='utf-8') as output_file:
#     output_file.write("Sentiment Score: {}\n".format(sentiment_score))
#     output_file.write("Keywords: {}\n".format(keywords))

# print("Insights have been saved to insights.txt")
print(insight_sent())