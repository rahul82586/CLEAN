[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Connect/Disconnect](../ConnectDisconnect.md) / Connect

[Previous](../ConnectDisconnect.md) | [Next](Disconnect.md)

# MTWebAPI::Connect

Connect a Web client to a trade server.
    
    
    MTAPIRES  MTWebAPI::Connect(
         $ip,           // IP address
         $port,         // Port
         $timeout,      // Timeout
         $login,        // Login
         $password      // Password
         $agent         // Web client name
       )

### Parameters

**$ip**  
[in] The IP address of the server to connect to.

**$port**  
[in] The port of the server to connect to.

**$timeout**  
[in] Server response timeout in seconds.

**$login**  
[in] The login of the manager account, using which you want to connect.

**$password**  
[in] The password of the manager account, using which you want to connect.

**$agent=WebAPI**  
[in] The name of the Web client. The default name is WebAPI. This information will be displayed in the server log, along with information about the connection with the manager account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The [encryption](../../../Text-Protocol-(Raw-API)/Encryption.md) of transmitted data stream is enable automatically when connecting to a trade server.
