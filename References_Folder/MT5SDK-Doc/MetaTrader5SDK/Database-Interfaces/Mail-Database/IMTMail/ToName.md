[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / ToName

[Previous](To.md) | [Next](ToRangesAdd.md)

# IMTMail::ToName

Get the name of the email recipient.

C++
    
    
    LPCWSTR  IMTMail::ToName()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTMail.ToName()

### Return Value

If successful, it returns a pointer to a string with the name of the recipient. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTMail](../IMTMail.md) object.

# IMTMail::ToName

Set the name of the email recipient.

C++
    
    
    MTAPIRES  IMTMail::ToName(
       LPCWSTR  name      // Recipient's name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.ToName(
       string   name      // Recipient's name
       )

### Parameters

**name**  
[in] The name of the email recipient.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the email recipient's name is not limited.
