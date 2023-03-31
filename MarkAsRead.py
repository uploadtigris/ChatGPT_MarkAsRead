import os
import google.auth
from googleapiclient.discovery import build

# Authenticate and create the Gmail API client
creds, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/gmail.modify'])
service = build('gmail', 'v1', credentials=creds)

# Get all the IDs of the unread emails in your inbox
results = service.users().messages().list(userId='me', q='is:unread').execute()
unread_msgs = results.get('messages', [])

# Mark each unread email as read
if unread_msgs:
    for msg in unread_msgs:
        service.users().messages().modify(userId='me', id=msg['id'], body={'removeLabelIds': ['UNREAD']}).execute()
        print(f"Marked email with ID {msg['id']} as read.")
else:
    print("No unread emails found in your inbox.")
