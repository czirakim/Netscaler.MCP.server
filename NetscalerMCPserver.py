"""

This is a MCP server, that interacts with an Netscaler device using NITRO API (REST).


"""

from mcp.server.fastmcp import FastMCP
from Tools.NetscalerObject import ADCobject

# Initialize FastMCP server
mcp = FastMCP("my_ADC_mcp_server")

@mcp.tool()
def list_tool(object_name: str, object_type: str):
    """ This tool lists object on an Netscaler device using NITRO API (REST).
     Args:
            object_name is the name of the object. 
            object_type can be : lbvserver,csvserver, service, server  
    """
    list = ADCobject(object_name = object_name, object_type = object_type)
    return list.list()



@mcp.tool()
def create_tool(payload: dict, object_type: str):
    """ This tool creates an object on an Netscaler device using NITRO API (REST).
        Args:
            payload contains the configuration of the pool. 
            object_type can be : lbvserver,csvserver, service, server  
        The configuration of the object is the body for an POST request.        
       
        """  
    # using python requests
    create = ADCobject(payload = payload, object_type = object_type)
    return create.create()


@mcp.tool()
def update_tool(payload: dict, object_type: str, object_name: str):
    """ This tool updates an object on an Netscaler device using NITRO API (REST).
        Args:
            payload contains the configuration of the pool. 
            object_type can be : lbvserver,csvserver, service, server
            object_name is the name of the object

        The configuration of the object is the body for an PATCH request.
       
    """    
    # using python requests
    update = ADCobject(payload=payload, object_type = object_type,object_name = object_name)
    return update.update()

@mcp.tool()
def delete_tool(object_type: str, object_name: str):
    """ This tool updates an object on an Netscaler device using NITRO API (REST).
        Args:
            object_type can be : lbvserver,csvserver, service, server
            object_name is the name of the objec

       
    """    
    # using python requests
    delete = ADCobject(object_type = object_type, object_name = object_name)
    return delete.delete()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
