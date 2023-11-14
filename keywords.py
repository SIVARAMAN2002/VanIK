import spacy
from nltk import *
from nltk.tokenize import sent_tokenize

# Load spaCy model and initialize NLTK
nlp = spacy.load('en_core_web_sm')
nltk.download('punkt')

# Define keywords related to businesses
business_keywords = ['Parking', 'Price', 'Service', 'Location', 'Ambiance']

# Function to extract sentences containing keywords
def extract_keyword_sentences(text, keywords):
    keyword_sentences = {}
    doc = nlp(text)

    for sentence in sent_tokenize(text):
        for keyword in keywords:
            if keyword.lower() in sentence.lower():
                if keyword in keyword_sentences:
                    keyword_sentences[keyword].append(sentence)
                else:
                    keyword_sentences[keyword] = [sentence]

    return keyword_sentences

# Read reviews from a text file
with open('reviews1.txt', 'r', encoding='utf-8') as file:
    reviews_text = file.read()

# Extract and print sentences containing keywords
keyword_sentences = extract_keyword_sentences(reviews_text, business_keywords)

for keyword, sentences in keyword_sentences.items():
    print(f"Sentences mentioning '{keyword}':")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}\n")
