from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause",
            description=f"Pause the Current Playin Stream on VC.",
            thumb_url="https://graph.org/file/82e478b5ad0e14b78fde3.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume",
            description=f"Resumw the Paused Stream on VC.",
            thumb_url="https://graph.org/file/82e478b5ad0e14b78fde3.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Skip",
            description=f"Skip the Current Playin Stream on VC & Moves to the Next Stream.",
            thumb_url="https://graph.org/file/82e478b5ad0e14b78fde3.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End",
            description="End the Current Playin Stream on VC.",
            thumb_url="https://graph.org/file/82e478b5ad0e14b78fde3.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Shuffle",
            description="Shufffle the Queued Song in Playlist.",
            thumb_url="https://graph.org/file/82e478b5ad0e14b78fde3.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Loop",
            description="Loop the Current Playin Track on VC.",
            thumb_url="https://graph.org/file/82e478b5ad0e14b78fde3.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
