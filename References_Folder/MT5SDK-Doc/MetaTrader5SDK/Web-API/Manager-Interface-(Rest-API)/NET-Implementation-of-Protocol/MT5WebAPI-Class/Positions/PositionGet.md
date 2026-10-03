[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Positions](../Positions.md) / PositionGet

[Previous](../Positions.md) | [Next](PositionGetTotal.md)

# MT5WebAPI.PositionGet

Get a client's trade position by the symbol.
    
    
    MTRetCode  MT5WebAPI.PositionGet(
       ulong           login,     // Login
       string          symbol,    // Symbol
       out MTPosition  position   // Position
       )

### Parameters

**login**  
[in] The login of a client.

**symbol**  
[in] The name of the symbol, for which you need to get a position.

**position**  
[out] The MTPosition structure that describes a trade position. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
