# AI Python Client (Cookie Based, No API key required)
Claude ✅
Gemini ❌ (Todo)

**This is unofficial package, just for educational purpose. Don't use it commercially.**

This Python client provides an interface to interact with the Claude AI API, allowing you to perform various actions such as sending messages, listing conversations, uploading attachments, and more.

## Installation

To use this client, you need Python installed on your system. You can install the client and its dependencies using pip:

```bash
git clone https://github.com/anujpaude1/ai-api && cd ai-api

#linux
python3 -m venv myenv
source myenv/bin/activate
#windows
python -m venv myenv
./myenv/Scripts/activate.bat

pip install -r requirements.txt
```

## Set Cookie for Claude
### Grab cookie from developer-tools(f12) and network panel
Open any fetch request and grab cookie from headers.
![Cookie grab claude AI](https://github.com/anujpaude1/ai-api/blob/main/assets/claude-cookie.png)

### Set Cookie in .env
```bash
claudeCookie = "paste your cookie here"
```
## Set Cookie for Gemini
Download Cookie for gemini website and you are good to go
```
https://chromewebstore.google.com/detail/exportthiscookie/dannllckdimllhkiplchkcaoheibealk?hl=en
```

## Start Server
```bash
uvicorn main:app --reload
```
## API Endpoints
``` bash
URL : http://127.0.0.1:8000/claude/send-message
BODY: 
{
    "prompt":"How much water should I drink each day ?"
}
URL : http://127.0.0.1:8000/gemini/send-message
BODY: 
{
    "prompt":"How much water should I drink each day ?"
}
```
