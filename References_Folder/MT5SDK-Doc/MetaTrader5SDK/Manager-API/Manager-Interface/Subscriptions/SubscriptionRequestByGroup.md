[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionRequestByGroup

[Previous](SubscriptionRequestByIDs.md) | [Next](SubscriptionRequestByLogins.md)

# IMTManagerAPI::SubscriptionRequestByGroup

Request subscriptions from the server by a client group.

C++
    
    
    MTAPIRES  IMTManagerAPI::SubscriptionRequestByGroup(
       LPCWSTR                group,     // Group
       IMTSubscriptionArray*  records    // Object of array of subscriptions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SubscriptionRequestByGroup(
       string                 mask,      // Group
       CIMTSubscriptionArray  records    // Object of array of subscriptions
       )

### Parameters

**group**  
[in] The groups for which the subscriptions are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**records**  
[out] An object of thearray of subscriptions. The 'records' object must be previously created via theIMTManagerAPI::SubscriptionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
