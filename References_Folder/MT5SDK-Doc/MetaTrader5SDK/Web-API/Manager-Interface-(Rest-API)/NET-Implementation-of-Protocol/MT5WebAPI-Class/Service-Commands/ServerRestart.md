[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Service Commands](../Service-Commands.md) / ServerRestart

[Previous](../Service-Commands.md) | [Next](../Common-Configuration.md)

# MT5WebAPI.ServerRestart

This method restarts the server to which the Web client is connected. If a Web client is connected to the main trade server, this command will restart all the trading platform.
    
    
    MTRetCode  MT5WebAPI.ServerRestart()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Restart servers only on weekends and holidays or at night when the trading activity is minimal. Restarting the server may take several seconds (up to a minute), during this time connection to the server is impossible.
