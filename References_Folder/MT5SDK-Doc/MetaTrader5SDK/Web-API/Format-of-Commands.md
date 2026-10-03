[🏠 Document Start](../README.md) / [Web API](README.md) / Format of Commands

[Previous](Getting-Started.md) | [Next](Authentication.md)

# Format of Commands

Web API commands are passed using standard POST and GET requests:

  * Command names and their parameters fully coincide with the [Web API protocol](Manager-Interface-(Rest-API).md).
  * Command parameters are specified after ? and are separated using &.
  * An additional request body is passed in the JSON format.
  * The domain connected with the access server's public point is specified as the host.
  * Contents type in the request: application/x-www-form-urlencoded.



The command can be schematically represented as follows:
    
    
    GET /command?param1=value1&param2=value2&...
    Host: {domain bound to public address}
    Accept: */*
    User-Agent: MetaTrader 5 Web API/5.2005 (Windows NT 6.2; x64)
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    {
    ...
    }
     
    POST /command?param1=value1&param2=value2&...
    Host: {domain bound to public address} 
    Accept: */*
    User-Agent: MetaTrader 5 Web API/5.2005 (Windows NT 6.2; x64)
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    {
    ...
    }

The following data is specified in the request:

  * Host — the domain with which the public point of the access server is connected.
  * command — the name of the [command](Manager-Interface-(Rest-API).md)
  * param1, value1, ... — additional parameters if they are used for this command.
  * { ... } — additional request body as a text in the JSON format if it is provided for the specified command. For example, when using the [/api/user/add](Manager-Interface-(Rest-API)/Users/Add.md) command, the created account parameters are passed in the additional body.  
Some of the parameters are case-sensitive, for example, the [LeadSource and LeadCampaign](Manager-Interface-(Rest-API)/Users/Data-Structure.md) fields of the trading account. Because of this, field names in a JSON body must always be passed in the case specified in the documentation. For example, the entry { ... "LEADCAMPAIGN":"website_ad" ... } is incorrect. The correct specification is { ... "LeadCampaing":"website_ad" ... }.



The response from the server is passed in the JSON format. The response code is always passed as the first parameter, which is followed by additional information.
    
    
    { "retcode" : "retcode", "answer" : {
    "param1" : "value1",
    "param2" : "value2",
    ... }
    }

For example, in response to the [/api/user/get](Manager-Interface-(Rest-API)/Users/Get-by-Login.md) command, you will receive the response code and data concerning the requested user.

  * Commands, parameters and the server response are passed in the Unicode (UTF-8) format.


  * All commands should be passed in the same session during and after the authentication.

  
---
