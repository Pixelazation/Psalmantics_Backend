import requests

class BibleAPIClient:
    BASE_URL = "https://bible-api.com/"

    @staticmethod
    def get_verse(reference: str) -> dict:
        """
        Fetches a verse or passage from the Bible API.
        :param reference: e.g. "John 3:16"
        :return: dict with verse data or error
        """
        url = f"{BibleAPIClient.BASE_URL}{reference.replace(' ', '%20')}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Could not fetch verse: {reference}"}