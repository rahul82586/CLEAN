[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Prices](../Prices.md) / Get Market Depth

[Previous](Get-M1-History.md) | [Next](../Daily-Reports.md)

# Get Depth of Market

The request allows receiving data from a symbol's Market Depth.

Request Format
    
    
    GET /api/book/get?symbol=symbols
    POST /api/book/get?symbol=symbols

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [ 
       { Market Depth description },
       { Market Depth description },
        ...
      ]
    }

The example
    
    
    //--- request to the server
    /api/book/get?symbol=EURUSD
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        {
          "Symbol": "EURUSD",
          "Datetime": 1586804133000,
          "Flags": 1,
          "Items": [
            { "Type": 1, "Price": 1.091460, "Volume": 1000 },
            { "Type": 2, "Price": 1.091370, "Volume": 1000 }
          ]
        }
      ]
    }

## Raw API

The command is not supported.

## Request Parameters

  * symbol — the symbol for which you want to receive Market Depth data. You can specify multiple symbols separated by commas or groups of symbols using the "*" mask and the negation sign "!". For example:


  * symbol=EURUSD,USDJPY — get quotes for symbols EURUSD and USDJPY.
  * symbol=Forex\Major*, GOLD — get quotes of all symbols from the Major subgroup and quotes of GOLD.
  * symbol=Forex\Crosses*,!AUDUSD — get quotes of all symbols of the Crosses subgroup except AUDUSD.
  * symbol=Forex\Major\EUR* — get quotes of all symbols with the basic currency EUR from the Major subgroup.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of Market Depth prices. The description of the passed parameters is given in the ["Data structure" (#dom)](Data-Structure.md#dom) section.



## Response Parameters

Market Depth data can only be obtained for the symbols which are available to the account.

Code "1 OK/None" means that the required data does not exist in the access server, and more time is needed to receive the data from the history server. In this case, you should repeat the request later, after the data from the history server is uploaded to the access server.
