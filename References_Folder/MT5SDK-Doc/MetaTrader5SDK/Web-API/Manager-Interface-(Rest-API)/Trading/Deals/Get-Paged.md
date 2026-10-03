[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Deals](../Deals.md) / Get Paged

[Previous](Get-Total.md) | [Next](Get-Multiple.md)

# Getting Deals Page by Page

This request is used for obtaining deals performed by a client within a specified time range.

## Rest API

Request format
    
    
    GET /api/deal/get_page?login=login&from=date&to=date&offset=index&total=number
    POST /api/deal/get_page?login=login&from=date&to=date&offset=index&total=number

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
    GET /api/deal/get_page?login=1020&from=1546345925&to=1569933125&offset=0&total=3
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        { 
         "Deal" : "11918642",
         "ExternalID" : '',
         "Login" : "1020",
         ...
        },
        { 
         "Deal" : "11918643",
         "ExternalID" : "",
         "Login" : "1020",
         ...
        },
    ...
      ]
    }

## Raw API

Request format
    
    
    DEAL_GET_PAGE|LOGIN=login|FROM=date|TO=date|OFFSET=index|TOTAL=number\r\n

Response format
    
    
    DEAL_GET_PAGE|RETCODE=code description|\r\n
    Deal bodies in JSON format

## Request Parameters

  * login — the login of the client whose deals you need to obtain.
  * from — the beginning of the period for requesting deals. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — the end of the period for requesting deals. The date is specified in seconds that have elapsed since 01.01.1970.
  * offset — the index of the deal starting from which you need to obtain deals. Numbering starts with 0.
  * total — the number of deals that should be obtained. The maximum number of deals that can be requested in one command is 100.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — deal array in JSON format. The complete description of the passed order parameters is given in the ["Data structure"](Data-Structure.md) section.



## Note

This method allows to easily arrange a paged output of resulting deals. First you should get the total number of a client's deals using the [/api/deal/get_total](Get-Total.md) method. After defining the number of deals that should be shown on one page (set by the total parameter), you can easily find the offset parameter for each page.
