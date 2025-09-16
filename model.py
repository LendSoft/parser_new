from langchain_gigachat.chat_models import GigaChat
import os
from dotenv import load_dotenv

load_dotenv()
giga_token = os.getenv("giga_token").strip()

giga_token = giga_token.strip()

model = GigaChat(
    credentials=giga_token,
    scope="GIGACHAT_API_PERS",
    model="GigaChat-2",
    verify_ssl_certs=False
)