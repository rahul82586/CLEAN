[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Prices](../Prices.md) / Get Statistics

[Previous](Get-Quotes-by-Group.md) | [Next](Get-Tick-History.md)

# Getting Price Statistics

This request allows to receive statistical data on the current symbol prices.

## Rest API

Request format
    
    
    GET /api/tick/stat?symbol=symbols&trans_id=id
    POST /api/tick/stat?symbol=symbols&trans_id=id

Response format
    
    
    {
     "retcode" : "code description",
     "trans_id" : "id",
      "answer" : [ 
       { statistics description },
       { statistics description },
    ...
    }

Example
    
    
    //--- request to the server
    /api/tick/last?symbol=EURUSD,GBPUSD&trans_id=0
    //--- server response
    {
       "retcode" : "0 Done",
       "trans_id" : "8116395",
       "answer" : [
         {
           "Symbol" : "EURUSD",
           "Digits" : "5",
           "Datetime" : "0",
           "DatetimeMsc" : "0",
           "Bid" : "1.10819",
           "BidLow" : "1.10666",
           "BidHigh" : "1.10927",
           "BidDir" : "0",
           "Ask" : "1.10822",
          ...
         },
         {
           "Symbol" : "GBPUSD",
           "Digits" : "5",
           "Datetime" : "0",
           "DatetimeMsc" : "0",
           "Bid" : "1.28748",
           "BidLow" : "1.28687",
           "BidHigh" : "1.28968",
           "BidDir" : "0",
           "Ask" : "1.28758",
         ...
         }
      ]
    }

## Raw API

Request format
    
    
    TICK_STAT|SYMBOL=symbols|TRANS_ID=id|\r\n

Response format
    
    
    TICK_STAT|RETCODE=code description|TRANDS_ID=id|\r\n
    Price description body in JSON format

## Request Parameters

  * symbol — comma separated symbols, the prices of which should be received. You may use the mask "*" and the negation sign "!" to specify groups of symbols. Example:


  * symbol=EURUSD,USDJPY — get quotes of EURUSD and USDJPY.
  * symbol=Forex\Major*, GOLD — get quotes of all symbols from the Major subgroup and quotes of GOLD.
  * symbol=Forex\Crosses*,!AUDUSD — get quotes of all symbols of the Crosses subgroup except AUDUSD.
  * symbol=Forex\Major\EUR* — get quotes of all symbols with the basic currency EUR from the Major subgroup.
  * trans_id — transaction identifier. During the first request 0 is specified, which means the first request of data. In this case the server passes all the information. In the response command, the server returns the TRANS_ID identifier, which corresponds to the data passed. During the next request of prices with this ID, the server will return only the data that have changed since the previous request. Such a system allows to cut the network traffic when broadcasting prices.



  * A mask can be used only when specifying the full path to a symbol or group. For example, you can't specify "USD*", the correct variant is "Forex\Major\USD*".
  * You can omit specification of the path to a symbol only if you enter its full name. For example, USDCAD.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * trans_id — the ID of sent statistical data for further request of changes.
  * answer — array of statistical data by symbols in JSON format. The complete description of the passed statistical data is given in the ["Data structure" (#stat)](Data-Structure.md#stat) section.


