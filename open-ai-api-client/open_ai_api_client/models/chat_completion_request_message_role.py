from enum import Enum


class ChatCompletionRequestMessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

    def __str__(self) -> str:
        return str(self.value)
