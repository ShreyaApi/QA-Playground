import json
from pathlib import Path


def read_json(relative_path):
    """
    Read JSON file from project root.

    Example:
    data = read_json("testdata/forms/form_data.json")
    """

    project_root = Path(__file__).resolve().parent.parent

    file_path = project_root / relative_path

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
