import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        endpoint='Misc/Cultures'
        url=self.get_url()+endpoint

        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url,headers=header)
        return response.json() if response.status_code==200 else response.status_code
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        endpoint='Misc/Random-Address'
        url=self.get_url()+endpoint

        if 1<=number<=1000 and len(culture)<=100:
            payload={
                "number":number,
                "culture":culture
            }
        else :
            return "Error query parametrs"
        
        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url=url,params=payload,headers=header)
        return response.json() if response.status_code==200 else response.status_code

