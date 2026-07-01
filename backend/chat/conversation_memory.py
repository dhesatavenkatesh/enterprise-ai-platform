from datetime import datetime, timedelta
import uuid


class ConversationMemory:

    def __init__(self):
        self.sessions = {}

    def create_session(self):

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "created_at": datetime.now(),
            "last_activity": datetime.now(),
            "questions": [],
            "answers": [],
            "preferences": {},
        }

        return session_id

    def add_message(
        self,
        session_id,
        question,
        answer
    ):

        if session_id not in self.sessions:
            raise ValueError("Session not found")

        session = self.sessions[session_id]

        session["questions"].append(question)
        session["answers"].append(answer)

        session["last_activity"] = datetime.now()

    def update_preferences(
        self,
        session_id,
        preferences: dict
    ):

        if session_id not in self.sessions:
            raise ValueError("Session not found")

        self.sessions[session_id]["preferences"].update(preferences)

    def get_memory(self, session_id):

        if session_id not in self.sessions:
            return None

        return self.sessions[session_id]

    def clear_session(self, session_id):

        if session_id in self.sessions:
            del self.sessions[session_id]

            return {
                "message": "Session deleted"
            }

        return {
            "message": "Session not found"
        }

    def cleanup_expired_sessions(
        self,
        expiry_minutes=60
    ):

        now = datetime.now()

        expired = []

        for session_id, session in self.sessions.items():

            if now - session["last_activity"] > timedelta(
                minutes=expiry_minutes
            ):
                expired.append(session_id)

        for session_id in expired:
            del self.sessions[session_id]

        return expired