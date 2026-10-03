[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMailSink](../IMTMailSink.md) / HookMail

[Previous](OnMail.md) | [Next](../../News-Database.md)

# IMTMailSink::HookMail

A hook of the event of email receiving.

C++
    
    
    virtual MTAPIRES  IMTMailSink::HookMail(
       IMTMail*  mail      // Mail object
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTMailSink.HookMail(
       CIMTMail  mail      // Mail object
       )

### Parameters

**mail**  
[in][out] An object of the email.

### Return Value

In case there are no handlers if this event, [MT_RET_OK_NONE](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called consistently in accordance with the order of plugins in the list until the first plugin that has returned a response code other than [MT_RET_OK_NONE](../../../Return-Codes/Successful-completion.md).
