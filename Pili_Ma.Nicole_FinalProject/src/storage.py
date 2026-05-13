"""
storage.py

Handles JSON file operations.
"""

import json
import os


def load_data(filepath):
    """
    Load JSON data safely.

    Args:
        filepath (str): JSON file path

    Returns:
        list: Loaded data
    """

    # Create file if missing
    if not os.path.exists(filepath):

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w") as file:
            json.dump([], file)

        return []

    with open(filepath, "r") as file:

        try:
            return json.load(file)

        except json.JSONDecodeError:
            return []


def save_data(filepath, data):
    """
    Save data into JSON file.

    Args:
        filepath (str): JSON file path
        data (list): Data to save
    """

    # Create folder automatically
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)