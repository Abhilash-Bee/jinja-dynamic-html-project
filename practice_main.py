import requests

# my_name = input()

parameters = {
    "name": "abhilash",
}

response = requests.get("https://www.npoint.io/docs/c790b4d5cab58020d391", params=parameters)
print(response.json()["gender"])
