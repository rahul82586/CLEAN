[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Common Requests](../Common-Requests.md) / Get Journal

[Previous](../Common-Requests.md) | [Next](../Text-Protocol-(Raw-API).md)

# Get trade server Journal

Get the Journal of the trade server to which the Web API application is connected.

## Rest API

Request Format
    
    
    GET /api/logger/server_request?mode=request mode&type=log type&from=date&to=date&filter=search string
     
    POST /api/logger/server_request?mode=request mode&type=log type&from=date&to=date&filter=search string

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : [ logs ]
      }
    }

Example
    
    
    //--- request to the server
    GET /api/logger/server_request?mode=0&type=0&from=1676894229&to=1676894230&filter=1068
    //--- server response
    {
      "retcode": "0 Done",
      "answer": [
        {
          "flags": "0",
          "code": "0",
          "type": "2",
          "datetime": "1676902504",
          "source": "192.168.0.1",
          "message": "'1068': server journal (192.145, 2023.02.20 - 2023.02.20)",
          "datetime_msc": "1676902504541"
        },
        {
          "flags": "0",
          "code": "0",
          "type": "2",
          "datetime": "1676902504",
          "source": "192.168.0.1",
          "message": "'1068': journal (time 125 ms, size: 0 kb)",
          "datetime_msc": "1676902504661"
        }
      ]
    }

## Raw API

Request Format
    
    
    LOGGER_SERVER_REQUEST|MODE=request mode|TYPE=log type|FROM=date|TO=date|FILTER=search string|\r\n

Response Format
    
    
    LOGGER_SERVER_REQUEST|RETCODE=code description|\r\n
    Array of server logs in the JSON format

## Request Parameters

  * mode — journal request mode. The mode is specified as a value of the [EnMTLogRequestMode (#enmtlogrequestmode)](../../../Journal-Constants/README.md#enmtlogrequestmode) enumeration. For example, 2 means all log types.
  * type — type of events that should be requested from the server journal. The type is specified as a value of the [EnMTLogType (#enmtlogtype)](../../../Journal-Constants/README.md#enmtlogtype) enumeration. For example, 0 means all event types.
  * from — the start date for requesting the logs. The date is specified in seconds since 01.01.1970. Only the date is taken into account, while the exact time is ignored.
  * to — the end date for requesting the logs. The date is specified in seconds since 01.01.1970. Only the date is taken into account, while the exact time is ignored.
  * filter — a keyword to search.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of log entries in the JSON format. The description of return fields is available in the [MTLogRecord](../../../Structures/MTLogRecord.md) section.


