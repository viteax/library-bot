from dataclasses import dataclass


@dataclass
class User:
    page: int = 1
    bookmarks: set = set()


users_db: dict[str, User] = {}
