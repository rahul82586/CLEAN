[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ExternalID

[Previous](Position.md) | [Next](TimeCreate.md)

# IMTPosition::ExternalID

Gets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    LPCWSTR  IMTPosition::ExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTPosition.ExternalID()

### Return Value

The ticket of a position in an external trading system.

# IMTPosition::ExternalID

Sets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    MTAPIRES  IMTPosition::ExternalID(
       LPCWSTR       id          // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ExternalID(
       string        id          // Position ticket
       )

### Parameters

**id**  
[in] The ticket of a position in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
