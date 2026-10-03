[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [News](../News.md) / Get With Body

[Previous](Get-Without-Body.md) | [Next](../Prices.md)

# Get the full news description

The request allows receiving the full news description, including its body.

## Rest API

Request Format
    
    
    GET /api/news/get_body?id=news_identifiers

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [
       { news description },
       { news description },
        ...
      ]
    }

The example
    
    
    //--- request to the server
    POST /api/news/get_body?id=496341,496342
    //--- server response
    {
       "retcode" : "0 Done",
       "answer": [
         {
            "Info" : {        
              "ID" : "496341",
              "Size" : "0",
              "Time" : "1565797554",
              "Language" : "9",
              "Category" : "Technical analysis",
              "Subject" : "EURUSD forecast for next week"
           },
           "Body": "PAAhAEQATwB...ADAANQAvAGgA"
         },
         {
            "Info" : {
              "ID" : "496342",
              "Size" : "0",
              "Time" : "1565797556",
              "Language" : "9",
              "Category" : "Macroeconomic indicators",
              "Subject" : "3Q employment rate published"
           },
           "Body": "PAAhAEQATwBDAFQAW...BjAG8AbgB0AGUAbgB0"
         }     
      ]
    }

## Raw API

The command is not supported.

## Request Parameters

  * id — one or more news identifiers separated by commas. Required parameter. Use the [/api/news/get](Get-Without-Body.md) request to get identifiers.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — an array of news in JSON format. The complete description of the passed data is given in the ["Data structure"](Data-Structure.md) section.


