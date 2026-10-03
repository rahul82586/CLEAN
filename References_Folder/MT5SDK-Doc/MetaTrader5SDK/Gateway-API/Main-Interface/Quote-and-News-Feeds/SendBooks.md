[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Quote and News Feeds](../Quote-and-News-Feeds.md) / SendBooks

[Previous](SendBookDiffs.md) | [Next](SendNews.md)

# IMTGatewayAPI::SendBooks

Send the entire state of the Depth of Market.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SendBooks(
       MTBook*     books,           // Depth of Market array
       const UINT  books_total      // Number of the elements in the array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendBooks(
       MTBook[]    books            // Depth of Market array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendBooks(
       MTBook      books            // Single description of the depth of market
       )

### Parameters

**books**  
[in] A pointer to the array of the Depth of Market described by theMTBookstructure.

**books_total**  
[in] Number of the elements in the bookdiffs array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method sends the filled [MTBook](../../../Structures/MTBookMTBookDiff.md) structures array to the trading platform.

All Market Depth items in one direction (buy or sell) must have different prices. If the source data contains several levels with the same price, you should aggregate them into one level with the total volume before sending them to the platform.
