import json
import datetime
from collections import Counter

DATA_FILE = "data.json"

POSITIVE = {
    "good", "great", "nice", "happy", "calm", "okay", "fine", "cool",
    "love", "loved", "loving",
    "enjoy", "enjoyed", "enjoying",
    "relaxed", "peaceful", "satisfied", "content",
    "excited", "exciting",
    "fun", "funny",
    "awesome", "amazing", "perfect",
    "hope", "hopeful",
    "safe", "comfortable",
    "proud", "confident",
    "motivated", "productive",
    "better", "improving",
    "grateful", "thankful",
    "smile", "smiling",
    "fresh", "free", "light",
    "full", "fed",
}


NEGATIVE = {
    "bad", "sad", "tired", "exhausted", "sleepy",
    "stress", "stressed", "stressful",
    "angry", "mad", "annoyed", "frustrated",
    "hate", "hated", "hating",
    "upset", "hurt", "pain",
    "lonely", "alone", "empty",
    "anxious", "anxiety", "worried",
    "fear", "scared",
    "depressed", "depression",
    "burnout", "burned",
    "quit", "givingup", "giveup",
    "stuck", "lost", "confused",
    "hopeless",
    "hungry", "starving",
    "sick", "ill",
    "lazy", "unmotivated",
    "boring", "bored",
    "cry", "crying",
    "overwhelmed",
    "pressure",
}

STOP_WORDS = {
    # pronouns
    "i", "me", "my", "mine", "myself",
    "you", "your", "yours", "yourself",
    "we", "us", "our", "ours",
    "they", "them", "their",

    # articles
    "a", "an", "the",

    # verbs (helpers)
    "is", "am", "are", "was", "were", "be", "been", "being",
    "do", "does", "did",
    "have", "has", "had",

    # prepositions
    "to", "of", "in", "on", "at", "for", "with", "from", "by", "about",

    # conjunctions
    "and", "or", "but", "if", "so", "because", "while", "though",

    # determiners
    "this", "that", "these", "those",
    "some", "any", "all", "every", "each",

    # adverbs / fillers
    "just", "very", "really", "quite", "maybe",
    "literally", "basically", "actually",

    # contractions / slang
    "im", "i'm", "ive", "i've",
    "dont", "don't", "cant", "can't",
    "wont", "won't", "isnt", "isn't",
    "its", "it's",

    # misc junk
    "ok", "okay",
    "yeah", "yes", "no",
    "uh", "um", "hmm",
}



def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_entry(text):
    now = datetime.datetime.now()
    data = load_data()

    entry = {
        "text": text.lower(),
        "time": now.isoformat(),
        "day": now.strftime("%A"),
        "hour": now.hour
    }

    data.append(entry)
    save_data(data)

def detect_mood(words):
    pos = sum(1 for w in words if w in POSITIVE)
    neg = sum(1 for w in words if w in NEGATIVE)

    if pos > neg:
        return "positive"
    if neg > pos:
        return "heavy"
    return "neutral"

def analyze():
    data = load_data()
    if len(data) < 5:
        return "Not enough data yet. Keep writing."

    words = []
    days = []
    hours = []
    texts = []

    for d in data:
        ws = d["text"].split()
        words.extend(w for w in ws if w not in STOP_WORDS)
        texts.append(d["text"])
        days.append(d["day"])
        hours.append(d.get("hour", 12))


    common_words = Counter(words).most_common(5)
    common_day = Counter(days).most_common(1)[0][0]

    night_entries = sum(1 for h in hours if h >= 22 or h <= 4)
    mood = detect_mood(words)

    repeated = Counter(texts).most_common(1)
    repetition_note = ""
    if repeated[0][1] > 2:
        repetition_note = f"You’ve repeated this thought: '{repeated[0][0]}'. "

    insight = "Reflection:\n"
    insight += f"- Frequent themes: {', '.join(w for w, _ in common_words)}\n"
    insight += f"- Most active day: {common_day}\n"

    if night_entries > len(data) * 0.4:
        insight += "- You write more at night.\n"

    insight += f"- Overall tone: {mood}\n"
    insight += repetition_note

    return insight
def weekly_summary():
    data = load_data()

    if len(data) < 7:
        return "Not enough data for a weekly summary yet."

    last_week = data[-7:]

    words = []
    for d in last_week:
        words.extend(
    w for w in d["text"].split() if w not in STOP_WORDS
)


    if not words:
        return "Not enough meaningful data this week."

    mood = detect_mood(words)
    themes = Counter(words).most_common(3)

    summary = "Weekly Summary:\n"
    summary += f"- Overall tone: {mood}\n"
    summary += f"- Recurring themes: {', '.join(w for w, _ in themes)}"

    return summary

