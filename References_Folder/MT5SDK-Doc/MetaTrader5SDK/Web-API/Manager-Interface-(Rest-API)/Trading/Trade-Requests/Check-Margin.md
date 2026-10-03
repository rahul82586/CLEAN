[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Trade Requests](../Trade-Requests.md) / Check Margin

[Previous](Calculate-Conversion-Rate-for-Sell.md) | [Next](Calculate-Profit.md)

# Check Margin for the Order

This request allows checking the availability of margin required for the execution of this order.

## Rest API

Request Format
    
    
    GET /api/trade/check_margin?login=login&symbol=symbol&type=operation&volume=volume&price=price
    POST /api/trade/check_margin?login=login&symbol=symbol&type=operation&volume=volume&price=price

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : {
        "new": {
         "Login": "login",
          ...
        },
        {  
        "current": {
         "Login": "login",
          ...
        }
      }
    }

The example
    
    
    //--- request to the server
    GET /api/trade/check_margin?login=3018855&symbol=EURUSD&type=1&volume=100000&price=1.27780
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "new": {
          "Login" : "3018855",
          "CurrencyDigits" : "2",
          "Balance" : "100000.00",
          "Credit" : "0.00",
          "Margin" : "0.88",
          "MarginFree" : "99999.12",
          "MarginLevel" : "11363636.36",
          ...
        },
        {  
        "current": {
          "Login" : "3018855",
          "CurrencyDigits" : "2",
          "Balance" : "100000.00",
          "Credit" : "0.00",
          "Margin" : "0.00",
          "MarginFree" : "100000.00",
          "MarginLevel" : "0.00",
          ...
        }
      }
    }

## Raw API

Request Format
    
    
    TRADE_MARGIN_CHECK|LOGIN=login|SYMBOL=symbol|TYPE=operation|VOLUME=volume|PRICE=price|\r\n

Response Format
    
    
    TRADE_MARGIN_CHECK|RETCODE=code description|\r\n
    Description of the account state after the operation execution and before the operation execution in the JSON format

## Request Parameters

  * login — the login of the account for which the order is executed.
  * symbol — the name of the trading symbol for which the order is executed.
  * type — trading order type:


  * 0 — Buy
  * 1 — Sell
  * 2 — Buy Limit
  * 3 — Sell Limit
  * 4 — Buy Stop
  * 5 — Sell Stop
  * 6 — Buy Stop Limit
  * 7 — Sell Stop Limit
  * 8 — Close By
  * volume — the volume of the trading orders, one unit correspond to 1/100000000 lots. The final order size is calculated based on the current [contract size](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ContractSize.md) for the specified trading instrument.
  * price — trading order execution type.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * new — trading account state after the execution of the specified order.
  * current — trading account state before the execution of the specified order.



## Note

The check is performed taking into account the current state of the [client account](../../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) (balance, credit, floating profit, open orders and positions, etc.) and using the current market prices for the [group](../../../../Configuration-Interfaces/Groups.md) of the client.
