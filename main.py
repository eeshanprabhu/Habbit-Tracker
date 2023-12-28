import requests
from datetime import datetime
today=datetime.now()

GRAPHID="graph1"
TOKEN="fjkdlsfjdk12ds"
USERNAME="eeshan555"
pixela_endpoint="https://pixe.la/v1/users"

user_params={
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':"yes",
    'notMinor':"yes"
}
graph_params={

    'id':GRAPHID,
    'name':'CodingTrackingGraph',
    'unit':"Hours",
    'type':"int",
    "color":"shibafu"
}
headers={
    "X-USER-TOKEN":"fjkdlsfjdk12ds"
}
# response=requests.post(url=pixela_endpoint,json=user_params)

#
# graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'
# graph_response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(graph_response.text)

pixel_params={
    'date':today.strftime("%Y%m%d"),
    'quantity':input("How many hours did you code today?"),
}

pixel_headers={
    "X-USER-TOKEN":TOKEN
}

pixel_add_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'

pixel_add_response=requests.post(url=pixel_add_endpoint,json=pixel_params,headers=pixel_headers)
print(pixel_add_response.text)

update_pixel_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{20231218}'

# update_pixel_response=requests.put(url=update_pixel_endpoint,json={'quantity':"5"},headers=headers)
# print(update_pixel_response.text)

delete_pixel_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{20231220}'

# delete_pixel_response=requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(delete_pixel_response.text)
