import requests
from randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        endpoint='Text/LoremIpsum'
        url=self.get_url()+endpoint

        if (loremType=='normal' or loremType=='business') and (type=='paragraphs' or type=='words') and 1<=number<=2147483647:
            payload={
                "loremType":loremType,
                "type":type,
                "number":number
            }
        else:
            return "Error query parametrs"
        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url=url,params=payload,headers=header)
        return response.json() if response.status_code==200 else response.status_code

    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        pass
