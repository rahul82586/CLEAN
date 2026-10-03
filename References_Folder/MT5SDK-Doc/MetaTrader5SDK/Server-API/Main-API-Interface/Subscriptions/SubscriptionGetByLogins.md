[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Subscriptions](../Subscriptions.md) / SubscriptionGetByLogins

[Previous](SubscriptionGetByID.md) | [Next](SubscriptionHistoryCreate.md)

# IMTServerAPI::SubscriptionGetByLogins

Get subscriptions by a list of logins.
    
    
    MTAPIRES  IMTServerAPI::SubscriptionGetByLogins(
       const UINT64*          logins,       // Logins
       const UINT             logins_total, // Number of logins
       IMTSubscriptionArray*  records       // Object of array of subscriptions
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**records**  
[out] An object of thearray of subscriptions. The 'records' object must be previously created via theIMTServerAPI::SubscriptionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
