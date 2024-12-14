class Lexicon:
    START = (
        "<b>Hello, reader!</b>\n\nThis is a bot where you "
        'can read the book "Taras Bulba" by Nikolai Vasilievich Gogol.\n\n'
        "To view the list of available commands, type /help."
    )
    HELP = (
        "<b>This is a reading bot</b>\n\nAvailable commands:\n\n/beginning - "
        "go to the beginning of the book\n/continue - continue reading\n"
        "/bookmarks - view the list of bookmarks\n/help - "
        "instructions on how to use the bot\n\nTo save a bookmark - "
        "press the button with the page number\n\n<b>Enjoy your reading!</b>"
    )

    OTHER = "I can't respond to that 😢"

    FORWARD = ">>"
    BACKWARD = "<<"

    BOOKMARKS = "<b>This is your list of bookmarks:</b>"
    EDIT_BOOKMARKS = "<b>Edit bookmarks</b>"
    EDIT_BOOKMARKS_BUTTON = "❌ EDIT"
    DEL = "❌"
    CANCEL = "Cancel"
    NO_BOOKMARKS = (
        "You don't have any bookmarks yet.\n\nTo add a page to bookmarks - "
        "while reading the book, press the button with that page's number\n\n"
        "/continue - continue reading",
    )
    CANCEL_TEXT = "/continue - continue reading"


COMMANDS = {
    "/start": "Initialize the database",
    "/beginning": "Go to the beginning of the book",
    "/continue": "Continue reading",
    "/bookmarks": "My bookmarks",
    "/help": "Instructions for using the bot",
}
