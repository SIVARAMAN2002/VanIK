import requests
from chatgpt import PalmConfig
import googlemaps
from geopy.geocoders import Nominatim
# from insights import insight_sent

from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

# Replace 'YOUR_API_KEY' with your actual Google API Key


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



def Process(keywords,genre):
  

    api_key = 'AIzaSyCeGZwfk9MYlwOIJk3uUbmenWJskyNkgO4'
    #gmaps = googlemaps.Client(key=api_key)

    response = requests.get("https://ipinfo.io")
    data = response.json()

    print("IP Address:", data["ip"])
    print("Location:", data["city"] + ", " + data["region"])
    print("Latitude, Longitude:", data["loc"])


    # Define the keyword and location (latitude and longitude)
    keyword = genre
    #geocode_result = gmaps.geocode(keywords)
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(keywords)
    #location = data["loc"]
    newstr= str(location.latitude)+","+str(location.longitude)
    print(type(location))     
    #location=geocode_result[0]['place_id']
   
    #Set the radius for the search (in meters)
    radius = 5000  # You can adjust this as needed

    # Create the API request URL
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={newstr}&radius={radius}&keyword={keyword}&key={api_key}'


    # Send the request and get the JSON response
    response = requests.get(url)
    data = response.json()
    review_texts=""
    # Check if the request was successful
    if data.get('status') == 'OK':
        # Create a file for writing the reviews
        with open('reviews.txt', 'w', encoding='utf-8') as file:
            # Loop through the places
            for place in data['results']:
                place_name = place['name']
                place_id = place['place_id']

                # Get the details for this place
                details_url = f'https://maps.googleapis.com/maps/api/place/details/json?placeid={place_id}&key={api_key}'
                details_response = requests.get(details_url)
                details_data = details_response.json()

                if details_data.get('status') == 'OK':
                    file.write(f'Reviews for {place_name}:\n')
                    review_texts=review_texts+"Reviews for"+place_name+":"+"\n"
                    # Get and write the top 10 reviews
                    reviews = details_data['result'].get('reviews', [])
                    for i, review in enumerate(reviews[:100], start=1):
                        review_text = review.get('text', '')
                        review_texts=review_texts+"\n"+"Review "+str(i)+":"+"\n"+review_text+"\n"+"\n"
                        print(review_texts)
                        file.write(f'Review {i}:\n{review_text}\n\n')
                    file.write('\n')    
                else:
                    file.write(f'Error fetching details for {place_name}: {details_data.get("status")}\n')
        print(review_texts)
        print('Reviews have been saved to reviews.txt')
        review_text = review_text + "\n" + insight_sent()
        return PalmConfig(review_texts)   
    else:
        print(f'Error: {data.get("status")} - {data.get("error_message", "No error message provided")}')
