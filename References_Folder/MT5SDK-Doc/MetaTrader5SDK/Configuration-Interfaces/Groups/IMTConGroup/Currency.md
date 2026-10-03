[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / Currency

[Previous](CompanyWithdrawalPage.md) | [Next](CurrencyDigits.md)

# IMTConGroup::Currency

Get the deposit currency of the group.

C++
    
    
    LPCWSTR  IMTConGroup::Currency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.Currency()

Python (Manager API)
    
    
    MTConGroup.Currency

### Return Value

If successful, it returns a pointer to a string with the group deposit currency. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGroup](../IMTConGroup.md) object.

# IMTConGroup::Currency

Set the deposit currency of the group.

C++
    
    
    MTAPIRES  IMTConGroup::Currency(
       LPCWSTR  currency      // Deposit currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.Currency(
       string   currency      // Deposit currency
       )

Python (Manager API)
    
    
    MTConGroup.Currency

### Parameters

**currency**  
[in] The group deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the currency name is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
