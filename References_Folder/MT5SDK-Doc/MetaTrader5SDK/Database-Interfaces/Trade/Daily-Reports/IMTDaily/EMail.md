[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / EMail

[Previous](Company.md) | [Next](Balance.md)

# IMTDaily::EMail

Get an email of a client in a daily report.

C++
    
    
    LPCWSTR  IMTDaily::EMail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDaily.EMail()

### Return Value

If successful, it returns a pointer to a string with the client's email address in a daily report. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDaily](../IMTDaily.md) object.

# IMTDaily::EMail

Set an email of a client in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::EMail(
       LPCWSTR  mail      // Email address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.EMail(
       string   mail      // Email address
       )

### Parameters

**mail**  
[in] An email of a client in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the address is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
