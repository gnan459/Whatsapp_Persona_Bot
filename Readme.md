# WhatsApp Persona Bot 🤖💬

A WhatsApp bot that replies **exactly like you**, trained from your own WhatsApp chat history and powered by **Google Gemini**.

This project uses **WhatsApp Web automation + LLM prompt engineering** to generate human‑like replies in your **native language (Telugu / Roman Telugu)**.  
The bot replies **only when explicitly triggered**, making it safe, controllable, and demo‑friendly.

---

## ✨ Features

- Persona cloning from WhatsApp chat export (PDF / TXT)
- Native Telugu (Roman Telugu) response generation
- Gemini API–powered LLM brain
- Reply‑to‑message trigger (`bot`)
- Works in **private chats and group chats**
- No WhatsApp Business API required
- Clean, modular, extensible architecture

---

## 🧠 How It Works

1. Export WhatsApp chat history
2. Extract one person’s messages
3. Build a persona profile + few‑shot examples
4. Use Gemini to generate persona‑style replies
5. Use Playwright to send replies via WhatsApp Web

---

## 🏗️ Project Architecture

```
WhatsApp Chat Export
        ↓
Persona Builder (Phase‑1)
        ↓
Persona JSON + Few‑Shot Examples
        ↓
Prompt Composer (Phase‑2)
        ↓
Gemini API
        ↓
WhatsApp Web Automation (Phase‑3)
        ↓
Reply sent to chat
```

---

## 📁 Project Structure

```
Whatsapp Persona Bot/
│
├── Phase-1/                  # Chat extraction & persona creation
├── Phase-2/
│   └── prompt_composer.py    # Gemini prompt logic
├── Phase-3/
│   └── whatsapp_bot.py       # WhatsApp Web automation
│
├── persona/
│   ├── persona.json
│   └── few_shot_examples.txt
│
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install playwright python-dotenv google-generativeai
playwright install
```

---

### 2️⃣ Create `.env` File

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ Never commit `.env` to GitHub.

---

### 3️⃣ Run the Bot

```bash
python Phase-3/whatsapp_bot.py
```

- Scan WhatsApp Web QR code
- Open a chat or group
- Reply to a message with `bot`

---

## 🧪 How to Use

In WhatsApp:

```
Friend: repu plan unda?
You (reply): bot
Bot: sarle chuddam le ra 😂
```

✔ Bot replies only when explicitly triggered  
✔ No accidental spam  
✔ Human‑like behavior  

---

## 🔐 Safety & Ethics

- Bot replies only on user command
- Uses **your own chat data only**
- Not intended for impersonation or misuse
- Educational & personal project

---

## 🛠️ Tech Stack

- Python
- Playwright
- Google Gemini API
- Prompt Engineering
- WhatsApp Web

---

## 🚀 Future Improvements

- Multi‑person bots (group of friends)
- Bot modes (`bot funny`, `bot serious`)
- Typing simulation (human‑like delays)
- Telegram version with official API
- FastAPI backend

---

## ⚠️ Disclaimer

WhatsApp Web automation relies on UI structure and may break if WhatsApp updates its interface.

This project is **not affiliated with WhatsApp or Meta**.

---

## 👨‍💻 Author

Built by **Gnann Saketh**  
AI / ML Engineer  

---

⭐ If you like this project, give it a star on GitHub!
