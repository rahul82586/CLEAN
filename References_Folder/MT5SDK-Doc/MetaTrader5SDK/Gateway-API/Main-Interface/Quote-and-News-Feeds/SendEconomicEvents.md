[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Quote and News Feeds](../Quote-and-News-Feeds.md) / SendEconomicEvents

[Previous](SendNews.md) | [Next](../History-Data.md)

# IMTGatewayAPI::SendEconomicEvents

Sending economic calendar events.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SendEconomicEvents(
       MTEconomicEvent*  events,       // An array of economic news
       const UINT        events_total  // The number of elements in the array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendEconomicEvents(
       MTEconomicEvent[] events        // An array of economic news
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendEconomicEvent(
       MTEconomicEvent   events        // A single description of economic news
       )

### Parameters

**events**  
[in] A pointer to the array of news of the economic calendar described by theMTEconomicEventstructure.

**events_total**  
[in] The number of elements in the events array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete. It always returns [MT_RET_OK](../../../Return-Codes/Successful-completion.md) but does not perform any action.

  * datetime
  * name
  * currency
  * period


