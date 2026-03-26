import secrets

urls = []
for number in range(1,101):
    random_part = secrets.token_urlsafe(8)
    link = f"https://teameffort.work/{random_part}"
    urls.append(link)

for link in urls:
    print(link)