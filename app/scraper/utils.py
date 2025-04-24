def extract_tags(text: str) -> list[str]:
    keywords = [
        "python", "javascript", "react", "fastapi", "aws", "docker", "sql",
        "machine learning", "flask", "django", "graphql", "node", "typescript"
    ]
    text = text.lower()
    return [kw for kw in keywords if kw in text]