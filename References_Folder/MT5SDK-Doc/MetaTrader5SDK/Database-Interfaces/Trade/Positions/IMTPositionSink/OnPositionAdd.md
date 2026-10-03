[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionSink](../IMTPositionSink.md) / OnPositionAdd

[Previous](../IMTPositionSink.md) | [Next](OnPositionUpdate.md)

# IMTPositionSink::OnPositionAdd

A handler of the event of adding a position.

C++
    
    
    virtual void  IMTPositionSink::OnPositionAdd(
       const IMTPosition*  position      // A pointer to the position object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTPositionSink::OnPositionAdd(
       CIMTPosition        position      // Position object
       )

### Parameters

**position**  
[in] A pointer to the object of the added position.

### Note

This method is called by the API to notify that a new trade position has been added.
