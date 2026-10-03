[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionSink](../IMTPositionSink.md) / OnPositionDelete

[Previous](OnPositionUpdate.md) | [Next](OnPositionClean.md)

# IMTPositionSink::OnPositionDelete

A handler of an event of trade position deletion.

C++
    
    
    virtual void  IMTPositionSink::OnPositionDelete(
       const IMTPosition*  position      // A pointer to the position object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTPositionSink.OnPositionDelete(
       CIMTPosition        position      // Position object
       )

### Parameters

**position**  
[in] A pointer to the object of the deleted position. Due to architecture specifics, the deleted position is transmitted with zero values in Volume, VolumeExt, PriceOpen, TimeCreate and TimeCreateMsc fields.

### Note

This method is called by the API to notify that a trade position has been deleted.
