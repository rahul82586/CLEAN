[🏠 Document Start](../../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../../../Platform-Setup.md) / [Symbols](../../../Symbols.md) / [Symbol Settings](../../Symbol-Settings.md) / [Trade](../Trade.md) / Profit Calculation

[Previous](Margin-Calculation/Stock-Exchange.md) | [Next](Conversion.md)

<a id="profit-calculation"></a>
# Profit Calculation (#profit-calculation)

Profit calculations differ for different types of trade instruments. The final amount of profit is calculated in two stages:

  * The main calculation for a symbol;
  * Conversion of a profit currency to the deposit currency.



<a id="main"></a>
## The main calculation for a symbol (#main)

The trading platform provides five types of profit calculation, which depend on the financial instrument. The calculation type is selected in the ["Calculation" (#calculation)](../Trade.md#calculation) of the "Trade" tab. When using calculation formulas, please consider the following features:

  * Mathematical rounding is used when calculating the profit. The calculated value is rounded to the number of decimal places in the price of the financial instrument. In the formulas given below the rounding is denoted as Normalize() function.


  * On [netting accounts (#netting)](../../../Groups/Position-Accounting-Systems.md#netting), the position opening price is equal to the [weighted average price (#open-price)](../../../Positions.md#open-price).



<a id="forex"></a>
### Forex (#forex)

Profit of Buy trades (execution of operations opposite to them) for Forex symbols is calculated by the following formula:

Normalize(Close Price * Contract Size * Volume in Lots) — Normalize(Open Price * Contract Size * Volume in Lots)

For Sell trades, open and close price change over in the formula:

Normalize(Open Price * Contract Size * Volume in Lots) — Normalize(Close Price * Contract Size * Volume in Lots)

Let's consider closing of 1 EURUSD lot Buy position. The position was opened at the price of 1.2000; by the moment of closing the price is equal to 1.2050; the contract size is 100,000. Substitute the values to the formula:

(1.2050 * 100 000 * 1) — (1.2000 * 100 000 * 1) = 500 USD

As a result we obtain the profit size in the symbol [profit currency (#base-currency)](../Currency.md#base-currency).

<a id="cfd-cfd-index-cfd-leverage-exchange-stocks-exchange-moex-stocks"></a>
### CFD, CFD Index, CFD Leverage, Exchange Stocks, Exchange MOEX Stocks (#cfd-cfd-index-cfd-leverage-exchange-stocks-exchange-moex-stocks)

Profit of Buy trades (execution of operations opposite to them) for CFD and Stocks symbols is calculated by the following formula:

Normalize((Close Price — Open Price) * Contract Size * Volume in Lots)

For Sell trades, open and close price change over in the formula:

Normalize((Open Price — Close Price) * Contract Size * Volume in Lots)

Let's consider closing of 1 EURUSD lot Buy position. The position was opened at the price of 1.2000; by the moment of closing the price is equal to 1.2050; the contract size is 100,000. Substitute the values to the formula:

(1.2050 — 1.2000) * 100,000 * 1 = 500 USD

As a result we obtain the profit size in the symbol [profit currency (#base-currency)](../Currency.md#base-currency).

<a id="futures"></a>
### Futures, Exchange Futures, FORTS Futures, Exchange Options, Exchange Margin Options (#futures)

Profit on Futures Buy trades is calculated by the following formula:

Normalize((Close Price — Open Price) * Volume in Lots * Tick Value / Tick Size)

For Sell trades, open and close price change over in the formula:

Normalize((Open Price — Close Price) * Volume in Lots * Tick Value / Tick Size)

Calculation of the profit on Futures trades also takes into account the ratio of the [value (#tick-price)](../Trade.md#tick-price) and [size (#tick-size)](../Trade.md#tick-size) of one tick.

<a id="bonds"></a>
### Exchange Bonds, Exchange MOEX Bonds (#bonds)

The profit is calculated as the difference between the prices of a position at the time of opening and closing. Position price is defined as follows:

Price/100 * Face value * Volume in lots * Contract size + Accrued interest * Volume in lots * Contract size

The price is divided by 100 since bond prices are passed as a face value percentage.

The current floating profit at bonds is calculated without an accrued interest:

(Current Price - Open Price)/100 * Face value * Volume in lots * Contract size

  * Accrued interest history is not stored in the platform, it is accounted by the exchange when processing deals.


  * The position value is calculated in the [symbol's base currency (#base-currency)](../Currency.md#base-currency) (not in the profit currency).

  
---  
  
<a id="collateral"></a>
### Collateral (#collateral)

Non-tradable instruments of this type are used as client's [assets to provide the required margin for open positions (#collateral)](../../../Accounts/Editing-Account.md#collateral) of other instruments. For these instruments the profit is not calculated.

<a id="conversion"></a>
## Conversion to the Deposit Currency (#conversion)

The stage of the calculated profit conversion appears if the profit currency differs from the [deposit currency (#currency)](../../../Groups/Group-Settings.md#currency) of the account.

For details, please visit the [Conversion](Conversion.md) section.

<a id="all-types-of-symbols-except-forex"></a>
### All Types of Symbols Except Forex (#all-types-of-symbols-except-forex)

The conversion process slightly differs for profitable and losing trades.

  * Profitable deals — the conversion is performed at the current rate of the profit currency to the deposit currency. The Bid price is taken for calculations, because as a result of a profitable deal, a trader obtains a certain amount of the profit currency and needs to sell it for the deposit currency.
  * Losing deals — The conversion is also performed at the current rate of the profit currency to the deposit currency. However, in this case the Ask price is taken, because as a result of a losing deal, a trader needs to buy a certain amount of currency for the deposit currency.



<a id="forex"></a>
### Forex (#forex)

For the Forex symbol, the conversion type can be selected using the ["Convert profit" (#convert)](../Trade.md#convert) option on the "Trade" tab.

By deal

This is a default mode for Forex symbols. To convert a profit when closing a position, the system uses the prices of the XXXYYY currency pair, where XXX is a trade profit currency, while YYY is a client deposit currency. The Ask price is used when closing buy positions and the Bid price is used when closing sell positions. It does not matter whether the position that is being closed is profitable or not. If possible, the price, at which the market exit has been performed, is used during the conversion (provided that the appropriate currency pair takes part in the conversion).

For example, a customer with a USD deposit currency closed the buy USDCHF position. In this case, the platform should apply the Ask price of the CHFUSD pair. Since there is only a reverse rate (USDCHF), the platform calculates the desired price the following way: Ask CHFUSD = 1/Bid USDCHF. Here, the price, at which the position was actually closed, is used as Bid USDCHF.

If there is no direct exchange rate between profit and deposit currencies, the conversion is performed via USD. For example, a customer with a TRY deposit currency performs a trade on USDRUR. Since there is no TRYRUR rate, the profit is converted via USDTRY.

By market

In this mode, the conversion is performed using the current Bid/Ask price depending of the profitability/unprofitability of a deal. The Bid price is taken for calculations for profitable deals, because as a result of a profitable deal, a trader obtains a certain amount of the profit currency and needs to sell it for the deposit currency. The Ask price is taken for losing deals, because as a result of a losing deal, a trader needs to buy a certain amount of currency for the deposit currency.

<a id="exchange"></a>
### Conversion features for Exchange-based settlement groups (#exchange)

In the [exchange model](Margin-Calculation/Stock-Exchange.md), the payment and receipt of assets (or the incurrence of liabilities in case of repurchase operations) occur immediately upon conclusion of the deal. The deal cost is immediately reflected in the client's balance. Accordingly, the profit currency is immediately converted into the deposit currency, both when entering and exiting a position.

Floating profits displayed in client terminals is calculated based on this feature. Let's consider the an example:

  1. Suppose you have a euro account (EUR). You buy shares that have US dollars (USD) as the profit currency.
  2. Upon completing a trade, the cost of the shares is immediately debited from your balance, and the shares become your asset.
  3. Since you do not have USD, you need to buy them with EUR to complete the trade. Therefore, the Ask price of the EURUSD pair at the time of opening the position is used for conversion.
  4. When closing a position, you will sell the shares for USD. To credit the funds to your balance, the cost of the shares must be converted into euros. This conversion will use the Bid price of the EURUSD pair at the time of closing the position.
  5. Thus, when calculating floating profit in the exchange mode, the profit currency is converted into the deposit currency at different rates at existing different points in time.



<a id="normalization"></a>
## Normalization (#normalization)

For all instruments except Forex, the total profit is mathematically rounded by the number of decimal places in a symbol profit currency. For Forex type symbols, a position price during closing and opening is normalized separately:

Buy trade profit = Normalize(Close price * Volume * Contract size, Digits) — Normalize(Open price * Volume * Contract size, Digits).

Sell trade profit = Normalize(Open price * Volume * Contract size, Digits) — Normalize(Close price * Volume * Contract size, Digits).

Here, Normalize is a mathematical rounding function. Its second argument (Digits) is the number of rounded decimal places, and it is equal to the number of digits after the decimal point in a symbol profit currency.
