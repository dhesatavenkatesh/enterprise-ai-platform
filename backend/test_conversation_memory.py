from backend.chat.conversation_memory import ConversationMemory

memory = ConversationMemory()

session_id = memory.create_session()

print("Session:", session_id)

memory.update_preferences(
    session_id,
    {
        "department": "HR",
        "language": "English"
    }
)

memory.add_message(
    session_id,
    "My department is HR.",
    "Okay, I'll remember that."
)

memory.add_message(
    session_id,
    "Show leave policies.",
    "Displaying HR leave policies."
)

print(memory.get_memory(session_id))