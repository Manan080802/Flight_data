from pprint import pprint
import requests
sheet_endpoint = "https://api.sheety.co/"
header = {
    "Authorization": "Bearer manasdfvbn"

}
class DataManager:
    def __init__(self):
        self.destination_data={}

    def get_destination_data(self):
        sheet_response = requests.get(url=sheet_endpoint, headers=header)
        sheet_response.raise_for_status()
        # print(sheet_response.json())
        data = sheet_response.json()
        print(data)
        self.destination_data = data["name"]
        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "name1": {
                    "iataCode": city["iataCode"]
                }
            }
            # print(new_data)
            response = requests.put(
                url=f"{sheet_endpoint}/{city['id']}",
                json=new_data,
                headers=header

            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint ="https://api.sheety.co/"
        response = requests.get(url=customers_endpoint,headers=header)
        data = response.json()
        print(data)
        self.customer_data = data["user"]
        return self.customer_data