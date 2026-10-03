[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Subscriptions](../Subscriptions.md) / SubscriptionGetByLogins

[Previous](SubscriptionGetByID.md) | [Next](SubscriptionHistoryCreate.md)

# IMTReportAPI::SubscriptionGetByLogins

Get subscriptions by a list of logins.
    
    
    MTAPIRES  IMTReportAPI::SubscriptionGetByLogins(
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
[out] An object of thearray of subscriptions. The 'records' object must be previously created via theIMTReportAPI::SubscriptionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
