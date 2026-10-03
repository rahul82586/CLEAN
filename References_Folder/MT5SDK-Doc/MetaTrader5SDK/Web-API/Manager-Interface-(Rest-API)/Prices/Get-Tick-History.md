[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Prices](../Prices.md) / Get Tick History

[Previous](Get-Statistics.md) | [Next](Get-M1-History.md)

# Get Tick History

The request allows receiving the history of ticks.

## Rest API

Request Format
    
    
    GET /api/tick/history?symbol=symbol&from=date&to=date&data=data
    POST /api/tick/history?symbol=symbol&from=date&to=date&data=data

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [ 
        [ tick description ],
        [ tick description ],
        ...
      ]
    }

Example
    
    
    //--- request to the server
    /api/tick/history?symbol=EURUSD&from=1574351000&to=1574351349&data=dba
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        [1574351000393,1.10777,1.10780],
        [1574351001034,1.10775,1.10778],
        [1574351001229,1.10774,1.10778],
        [1574351001610,1.10774,1.10777],
        ...
      ]
    }

## Raw API

The command is not supported.

## Request Parameters

  * symbol — the symbol for which you want to receive tick data.
  * from — the beginning of the period for which you want to receive data. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — the end of the period for which you want to receive data. The date is specified in seconds that have elapsed since 01.01.1970.
  * data — data set to be received. It is specified as a string of letters, each of which corresponds to the requested data type:


  * d — tick date and time. The date is specified in seconds that have elapsed since 01.01.1970.
  * b — bid price.
  * a — ask price.
  * l — last deal price (last).
  * v — last deal volume.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of ticks. The data set depends in the "data" parameter in the request.



## Response Parameters

Each response is limited in size to 16 megabytes. If the response matching the query criteria is larger, the first 16 megabytes of the response will be returned, along with the response code "14 Operation has not been completed". In this case, the request should be repeated, using the date-time of the last row from the current result as the value of the "from" parameter for the new request. This operation should be repeated until the response code "0 Done" is received.

Code "1 OK/None" means that the required data does not exist in the access server, and more time is needed to receive the data from the history server. In this case, you should repeat the request later, after the data from the history server is uploaded to the access server.
