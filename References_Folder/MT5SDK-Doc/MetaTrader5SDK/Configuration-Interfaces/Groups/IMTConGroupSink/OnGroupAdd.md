[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSink](../IMTConGroupSink.md) / OnGroupAdd

[Previous](../IMTConGroupSink.md) | [Next](OnGroupUpdate.md)

# IMTConGroupSink::OnGroupAdd

A handler of the event of adding a new group.

C++
    
    
    virtual void  IMTConGroupSink::OnGroupAdd(
       const IMTConGroup*  config      // A pointer to the group object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConGroupSink.OnGroupAdd(
       CIMTConGroup        config      // The group object
       )

### Parameters

**config**  
[in] A pointer to the object of the added group.

### Note

This method is called by the API to notify of adding of a new group.
