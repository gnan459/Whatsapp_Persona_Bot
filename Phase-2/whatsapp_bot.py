import time
import sys
from playwright.sync_api import sync_playwright
import re

TIME_PATTERN = re.compile(r"\d{1,2}:\d{2}\s?(AM|PM)?", re.IGNORECASE)

# ---- IMPORT GEMINI PERSONA BRAIN ----
# Adjust path if needed
sys.path.append("../Phase-2")
from prompt_composer import generate_reply


# -----------------------------------
# WhatsApp Web Setup
# -----------------------------------
def open_whatsapp():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://web.whatsapp.com")
    input("📱 Scan QR code in WhatsApp Web, then press ENTER...")

    return playwright, browser, page


# -----------------------------------
# Message Utilities
# -----------------------------------
def get_messages(page):
    # All message bubbles (incoming + outgoing)
    return page.query_selector_all("div[role='row']")


def is_bot_trigger(msg):
    try:
        lines = [l.strip() for l in msg.inner_text().split("\n") if l.strip()]

        content_lines = [l for l in lines if not TIME_PATTERN.fullmatch(l)]

        if len(content_lines) < 2:
            return False

        last_content = content_lines[-1].lower()

        # 🔒 Only allow your own messages to trigger
        sender_name = content_lines[0].lower()
        if sender_name != "Gnann Saketh":
            return False

        return last_content == "bot"
    except:
        return False



def get_quoted_text(msg):
    try:
        lines = [l.strip() for l in msg.inner_text().split("\n") if l.strip()]

        # Remove timestamps
        content_lines = [l for l in lines if not TIME_PATTERN.fullmatch(l)]

        # Remove last line ("bot")
        content_lines = content_lines[:-1]

        # Remove sender name (usually first line)
        if content_lines and len(content_lines[0].split()) <= 3:
            content_lines = content_lines[1:]

        return " ".join(content_lines).strip()
    except:
        return None



def send_message(page, text):
    # WhatsApp chat input box is inside the footer
    input_box = page.query_selector("footer div[contenteditable='true'][role='textbox']")

    if not input_box:
        print("❌ Chat input box not found")
        return

    input_box.click()
    input_box.fill(text)
    input_box.press("Enter")


# -----------------------------------
# MAIN BOT LOOP
# -----------------------------------
def start_bot(page):
    seen_messages = set()
    print("🤖 Bot is running... Waiting for trigger")

    while True:
        try:
            messages = get_messages(page)
            if not messages:
                time.sleep(1)
                continue

            last = messages[-1]
            msg_id = last.inner_text()

            if msg_id in seen_messages:
                time.sleep(1)
                continue

            seen_messages.add(msg_id)

            print("====== RAW MESSAGE ======")
            print(last.inner_text())
            print("=========================")
            if is_bot_trigger(last):
                quoted_text = get_quoted_text(last)

                if quoted_text:
                    print("✅ Trigger detected")
                    print("📩 Quoted message:", quoted_text)

                    reply = generate_reply(quoted_text)
                    print("🤖 Bot reply:", reply)

                    time.sleep(2)  # human-like delay
                    send_message(page, reply)

            time.sleep(1)

        except Exception as e:
            print("⚠️ Error:", e)
            time.sleep(2)


# -----------------------------------
# ENTRY POINT
# -----------------------------------
if __name__ == "__main__":
    playwright, browser, page = open_whatsapp()
    start_bot(page)
