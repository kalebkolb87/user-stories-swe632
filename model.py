import json


def load_tools():
    with open("mock_tools.json") as f:
        return json.load(f)


tools_db = load_tools()


def load_user_stories():
    with open("user_stories_db.json") as f:
        return json.load(f)


user_stories = load_user_stories()

