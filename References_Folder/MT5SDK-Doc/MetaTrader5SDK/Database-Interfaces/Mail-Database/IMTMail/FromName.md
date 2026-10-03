[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / FromName

[Previous](From.md) | [Next](To.md)

# IMTMail::FromName

Get the name of the email sender.

C++
    
    
    LPCWSTR  IMTMail::FromName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTMail.FromName()

### Return Value

If successful, it returns a pointer to a string with the name of the sender. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTMail](../IMTMail.md) object.

# IMTMail::FromName

Set the name of the email sender.

C++
    
    
    MTAPIRES  IMTMail::FromName(
       LPCWSTR  name      // Sender's name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.FromName(
       string   name      // Sender's name
       )

### Parameters

**name**  
[in] The name of the email sender.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the email sender's name is unlimited.
