[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSink](../IMTConGroupSink.md) / OnGroupDelete

[Previous](OnGroupUpdate.md) | [Next](OnGroupSync.md)

# IMTConGroupSink::OnGroupDelete

A handler of the event of group removal.

C++
    
    
    virtual void  IMTConGroupSink::OnGroupDelete(
       const IMTConGroup*  config      // A pointer to the group object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConGroupSink.OnGroupDelete(
       CIMTConGroup        config      // The group object
       )

### Parameters

**config**  
[in] A pointer to the object of the deleted group.

### Note

This method is called by the API to notify of a fact that a group has been deleted.
