# Create and initialize the application

# Create a new Python script in your favorite IDE or editor, and the following imports:
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

# Create variables for your subscription key and search term.
subscription_key = "Enter your key here"
search_term = "canadian rockies"

# Create the image search client
# Create an instance of CognitiveServicesCredentials, and use it to instantiate the client:
client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))
# Send a search query to the Bing Image Search API:
image_results = client.images.search(query=search_term)
# Process and view the results
# Parse the image results returned in the response.
# If the response contains search results, store the first result and print out its details, such as a thumbnail URL, the original URL,along with the total number of returned images.
if image_results.value:
    first_image_result = image_results.value[0]
    print("Total number of images returned: {}".format(len(image_results.value)))
    print("First image thumbnail url: {}".format(
        first_image_result.thumbnail_url))
    print("First image content url: {}".format(first_image_result.content_url))
else:
    print("No image results returned!")
