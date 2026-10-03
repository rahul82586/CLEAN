[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserUpdate

[Previous](OnUserAddExt.md) | [Next](OnUserDelete.md)

# IMTUserSink::OnUserUpdate

A handler of an event of account update.

C++
    
    
    virtual void  IMTUserSink::OnUserUpdate(
       const IMTUser*  user      // A pointer to the updated record
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserUpdate(
       CIMTUser        user      // The updated record
       )

### Parameters

**user**  
[in] A pointer to the object of the updated recordIMTUser.

### Note

The API calls the method to notify about an update of a trading account. The update event occurs not only when the account parameters are changed, but also when any trading operation is performed on it, as each operation changes the account state.
