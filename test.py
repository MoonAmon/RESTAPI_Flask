import requests


base_url = "https://api.mangadex.org"

title = "jujutsu kaisen"

r = requests.get(
    f"{base_url}/manga",
    params={"title": title}
)

manga_data = r.json()["data"]

print(manga_data)