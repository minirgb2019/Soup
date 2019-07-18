pip install azure
pip install azure-cognitiveservices
pip install azure-cognitiveservices-search-imagesearch
pip install msrest
pip install pillow

from azure.cognitiveservices.search import imagesearch
from IPython import display
from msrest import authentication
from PIL import Image
import requests
# import StringIO

image_search_subscription_key = "118a07809b484ba1970d84f931f01437"
cognitive_services_credentials = authentication.CognitiveServicesCredentials(image_search_subscription_key)
client = imagesearch.ImageSearchAPI(cognitive_services_credentials)
