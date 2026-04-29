import requests
import json
import os

API_TOKEN = "YOUR_CLOUDFLARE_API_TOKEN"
ACCOUNT_ID = "YOUR_CLOUDFLARE_ACCOUNT_ID"

# 🧠 Model endpoint (LLaMA 3)
URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3-8b-instruct"


headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# 💬 Chat memory (important!)
HISTORY_FILE = "chat_history.json"

if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
else:
    history = [
        {"role": "system", "content": "You are a helpful AI assistant. You have conversation memory, so you can remember previous messages from the user."}
    ]

def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def chat(prompt):
    # Add user message to memory
    history.append({"role": "user", "content": prompt})
    save_history()

    payload = {
        "messages": history
    }

    response = requests.post(URL, headers=headers, json=payload)

    data = response.json()

    # ❗ Safety check
    if "result" not in data:
        return f"Error: {data}"

    reply = data["result"]["response"]

    # Add bot reply to memory
    history.append({"role": "assistant", "content": reply})
    save_history()

    return reply


# 🚀 CLI chatbot loop
if __name__ == "__main__":
    print("🤖 AI Chatbot started (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye","ha det bra", "ha det"]:
            print("Bot: Bye 👋")
            break

        response = chat(user_input)
        print("Bot:", response)