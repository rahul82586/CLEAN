[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountSink](../IMTAccountSink.md) / OnAccountMarginCallLeave

[Previous](OnAccountMarginCallEnter.md) | [Next](OnAccountStopOutEnter.md)

# IMTAccountSink::OnAccountMarginCallLeave

The event handler for the account exiting the Margin Call state.

C++
    
    
    virtual void  IMTAccountSink::OnAccountMarginCallLeave(
       const IMTAccount*   account,      // a pointer to the trading state object
       const IMTConGroup*  group         // a pointer to the group object
       )

.NET (Manager API)
    
    
    virtual void  CIMTAccountSink::OnAccountMarginCallLeave(
       CIMTAccount         account,      // trading state object
       CIMTConGroup        group         // group object
       )

### Parameters

**account**  
[in] A pointer to theIMTAccountobject of the account's trading state.

**group**  
[in] A pointer to theIMTConGroupobject of a group to which the account belongs.

### Note

Used only in the Manager API.
