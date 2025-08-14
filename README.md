# **⏰ WhatsApp Message Scheduler (RemindMeBot)**

**This project provides a simple Python script to schedule and send WhatsApp messages to a specified recipient at a future date and time. It leverages the Twilio API for sending messages, making it easy to automate personal reminders or timely communications.**

## **✨ Features**
Scheduled Delivery: Send WhatsApp messages at a precise future date and time.

Twilio Integration: Utilizes the Twilio API for reliable message delivery.

User-Friendly Input: Prompts the user for recipient details, message content, and desired delivery time.

Input Validation: Ensures the scheduled time is in the future and in the correct format.

## **⚙️ Prerequisites**
Before you run this script, you'll need the following:

**Python 3.10:** Ensure Python is installed on your system.

**Twilio Account:** A Twilio account is required to send messages. You'll need your Account SID, Auth Token, and a Twilio phone number capable of sending WhatsApp messages.

**WhatsApp Sandbox (Optional but Recommended):** For testing, you can use Twilio's WhatsApp Sandbox.

# **🚀 Setup**
Follow these steps to get the project running on your local machine:

1. Clone the Repository (if applicable) or Save the Script
Save the provided Python code as whatsapp_scheduler.py (or any .py file name you prefer).

2. Install Dependencies
You'll need python-dotenv to manage environment variables and twilio to interact with the Twilio API. Install them using pip:

pip install python-dotenv twilio

3. Configure Environment Variables
Create a file named .env in the same directory as your Python script. This file will store your sensitive Twilio credentials. Add the following lines, replacing the placeholder values with your actual Twilio details:

    - **TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx**
    - **TWILIO_AUTH_TOKEN=your_auth_token_here**
    - **TWILIO_PHONE_NUMBER=whatsapp:+1xxxxxxxxxx # Your Twilio WhatsApp-enabled number (e.g., whatsapp:+15017122661)**
    

TWILIO_ACCOUNT_SID: Found on your Twilio Dashboard.

TWILIO_AUTH_TOKEN: Also found on your Twilio Dashboard.

TWILIO_PHONE_NUMBER: Your Twilio phone number configured for WhatsApp, including the whatsapp: prefix (e.g., whatsapp:+1234567890).

# **👨‍💻 How to Use**
Run the script from your terminal:

python whatsapp_scheduler.py

The script will then prompt you for the following information:

**Recipient name:** The name of the person you're sending the message to (for your reference).

**Recipient WhatsApp number:** The full WhatsApp number of the recipient, including the country code (e.g., +1234567890).

**Message for [Recipient Name]:** The content of the WhatsApp message you want to send.

**Enter date (YYYY-MM-DD):** The date you want the message to be sent (e.g., 2025-12-25).

**Enter time (HH:MM 24h format):** The time you want the message to be sent (e.g., 14:30).

After you provide all the information, the script will display a confirmation message indicating when the message will be sent. The script will then pause until the scheduled time.

To cancel the scheduled message before it's sent, **press Ctrl+C** in your terminal.

# **📝 Code Structure**
The script is organized into three main functions for clarity and and modularity:

**send_message(recipient_num, message_text)**
This function handles the actual sending of the WhatsApp message using the Twilio client. It takes the recipient's phone number and the message text as arguments and prints the message SID upon successful delivery or an error if sending fails.

**get_valid_future_datetime()**
This utility function prompts the user to enter a date and time, validates the input format, and ensures that the entered time is in the future. It continuously prompts until a valid future datetime is provided.

**main()**
This is the main function that orchestrates the program flow. It collects user input for the recipient, message, and desired send time. It then calculates the delay and uses **time.sleep()** to pause execution until the scheduled time before calling **send_message()**. It also includes basic error handling for KeyboardInterrupt to allow cancellation.

# **🛡️ Error Handling**
The send_message function includes a try-except block to catch potential errors during the Twilio API call and prints a descriptive error message.

The get_valid_future_datetime function uses a while True loop and try-except ValueError to ensure that the user provides a valid date and time format and that the scheduled time is in the future.

The main function incorporates a try-except KeyboardInterrupt to allow the user to gracefully cancel the script's execution while it's waiting to send the message.