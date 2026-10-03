[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Company

[Previous](CurrencyDigits.md) | [Next](EMail.md)

# IMTDaily::Company

Get the company serving the client in a daily report.

C++
    
    
    LPCWSTR  IMTDaily::Company()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDaily.Company()

### Return Value

If successful, it returns a pointer to a string with the company name in a daily report. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDaily](../IMTDaily.md) object.

# IMTDaily::Company

Set the company serving the client in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Company(
       LPCWSTR  company      // Company
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Company(
       string   company      // Company
       )

### Parameters

**company**  
[in] The company serving the client in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of company name is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
