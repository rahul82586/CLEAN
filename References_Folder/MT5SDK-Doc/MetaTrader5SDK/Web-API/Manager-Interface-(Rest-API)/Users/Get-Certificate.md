[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get Certificate

[Previous](Update-Certificate.md) | [Next](Delete-Certificate.md)

# Get User Certificate

The request allows receiving a user certificate.

## Rest API

Request format
    
    
    GET /api/user/certificate/get?login=login
    POST /api/user/certificate/get?login=login
    [array of logins and certificates]

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [certificate description in PEM format]
    }

Example
    
    
    //--- request to the server
    GET /api/user/certificate/get?login=61232
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        "-----BEGIN CERTIFICATE-----",
        "MIIClTC5AX2gAwIBAgIIF0mMFC+rOagwDQYJKoZIhvcNAQEFBQAwNzEcMBoGA1UE",
        "AxMTZGV2Lm1ldGF0cmFkZXI1LmRldjEXMBUGA1UEChMOTWV0YVF1b3RlcyBERVYw",
        "IC0gc2Vjb25kIDI4MjIyMjEWMBQGA1UEKh5Nc2Vjb25kIDIyMjIyMjEXMBUGA1UE",
        "HhcNMTkwNzAxMDAwMDAwWhcNMjkwNzAxMDAwMDAwWjBiMR0wGwY8VQQDExQxMDAz",
        "ChMOT2V0YVF1b3RlcyVERYYxEDAOBgNVBAsTB01ldGFERVYwgZ8wDQYJKoZIhvcN",
        "vVSBo+Lg4Il7GsHtbZNXGF5ce8afLoz7GvQJG32itIs0nTqt3VWgWLs9OTE1a6Yl",
        "wrG73F3dV6nHDUa22BXBxrtJWSkHTJbiCCLgLYvf2CttWUcqrphV9SqM9Bx17GmN",
        "AgMBAAEwDQYJKoZIhvcNAQEFBQADggEBAKXuEvPGWQvbLn4MqKgddikXog4YvN8X",
        "RdpwBYbzezWZtGqnMd4Hmp/S+FWLBdvUNICfrtX8kO6feA1r1Zz9RTFgbOdXK8ed",
        "AQEBBQADgY0AMIGJAoGBANFtI7+LVQ4sgIEEl26vojeMK11bzuXLCRHsWZENjV1Y",
        "9sqKlMyR5eHb9elQQ+rpBTuP87QHItUeif/xuWvE4qU7RGgrevQ3mBdLHa+Th304",
        "6a/Cy87KrOr/BxThJtz7XG2jNmzdBNu0JvZCM2pHCfQdiwsURPBieQw7/bA8IjRC",
        "qaVxz8OK7MvMjVwRT1BxS5WzNZR9BSzGJ9jMi0q11bEaJO48OnHDfPXQeabJ5+kg",
        "B65dMGB4CAManPcMv3rU8CGSyH+nh1qiE3FMWur8lwoiCQi7gBIK/x0=",
        "-----END CERTIFICATE-----"]
    }

## Raw API

Request format
    
    
    USER_CERT_GET|LOGIN=login|\r\n

Response format
    
    
    USER_CERT_GET|RETCODE=code description|\r\n
    [certificate description in PEM format]

## Request Parameters

  * login — the login of the user whose certificate you want to receive.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — certificate description in PEM format.


