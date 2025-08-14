import os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Load environment variables from .env file
load_dotenv()

# Initialize Twilio client using environment variables
client = Client(
    os.getenv('TWILIO_ACCOUNT_SID'),
    os.getenv('TWILIO_AUTH_TOKEN')
)

def send_message(recipient_num, message_text):
    """Send WhatsApp message via Twilio"""
    try:
        message = client.messages.create(
            from_=os.getenv('TWILIO_PHONE_NUMBER'),
            body=message_text,
            to=f'whatsapp:{recipient_num}'
        )
        print(f"Message sent to {recipient_num} | SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {str(e)}")

def get_valid_future_datetime():
    """Get a valid future datetime from user input"""
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        time_str = input("Enter time (HH:MM 24h format): ")
        
        try:
            scheduled_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            if scheduled_time <= datetime.now():
                print("Please enter a future date/time")
                continue
            return scheduled_time
        except ValueError:
            print("Invalid format. Please try again.")

def main():
    """Main program flow"""
    print("\n=== WhatsApp Message Scheduler ===")
    name = input("Recipient name: ")
    recipient_num = input("Recipient WhatsApp number (e.g. +1234567890): ")
    message_text = input(f"Message for {name}: ")
    
    scheduled_time = get_valid_future_datetime()
    delay_seconds = (scheduled_time - datetime.now()).total_seconds()
    
    print(f"\nMessage will be sent to {name} at {scheduled_time}")
    print("Press Ctrl+C to cancel...")
    
    try:
        time.sleep(delay_seconds)
        send_message(recipient_num, message_text)
    except KeyboardInterrupt:
        print("\nSending cancelled")

if __name__ == "__main__":
    main()