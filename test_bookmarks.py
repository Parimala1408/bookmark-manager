# test_bookmarks.py
import os
import json
from bookmarks import add_bookmark, load_bookmarks

def test_add_bookmark(tmp_path):
    os.chdir(tmp_path)
    add_bookmark("Google", "https://www.google.com", "Search")
    data = load_bookmarks()
    assert len(data) == 1
    assert data[0]["title"] == "Google"
