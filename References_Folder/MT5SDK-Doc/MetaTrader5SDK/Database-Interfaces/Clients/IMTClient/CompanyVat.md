[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyVat

[Previous](CompanyRegAuthority.md) | [Next](CompanyLei.md)

# IMTClient::CompanyVat

Get the VAT payer ID (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyVat()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyVat()

### Return Value

If successful, a pointer to a string with the LEI number is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyVat

Set the VAT payer ID (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyVat(
       LPCWSTR       vat          // VAT payer number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyVat(
       string        vat          // VAT payer number
       )

### Parameters

**vat**  
[in] VAT payer number.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The number length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
