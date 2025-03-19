from kafka import KafkaConsumer
from telegram import Bot
import asyncio

# Your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "7761640597:AAGZ2uN7sVL2k1GMSr0RaNITbLoXmTWi_rc"
TELEGRAM_CHAT_ID = "8097012944"

# Kafka consumer setup
consumer = KafkaConsumer(
    "youtube_videos",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest"  # Only new messages
)
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Async function to send Telegram messages
async def send_telegram_message(message):
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# Main async function to process Kafka messages
async def process_messages():
    print("Listening for messages from Kafka...")
    for message in consumer:
        title = message.value.decode("utf-8")
        print(f"Received from Kafka: {title}")
        await send_telegram_message(f"New YouTube Video: {title}")

# Run the async function in a single event loop
if __name__ == "__main__":
    asyncio.run(process_messages())