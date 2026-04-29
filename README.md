# Mini AI Chatbot

A simple Command-Line Interface (CLI) AI chatbot in Python, powered by the Cloudflare Workers AI API and Meta's LLaMA 3 model.

## Features
- **Persistent Conversational Memory**: The bot remembers previous messages even after you exit, storing the chat history in a local `chat_history.json` file.
- **LLaMA 3 Powered**: Utilizes the powerful `@cf/meta/llama-3-8b-instruct` model via Cloudflare's infrastructure.
- **Simple CLI**: Easy to run in the terminal for quick queries.

## Prerequisites
- Python 3.x
- `requests` library (`pip install requests`)

## How it Works (`main.py` Explanation)

### 1. Setup & Configuration
The script starts by importing the `requests` library to make HTTP requests. It configures the Cloudflare API credentials (`API_TOKEN` and `ACCOUNT_ID`) and constructs the `URL` pointing specifically to the LLaMA 3 model endpoint. Headers are defined for authorization and to specify JSON content type.

### 2. Chat Memory (`history`)
```python
HISTORY_FILE = "chat_history.json"
```
Instead of resetting every time the script runs, the bot checks for `chat_history.json` on startup.
- If it exists, it loads the past messages and resumes the conversation.
- If not, it creates a new history starting with a System Prompt.
The `history` list is updated and instantly saved back to the JSON file every time a message is sent or received.

### 3. The `chat(prompt)` Function
This function handles communicating with the AI:
- **Append User Prompt**: The user's input is appended to the `history` list as a dictionary with `role: "user"`.
- **API Request**: The entire `history` is packaged into a JSON payload and sent via a POST request to the Cloudflare API.
- **Error Handling**: It checks if the "result" is in the response. If the API fails, it returns the error data.
- **Append AI Response**: The reply from the model is extracted and appended back to the `history` list as `role: "assistant"`. This maintains the flow of conversation.
- **Return**: Finally, the bot's reply is returned to be printed.

### 4. CLI Chatbot Loop
The bottom section of the file (`if __name__ == "__main__":`) runs an infinite `while True:` loop, prompting the user for input. 
- If the user types an exit command (like 'exit', 'quit', or 'bye'), the loop breaks and the program ends.
- Otherwise, it passes the user's input to the `chat()` function and prints the bot's response to the console.

## Usage
Simply run the script in your terminal:
```bash
python main.py
```
Type your messages and press Enter. To quit, type `exit` or `bye`.
