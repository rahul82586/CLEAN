[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / GroupAdd

[Previous](CountryNext.md) | [Next](GroupUpdate.md)

# IMTConMessenger::GroupAdd

Add a group of accounts for which the messenger will be used.

C++
    
    
    MTAPIRES  IMTConMessenger::GroupAdd(
       IMTConMessengerGroup*  group      // Group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessenger.GroupAdd(
       CIMTConMessengerGroup  group      // Group object
       )

Python
    
    
    MTConMessenger.GroupAdd(
       group                  # Group object
       )

### Parameters

**group**  
[in] Group objectIMTConMessengerGroup.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
