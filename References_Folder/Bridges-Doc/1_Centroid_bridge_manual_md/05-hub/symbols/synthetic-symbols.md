[🏠 Document Start](..\..\README.md) / [Securities](..\README.md) / [Symbols](README.md) / Synthetic Symbols

# Synthetic Symbols

Overview
The Synthetic Symbols offer the ability to create and price new products by combining one or multiple Symbols as well as using complex
formulas to price the new Symbols. For instance, you can derive the price of Gold in KG out of the price of XAUUSD by setting a multiplier
of 32.15. Similarly, you can make an Exotic FX Symbol by combining two currency pairs. The Exotic Symbol starts at the level of the
Liquidity Model and follows the same flow other Symbols follow in terms of Markup Models which are applicable at the level of the Taker
(Feed and Execution).
Format and Usage
The two main used operators are division and multiplication involving source symbols and numbers and should be written as follows:
Division: @
Multiplication: *
Additionally, you may use a variety of formulas as follows:
SQRT– Square Root (1 parameter)
POW – Power (2 parameters) - POW(x^y)
AVG – Average (n parameters) - AVG(a,b,c,…)
SUM – Sum (n parameters) - SUM(a,b,c,…)
ABS – Absolute Value (1 parameter) – ABS(x)

All formulas need to be written between # # where b refers to the BID price and a to the ASK price, and can be applied differently as
follows:
1. One-sided formula: #b=x@y# This obtains the BID price by dividing x BID price by y BID price and does the same to the ASK price.
2. Two sided formula: #b=x*y#a=(x*y)+0.0001# This obtains the BID price by dividing x BID price by y BID price. As for the ASK price, it
divides x BID price by y BID price and adds 0.0001 to it.
3. In terms of formula: #b=x*y*z#a=_b_+0.05# This obtains the BID price by multiplying x and y and z. As for the ASK price, the _ _
indicates that the BID price of the calculated Synthetic Symbol is taken and 0.05 is getting added to it, hence we increase the ASK price by
0.05 ensuring that spread constantly stands at 0.05
Note: x, y, and z in the above example are the source symbols.
Examples
1. Create XAGGBP Synthetic Symbol: This is done by simply creating the Synthetic Symbol XAGGBP as a Universal Symbol and then
combining Symbols XAGUSD and GBPUSD where XAGUSD is divided by GBPUSD, by writing the formula in the description as follows:
In the above example, we only applied the formula on the BID price which automatically simulates the same behavior on the ASK price.
Once the formula has been written in the correct format and saved, the newly added symbol will start pricing instantly.


2. Create GOLD_KG Synthetic Symbol:
This is done by simply creating the Synthetic Symbol GOLD_KG as a Universal Symbol and then multiplying the source symbol XAUUSD
by 32.15.
In the above example, we obtained the BID price by multiplying the BID price of the source symbol XAUUSD by 32.15 to convert from troy
ounce to Kilo. As for the ASK price, we just used the same BID price we got and added 0.3 which fixed the spread at 0.3.
Notes:
Synthetic Symbols can be used only for pricing and B Book execution at this stage
You may increase the default volume of the Synthetic Symbols by using the Book Construction feature at the level of the Liquidity
Model


