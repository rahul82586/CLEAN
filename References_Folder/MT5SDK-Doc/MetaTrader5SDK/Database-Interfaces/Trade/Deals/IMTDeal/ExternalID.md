[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / ExternalID

[Previous](DealSet.md) | [Next](Login.md)

# IMTDeal::ExternalID

Get the deal ID in external trading systems.

C++
    
    
    LPCWSTR  IMTDeal::ExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDeal.ExternalID()

### Return Value

If successful, it returns a pointer to the string with the identifier. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDeal](../IMTDeal.md) object.

# IMTDeal::ExternalID

Set the ID of the deal in external trading systems.

C++
    
    
    MTAPIRES  IMTDeal::ExternalID(
       LPCWSTR  id      // External ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.ExternalID(
       string   id      // External ID
       )

### Parameters

**id**  
[in] The ID of the deal in external trading systems.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the ID is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
