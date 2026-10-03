[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal ExternalID

[Previous](IMTHistoryDeal-Server.md) | [Next](IMTHistoryDeal-TimeMsc.md)

# IMTECNHistoryDeal::ExternalID

Get the deal identifier in the external system.

C++
    
    
    LPCWSTR  IMTECNHistoryDeal::ExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNHistoryDeal.ExternalID()

### Return Value

Deal ID in the external system.

### Note

The ID is filled by the gateway through which the order is forwarded.

# IMTECNHistoryDeal::ExternalID

Set the filling deal identifier in the external system.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::ExternalID(
       LPCWSTR       id    // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.ExternalID(
       string        id    // identifier
       )

### Parameters

**id**  
[in] Filling deal identifier in the external system.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The ID length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
