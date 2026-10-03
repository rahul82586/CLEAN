[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Position

[Previous](Requests-SourceLogin.md) | [Next](Requests-PositionBy.md)

# IMTRequest::Position

Gets the ticket (a unique number) of a trade position in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTRequest::Position()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.Position()

### Return Value

The ticket of a position in the MetaTrader 5 platform.

# IMTRequest::Position

Sets the ticket (a unique number) of a trade position in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTRequest::Position(
       UINT64  position      // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Position(
       ulong   position      // Position ticket
       )

### Parameters

**position**  
[in] The ticket of a trade position in the MetaTrader 5 platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The position ticket must be specified if the account supports the hedging option.
