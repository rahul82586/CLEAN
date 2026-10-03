[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PositionBy

[Previous](Requests-Position.md) | [Next](Requests-PositionExternalID.md)

# IMTRequest::PositionBy

Gets the ticket (a unique number) of an opposite trade position in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTRequest::PositionBy()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.PositionBy()

### Return Value

The ticket of an opposite position in the MetaTrader 5 platform.

### Note

The method is used for Close By operations [EnTradeActions::TA_CLOSE_BY](Requests-Enumerations.md) and [EnTradeActions::DEALER_CLOSE_BY](Requests-Enumerations.md). 

# IMTRequest::PositionBy

Sets the ticket (a unique number) of an opposite trade position in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTRequest::PositionBy(
       UINT64  position      // The ticket of an opposite position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.PositionBy(
       ulong   position      // The ticket of an opposite position
       )

### Parameters

**position**  
[in] The ticket of an opposite position in the MetaTrader 5 platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is used for Close By operations [EnTradeActions::TA_CLOSE_BY](Requests-Enumerations.md) and [EnTradeActions::DEALER_CLOSE_BY](Requests-Enumerations.md). 
