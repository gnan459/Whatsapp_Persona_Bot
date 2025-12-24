import re
TARGET_USER = "Gnann Saketh"

user_messages = []

with open("D:\\Whatsapp Persona Bot\\WhatsApp Chat with Dump Here.txt", encoding="utf-8") as f:
    for line in f:
        if f"- {TARGET_USER}:" in line:
            msg = line.split(f"- {TARGET_USER}:")[1].strip()
            if msg:
                user_messages.append(msg)

cleaned = []
for line in user_messages:
    line = line.strip()
    if not line:
            continue
    if "media omitted" in line.lower():
            continue
    if re.search(r"https?://", line):
            continue
    cleaned.append(line)

with open("D:\\Whatsapp Persona Bot\\saketh_cleaned.txt", "w",  encoding="utf-8") as f:
    for m in cleaned:
         f.write(m + "\n")