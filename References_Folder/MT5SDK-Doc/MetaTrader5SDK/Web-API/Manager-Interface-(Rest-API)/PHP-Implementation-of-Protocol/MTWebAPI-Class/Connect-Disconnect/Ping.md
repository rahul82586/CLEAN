[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Connect/Disconnect](../ConnectDisconnect.md) / Ping

[Previous](IsConnected.md) | [Next](../Logging-Management.md)

# MTWebAPI::Ping

If no [packets](../../../Text-Protocol-(Raw-API)/Format-of-Packages.md) were received from a client for 120 seconds, the server breaks connection. Thus, the further execution of commands will be impossible until you complete the [authentication](../../../Text-Protocol-(Raw-API)/Authentication.md) procedure.

This feature allows you to send empty packets to the server (called "pings").
    
    
    MTAPIRES  MTWebAPI::Ping()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The optimal time between sending pings is 20 seconds. You should not send pings too often.
