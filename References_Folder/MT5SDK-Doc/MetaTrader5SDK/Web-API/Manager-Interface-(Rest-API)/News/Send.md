[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [News](../News.md) / Send

[Previous](Data-Structure.md) | [Next](Get-Without-Body.md)

# Sending the news

This request is used for sending news to clients via the internal system of the platform.

## Rest API

Request format
    
    
    POST /api/news/send?subject=header&category=category&language=language&priority=priority
    { news text }

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    POST /api/news/send?subject=Price%20Alert&category=Technical%20Analysis&language=0&priority=0
    \<html\>\<body\>EURUSD reached 1.12399\<\/body\>\<\/html\>
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    NEWS_SEND|SUBJECT=header|CATEGORY=category|LANGUAGE=language|PRIORITY=priority\r\n
    { news text }

Response format
    
    
    NEWS_SEND|RETCODE=xxxx yyyy|\r\n

## Request Parameters

  * subject — news subject.
  * category — the category the news belongs to. To specify a subcategory use a backlash "\". For example, "Economy\World".
  * language — the language in the LANGID format used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (value from Prim.lang.identifier). The zero value means that the news has no language binding.
  * priority — priority of the news. 0 — normal news, 1 — high-priority news.



The news body is passed as an additional body of the request command in the Unicode format. You may use HTML to format news.

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.


