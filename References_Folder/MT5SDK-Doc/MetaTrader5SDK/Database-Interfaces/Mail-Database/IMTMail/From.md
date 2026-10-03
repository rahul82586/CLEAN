[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / From

[Previous](Subject.md) | [Next](FromName.md)

# IMTMail::From

Get the login of the email sender.

C++
    
    
    UINT64  IMTMail::From()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTMail.From()

### Return Value

The login of the email sender.

# IMTMail::From

Set the login of the email sender.

C++
    
    
    MTAPIRES  IMTMail::From(
       const UINT64  id      // Sender's login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.From(
       ulong         id      // Sender's login
       )

### Parameters

**id**  
[in] The login of the email sender.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
