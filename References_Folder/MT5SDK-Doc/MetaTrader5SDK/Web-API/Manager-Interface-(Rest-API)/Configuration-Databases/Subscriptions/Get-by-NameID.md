[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / Get by NameID

[Previous](Get-by-Index.md) | [Next](../../Trading.md)

# Get a subscription configuration by name/ID.

The request enables the obtaining of subscription configurations by a list of IDs or indexes, as well as by name.

## Rest API

Request Format
    
    
    GET /api/subscription/config/get?index=indices
    GET /api/subscription/config/get?id=identifiers
    GET /api/subscription/config/get?name=name
     
    POST /api/subscription/config/get?index=indices
    POST /api/subscription/config/get?id=identifiers
    POST /api/subscription/config/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/subscription/config/get?name=US%20Mutual%20Funds
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
    
    
    SUBSCRIPTION_CFG_GET|INDEX=index\r\n
    SUBSCRIPTION_CFG_GET|ID=identifier\r\n
    SUBSCRIPTION_CFG_GET|NAME=name\r\n

Response Format
    
    
    SUBSCRIPTION_CFG_GET|RETCODE=code description|\r\n
    Server configuration body in JSON format

## Request Parameters

  * index — subscription configuration index starting with 0. Multiple indices can be specified as separated by commas.
  * id — subscription configuration identifier. Multiple indices can be specified as separated by commas.
  * name — subscription configuration name. Multiple names can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent group is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — subscription configuration in the JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.



## Note

Only one of the parameters can be specified in a request, i.e. id, index or name. Indication of multiple lists is not allowed.
