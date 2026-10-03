[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionSink](../IMTPositionSink.md) / OnPositionClean

[Previous](OnPositionDelete.md) | [Next](OnPositionSync.md)

# IMTPositionSink::OnPositionClean

A handler of the event of clearing trade positions of a client.

C++
    
    
    virtual void  IMTPositionSink::OnPositionClean(
       const UINT64  login      // User's login
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTPositionSink.OnPositionClean(
       ulong         login      // User's login
       )

### Parameters

**login**  
[in] The login of a user.

### Note

Every day, at server time, expired demo accounts are automatically deleted on trade servers. All positions of these accounts are also deleted. The handler notifies of such an operation and transmits the logins of the accounts whose positions were deleted.
