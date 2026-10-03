[🏠 Document Start](../README.md) / [Manager API](README.md) / Dealer Interface

[Previous](Manager-Interface/Geo-Services/GeoResolveBatch.md) | [Next](Dealer-Interface/OnDealerResult.md)

# Dealer Interface IMTDealerSink

The IMTDealerSink interface is used for subscribing to answers on trade requests that are formed by the dealer using the [IMTManagerAPI::DealerSend](Manager-Interface/Trade-Activity/Dealing/DealerSend.md). The answer is sent in two forms for each trade request:

Method | Purpose  
---|---  
[OnDealerResult](Dealer-Interface/OnDealerResult.md) | Asynchronous answer to a dealer's trade request in the form of the object of confirmation.  
[OnDealerAnswer](Dealer-Interface/OnDealerAnswer.md) | Asynchronous answer to a dealer's trade request in the form of the object of request.
