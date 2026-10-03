[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / NewsMode

[Previous](ReportsSMTPPass.md) | [Next](NewsCategory.md)

# IMTConGroup::NewsMode

Get the mode of news sending to the clients from the group.

C++
    
    
    UINT  IMTConGroup::NewsMode()  const

.NET (Gateway/Manager API)
    
    
    EnNewsMode  CIMTConGroup.NewsMode()

Python (Manager API)
    
    
    MTConGroup.NewsMode

### Return Value

A value from the [IMTConGroup::EnNewsMode (#ennewsmode)](Enumerations.md#ennewsmode) enumeration.

# IMTConGroup::NewsMode

Set the mode of news sending to the clients from the group.

C++
    
    
    MTAPIRES  IMTConGroup::NewsMode(
       const UINT  mode      // Mode of news sending
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.NewsMode(
       EnNewsMode  mode      // Mode of news sending
       )

Python (Manager API)
    
    
    MTConGroup.NewsMode

### Parameters

**mode**  
[in] TheIMTConGroup::EnNewsModeenumeration is used for setting the news sending mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
