import json
import os
from datetime import datetime
from typing import Dict, List


def save_articles(articles: List[Dict], storage_path: str) -> str:
    """Save articles to a JSON file"""
    try:
        # Ensure storage path exists
        os.makedirs(storage_path, exist_ok=True)

        # Create filename with current date
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = os.path.join(storage_path, f"arxiv-{date_str}.json")

        # Save to JSON file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(articles, f, indent=2, ensure_ascii=False)

        print(f"Articles saved to: {filename}")
        return filename

    except Exception as e:
        print(f"Error saving articles: {str(e)}")
