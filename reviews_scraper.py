import requests

# Replace 'YOUR_API_KEY' with your actual Google API Key
api_key = 'AIzaSyCeGZwfk9MYlwOIJk3uUbmenWJskyNkgO4'


response = requests.get("https://ipinfo.io")
data = response.json()

print("IP Address:", data["ip"])
print("Location:", data["city"] + ", " + data["region"])
print("Latitude, Longitude:", data["loc"])


# Define the keyword and location (latitude and longitude)
keyword = 'Restaurants'
location = data["loc"]

# Set the radius for the search (in meters)
radius = 5000  # You can adjust this as needed

# Create the API request URL
url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={keyword}&key={api_key}'

# Send the request and get the JSON response
response = requests.get(url)
data = response.json()

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

                # Get and write the top 10 reviews
                reviews = details_data['result'].get('reviews', [])
                for i, review in enumerate(reviews[:100], start=1):
                    review_text = review.get('text', '')
                    file.write(f'Review {i}:\n{review_text}\n\n')
                file.write('\n')
            else:
                file.write(f'Error fetching details for {place_name}: {details_data.get("status")}\n')

    print('Reviews have been saved to reviews.txt')
else:
    print(f'Error: {data.get("status")} - {data.get("error_message", "No error message provided")}')
