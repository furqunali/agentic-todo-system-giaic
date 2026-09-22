ALLOWED_PRIORITIES = {"High", "Medium", "Low"}

def validate_title(title: str) -> str:
    value = str(title).strip()
    if not value:
        raise ValueError("title is required")
    if len(value) > 200:
        raise ValueError("title must be 200 characters or fewer")
    return value

def validate_priority(priority: str) -> str:
    value = str(priority).title()
    if value not in ALLOWED_PRIORITIES:
        raise ValueError("priority must be High, Medium, or Low")
    return value
