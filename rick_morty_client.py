import requests

class RickMortyClient:
    BASE_URL = "https://rickandmortyapi.com/api"

    def get_characters(self, page=1, name=None ):
        params = {"page": page, "name": name}
        params = {k: v for k, v in params.items() if v is not None}
        try:
            response = requests.get(f"{self.BASE_URL}/character", params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Erro: {e}")
            return None

if __name__ == '__main__':
    client = RickMortyClient()
    print("\n--- Buscando personagens ---")
    data = client.get_characters()
    if data:
        for char in data['results'][:5]:
            print(f"- {char['name']} ({char['species']})")
