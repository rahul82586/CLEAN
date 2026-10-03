[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Trade Requests](../Trade-Requests.md) / Calculate Conversion Rate for Buy

[Previous](DepositWithdrawal.md) | [Next](Calculate-Conversion-Rate-for-Sell.md)

# Calculate Conversion Rate to Buy Currency

The request allows calculating the conversion rate when buying one currency for another in accordance with the account group settings.

## Rest API

Request Format
    
    
    GET /api/trade/calc_rate_buy?base=currency&currency=currency&group=group&symbol=symbol&price=price
    POST /api/trade/calc_rate_buy?base=currency&currency=currency&group=group&symbol=symbol&price=price

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Rate" : "rate" }
    }

The example
    
    
    //--- request to the server
    GET /api/trade/calc_rate_buy?base=EUR&currency=USD
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Rate" : "1.126760" }
    }

## Raw API

Request Format
    
    
    TRADE_RATE_BUY|BASE=currency|CURRENCY=currency|GROUP=group|SYMBOL=symbol|PRICE=price|\r\n

Response Format
    
    
    TRADE_RATE_BUY|RETCODE=code description|RATE=rate|\r\n

## Request Parameters

  * base — the name of the base currency (the one which is being purchased). Three-letter abbreviation for the currency, for example, EUR. Required parameter 
  * currency — the name of the currency, for which the other currency is purchased. Three-letter abbreviation for the currency, for example, USD. Required parameter 
  * group — the name of the client group for which the calculation is performed. If the group is specified, then the conversion rate is calculated using the market prices, taking into account spread [adjustment](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SpreadDiff.md) for this group. If a group is not specified, market prices are used.
  * symbol — the name of the symbol that should be taken into account when calculating the conversion rate. If a trading symbol with the name specified in the symbol parameter is used for calculating the conversion rate, then the 'price' price will be used as the price of this symbol. If the symbol parameter is not specified, current market prices of the symbol (including spread adjustment for this client group) will be used for conversion.
  * price — the price of the symbol specified in the symbol parameter, which will be used for conversion instead of the current market price.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * rate — the calculated conversion rate for buying the 'base' currency for the 'currency' currency.


