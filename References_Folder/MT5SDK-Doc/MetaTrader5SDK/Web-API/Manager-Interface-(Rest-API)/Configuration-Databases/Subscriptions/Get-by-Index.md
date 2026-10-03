[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-NameID.md)

# Get a subscription configuration by index

Get one or more subscription configurations by index in the list.

## Rest API

Request Format
    
    
    GET /api/subscription/config/next?index=index&count=number
    POST /api/subscription/config/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/subscription/config/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "ID" : "132240227905103158",
        "ParentID" : "132240225640031925",
        "Type" : "0",
        "Name" : "US Mutual Funds",
        "URL" : "https:\/\/www.fundserv.com\/home\/#fundserv",
        "AgreementURL" : "",
        "Flags" : "3",
        "Control" : "0",
        "Image" : "1006",
        "ImageURL" : "",
        "Period" : "3",
        "PeriodCustom" : "0",
        "FreePeriod" : "0",
        "FreePeriodCustom" : "0",
        "Price" : "0.0000",
        "PriceCurrency" : "USD",
        "PriceProfessional" : "0.0000",
        "PriceCost" : "0.0000",
        "DependsID" : "0",
        "Description" : "<p>Provides <a href=\"https:\/\/www.investopedia.com\/terms\/n\/no-loadfund.asp\" target=\"_blank\">no-load mutual funds<\/a><\/p>",
        "Countries" : ["DZ", "AI", "AR"],
        "Groups" : ["preliminary"],
        "Symbols" : [
          {
            "Level" : "2",
            "Symbols" : "Forex\*",
            "TickHistory" : "10"
          } 
         ],
         "News" : [
           {
             "Category" : "Fnance",
             "Language" : "12"
           }
         ]
      }
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_CFG_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    SUBSCRIPTION_CFG_NEXT|RETCODE=code description|\r\n
    Server configuration body in JSON format

## Request Parameters

  * index — subscription configuration index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent group is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — subscription configuration in the JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.


