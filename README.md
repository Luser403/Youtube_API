# YouTube Video Notification System

This project monitors YouTube for new videos based on specific search criteria and sends notifications via Telegram.

## Components

1. **YouTube Fetcher (`youtube_fetch.py`)**: Fetches videos from YouTube using the YouTube Data API and sends them to a Kafka topic.
2. **Kafka Consumer (`kafka_consumer.py`)**: Listens for new video notifications from Kafka and forwards them to a Telegram bot.

## Prerequisites

- Python 3.x
- Docker and Docker Compose (for running Kafka)
- YouTube Data API key
- Telegram Bot Token

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Kafka using Docker Compose:
```bash
docker-compose up -d
```

3. Configure your environment:
   - Add your YouTube API key in `youtube_fetch.py`
   - Add your Telegram Bot Token and Chat ID in `kafka_consumer.py`

## Running the Application

1. Start the Kafka consumer:
```bash
python kafka_consumer.py
```

2. In a separate terminal, run the YouTube fetcher:
```bash
python youtube_fetch.py
```

## Configuration

- The YouTube fetcher is configured to search for "python coding" videos by default
- The Kafka topic used is "youtube_videos"
- Kafka runs on localhost:9092

## License

MIT License 