import requests

url = f"https://graph.facebook.com/v18.0/239652215897765/messages"

headers = {
    'Authorization': 'Bearer EAAGNQ6naY5UBO6iiMbFJ7Vojj3iSa8FRtHCDf8aZCkFxGgJEi12QDP0RIQ85K1UyYsihr0ZC18L3h8nZBDESGm9Lz0QFWuHllAM0BvQsKSKzUGk9eyqXzPqfC6U2fiCcr6WBt2VfJCJdPERtSamvsqStjL9FdarZC9scNvZAbZCvj0lIK8BzXdoYoijHrAxm64pQzB7mZB5JRDf30iT',
    'Content-Type': 'application/json'
}


response = requests.post(url, headers=headers, json=data)

print(response.text)
print(response.status_code)
print(response.json())
