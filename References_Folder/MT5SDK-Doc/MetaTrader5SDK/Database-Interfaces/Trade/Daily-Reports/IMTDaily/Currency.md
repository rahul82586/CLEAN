[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Currency

[Previous](Group.md) | [Next](CurrencyDigits.md)

# IMTDaily::Currency

Get the client's deposit currency in a daily report.

C++
    
    
    LPCWSTR  IMTDaily::Currency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDaily.Currency()

### Return Value

If successful, it returns a pointer to a string with the client's deposit currency in a daily report. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDaily](../IMTDaily.md) object.

# IMTDaily::Currency

Set the client's deposit currency in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::Currency(
       LPCWSTR  curr      // Deposit currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Currency(
       string   curr      // Deposit currency
       )

### Parameters

**curr**  
[in] Client's deposit currency in a daily report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of currency name is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
