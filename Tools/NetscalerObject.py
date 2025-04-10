"""
    this is a class for create,update,list or delete and object on an Netscaler device.
    It uses NITRO API (REST) to make  requests to the Netscaler device.
   
"""

import os
from dotenv import load_dotenv
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Specify the path to the .env file
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)  # load environment variables from .env

# list of forbidden objects
forbidden_objects = ["systemuser"]
# IP of the Netscaler device
IP_ADDRESS = os.getenv('IP_ADDRESS')
# Auth user and password
USER = os.getenv('X-NITRO-USER')
PASS = os.getenv('X-NITRO-PASS')


headers = {
    'X-NITRO-USER': f'{USER}',
    'X-NITRO-PASS': f'{PASS}',
    'Content-Type': 'application/json'
   }

class ADCobject:
    
    """this is a class for create action. It can create vips,pools,irules and profiles.
    It uses the  NITRO API (REST) to make POST requests to the Netscaler device and sends data as a payload.
    
    """

    def __init__(self, **kwargs):
        """Initialize the class with the specified parameters using kwargs."""
        self.payload = kwargs.get('payload', None)
        self.object_type = kwargs.get('object_type', None)
        self.object_name = kwargs.get('object_name', None)
    
    def list(self):
        """This tool lists an object on an Netscaler device using NITRO API (REST).         
    
        Args:
            object_name is the name of the object. 
            object_type is the type of the object to be created. It can be : lbvserver,csvserver, service, server.
                    
        """

        url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/{self.object_name}"
        # Convert input_data dictionary to JSON string
        #json_payload = str(self.payload).replace("'", '"')  # Ensures proper JSON formatting

        try:
            response = requests.request("GET", url, headers=headers, verify=False, timeout=20)
            response.raise_for_status()   
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
        
    def create(self):
        """This tool creates an object on Netscaler device using NITRO API (REST).         
    
        Args:
            url_body is the configuration of teh object.
            object_type is the type of the object to be created. It can be : lbvserver,csvserver, service, server.
                    
        """

         # make sure it can not create a user
        if(self.object_type in forbidden_objects):
            url = f"https://{IP_ADDRESS}/nitro/v1"
        else:
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/"

        try:
            response = requests.request("POST", url, headers=headers, json=self.payload, verify=False, timeout=20)
            response.raise_for_status()   
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text
        
    def update(self):
        """ This tool updates an object on an Netscaler device using NITRO API (REST).

        Args:
            url_body is the configuration of teh object.
            object_type is the type of the object to be created. It can be : lbvserver,csvserver, service, server.
            object_name is the name of teh object to be updated.                       

        """

        # make sure it can not update a user
        if(self.object_type in forbidden_objects):
            url = f"https://{IP_ADDRESS}/nitro/v1"
        else:
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/{self.object_name}"

        try:
            response = requests.request("PATCH", url, headers=headers, json=self.payload, verify=False, timeout=20)
            response.raise_for_status()           
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text    

    def delete(self):
        """ This tool deletes an object from Netscaler device using NITRO API (REST).

        Args:
            url_body is the configuration of teh object.
            object_type is the type of the object to be created. It can be : lbvserver,csvserver, service, server.                      
            object_name is the name of teh object to be deleted.
        """

        # make sure it can not delete a user
        if(self.object_type in forbidden_objects):
            url = f"https://{IP_ADDRESS}/nitro/v1"
        else:
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/{self.object_name}"
   

        try:
            response = requests.request("DELETE", url, headers=headers, verify=False, timeout=20)
            response.raise_for_status()           
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text   
        
