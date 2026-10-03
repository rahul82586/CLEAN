[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Get Closed by Ticket

[Previous](Move-to-History.md) | [Next](Get-Closed-Total.md)

# Getting a Closed Order by Ticket

This request allows to get an order from the history by a ticket.

## Rest API

Request format
    
    
    GET /api/history/get?ticket=ticket
    POST /api/history/get?ticket=ticket

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/history/get?ticket=12832917
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Order" : "12832917",
        "ExternalID" : "",
        "Login" : "938252",
        "Dealer" : "0",
        "Symbol" : "AUDCAD",
        "Digits" : "5",
        "DigitsCurrency" : "2",
        "ContractSize" : "100000.00",
        "State" : "1",
        "Reason" : "0",
    ...
    }

## Raw API

Request format
    
    
    HISTORY_GET|TICKET=ticket|\r\n

Response format
    
    
    HISTORY_GET|RETCODE=code description|\r\n
    Order body in JSON format

## Request Parameters

  * ticket — the ticket of the order that you need to get.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — order parameters in JSON format. The complete description of the passed order parameters is given in the ["Data structure"](Data-Structure.md) section.


