[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Data Structure

[Previous](../Positions.md) | [Next](Get-by-Symbol.md)

# Data Structure

Data on positions is passed in JSON format as a response to the [/api/position/get](Get-by-Symbol.md) and [/api/position/get_page](Get-Paged.md) requests. Position information includes the following parameters:

Option Field | Type | Description  
Login | Integer | The login of the client, to whom the trade position belongs.  
Symbol | String | The symbol of a trade position.  
Action | Integer | Position type. Passed as a value of the [EnPositionAction (#enpositionaction)](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Enumerations.md#enpositionaction) enumeration.  
Digits | Integer | The number of decimal places in the price of a position.  
DigitsCurrency | Integer | The number of decimal places the deposit currency of the client who has opened the position.  
ContractSize | Float | The contract size of the symbol, for which a position is opened.  
Position | Integer | The ticket (unique identifier) of a trade position in a MetaTrader 5 platform.  
ExternalID | String | The position ticket (unique number) in an external trading system.  
TimeCreate | Integer | Time of position creation, in seconds that have elapsed since 01.01.1970.  
TimeUpdate | Integer | Time of the last modification of a position, in seconds that have elapsed since 01.01.1970. Position modification time is the time of its last volume modification. It is actually the time of the last deal of the financial instrument that corresponds to this position.  
TimeCreateMsc | Integer | The position creation time in milliseconds.  
TimeUpdateMsc | Integer | The time of the last modification of a trade position in milliseconds. Position modification time is the time of its last volume modification. It is actually the time of the last deal of the financial instrument that corresponds to this position.  
PriceOpen | Float | The weighted average open price of a position. Calculated by the following formula: (price of deal 1 * volume of deal 1 1 + ... + price of deal N * volume of deal N) / (volume of deal 1 + ... + volume of deal N).  
PriceCurrent | Float | The current price of the symbol, for which a trade position has been opened.  
PriceSL | Float | The Stop Loss level of a trade position.  
PriceTP | Float | The Take Profit level of a trade position.  
Volume | Integer | The volume of a trade position. One unit corresponds to 1/10000 lot.  
VolumeExt | Integer | The volume of a trade position with an extended accuracy. One unit corresponds to 1/100000000 lot.  
Profit | Float | The current profit/loss of a trade position.  
Storage | Float | The swap size for a position in deposit currency.  
RateProfit | Float | The exchange rate of the profit currency of a position to the deposit currency of a client group.  
RateMargin | Float | The exchange rate of the margin currency of a position to the client's deposit currency.  
ExpertID | Integer | The ID of the Expert Advisor that has opened the position.  
ExpertPositionID | Integer | Position ID.  
Comment | String | A comment to a position.  
Dealer | Integer | The login of a dealer, who has processed the order that opened the position.  
ActivationMode | Integer | Position activation type. Passed in a value of the [EnActivation (#enactivation)](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Enumerations.md#enactivation) enumeration.  
ActivationTime | Integer | Time of position activation, in seconds that have elapsed since 01.01.1970.  
ActivationPrice | Float | Position activation price.  
ActivationFlags | Integer | Position activation flags. Passed as a value of the [EnTradeActivationFlags (#entradeactivationflags)](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Enumerations.md#entradeactivationflags) enumeration (sum of values of appropriate flags).  
ModificationFlags | Integer | The position modification flags. Passed as a value of the [EnTradeModifyFlags (#entrademodifyflags)](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Enumerations.md#entrademodifyflags) enumeration (sum of values of appropriate flags). Deals that close a position or part of it inherit its modification flags. After closing, no separate entry about the position remains in the database. To prevent the information about modification from being lost, flags are copied to the deal that closes his position. At the same time, the additional EnTradeModifyFlags::MODIFY_FLAGS_POSITION modification flag is set for the deal meaning that the flags were inherited from the position.  
Reason | Integer | The reason for position opening. Passed as a value of the [EnPositionReason (#enpositionreason)](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Enumerations.md#enpositionreason) enumeration.
