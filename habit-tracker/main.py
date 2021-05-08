import requests
import os
import datetime as dt

username = "gleny4001"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
token = os.environ.get("TOKEN")
today = dt.datetime.today()
today_format = today.strftime("%Y%m%d")
update_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today_format}"
graph_pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {

    "id": "graph1",
    "name": "Coding",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": token
}

post_graph = {
    "date": today_format,
    "quantity": input("How many minutes did you work today?"),
}

update_params = {
    "quantity": "20",

}

#
# #make an account
# requests.post(pixela_endpoint, json=user_params)

# Make a graph
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# #Post pixel
requests.post(url=graph_pixel_endpoint, json=post_graph, headers=headers)
# #update pixel
# requests.put(url=update_delete_endpoint, json=update_params, headers=headers)
# #delete pixel
# requests.delete(url=update_delete_endpoint, headers=headers)
# #delete graph
# requests.delete(url=graph_pixel_endpoint, headers=headers)
