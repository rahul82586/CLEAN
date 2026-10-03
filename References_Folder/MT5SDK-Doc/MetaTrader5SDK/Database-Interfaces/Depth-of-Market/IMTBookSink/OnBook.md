[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Depth of Market](../../Depth-of-Market.md) / [IMTBookSink](../IMTBookSink.md) / OnBook

[Previous](../IMTBookSink.md) | [Next](../../Mail-Database.md)

# IMTBookSink::OnBook

A handler of the event of the received update of the Depth of Market.

C++
    
    
    virtual void  IMTBookSink::OnBook(
       const MTBook&       book        // A reference to the update structure
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTBookSink.OnBook(
       MTBook              book        // The update structure
       )

### Parameters

**tick**  
[out] A reference to the structure that describes change of the Market Depth (MTBook).

### Note

Manager API always receives the full Marked Depth state in this handler (rather than changes relative to the current state). Market Depth elements passed in [MTBook::items](../../../Structures/MTBookMTBookDiff.md) are sorted by price in the descending order. Market Depth reset elements ([MTBookItem::ItemReset (#enbookitem)](../../../Structures/MTBookItem.md#enbookitem)) are not used in Manager API.
