[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Prices](../Prices.md) / Get Quotes by Group

[Previous](Get-Quotes.md) | [Next](Get-Statistics.md)

# Getting Quotes by Group

This request is used for getting the current quotes of a symbol taking into account conversion for this group.

## Rest API

Request format
    
    
    GET /api/tick/last_group?symbol=symbols&group=group&trans_id=id
    POST /api/tick/last_group?symbol=symbols&group=group&trans_id=id

Response format
    
    
    {
     "retcode" : "code description",
     "trans_id" : "id",
      "answer" : [ 
       { symbol quotes description },
       { symbol quotes description },
    ...
    }

Example
    
    
    //--- request to the server
    /api/tick/last_group?symbol=EURUSD,GBPUSD&group=demoforex&trans_id=0
    //--- server response
    {
       "retcode" : "0 Done",
       "trans_id" : "8116395",
       "answer" : [
         {
          "Symbol" : "EURUSD",
          "Digits" : "5",
          "Datetime" : "1573048380",
          "DatetimeMsc" : "1573048380097",
          "Bid" : "1.10868",
          "Ask" : "1.10871",
          "Last" : "0.00000",
          "Volume" : "0",
          "VolumeReal" : "0.00"
         },
         {
          "Symbol" : "GBPUSD",
          "Digits" : "5",
          "Datetime" : "1573048380",
          "DatetimeMsc" : "1573048380098",
          "Bid" : "1.28850",
          "Ask" : "1.28858",
          "Last" : "0.00000",
          "Volume" : "0",
          "VolumeReal" : "0.00"
         }
      ]
    }

## Raw API

Request format
    
    
    TICK_LAST_GROUP|SYMBOL=symbols|GROUP=group|TRANS_ID=id|\r\n

Response format
    
    
    TICK_LAST_GROUP|RETCODE=code description|TRANDS_ID=id|\r\n
    Price description body in JSON format

## Request Parameters

  * symbol — comma separated symbols for which you need to get prices. You may use the mask "*" to specify groups of symbols. Example:


  * symbol=EURUSD,USDJPY — get quotes of EURUSD and USDJPY.
  * symbol=Forex\Major*, GOLD — get quotes of all symbols from the Major subgroup and quotes of GOLD.
  * symbol=Forex\Crosses*,!AUDUSD — get quotes of all symbols of the Crosses subgroup except AUDUSD.
  * symbol=Forex\Major\EUR* — get quotes of all symbols with the basic currency EUR from the Major subgroup.
  * group — groups in accordance with which the price is converted.
  * trans_id — transaction identifier. During the first request 0 is specified, which means the first request of data. In this case the server passes all the information. In the response command, the server returns the TRANS_ID identifier, which corresponds to the data passed. During the next request of prices with this ID, the server will return only the data that have changed since the previous request. Such a system allows to cut the network traffic when broadcasting prices.



  * A mask can be used only when specifying the full path to a symbol or group. For example, you can't specify "USD*", the correct variant is "Forex\Major\USD*".
  * You can omit specification of the path to a symbol only if you enter its full name. For example, USDCAD.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * trans_id — the ID of sent price data for further request of changes.
  * answer — price arrays by symbols in JSON format. The complete description of the passed prices is given in the ["Data structure"](Data-Structure.md) section.


