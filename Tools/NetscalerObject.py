"""
    this is a class for create,update,list,bind,unbind or delete and object on an Netscaler device.
    It uses NITRO API (REST) to make  requests to the Netscaler device.
   
"""

from operator import contains
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
    It uses the  NITRO API (REST) to make requests to the Netscaler device and sends data as a payload.
    
    """

    def __init__(self, **kwargs):
        """Initialize the class with the specified parameters using kwargs."""
        self.payload = kwargs.get('payload', None)
        self.object_type = kwargs.get('object_type', None)
        self.object_name = kwargs.get('object_name', None)
        self.name = kwargs.get('name', None)
    
    def list(self):
        """This tool lists an object on an Netscaler device using NITRO API (REST).         
    
        Args:
           object_name is the name of the object. 
           object_type can be : lbvserver,csvserver, service, server
           Use empty string "" to list all objects of the type. server.
                    
        """

        # If object_name is empty or None, list all objects of the type
        if not self.object_name or self.object_name.strip() == "":
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}"
        else:
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
            payload is the configuration of the object.
            object_type is the type of the object to be created. It can be : lbvserver,csvserver, service, server.
                    
        """

         # make sure it can not create a forbidden object
        if(self.object_type in forbidden_objects):
            url = f"http://{IP_ADDRESS}/nitro/v1"
        else:
            url = f"http://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/"

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
            payload is the configuration of the object.
            object_type is the type of the object to be updated. It can be : lbvserver,csvserver, service, server.
            object_name is the name of the object to be updated.                       

        """

        # make sure it can not update a forbidden object
        if(self.object_type in forbidden_objects):
            url = f"https://{IP_ADDRESS}/nitro/v1"
        else:
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/{self.object_name}"

        try:
            response = requests.request("PUT", url, headers=headers, json=self.payload, verify=False, timeout=20)
            response.raise_for_status()           
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text    

    def bind(self):
        """ This tool binds an object on an Netscaler device using NITRO API (REST).

        Args:
            payload is the configuration of the object. It contains what service,policy,monitor, etc is binding to what object
            object_type is the type of the object used to bind. It can be : lbvserver_service_binding, lbvserver_responderpolicy_binding,
            lbvserver_rewritepolicy_binding, csvserver_lbvserver_binding,csvserver_responderpolicy_binding,csvserver_rewritepolicy_binding,
            service_binding
                     

        """

        # make sure it can not update a forbidden object
        if(self.object_type in forbidden_objects):
            url = f"https://{IP_ADDRESS}/nitro/v1"
        else:
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}"

        try:
            response = requests.request("PUT", url, headers=headers, json=self.payload, verify=False, timeout=20)
            response.raise_for_status()           
        except requests.exceptions.HTTPError:
            if (response.status_code == 400 or response.status_code == 404):
                return f"An error occurred while making the request: {response.text}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred while making the request: {e}"
        else:
            return response.text      


    def unbind(self):
        """ This tool unbinds an object on an Netscaler device using NITRO API (REST).

        Args:            
            object_type is the type of the object used to bind. It can be : lbvserver_service_binding, lbvserver_responderpolicy_binding,
            lbvserver_rewritepolicy_binding, csvserver_lbvserver_binding,csvserver_responderpolicy_binding,csvserver_rewritepolicy_binding,
            service_binding
            object_name is the name of the object to be unbound.
            name is the name binded to the object_name to be unbound. name can be a servicename , a policyname, etc
                     

        """

        # make sure it can not update a forbidden object
        if(self.object_type in forbidden_objects):
            url = f"https://{IP_ADDRESS}/nitro/v1"
        elif("service" in self.object_type):
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/{self.object_name}?args=servicename:{self.name}"
        elif("policy" in self.object_type):
            url = f"https://{IP_ADDRESS}/nitro/v1/config/{self.object_type}/{self.object_name}?args=policyname:{self.name}"
        else:
            return

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

    def delete(self):
        """ This tool deletes an object from Netscaler device using NITRO API (REST).

        Args:
            object_type is the type of the object to be created. It can be : lbvserver,csvserver, service, server.                      
            object_name is the name of the object to be deleted.
        """

        # make sure it can not delete a forbidden object
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
        
