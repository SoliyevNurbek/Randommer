import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        endpoint='Finance/CryptoAddress/Types'
        url=self.get_url()+endpoint

        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url,headers=header)

        if response.status_code==200:
            return response.json()
        return response.status_code

    def get_crypto_address(self, crypto_type,api_key) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        endpoint='Finance/CryptoAddress'
        url=self.get_url()+endpoint
        header={
            "X-Api-Key":api_key
        }
        payload = {
            "cryptoType":crypto_type
            }
        response=requests.get(url,params=payload,headers=header)
        if response.status_code==200:
            return response.json()
        return response.status_code
    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        endpoint='Finance/Countries'
        url=self.get_url()+endpoint

        header={
            "X-Api-Key":api_key
        }

        response=requests.get(url,headers=header)

        if response.status_code==200:
            return response.json()
        return response.status_code

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        payload={
            "countryCode":country_code
        }

        header={
            "X-Api-Key":api_key
        }
        endpoint="Finance/Iban/"+f"{country_code}"
        url=self.get_url()+endpoint

        response=requests.get(url,params=payload,headers=header)

        if response.status_code==200:
            return response.json()
        return response.status_code