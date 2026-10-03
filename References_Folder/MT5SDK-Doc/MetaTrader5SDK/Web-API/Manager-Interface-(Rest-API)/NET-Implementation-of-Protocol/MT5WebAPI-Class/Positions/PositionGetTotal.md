[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Positions](../Positions.md) / PositionGetTotal

[Previous](PositionGet.md) | [Next](PositionGetPage.md)

# MT5WebAPI.PositionGetTotal

Get the number of open positions of a client by the login.
    
    
    MTRetCode  MT5WebAPI.PositionGetTotal(
       ulong      login,     // Login
       out uint   total      // The number of positions
       )

### Parameters

**login**  
[in] The login of a client.

**total**  
[out] The number of currently open positions of the client with the specified login.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
