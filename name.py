import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        endpoint='Name'
        url=self.get_url()+endpoint
        if 1<=quantity<=5000 and (nameType=='firstname'or nameType=='surname'or nameType=='fullname'):
            payload={
                "nameType":nameType,
                "quantity":quantity
            }   
        else:
            return "Error query parametrs"
        header={
            "X-Api-Key":api_key
        } 

        response = requests.get(url,params=payload,headers=header)
        return response.json() if response.status_code==200 else response.status_code


    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        endpoint='Name/Suggestions'
        url=self.get_url()+endpoint

        if len(startingWords)<=100:
            payload={
                "startingWords":startingWords
            }
        else:
            return "Error query parametrs"
        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url,params=payload,headers=header)
        return response.json() if response.status_code==200 else response.status_code
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        endpoint='Name/Cultures'
        url=self.get_url()+endpoint

        header={
            "X-Api-Key":api_key
        }
        response = requests.get(url,headers=header)
        return response.json() if response.status_code==200 else response.status_code
    