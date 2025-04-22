
# Email Sender
A simple Python script to send emails using the Gmail SMTP server.

## Features
- Sends plain text emails.
- Configurable sender and receiver details.

## Setup
1. Update the `config.py` file with your email credentials:
   ```python
   sender_mail = "your_email@gmail.com"
   sender_password = "your_password"
   receiver_mail = "receiver_email@gmail.com"
   ```

2. Install required libraries (if not already installed):
   ```bash
   pip install secure-smtplib
   ```

## Usage
Run the script:
```bash
python main.py
```

## Note
- Ensure "Less secure app access" is enabled for the sender's Gmail account.
- Use this script responsibly.
```