[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Quote and News Feeds](../Quote-and-News-Feeds.md) / SendNews

[Previous](SendBooks.md) | [Next](SendEconomicEvents.md)

# IMTGatewayAPI::SendNews

Passing the news.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SendNews(
       MTNews*     news,           // News array
       const UINT  news_total      // Number of the elements in the array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendNews(
       MTNews[]    news            // News array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendNews(
       MTNews      news            // A single description of news
       )

### Parameters

**news**  
[in] A pointer to the news array described by theMTNewsstructure.

**news_total**  
[in] Number of the elements in the news array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method sends the filled [MTNews](../../../Structures/MTNews.md) structures array to the trading platform. After the news are sent, a programmer has to manually free the memory used for the news bodies (*body parameter in the MTNews structure).
