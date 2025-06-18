import requests

session = requests.Session()
session.get("https://city.imd.gov.in/citywx/responsive/")

def native_json(city_id):
    json_data = {
        "ID" : city_id
    }
    response = session.post("https://city.imd.gov.in/citywx/responsive/api/fetchCity_static.php", data=json_data)

    return response.json()

if __name__ == "__main__":
    print(
        native_json(42139)
    )
