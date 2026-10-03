[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Get Multiple Open

[Previous](Get-Open-Paged.md) | [Next](Update-Open.md)

# Get Multiple Open Orders

The request allows receiving information related to multiple open orders, based on a list of logins, tickets or groups.

## Rest API

Request Format
    
    
    GET /api/order/get_batch?login=logins&group=groups&ticket=tickets&symbol=symbol
    POST /api/order/get_batch?login=logins&group=groups&ticket=tickets&symbol=symbol
    POST /api/order/get_batch?symbol=symbol
    {
      "ticket": [
        1012,
        4034
      ],
      "group": [
        demoforex-eur,
        demoforex-usd
      ],
      "ticket": [
        96639,
        13549
      ],
    }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ description of orders ]
    }

Example
    
    
    //--- request to the server
    GET /api/order/get_batch?ticket=12832917,12832918
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

Request Format
    
    
    ORDER_GET_BATCH|LOGIN=logins|GROUP=groups|TICKET=tickets|\r\n

Response Format
    
    
    ORDER_GET_BATCH|RETCODE=code description|\r\n
    An array of orders in JSON format

## Request Parameters

  * login — list of logins, the orders of which you want to receive. A commas separated list. Logins can also be specified as an array in the POST request body.
  * group — the list of groups, for users from which you want to receive orders. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex. Groups can also be specified as an array in the POST request body.
  * ticket — the list of order tickets to receive. Tickets can be specified as an array in the POST request body.
  * symbol — the symbol orders for which you are requesting. You can specify multiple symbols separated by commas. Only makes sense when used together with the 'login' or 'group' parameter.



> Operations can be requested with only one parameter: by logins, by groups, or by tickets. You cannot specify all the three parameters together.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — order array in JSON format. The complete description of the passed order parameters is given in the ["Data structure"](Data-Structure.md) section.


