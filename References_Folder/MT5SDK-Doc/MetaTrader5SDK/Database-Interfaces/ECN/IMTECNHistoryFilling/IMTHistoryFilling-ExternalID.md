[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling ExternalID

[Previous](IMTHistoryFilling-TimeDoneMsc.md) | [Next](IMTHistoryFilling-Symbol.md)

# IMTECNHistoryFilling::ExternalID

Get the filling order identifier in the external system.

C++
    
    
    LPCWSTR  IMTECNHistoryFilling::ExternalID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNHistoryFilling.ExternalID()

### Return Value

Filling order identifier in the external system.

### Note

The ID is filled by the gateway through which the order is forwarded.

# IMTECNHistoryFilling::ExternalID

Set the filling order identifier in the external system.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::ExternalID(
       LPCWSTR       id    // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.ExternalID(
       string        id    // identifier
       )

### Parameters

**id**  
[in] Filling order identifier in the external system.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The ID length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
