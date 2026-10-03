[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Trade Requests](../Trade-Requests.md) / Calculate Profit

[Previous](Check-Margin.md) | [Next](Send-Request.md)

# Calculate Profit for a Position

The request allows calculating profit to be received after closing the position under the specified conditions.

## Rest API

Request Format
    
    
    GET /api/trade/calc_profit?group=group&symbol=symbol&type=operation&volume=volume&price_open=open price&price_close=close price
    POST /api/trade/calc_profit?group=group&symbol=symbol&type=operation&volume=volume&price_open=open price&price_close=close price

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : {
       "Profit" : "profit",
       "Profit_rate" : "profit conversion rate"
      }
    }

The example
    
    
    //--- request to the server
    GET /api/trade/calc_profit?group=demoforex&symbol=EURUSD&type=0&volume=10000000&price_open=1.11500&price_close=1.12500
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Profit" : "77.750000",
        "Profit_rate" : "0.777508"
      }
    }

## Raw API

Request Format
    
    
    TRADE_PROFIT|GROUP=group|SYMBOL=symbol|TYPE=operation|VOLUME=volume|PRICE_OPEN=open price|PRICE_CLOSE=close price|\r\n

Response Format
    
    
    TRADE_PROFIT|RETCODE=code description|PROFIT=profit|PROFIT_RATE=conversion rate|\r\n

## Request Parameters

  * group — the name of the account group for which the calculation is performed.
  * symbol — the name of the trading instrument for which the calculation is performed.
  * type — position direction: buying - 0, selling - 1.
  * volume — position volume, one unit correspond to 1/100000000 lots.
  * price_open — position open price.
  * price_close — position close price.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * profit — position profit in the [deposit currency](../../../../Configuration-Interfaces/Groups/IMTConGroup/Currency.md) of the specified group.
  * profit_rate — position profit conversion rate from the trading symbol [profit currency](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyProfit.md) to the group deposit currency.



## Note

  * Profit is converted from the profit currency of a trading instrument to the group deposit currency using the current market prices for the group.
  * The symbol involved in the calculation must be available to the group for which the calculation is performed.


