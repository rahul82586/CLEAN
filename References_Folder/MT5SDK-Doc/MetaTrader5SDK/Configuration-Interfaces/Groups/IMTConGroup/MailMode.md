[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / MailMode

[Previous](NewsLangNext.md) | [Next](TradeFlags.md)

# IMTConGroup::MailMode

Get the mode of operation of the internal mail system for the group.

C++
    
    
    UINT  IMTConGroup::MailMode()  const

.NET (Gateway/Manager API)
    
    
    EnMailMode  CIMTConGroup.MailMode()

Python (Manager API)
    
    
    MTConGroup.MailMode

### Return Value

A value from the [IMTConGroup::EnMailMode (#enmailmode)](Enumerations.md#enmailmode) enumeration.

# IMTConGroup::MailMode

Set the mode of operation of the internal mail system for the group.

C++
    
    
    MTAPIRES  IMTConGroup::MailMode(
       const UINT  mode      // Email operation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.MailMode(
       EnMailMode  mode      // Email operation mode
       )

Python (Manager API)
    
    
    MTConGroup.MailMode

### Parameters

**mode**  
[in] To set the mode of operation of the internal mail system, theIMTConGroup::EnMailModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
