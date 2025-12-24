from collections import Counter
import re

INPUT_FILE = r"D:\Whatsapp Persona Bot\saketh_cleaned.txt"

with open(INPUT_FILE, encoding="utf-8") as f:
    messages = [line.strip() for line in f if line.strip()]

print(f"Total messages: {len(messages)}")

length = [len(m.split()) for m in messages]
avg_len = sum(length) / len(length)
print("Average words per message:", round(avg_len, 2))

words = []
for msg in messages:
    words.extend(msg.lower().split())

common_words = Counter(words).most_common(30)

print("\nTop Words:")
for word, count in common_words:
    print(word, count)


bigrams = []
for msg in messages:
    tokens = msg.lower().split()
    for i in range(len(tokens) - 1):
        bigrams.append(tokens[i] + " " + tokens[i+1])

common_phrases = Counter(bigrams).most_common(20)

print("\nCommon Phrases:")
for phrase, count in common_phrases:
    print(phrase, count)

emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "]+",
    flags=re.UNICODE
)

emojis = []
for msg in messages:
    emojis.extend(emoji_pattern.findall(msg))

emoji_freq = Counter(emojis)

print("\nEmoji Usage:")
for e, c in emoji_freq.most_common():
    print(e, c)


question_count = sum(1 for m in messages if "?" in m)
exclamation_count = sum(1 for m in messages if "!" in m)

print("\nStyle Signals:")
print("Questions:", question_count)
print("Exclamations:", exclamation_count)