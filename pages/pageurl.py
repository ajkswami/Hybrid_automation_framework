import requests
from collections import Counter

# Specify the URL of the log file
url = "https://public.karat.io/content/q015/urls.txt"

r = requests.get(url=url)
r_content = r.text

print(r_content)



url_count = Counter(r_content.splitlines())

most_common, url_occ = url_count.most_common(1)[0]

print(f"The most common URL is {most_common} (with {url_occ} occurrences)")
