[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserDelete

[Previous](OnUserUpdate.md) | [Next](OnUserClean.md)

# IMTUserSink::OnUserDelete

A handler of an event of account deletion.

C++
    
    
    virtual void  IMTUserSink::OnUserDelete(
       const IMTUser*  user      // A pointer to the deleted record
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserDelete(
       CIMTUser        user      // The deleted record
       )

### Parameters

**user**  
[in] A pointer to the object of the deleted recordIMTUser.

### Note

This handler is called by the API to notify of deletion of a trading account.
