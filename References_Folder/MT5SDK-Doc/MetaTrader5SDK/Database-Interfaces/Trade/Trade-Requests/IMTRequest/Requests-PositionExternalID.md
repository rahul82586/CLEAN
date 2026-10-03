[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests PositionExternalID

[Previous](Requests-PositionBy.md) | [Next](Requests-PositionByExternalID.md)

# IMTRequest::PositionExternalID

Gets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    LPCWSTR  IMTRequest::PositionExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.PositionExternalID()

### Return Value

The ticket of a position in an external trading system.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTRequest](../Requests-IMTRequest.md) object.

  * When a dealer confirms a trade request to open a new position. In this case the field is filled with a value of [IMTConfirm::PositionExternalID](../IMTConfirm/Requests-OrderID.md).
  * When the server receives a request to modify\close an existing position. In this case the field is filled with the [IMTPosition::ExternalID](../../Positions/IMTPosition/ExternalID.md) value of the appropriate position.



# IMTRequest::PositionExternalID

Sets the ticket (a unique number) of a position in an external trading system.

C++
    
    
    MTAPIRES  IMTRequest::PositionExternalID(
       LPCWSTR       id    // Position ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.PositionExternalID(
       string        id    // Position ticket
       )

### Parameters

**id**  
[in] The ticket of a position in an external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The ID length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

  * When a dealer confirms a trade request to open a new position. In this case the field is filled with a value of [IMTConfirm::PositionExternalID](../IMTConfirm/Requests-OrderID.md).
  * When the server receives a request to modify\close an existing position. In this case the field is filled with the [IMTPosition::ExternalID](../../Positions/IMTPosition/ExternalID.md) value of the appropriate position.



### 
