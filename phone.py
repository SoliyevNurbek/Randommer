import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint='Phone/Generate'
        url=self.get_url()+endpoint
        if len(CountryCode)<=2 and 1<=Quantity<=1000:
            payload={
                "CountryCode":CountryCode,
                "Quantity":Quantity
            }
        else:
            return "Error query parametrs"
        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url=url,params=payload,headers=header)
        return response.json() if response.status_code==200 else response.status_code

    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint='Phone/IMEI'
        url=self.get_url()+endpoint
        if 1<=Quantity<=1000:
            payload={
                "Quantity":Quantity
            }
        else:
            return "Error query parametr"
        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url=url,params=payload,headers=header)
        return response.json() if response.status_code==200 else response.status_code

    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        endpoint='Phone/Validate'
        url=self.get_url()+endpoint
        if len(telephone)<=25 and len(CountryCode)<=2:
            payload={
                "telephone":telephone,
                "CountryCode":CountryCode
            }
        else:
            return "Error query parametrs"
        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url=url,params=payload,headers=header)
        return response.json() if response.status_code==200 else response.status_code

    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        endpoint='Phone/Countries'
        url=self.get_url()+endpoint

        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url=url,headers=header)
        return response.json() if response.status_code==200 else response.status_code