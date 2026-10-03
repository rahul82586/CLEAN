[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Trade Requests](../Trade-Requests.md) / Send Request

[Previous](Calculate-Profit.md) | [Next](Get-Request-Result.md)

# Send Trade Request

The request allows sending a trade request to a server on behalf of the dealer.

## Rest API

Request Format
    
    
    POST /api/dealer/send_request
    { Description of the trade request }

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : {
       "ID" : "request identifier"
      }
    }

The example
    
    
    //--- request to the server
    POST /api/dealer/send_request
    {
       "Action" : "200",
       "Login" : "1010",
       "Symbol" : "EURUSD",
       "Volume" : "100",
       "TypeFill" : "0",
       "Type" : "0",
       "PriceOrder" : "1.11850",
       "Digits" : "5"
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "ID" : "13992"
      }
    }

## Raw API

Request Format
    
    
    DEALER_SEND|\r\n

Response Format
    
    
    DEALER_SEND|RETCODE=code description|ID=identifier|\r\n

## Request Parameters

The request has no parameters. The request description is passed in JSON format as an additional body.

  * The full description of possible parameters is provided in the [Data structure](Data-Structure.md) section. 
  * Required fields are determined by request type. For details, please see the [appropriate section (#entradeactions)](../../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Enumerations.md#entradeactions).



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * id — trade request identifier in [/api/dealer/get_request_result](Get-Request-Result.md) for receiving request execution results.



## Note

  * For correct operations with prices, be sure to fill the "Digits" field in the request.
  * The response code 0 does not indicate the execution of the request. It indicates that the request has been verified and enqueued to be processed by the server.
  * Only [dealer actions (#entradeactions)](../../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Enumerations.md#entradeactions) (200-255) can be set as a request type (Action field).
  * A trade request execution result can be obtained via [/api/dealer/get_request_result](Get-Request-Result.md).
  * Up to 128 trade requests can be enqueued at the same time. If this limit is exceeded, the server returns the error [10024](../../../../Return-Codes/Trade-Requests.md).
  * After each call of /api/dealer/send_request, a [subscription to events (#subscription)](Get-Request-Result.md#subscription) related to the execution of this request is created automatically.


