[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Daily Reports](../Daily-Reports.md) / Get

[Previous](Data-Structure.md) | [Next](Get-Light.md)

# Get Daily Reports

The request allows receiving daily reports by a date range and a login.

## Rest API

Request Format
    
    
    GET /api/daily_get?from=date&to=date&login=login
    POST /api/daily_get?from=date&to=date&login=login

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" :  
       { report description },
       { report description },
    ...
    }

The example
    
    
    //--- request to the server
    /api/daily_get?from=1585904106&to=1586768106&login=765114
    //--- server response
    {
       "retcode" : "0 Done",
       "answer" : 
         {
           "Timestamp" : "132302519992466852",
           "DatetimePrev" : "1585699199",
           "Login" : "765114",
           "Name" : "Test Collateral",
           "Group" : "demo\\demoforex-hedged",
           "Currency" : "USD",
           "CurrencyDigits" : "2",
           "Company" : "MetaQuotes DEV",
           "EMail" : "",
           "Balance" : "10010.31",
           "Credit" : "0.00",
           "InterestRate" : "0.00",
           "CommissionDaily" : "0.00",
           "CommissionMonthly" : "0.00",
           "AgentDaily" : "0.00",
           ...
         },
         {
           "Timestamp" : "132303383992178046",
           "DatetimePrev" : "1585785599",
           "Login" : "765114",
           "Name" : "Test Collateral",
           "Group" : "demo\\demoforex-hedged",
           "Currency" : "USD",
           "CurrencyDigits" : "2",
           "Company" : "MetaQuotes DEV",
           "EMail" : "",
           "Balance" : "10010.31",
           "Credit" : "0.00",
           "InterestRate" : "0.00",
           "CommissionDaily" : "0.00",
           "CommissionMonthly" : "0.00",
           "AgentDaily" : "0.00",
           ...
         },
         ...
    }

## Raw API

Request Format
    
    
    DAILY_GET|FROM=date|TO=date|LOGIN=login|\r\n

Response Format
    
    
    DAILY_GET|RETCODE=code description|\r\n
    Description of daily reports in JSON format

## Request Parameters

  * login — client login for which you wish to receive daily reports.
  * from — the beginning of the period for requesting reports. The date is specified in seconds that have since 01.01.1970.
  * from — the end of the period for requesting reports. The date is specified in seconds that have since 01.01.1970.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — an array of daily reports in JSON format. The complete description of the passed data is given in the ["Data structure"](Data-Structure.md) section.


