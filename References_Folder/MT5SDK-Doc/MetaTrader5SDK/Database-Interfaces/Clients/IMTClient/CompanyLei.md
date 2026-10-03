[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / CompanyLei

[Previous](CompanyVat.md) | [Next](CompanyLicenseNumber.md)

# IMTClient::CompanyLei

Get the LEI number for EMIR reports (for corporate clients).

C++
    
    
    LPCWSTR  IMTClient::CompanyLei()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.CompanyLei()

### Return Value

If successful, a pointer to a string with the LEI number is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::CompanyLei

Set the LEI number for EMIR reports (for corporate clients).

C++
    
    
    MTAPIRES  IMTClient::CompanyLei(
       LPCWSTR       lei          // LEI number
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.CompanyLei(
       string        lei          // LEI number
       )

### Parameters

**lei**  
[in] LEI number for EMIR reports.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The number length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
