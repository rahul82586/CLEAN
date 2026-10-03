[🏠 Document Start](../README.md) / [Web API](README.md) / Maintaining Connections

[Previous](Escaping-Special-Characters.md) | [Next](Protocol-Extension.md)

<a id="connection-maintenance"></a>
# Connection Maintenance (#connection-maintenance)

The access server operates as a 'stateful' service: you should first [authenticate](Authentication.md) and then maintain connection until you complete operation (the Keep-Alive connection). Re-authentication will be required in case of connection loss.

The connection type should be indicated as "keep-alive" in all passed commands:
    
    
    GET /command?param1=value1&param2=value2&...
    Host: {domain bound to public address}
    Accept: */*
    User-Agent: MetaTrader 5 Web API/5.2005 (Windows NT 6.2; x64)
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    {
    ...
    }

If no packets were received from a client for 180 seconds, the server breaks connection. Thus, the further execution of commands will be impossible until you complete the [authentication](Manager-Interface-(Rest-API)/Text-Protocol-(Raw-API)/Authentication.md) procedure.

In order to maintain a connection to the server, a Web client must send empty commands/packets (called "pings") to the server. The optimal time between sending pings is 20 seconds. You should not send pings too often.

In the Rest API, you can use the [/api/test/access (#test-access)](Maintaining-Connections.md#test-access) query for these purposes.

PHP and .NET implementations provide separate methods to maintain the connection:

  * [MTWebAPI::Ping](Manager-Interface-(Rest-API)/PHP-Implementation-of-Protocol/MTWebAPI-Class/Connect-Disconnect/Ping.md)
  * [MTWebAPI.Ping](Manager-Interface-(Rest-API)/NET-Implementation-of-Protocol/MT5WebAPI-Class/Connect-Disconnect/Ping.md)



When using the text API, an empty packet (a packet with an empty body and the zero packet continuation flag) should be sent. Packet number should be in the range specified for the client commands (0-3FFF).

Examples of empty packets of a client:
    
    
    000000010
    000000640

The MetaTrader 5 Access Server also automatically sends empty packets to a client every 20 seconds. Number of such commands are in the range 4000-7FFF.

Examples of empty packets of a server:
    
    
    000042680
    000062170

> Note that sending of empty commands are sent from the server does not depend on sending of responses to the commands of a Web client. These packets are received in one mixed stream.

<a id="test-access"></a>
## Check connection status (#test-access)

To check the Web client connection with the platform access server, as well as to verify the response to sent requests, send the /api/test/access command.

<a id="rest-api"></a>
### Rest API (#rest-api)

Request Format
    
    
    GET /api/test/access
    POST /api/test/access

Response Format
    
    
    { "retcode" : "xxxx yyyy" }

<a id="raw-api"></a>
### Raw API (#raw-api)

Request Format
    
    
    TEST_ACCESS\r\n

Response Format
    
    
    TEST_ACCESS|RETCODE=xxxx yyyy|\r\n

<a id="response-parameters"></a>
### Response Parameters (#response-parameters)

  * retcode — if successful, the [response code](../Return-Codes/Successful-completion.md) 0 is returned. Otherwise, an error code is returned.



<a id="quit-operation"></a>
## Quit Operation (#quit-operation)

To terminate the connection between the Web client and the trading platform, send the /api/quit command.

<a id="rest-api"></a>
### Rest API (#rest-api)

Request format
    
    
    GET /api/quit
    POST /api/quit

Response format
    
    
    { "retcode" : "xxxx yyyy" }

<a id="raw-api"></a>
### Raw API (#raw-api)

Request format
    
    
    QUIT\r\n

Response format
    
    
    QUIT|RETCODE=xxxx yyyy|\r\n
