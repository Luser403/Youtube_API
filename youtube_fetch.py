from googleapiclient.discovery import build
from kafka import KafkaProducer
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv('YOUTUBE_API_KEY')
youtube = build("youtube", "v3", developerKey=API_KEY)
producer = KafkaProducer(bootstrap_servers="localhost:9092")

request = youtube.search().list(
    part="snippet",
    q="python coding",
    maxResults=5
)
response = request.execute()

for item in response["items"]:
    title = item["snippet"]["title"]
    producer.send("youtube_videos", title.encode("utf-8"))
    print("Sent to Kafka:", title)

producer.flush()