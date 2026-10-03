[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / ExternalID

[Previous](OrderSet.md) | [Next](Login.md)

# IMTOrder::ExternalID

Get the order ID in external trading systems.

C++
    
    
    LPCWSTR  IMTOrder::ExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTOrder.ExternalID()

Python
    
    
    MTOrder.ExternalID()

### Return Value

If successful, it returns a pointer to the string with the identifier. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTOrder](../IMTOrder.md) object.

# IMTOrder::ExternalID

Set the order ID in external trading systems.

C++
    
    
    MTAPIRES  IMTOrder::ExternalID(
       LPCWSTR  id      // External ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  IMTOrder::ExternalID(
       string   id      // External ID
       )

Python
    
    
    MTOrder.ExternalID()

### Parameters

**id**  
[in] The order ID in external systems.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the ID is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
