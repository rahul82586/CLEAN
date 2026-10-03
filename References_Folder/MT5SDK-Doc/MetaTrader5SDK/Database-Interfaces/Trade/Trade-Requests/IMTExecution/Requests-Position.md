[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Position

[Previous](Requests-DealCommission.md) | [Next](Requests-PositionBy.md)

# IMTExecution::Position

Gets the ticket (a unique number) of a position in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTExecution::Position()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.Position()

### Return Value

The ticket of a position in the MetaTrader 5 platform.

# IMTExecution::Position

Sets the ticket (a unique number) of a position in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTExecution::Position(
       const UINT64  position    // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Position(
       ulong         position    // Position ticket
       )

### Parameters

**position**  
[in] The ticket of a position in the MetaTrader 5 platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
