# bookmarks.py
# Simple Bookmark Manager using JSON file storage.

import json
import os

DB_FILE = "bookmarks.json"

def load_bookmarks():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_bookmarks(bookmarks):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(bookmarks, f, indent=2)

def add_bookmark(title, url, category):
    bookmarks = load_bookmarks()
    bookmarks.append({
        "title": title,
        "url": url,
        "category": category
    })
    save_bookmarks(bookmarks)
    print(f"✅ Added bookmark: {title}")

def list_bookmarks():
    bookmarks = load_bookmarks()
    if not bookmarks:
        print("No bookmarks yet.")
        return
    print("📚 Your Bookmarks:")
    for i, b in enumerate(bookmarks, 1):
        print(f"{i}. {b['title']} ({b['category']}) → {b['url']}")

def search_bookmarks(keyword):
    bookmarks = load_bookmarks()
    results = [b for b in bookmarks if keyword.lower() in b["title"].lower()]
    if not results:
        print("No matching bookmarks.")
        return
    print(f"🔍 Results for '{keyword}':")
    for b in results:
        print(f"- {b['title']} ({b['category']}) → {b['url']}")

if __name__ == "__main__":
    print("\nBookmark Manager\n")
    print("1. Add bookmark")
    print("2. List all bookmarks")
    print("3. Search bookmarks")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        title = input("Title: ").strip()
        url = input("URL: ").strip()
        category = input("Category: ").strip()
        add_bookmark(title, url, category)
    elif choice == "2":
        list_bookmarks()
    elif choice == "3":
        keyword = input("Search keyword: ").strip()
        search_bookmarks(keyword)
    else:
        print("Invalid choice.")
