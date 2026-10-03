[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Quote and News Feeds](../Quote-and-News-Feeds.md) / SendBookDiffs

[Previous](SendTicks.md) | [Next](SendBooks.md)

# IMTGatewayAPI::SendBookDiffs

Send the Depth of Market changes.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SendBookDiffs(
       MTBookDiff*  bookdiffs,          // Depth of Market changes array
       const UINT   bookdiffs_total     // Number of the elements in the array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendBookDiffs(
       MTBook[]     bookdiffs           // Depth of Market changes array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendBookDiff(
       MTBook       bookdiffs           // A single change of the depth of market
       )

### Parameters

***bookdiffs**  
[in] A pointer to the array of the Depth of Market changes described by theMTBookDiffstructure.

**bookdiffs_total**  
[in] Number of the elements in the bookdiffs array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred which corresponds to the response code.

### Note

This method sends the filled [MTBookDiff](../../../Structures/MTBookMTBookDiff.md) structures array to the trading platform.

## Filling MTBookDiff Structure

Each element of the aggregated depth of market is unique in type and price. The [MTBookDiff](../../../Structures/MTBookMTBookDiff.md) structure contains information about volume changes for a given type and price in the form of an array of MTBookItem [MTBookItem](../../../Structures/MTBookItem.md) elements. One MTBookDiff structure contains changes only for one instrument, described in the 'symbol' value of the structure.

Depth of Market change element types are listed below together with the actions of a history server when getting the elements of a specified type for the aggregative Depth of Market generation:

  * ItemReset — a history server will clean up the aggregative Depth of Market by the specified symbol when getting the element with such a type.
  * ItemSell, ItemBuy — a history server will look for the aggregative Depth of Market element by its type and price specified in MTBookItem when getting the [MTBookItem](../../../Structures/MTBookItem.md) structure with such a type. If the element is not found, then a new element (of MTBookItem type and price) is added to the aggregated depth of market. If the element is found in the aggregated depth of market, then element volume changes by the volume value, specified in the MTBookItem structure. In case a zero volume is indicated in the MTBookItem structure, the element found in the aggregative Depth of Market will be deleted.



  * The volume of element change in the aggregated depth of market, described in MTBookItem, can be both positive and negative.
  * The trading platform analyzes the items elements sent in the MTBookDiff structure strictly from the beginning to the end, consequently applying changes to the market depth.


  * All the symbol prices delivered into the platform are rounded in accordance with the [IMTConSymbol::Digits](../../../Configuration-Interfaces/Symbols/IMTConSymbol/Digits.md) parameter of the symbol. When broadcasting prices with higher accuracy, different levels can be combined into one rounded level. To avoid collisions, set the precision of the symbols in accordance with the precision of transmitted data.

  
---  
  
### Example

Let's analyze an example of how the difference between the Depths of Market at different time points is calculated:

Time point 1 | Time point 2 | Comparison result | Comment  
---|---|---|---  
Type | Price | Size | Type | Price | Size | Type | Price | Size  
Sell | 1.32464 | 5 | Sell | 1.32464 | 5 | Sell | 1.32463 | -3 | Bid volume with the price 1.32463 decreased by 3 lots.  
Sell | 1.32463 | 6 | Sell | 1.32463 | 3 | Buy | 1.32461 | 0 | Bid with the price 1.32461 disappeared from the Depth of Market.  
Buy | 1.32461 | 3 | Buy | 1.32460 | 4  | Buy | 1.32459 | 0 | Bid with the price 1.32459 disappeared from the Depth of Market.  
Buy | 1.32459 | 1 |  |  |  | Buy | 1.32460 | 4  | Bid with the price 1.32460 and the volume of 4 lots appeared in the Depth of Market.
