"""
wellness.py

Contains the wellness system functions.
"""

import random
from collections import Counter

from models import MoodEntry, JournalEntry
from storage import load_data, save_data


MOODS_FILE = "data/moods.json"
JOURNALS_FILE = "data/journals.json"


# =========================
# MOTIVATIONAL QUOTES
# =========================

QUOTES = {
    "happy": [
        "Keep spreading positivity.",
        "Celebrate your happiness."
    ],

    "sad": [
        "Better days are coming.",
        "Your feelings are valid."
    ],

    "stressed": [
        "Take things one step at a time.",
        "Rest is productive too."
    ],

    "anxious": [
        "Focus on the present moment.",
        "Take a deep breath."
    ],

    "motivated": [
        "Keep pushing forward.",
        "Progress matters more than perfection."
    ],

    "angry": [
        "Pause before reacting.",
        "Calm minds make better decisions."
    ]
}


def get_quote(emotion):
    """
    Return motivational quote based on emotion.
    """

    emotion = emotion.lower()

    if emotion in QUOTES:
        return random.choice(QUOTES[emotion])

    return "Every day is a new beginning."


# =========================
# MOOD FUNCTIONS
# =========================

def add_mood():
    """
    Add mood entry.
    """

    moods = load_data(MOODS_FILE)

    print("\n===== ADD MOOD ENTRY =====")

    try:
        score = int(input("Mood Score (1-10): "))

        if score < 1 or score > 10:
            print("Mood score must be between 1 and 10.")
            return

    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    emotion = input("Emotion: ")
    note = input("Short Note: ")

    mood = MoodEntry(score, emotion, note)

    moods.append(mood.to_dict())

    save_data(MOODS_FILE, moods)

    print("\nMood entry saved successfully.")

    print("\nMotivational Quote:")
    print(get_quote(emotion))


# =========================
# JOURNAL FUNCTIONS
# =========================

def write_journal():
    """
    Write journal entry.
    """

    journals = load_data(JOURNALS_FILE)

    print("\n===== WRITE JOURNAL =====")

    content = input("Write your journal entry:\n")

    entry = JournalEntry(content)

    journals.append(entry.to_dict())

    save_data(JOURNALS_FILE, journals)

    print("Journal entry saved successfully.")


def search_journal():
    """
    Search journal entries by keyword.
    """

    journals = load_data(JOURNALS_FILE)

    print("\n===== SEARCH JOURNAL =====")

    keyword = input("Enter keyword: ").lower()

    results = [
        entry for entry in journals
        if keyword in entry["content"].lower()
    ]

    if not results:
        print("No matching journal entries found.")
        return

    print("\n===== SEARCH RESULTS =====")

    for entry in results:
        print("\n----------------------")
        print(f"Date: {entry['date']}")
        print(f"Entry: {entry['content']}")


# =========================
# ANALYTICS
# =========================

def view_analytics():
    """
    Display mood analytics.
    """

    moods = load_data(MOODS_FILE)

    print("\n===== MOOD ANALYTICS =====")

    # No data check
    if not moods:
        print("No mood data available.")
        return

    # Minimum entries validation
    if len(moods) < 3:
        print("Not enough mood entries for full analytics.")
        print("Please add at least 3 mood entries.")
        return

    # DATA PROCESSING

    scores = [
        mood["mood_score"]
        for mood in moods
    ]

    average_score = sum(scores) / len(scores)

    emotions = [
        mood["emotion"]
        for mood in moods
    ]

    emotion_counter = Counter(emotions)

    most_common_emotion = emotion_counter.most_common(1)[0][0]

    print(f"Average Mood Score: {average_score:.2f}")
    print(f"Most Common Emotion: {most_common_emotion}")

    # SORTING ALGORITHM

    sorted_moods = sorted(
        moods,
        key=lambda mood: mood["mood_score"],
        reverse=True
    )

    print("\nTop Mood Entries:")

    for mood in sorted_moods[:3]:
        print(
            f"{mood['date']} | "
            f"{mood['emotion']} | "
            f"Score: {mood['mood_score']}"
        )

    # SORTING ALGORITHM

    sorted_moods = sorted(
        moods,
        key=lambda mood: mood["mood_score"],
        reverse=True
    )

    print("\nTop Mood Entries:")

    for mood in sorted_moods[:3]:
        print(
            f"{mood['date']} | "
            f"{mood['emotion']} | "
            f"Score: {mood['mood_score']}"
        )