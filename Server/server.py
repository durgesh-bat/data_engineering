import requests,json
data = None
url = "https://jsonplaceholder.typicode.com/users"


def fetch_users():

    try:
        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        print("API Error:", e)
        return None

# Make_GET_request()

def Convert_response():
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("API Error : ",e)
    print(type(response.json()))

# Convert_response()

def Print_users():
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("API Error : ",e)

    for user in response.json():
        print(f"{user['name']}-> {user['email']} -> {user['address']['city']}")

# Print_users()

def Count_users():
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("API Error : ",e)

    count = 0
    for user in response.json():
        count+=1
    return count
# Count_users()

def transformed_list():
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("API Error : ",e)

    cleaned_data = []
    for user in response.json():
        temp={
            "id": user['id'],
            "name": user['name'],
            "email": user['email'],
            "city": user['address']['city'],
        }
        cleaned_data.append(temp)
    return cleaned_data

# print(transformed_list())

def transformed_list_save():
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("API Error : ",e)

    cleaned_data = []
    for user in response.json():
        temp={
            "name": user['name'],
            "email": user['email'],
            "city": user['address']['city'],
        }
        cleaned_data.append(temp)
    with open('Foundations/Data/users_clean.json','w') as file:
        json.dump(cleaned_data,file,indent=4)

transformed_list_save()