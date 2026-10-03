[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [History Server](../History-Server.md) / Quotes Filtration

[Previous](Interaction-with-Quote-Providers.md) | [Next](Console-Commands.md)

# Quotes Filtration

The filtration system is intended for controlling the correctness of quotes on financial symbols from [data feeds](../../Platform-Setup/Data-Feeds.md). Filters can be set upon the ["Quotes"](../../Platform-Setup/Symbols/Symbol-Settings/Quotes.md) tab of each symbol.

  * Filters cannot be applied to instruments with the [enabled Depth of Market (#dom)](../../Platform-Setup/Symbols/Symbol-Settings/Common.md#dom) and with the one of the following properties: [Exchange calculation type (#calculation)](../../Platform-Setup/Symbols/Symbol-Settings/Trade.md#calculation) (begins with "Exchange") or [Last price based charting mode (#charts)](../../Platform-Setup/Symbols/Symbol-Settings/Common.md#charts). Also, filtering is not applied to [splice symbols](../../Platform-Setup/Symbols/Splicing-Futures.md).


  * To completely disable filtering, set 0 for all levels: Soft, Hard and Discard.


  * The platform automatically filters out negative and zero Bid and Ask prices of OTC instruments, regardless of whether their Market Depth is enabled or not. OTC (over-the-counter or off-exchange) symbols include financial instruments whose [calculation type (#calculation)](../../Platform-Setup/Symbols/Symbol-Settings/Trade.md#calculation) does not start with "Exchange".


  * Analysis and filtration are performed separately for Bid and Ask.


  * Filters are not applied to the first tick after a break in the quotes stream: after platform restart, after a break in [quoting sessions](../../Platform-Setup/Symbols/Symbol-Settings/Sessions.md), after [off-hours](../../Platform-Setup/Time.md) and after [holidays](../../Platform-Setup/Holidays.md). Filtration cannot be applied because it is not known in advance what was the price preceding the break. This rule does not apply to other price checks, including [allowable spread (#spread)](../../Platform-Setup/Symbols/Symbol-Settings/Quotes.md#spread).

  
---  
  
Three levels of quote filtration are available:

  * Soft filtration — the soft filtration level is the first border of the channel of allowed symbol prices. If a new price (Bid or Ask) differs from the previous one by more than the specified value (in points), it is deleted from the thread translated to clients. However, if such a price difference appears again the number of times specified in the "Filter" field, the new price level is accepted, and the filtration level is shifted by the specified value. Such quotes will be translated again.
  * Hard filtration — the hard filtration level is the second border of the price channel. If a received quote exceeds the level both of the soft and of the hard filtration, it is cut out from the thread translated to clients. For a new level of accepted price to be set, the quotes must be repeat the number of times specified in both levels;
  * Discard filtration level — if the difference between prices of the previous and new quote exceed the specified value, such new prices are definitely removed from the thread.



![Operation scheme of filters](images/filtration_scheme.png)

![Channel of allowed prices](images/filtration_scheme_acceptable.png) | — channel of allowed prices | ![Previous quote](images/filtration_scheme_previous.png) | — previous quote  
---|---|---|---  
![Soft filtration zone](images/filtration_scheme_soft.png) | — soft filtration zone | ![New quote](images/filtration_scheme_next.png) | — new quote  
![Hard filtration zone](images/filtration_scheme_hard.png) | — hard filtration zone | N | — number of quotes (set in the "Filter" filed) required to move to a new level  
![Discard filtration zone](images/filtration_scheme_discard.png) | — discard filtration zone |   
  
It is considered that there is a certain acceptable channel of price data fluctuation. This channel is limited by the set level of soft filtration. If the Bid or Ask price of the newly received quote differs from appropriate prices of the previous quote by the value of the specified soft filtration level, it is discarded. If several following quotes (the number is specified in the "Filter" parameter) also exceed the soft filtration level, the new price channel is set.

Example:  
---  
The last EURUSD quote was 1.50213/1.50231 (Bid/Ask). The soft filtration level is equal to 150, "Filter" parameter is equal to 3. The following quotes are received: 1.50373/1.50391, 1.50370/1.50388, 1.50372/1.50390, 1.50374/1.50392. In this case the first three quotes will be filtered away, because they exceed the previous one by more than 150 points. The last quote will be let in, and the new filtration level will be set 1.50374/1.50392 ± 150.   
  
The hard filtration level is an additional way to protect from incorrect quotes. If a new quote differs from the previous one by the value that is higher than the specified hard filtration level, it will be filtered away. The additional hard filtration protection is a more complicated mechanism of setting the new price channel. To confirm the new level, first the soft filter (specified number of quotes that exceed this value) must be passed, and then the hard one.

The discard filtration implies the unconditional filtering away of quotes that differ by this value. Such prices are deliberately considered incorrect.

## Filtration of Similar Quotes

The trading platform filters similar quotes received from data sources. If the platform receives the same quote as the previous one within a minute, it skips the quote. If the time interval is greater than one minute, the platform accepts the quote. The same quote is also accepted if the minute has changed. It allows plotting the charts correctly on a low liquidity market.

Example:

  * 13:01:15 a quote is received
  * 13:01:32 the same quote is received, it is not accepted
  * 13:01:50 the same quote is received, it is not accepted
  * 13:02:01 the same quote is received, it is accepted (the interval between quotes is less than 60 seconds, but the minute has changed)



## Spread Control

The Minimum Spread and Maximum Spread parameters in the Quotes tab are provided for additional protection. If the difference between the Bid and Ask prices in the incoming quote does not fall within the specified values, such a quote is removed from the stream.

The check only applies to over-the-counter (OTC) financial instruments with the [floating spread (#spread)](../../Platform-Setup/Symbols/Symbol-Settings/Common.md#spread). OTC instruments have one of the following [calculation types (#calculation)](../../Platform-Setup/Symbols/Symbol-Settings/Trade.md#calculation): Forex, Futures, CFD, CFD Leverage or CFD Index.
