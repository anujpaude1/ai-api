from claude import Client
from dotenv import load_dotenv
import os
load_dotenv()

claudeCookie=os.getenv("claudeCookie")
claude=Client(claudeCookie)
conversationIDs=claude.list_all_conversations()