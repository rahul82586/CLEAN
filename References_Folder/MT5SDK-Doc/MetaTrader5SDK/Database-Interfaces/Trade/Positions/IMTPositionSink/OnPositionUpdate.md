[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionSink](../IMTPositionSink.md) / OnPositionUpdate

[Previous](OnPositionAdd.md) | [Next](OnPositionDelete.md)

# IMTPositionSink::OnPositionUpdate

A handler of an event of trade position modification.

C++
    
    
    virtual void  IMTPositionSink::OnPositionUpdate(
       const IMTPosition*  position      // A pointer to the position object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTPositionSink.OnPositionUpdate(
       CIMTPosition        position      // Position object
       )

### Parameters

**position**  
[in] A pointer to the object of the updated position.

### Note

This method is called by the API to notify that a trade position has been modified.
