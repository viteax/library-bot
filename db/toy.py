from dataclasses import dataclass, field


@dataclass
class User:
    page: int = 1
    bookmarks: set[int] = field(default_factory=set)


users_db: dict[int, User] = {}
