book: dict[int, str] = {}
PAGE_SIZE = 200
END_SIGNS = {",", ".", "!", ":", ";", "?"}


def _get_part_text(text, start, page_size) -> tuple[str, int]:
    for i in range(min(start + page_size, len(text)) - 1, start, -1):
        if i + 1 == len(text) or text[i] in END_SIGNS and text[i + 1] not in END_SIGNS:
            return text[start : i + 1], i + 1 - start
    return "", 0


def prepare_book(path: str) -> None:
    with open(path, encoding="utf-8") as f:
        book_text = f.read()
    start, page_no = 0, 1
    while start < len(book_text):
        page_text, page_size = _get_part_text(book_text, start, PAGE_SIZE)
        book[page_no] = page_text.lstrip()
        start += page_size
        page_no += 1


prepare_book("book.txt")
