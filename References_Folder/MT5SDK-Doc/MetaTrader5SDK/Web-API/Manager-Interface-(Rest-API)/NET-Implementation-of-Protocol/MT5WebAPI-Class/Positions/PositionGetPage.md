[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Positions](../Positions.md) / PositionGetPage

[Previous](PositionGetTotal.md) | [Next](../Trade.md)

# MT5WebAPI.PositionGetPage

Get open positions of a client by the login.
    
    
    MTRetCode  MT5WebAPI.PositionGetPage(
       ulong                 login,     // Login
       uint                  offset,    // Position index
       uint                  total,     // Number of positions
       out List<MTPosition>  positions  // An array of positions
       )

### Parameters

**login**  
[in] The login of the client whose positions you need to get.

**offset**  
[in] The index of the position starting from which you need to obtain positions. Numbering starts from 0.

**total**  
[in] The number of positions that should be obtained. The maximum number of positions that can be requested in one method call is 100.

**positions**  
[out] The MTPosition array of structures in which trade positions are described. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method allows to easily arrange a paged output of resulting positions. First you should get the total number of a client's positions using the [MT5WebAPI.PositionGetTotal](PositionGetTotal.md) method. After defining the number of positions that should be shown on one page (set by the total parameter), you can easily find the offset parameter for each page.
