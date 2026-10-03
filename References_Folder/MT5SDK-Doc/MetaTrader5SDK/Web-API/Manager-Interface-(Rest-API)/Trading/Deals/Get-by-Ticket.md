[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Deals](../Deals.md) / Get by Ticket

[Previous](Data-Structure.md) | [Next](Get-Total.md)

# Getting a Deal by Ticket

This request allows to receive a deal by its ticket.

## Rest API

Request format
    
    
    GET /api/deal/get?ticket=ticket
    POST /api/deal/get?ticket=ticket

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/deal/get?ticket=13761310
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Deal" : "13761310",
        "ExternalID" : "",
        "Login": "937718",
        "Dealer": "0",
        "Order": "14837694",
        "Action": "1",
        "Entry": "0",
        "Reason": "16",
    ...
    }

## Raw API

Request format
    
    
    DEAL_GET|TICKET=ticket|\r\n

Response format
    
    
    DEAL_GET|RETCODE=code description|\r\n
    Deal body in JSON format

## Request Parameters

  * ticket — the ticket of the deal that you need to get.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — deal parameters in JSON format. The complete description of the passed deal parameters is given in the ["Data structure"](Data-Structure.md) section.


