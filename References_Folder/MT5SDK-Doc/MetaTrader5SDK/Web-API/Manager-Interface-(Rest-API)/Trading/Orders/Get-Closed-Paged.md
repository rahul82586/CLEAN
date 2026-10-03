[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Get Closed Paged

[Previous](Get-Closed-Total.md) | [Next](Get-Multiple-Closed.md)

# Getting Closed Orders Page by Page

This request is used for obtaining orders from a client's history within a specified time range.

## Rest API

Request format
    
    
    GET /api/history/get_page?login=login&from=date&to=date&offset=index&total=number
    POST /api/history/get_page?login=login&from=date&to=date&offset=index&total=number

Response format
    
    
    {
     "retcode" : "code description",
      "answer" : [
       { description },
       { description },
       { description },
    ...
      ]
    }

Example
    
    
    //--- request to the server
    GET /api/history/get_page?login=1020&from=1546345925&to=1569933125&offset=0&total=3
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        { 
         "Order" : "12832917",
         "ExternalID" : "",
         "Login" : "1020",
         ...
        },
        { 
         "Order" : "12832918",
         "ExternalID" : "",
         "Login" : "1020",
         ...
        },
    ...
      ]
    }

## Raw API

Request format
    
    
    HISTORY_GET_PAGE|LOGIN=login|FROM=date|TO=date|OFFSET=index|TOTAL=number\r\n

Response format
    
    
    HISTORY_GET_PAGE|RETCODE=code description|\r\n
    Order bodies in JSON format

## Request Parameters

  * login — the login of the client whose orders you need to obtain.
  * from — the beginning of the period for requesting orders. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — the end of the period for requesting orders. The date is specified in seconds that have elapsed since 01.01.1970.
  * offset — the index of the order starting from which you need to obtain orders. Numbering starts with 0.
  * total — the number of orders that should be obtained. The maximum number of orders that can be requested in one command is 100.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — order array in JSON format. The complete description of the passed order parameters is given in the ["Data structure"](Data-Structure.md) section.



## Note

This method allows to easily arrange a paged output of resulting orders. First you should get the total number of a client's orders using the [/api/history/get_total](Get-Closed-Total.md) method. After defining the number of orders that should be shown on one page (set by the total parameter), you can easily find the offset parameter for each page.
