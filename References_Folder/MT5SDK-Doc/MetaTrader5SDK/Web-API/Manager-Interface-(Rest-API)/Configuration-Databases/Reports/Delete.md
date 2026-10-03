[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Delete

[Previous](Add.md) | [Next](Shift.md)

# Delete Report

The request allows deleting report configurations from the trading platform.

## Rest API

Request Format
    
    
    GET /api/report/delete?server=identifier&name=names
    POST /api/report/delete?server=identifier&name=names

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    GET /api/report/delete?server=1&name=Daily%20Trades
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    REPORT_DELETE|SERVER=identifier|NAME=names\r\n

Response Format
    
    
    REPORT_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * server — the identifier of the server from which the report configuration should be deleted.
  * name — the name of the configuration to be deleted. Multiple indices can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit report configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.


