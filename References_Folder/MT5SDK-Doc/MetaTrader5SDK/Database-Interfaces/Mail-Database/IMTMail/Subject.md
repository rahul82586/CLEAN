[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / Subject

[Previous](Parent.md) | [Next](From.md)

# IMTMail::Subject

Get the subject of an email.

C++
    
    
    LPCWSTR  IMTMail::Subject()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTMail.Subject()

### Return Value

If successful, it returns a pointer to a string with the email subject. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTMail](../IMTMail.md) object.

# IMTMail::Subject

Sets the email subject.

C++
    
    
    MTAPIRES  IMTMail::Subject(
       LPCWSTR  subject      // Email subject
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.Subject(
       string   subject      // Email subject
       )

### Parameters

**subject**  
[in] Subject of an email.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the email subject is not limited.
