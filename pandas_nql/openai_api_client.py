import os
from openai import OpenAI

DEFAULT_GPT_MODEL = "gpt-3.5-turbo-0613"
OPENAI_API_KEY_NAME = "OPENAI_API_KEY"

client = OpenAI(
    api_key=os.environ.get(OPENAI_API_KEY_NAME),
)

class OpenAIApiClient():
    """
    Client for OpenAI Api

    :param model: GPT model to use when calling the API.
    :type model: str
    """

    def __init__(self, model: str = DEFAULT_GPT_MODEL):
        self.model = model

    def chat_completion(self, messages: list):
        """
        Calls chat completion endpoint with supplied list of messages and model

        :param messages: List of messages. See official OpenAI documentation for help defining messages.
        :type messages: list

        :return: The chat completion message content
        :rtype: str
        """
        chat_completion = client.chat.completions.create(
                            messages=messages,
                            model=self.model,)
        
        return chat_completion.choices[0].message.content