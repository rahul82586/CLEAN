[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserSink](../IMTUserSink.md) / OnUserAdd

[Previous](../IMTUserSink.md) | [Next](OnUserAddExt.md)

# IMTUserSink::OnUserAdd

A handler of the event of adding a new account.

C++
    
    
    virtual void  IMTUserSink::OnUserAdd(
       const IMTUser*  user      // A pointer to the added record
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTUserSink.OnUserAdd(
       CIMTUser        user      // The added record
       )

### Parameters

**user**  
[in] A pointer to the object of the added record IMTUser.

### Note

This method is called by the API to notify that a new trading account has been added.
