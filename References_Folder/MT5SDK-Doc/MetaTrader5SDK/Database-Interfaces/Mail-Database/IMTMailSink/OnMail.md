[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMailSink](../IMTMailSink.md) / OnMail

[Previous](../IMTMailSink.md) | [Next](HookMail.md)

# IMTMailSink::OnMail

A handler of the event of email receiving.

C++
    
    
    virtual void  IMTMailSink::OnMail(
       const IMTMail*  mail      // A pointer to the email object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTMailSink.OnMail(
       CIMTMail        mail      // An email object
       )

### Parameters

**mail**  
[in] A pointer to the email object.

### Note

This method is called by the the API in order to notify of the fact that a new email has been received.
