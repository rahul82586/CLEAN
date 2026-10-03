[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests PositionExternalID

[Previous](Requests-OrderID.md) | [Next](Requests-PriceGateway.md)

# IMTConfirm::PositionExternalID

Gets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    LPCWSTR  IMTConfirm::PositionExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConfirm.PositionExternalID()

### Return Value

The ticket of a position in an external trading system.

### Note

The pointer to the resulting string is valid for the lifetime of [IMTConfirm](../Requests-IMTConfirm.md) object.

# IMTConfirm::PositionExternalID

Sets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    MTAPIRES  IMTConfirm::PositionExternalID(
       LPCWSTR       id    // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.PositionExternalID(
       string        id    // Position ticket
       )

### Parameters

**id**  
[in] The ticket of a position in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
