"""
models.py

Contains the classes used in the application.
"""

from datetime import datetime


class MoodEntry:
    """
    Represents a mood entry.
    """

    def __init__(self, mood_score, emotion, note):
        self.mood_score = mood_score
        self.emotion = emotion
        self.note = note
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """
        Convert object into dictionary format.
        """

        return {
            "mood_score": self.mood_score,
            "emotion": self.emotion,
            "note": self.note,
            "date": self.date
        }


class JournalEntry:
    """
    Represents a journal entry.
    """

    def __init__(self, content):
        self.content = content
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """
        Convert object into dictionary format.
        """

        return {
            "content": self.content,
            "date": self.date
        }