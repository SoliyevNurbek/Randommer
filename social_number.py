import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        endpoint='SocialNumber'
        url=self.get_url()+endpoint

        header={
            "X-Api-Key":api_key
        }

        response = requests.get(url,headers=header)
        return response.json() if response.status_code==200 else response.status_code
