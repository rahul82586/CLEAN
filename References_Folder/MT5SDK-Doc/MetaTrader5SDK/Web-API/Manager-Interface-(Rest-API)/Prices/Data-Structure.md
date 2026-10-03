[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Prices](../Prices.md) / Data Structure

[Previous](../Prices.md) | [Next](Get-Quotes.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

Price data is passed in JSON format as a response to the [/api/tick/last](Get-Quotes.md), [/api/tick/last_group](Get-Quotes-by-Group.md) and [/api/tick/stat](Get-Statistics.md) requests.

<a id="tick"></a>
## Tick Structure (#tick)

This structure describes the full information about a tick. It contains the following parameters:

Field | Type | Description  
Symbol | String | Symbol name.  
Digits | Integer | The number of decimal places in the price.  
Bid | Float | The Bid price.  
Ask | Float | The Ask price.  
Last | Float | The price of the last committed transaction.  
Volume | Integer | Volume of a last executed deal.  
Datetime | Integer | Date and time of the tick in seconds passed since 01.01.1970.  
DatetimeMsc | Integer | Date and time of the tick in milliseconds passed since 01.01.1970.  
  
This structure is used in the following commands:

  * [/api/tick/last](Get-Quotes.md)
  * [/api/tick/last_group](Get-Quotes-by-Group.md)
  * [/tick_history](Get-Tick-History.md)



<a id="stat"></a>
## Statistics Structure (#stat)

This structure describes the statistical information about a symbol. It contains the following parameters:

Field | Type | Description  
Symbol | String | Symbol name.  
Digits | Integer | The number of decimal places in the price.  
Bid | Float | The Bid price.  
BidLow | Float | The lowest bid price for the current day.  
BidHigh | Float | The highest bid price for the current day.  
BidDir | Integer | The direction of change of the bid price relative to its previous state (0 — unchanged, 1 — upwards, 2 — downwards).  
Ask | Float | The Ask price.  
AskLow | Float | The highest and lowest ask prices for the current day.  
AskHigh | Float | The highest ask price for the current day.  
AskDir | Integer | The direction of change of the ask price relative to its previous state (0 — unchanged, 1 — upwards, 2 — downwards).  
Last | Float | The price of the last committed transaction.  
LastLow | Float | The lowest price at which a deal has been conducted for the current day.  
LastHigh | Float | The highest price, at which a deal was executed during the current day.  
LastDir | Integer | The change direction of the price of the last deal relative to its previous state (0 — unchanged, 1 — upwards, 2 — downwards).  
Volume | Integer | Volume of a last executed deal.  
VolumeLow | Integer | The lowest deal volume for the current day.  
VolumeHigh | Integer | The highest deal volume for the current day.  
VolumeDir | Integer | The direction of change of the volume relative to its previous state (0 — unchanged, 1 — upwards, 2 — downwards).  
TradeDeals | Integer | The total number of deals executed for the current session.  
TradeVolume | Integer | The total volume of deals executed for the current session.  
TradeTurnover | Integer | Money turnover for a symbol for the current session.  
TradeInterest | Integer | The total volume of effective contracts (futures, options) for which there have been no calculations yet.  
TradeBuyOrders | Integer | The total number of buy requests.  
TradeBuyVolume | Integer | The total amount of buy requests.  
TradeSellOrders | Integer | The total number of sell requests.  
TradeSellVolume | Integer | The total amount of buy sell requests.  
Datetime | Integer | Date and time of the tick in seconds passed since 01.01.1970.  
DatetimeMsc | Integer | Date and time of the tick in milliseconds passed since 01.01.1970.  
PriceOpen | Float | The open price of the last (current) session.  
PriceClose | Float | The close price of the last (current) session.  
PriceAw | Float | The weighted average price for a session.  
PriceChange | Float | Price change in percentage terms. Indicates the difference between the price of a last deal and the close price of the last session in percentage terms: ((last - price_close)/price_close)*100.  
PriceVolatility | Float | The implied volatility. It is specified as a percentage, and characterizes the expectations of market participants about the value of the underlying asset of the option.  
PriceTheoretical | Float | The theoretical (fair) price of an option calculated for the specified strike based on historical data.  
PriceGreeksDelta | Float | Option delta. "[The Greeks (#greeks)](https://www.metatrader5.com/ru/terminal/help/trading/options_board#greeks)", which include Delta, Theta, Gamma, Vega, Po and Omega, are quantities representing the sensitivity of the option price to changes in various parameters: strike prices, volatility, etc.  
PriceGreeksTheta | Float | Option theta.  
PriceGreeksGamma | Float | Option gamma.  
PriceGreeksVega | Float | Option vega.  
PriceGreeksRho | Float | Option rho.  
PriceGreeksOmega | Float | Option omega.  
PriceSensitivity | Float | Option sensitivity. It shows by how many points the price of the option's underlying asset should change so that the price of the option changes by one point.  
  
This structure is used in the [/api/tick/stat](Get-Statistics.md) command.

<a id="dom"></a>
## Market Depth structure (#dom)

This structure describes the full information about a tick. It contains the following parameters:

Field | Type | Description  
Symbol | String | Symbol name.  
datetime | Integer | Date and time of the last Market Depth change in seconds elapsed since 01.01.1970.  
flags | Integer | Market Depth flags. Flags are passed using the [EnBookFlags (#enbookflags)](../../../Structures/MTBookMTBookDiff.md#enbookflags) enumeration.  
items | Integer | An array of elements of Market Depth changes.  
  
<a id="dom-item"></a>
## Market Depth element structure (#dom-item)

This structure describes the full information about a tick. It contains the following parameters:

Field | Type | Description  
type | Integer | The type of the record which is passed using the [EnBookItem (#enbookitem)](../../../Structures/MTBookItem.md#enbookitem) enumeration.  
price | Float | Order price.  
volume | Integer | Order volume.
