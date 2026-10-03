[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTMail::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTMail::Assign(
       const IMTMail*  mail      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTMail.Assign(
       CIMTMail        mail      // Source object
       )

### Parameters

**mail**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
