[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / GroupNext

[Previous](GroupTotal.md) | [Next](TemplateAdd.md)

# IMTConMessenger::GroupNext

Get the group for which the messenger is used, by its index in the list.

C++
    
    
    MTAPIRES  IMTConMessenger::GroupNext(
       const UINT             pos,       // Group position
       IMTConMessengerGroup*  group      // Group object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.GroupNext(
       uint                   pos,       // Group position
       CIMTConMessengerGroup  group      // Group object
       )

Python
    
    
    MTConMessenger.GroupNext(
       pos                    # Group position
       )
    
    
    MTConMessenger.GroupGet()

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**group**  
[out] Group object. The 'group' object must be previously created via theIMTServerAPI::MessengerGroupCreateorIMTAdminAPI::MessengerGroupCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
