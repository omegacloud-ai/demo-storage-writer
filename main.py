from typing import Dict, List

import arxiv

from utils import save_articles

STORAGE_NAME = "arxiv"
STORAGE_PATH = f"/tmp/{STORAGE_NAME}"
MAX_ARTICLES = 10


def fetch_articles(category: str, max_results: int = 10) -> List[Dict[str, str]]:
    """Fetch latest articles from arXiv"""
    articles = []
    try:
        # Define the search parameters
        search = arxiv.Search(
            query=category,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        # Use the Client to fetch results
        client = arxiv.Client()
        results = client.results(search)

        print()
        print("Reading articles...")
        for result in results:
            article = {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "abstract": result.summary,
                "url": result.entry_id,
                "published": result.published.isoformat(),
            }
            articles.append(article)
            print(f"* {article['title']}")
        print()

    except Exception as e:
        print(f"Error fetching articles: {str(e)}")

    return articles


def main():
    articles = fetch_articles(category="cs.AI", max_results=MAX_ARTICLES)
    save_articles(articles, STORAGE_PATH)


if __name__ == "__main__":
    main()
