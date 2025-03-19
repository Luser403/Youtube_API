from googleapiclient.discovery import build
from kafka import KafkaProducer

API_KEY = "AIzaSyACHH6xoppSRZisCuMA-Ntz79TBy1MF3Ik"
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