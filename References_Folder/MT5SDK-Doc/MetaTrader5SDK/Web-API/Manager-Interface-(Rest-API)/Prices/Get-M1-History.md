[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Prices](../Prices.md) / Get M1 History

[Previous](Get-Tick-History.md) | [Next](Get-Market-Depth.md)

# Get Bar History

The request allows receiving the history of bars (1-minute data).

## Rest API

Request Format
    
    
    GET /api/chart/get?symbol=symbol&from=date&to=date&data=data
    POST /api/chart/get?symbol=symbol&from=date&to=date&data=data

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [ 
       [ bar description ],
       [ bar description ],
        ...
      ]
    }

Example
    
    
    //--- request to the server
    /api/chart/get?symbol=EURUSD&from=1574351000&to=1574351349&data=dohlc
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        [1574351040,1.10779,1.10798,1.10778,1.10798],
        [1574351100,1.10798,1.10807,1.10790,1.10795],
        [1574351160,1.10795,1.10795,1.10775,1.10777],
        ...
      ]
    }

## Raw API

The command is not supported.

## Request Parameters

  * symbol — the symbol 1-minute data for which you want to receive.
  * from — the beginning of the period for which you want to receive data. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — the end of the period for which you want to receive data. The date is specified in seconds that have elapsed since 01.01.1970.
  * data — data set to be received. It is specified as a string of letters, each of which corresponds to the requested data type:


  * d — bar date and time. The date is specified in seconds that have elapsed since 01.01.1970.
  * o — opening. The price at the bar formation beginning (the beginning of the minute).
  * h — high. The highest price during the bar time.
  * l — low. The lowest price during the bar time.
  * c — closing. The price at the end of bar formation (the end of the minute).
  * t — tick volume. The number of ticks received during bar formation ().
  * v — real volume. The real volume of trades executed during bar formation.
  * s — spread. The lowest symbol spread recorded during the bar formation time.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of bars. The data set depends in the "data" parameter in the request.



## Response Parameters

Each response is limited in size to 16 megabytes. If the response matching the query criteria is larger, the first 16 megabytes of the response will be returned, along with the response code "14 Operation has not been completed". In this case, the request should be repeated, using the date-time of the last row from the current result as the value of the "from" parameter for the new request. This operation should be repeated until the response code "0 Done" is received.

Code "1 OK/None" means that the required data does not exist in the access server, and more time is needed to receive the data from the history server. In this case, you should repeat the request later, after the data from the history server is uploaded to the access server.
