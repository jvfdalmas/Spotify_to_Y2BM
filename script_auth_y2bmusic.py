import json

cookie_string = ""

headers_auth = {
    "Cookie": cookie_string,
    "x-goog-authuser": "0",
    "x-origin": "https://music.youtube.com",
    "x-youtube-client-name": "1",
    "x-youtube-client-version": "17.31.35"
}

with open("headers_auth.json", "w") as f:
    json.dump(headers_auth, f, indent=2)

print("File headers_auth.json creato con successo.")
