import json
import os
import re
import copy

@staticmethod
def handle_message_text(message):
    if message.get("text") is not None:
        print("message received")
        message_response = copy.deepcopy(message)
        return message_response