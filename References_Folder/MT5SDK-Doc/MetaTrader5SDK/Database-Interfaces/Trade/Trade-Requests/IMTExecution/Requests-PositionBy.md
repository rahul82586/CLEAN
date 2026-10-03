[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests PositionBy

[Previous](Requests-Position.md) | [Next](Requests-PositionExternalID.md)

# IMTExecution::PositionBy

Gets the ticket (a unique number) of an opposite trade position in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTExecution::PositionBy()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.PositionBy()

### Return Value

The ticket of an opposite position in the MetaTrader 5 platform.

### Note

IMTExecution::PositionBy is used for Close By operations.

# IMTExecution::PositionBy

Sets the ticket (a unique number) of an opposite trade position in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTExecution::PositionBy(
       const UINT64  position    // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.PositionBy(
       ulong         position    // Position ticket
       )

### Parameters

**position**  
[in] The ticket of an opposite position in the MetaTrader 5 platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

IMTExecution::PositionBy is used for Close By operations.

It is only used in the hedging position accounting mode [EnMarginMode::MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode).
