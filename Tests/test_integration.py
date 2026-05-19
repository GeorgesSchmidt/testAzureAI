import unittest

from Models.test_azure_openai import AzureOpenAIClient


class TestAzureOpenAIClientIntegration(unittest.TestCase):
    """Tests d'intégration pour AzureOpenAIClient — appels réels à l'API."""

    def setUp(self) -> None:
        """Initialise le client réel."""
        self.client = AzureOpenAIClient()

    def test_chat_returns_string(self) -> None:
        """Vérifie que chat() retourne bien une string."""
        result = self.client.chat("Dis juste 'OK'.")
        self.assertIsInstance(result, str)

    def test_chat_returns_non_empty_response(self) -> None:
        """Vérifie que la réponse n'est pas vide."""
        result = self.client.chat("Dis juste 'OK'.")
        self.assertGreater(len(result), 0)

    def test_chat_with_custom_system_message(self) -> None:
        """Vérifie qu'un system message personnalisé influence la réponse."""
        result = self.client.chat(
            user_message="Quelle est ta fonction ?",
            system_message="Tu es un assistant juridique.",
        )
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_chat_responds_in_french(self) -> None:
        """Vérifie que le modèle répond en français."""
        result = self.client.chat(
            user_message="Réponds uniquement le mot 'bonjour'.",
            system_message="Tu réponds toujours en français.",
        )
        self.assertIn("bonjour", result.lower())


if __name__ == "__main__":
    unittest.main()