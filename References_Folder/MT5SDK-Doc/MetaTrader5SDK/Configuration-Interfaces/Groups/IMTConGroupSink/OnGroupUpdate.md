[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSink](../IMTConGroupSink.md) / OnGroupUpdate

[Previous](OnGroupAdd.md) | [Next](OnGroupDelete.md)

# IMTConGroupSink::OnGroupUpdate

A handler of the event of updating group settings.

C++
    
    
    virtual void  IMTConGroupSink::OnGroupUpdate(
       const IMTConGroup*  config      // A pointer to the group object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConGroupSink.OnGroupUpdate(
       CIMTConGroup        config      // The group object
       )

### Parameters

**config**  
[in] A pointer to the updated group object.

### Note

This method is called by the API to notify of updates in group settings.
