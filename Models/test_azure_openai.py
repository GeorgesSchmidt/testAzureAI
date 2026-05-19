import os
from openai import AzureOpenAI
from dotenv import load_dotenv


class AzureOpenAIClient:
    """Client pour interagir avec Azure OpenAI."""

    def __init__(self) -> None:
        load_dotenv()
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-12-01-preview",
        )
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def chat(self, user_message: str, system_message: str = "Tu es un assistant utile.") -> str:
        """Envoie un message et retourne la réponse du modèle."""
        response = self.client.chat.completions.create(
            model=self.deployment,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content


def main() -> None:
    client = AzureOpenAIClient()
    response = client.chat("Explique le machine learning en 3 phrases.")
    print(response)


if __name__ == "__main__":
    main()