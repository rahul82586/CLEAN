[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonBirthDate

[Previous](PersonLastName.md) | [Next](PersonCitizenship.md)

# IMTClient::PersonBirthDate

Get the client's date of birth.

C++
    
    
    INT64  IMTClient::PersonBirthDate()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTClient.PersonBirthDate()

### Return Value

The client's date of birth. The date of birth is specified in the [FILETIME](https://docs.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime) format: the number of 100-nanosecond intervals that have elapsed since January 1, 1601.

# IMTClient::PersonBirthDate

Set the client's date of birth.

C++
    
    
    MTAPIRES  IMTClient::PersonBirthDate(
       const INT64  date      // Date of birth
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonBirthDate(
       long         date      // Date of birth
       )

### Parameters

**time**  
[in] Client's date of birth. The date of birth is specified in theFILETIMEformat: the number of 100-nanosecond intervals that have elapsed since January 1, 1601.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
