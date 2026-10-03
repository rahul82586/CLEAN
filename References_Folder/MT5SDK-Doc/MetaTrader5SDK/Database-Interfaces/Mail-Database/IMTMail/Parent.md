[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Mail Database](../../Mail-Database.md) / [IMTMail](../IMTMail.md) / Parent

[Previous](ID.md) | [Next](Subject.md)

# IMTMail::Parent

Get the ID of the parent email.

C++
    
    
    UINT64  IMTMail::Parent()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTMail.Parent()

### Return Value

The ID of the parent email.

### Note

The mail system combines emails into conversations (chains). An emails is combined with another one into a chain, if the "Reply" command is used to send a reply. Using the ID of the parent email, you can define a chain of emails.
