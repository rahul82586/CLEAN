[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Update Certificate

[Previous](Get-Group.md) | [Next](Get-Certificate.md)

# Update user certificates

The request allows adding and updating user certificates

## Rest API

Request format
    
    
    POST /api/user/certificate/update
    [array of logins and certificates]

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [list of accounts]
    }

Example
    
    
    //--- request to the server
    POST /api/user/certificate/update
    [
      {
        "Login": "1000",
        "Cert": [
          "-----BEGIN CERTIFICATE-----",
          "MIIClTC5AX2gAwIBAgIIF0mMFC+rOagwDQYJKoZIhvcNAQEFBQAwNzEcMBoGA1UE",
          "AxMTZGV2Lm1ldGF0cmFkZXI1LmRldjEXMBUGA1UEChMOTWV0YVF1b3RlcyBERVYw",
          "IC0gc2Vjb25kIDI4MjIyMjEWMBQGA1UEKh5Nc2Vjb25kIDIyMjIyMjEXMBUGA1UE",
          "HhcNMTkwNzAxMDAwMDAwWhcNMjkwNzAxMDAwMDAwWjBiMR0wGwY8VQQDExQxMDAz",
          "ChMOT2V0YVF1b3RlcyBERVYxEDAOBgNVBAsTB01ldGFERVYwgZ8wDQYJKoZIhvcN",
          "vVSBo+Lg4Il7GsHtbZNXPO9ce8afLoz7GvQJG32itIs0nTqt3VWgWLs9OTE1a6Yl",
          "wrG73F3dV6nHDUa22BXBxrtJWSkHTJbiCCLgLYvf2CttWUcqrphV9SqM9Bx17GmN",
          "AgMBAAEwDQYJKoZIhvcNAQEFBQADggEBAKXuEvPGWQvbLn4MqKgddikXog4YvN8X",
          "RdpwBYbzezWZtGqnMd4Hmp/S+FWLBdvUNICfrtX8kO6feA1r1Zz9RTFgbOdXK8ed",
          "AQEBBQADgY0AMIGJAoGBANFtI7+LVQ4sgIEEl26vojeMK11bzuXLCRHsWZENjV1Y",
          "9sqKlMyR5eHb9elQQ+rpBTuP87QHItUeif/xuWvE4qU7RGgrevQ3mBdLHa+Th304",
          "6a/Cy87KrOr/BxThJtz7XG2jNmzdBNu0JvZCM2pHCfQdiwsURPBieQw7/bA8IjRC",
          "qaVxz8OK7MvMjVwRT1BxS5WzNZR9BSzGJ9jMi0q11bEaJO48OnHDfPXQeabJ5+kg",
          "B65dMGB4CAManPcMv3rU8CGSyH+nh1qiE3FMWur8lwoiCQi7gBIK/x0=",
          "-----END CERTIFICATE-----"
        ]
      },
      {
        "Login": "1003",
        "Cert": [
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
          "-----END CERTIFICATE-----"
        ]
      }
    ]
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [1000, 1003]
    }

## Raw API

Request format
    
    
    USER_CERT_UPDATE|\r\n
    [array of logins and certificates]

Response format
    
    
    USER_CERT_UPDATE|RETCODE=code description|\r\n
    [list of accounts]

## Request Parameters

The request has no parameters. User and certificate descriptions are passed in JSON format as an additional body:

  * login — user login for which the certificate is updated.
  * cert — certificate description in PEM format.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — list of accounts whose certificates have been successfully updated.



## Note

  * If a client already has a certificate, it is updated, otherwise a new certificate is added.
  * A user certificate can be updated only when you are connected to the same trade server where the account is located. If an account with the specified login is not found, response code [13](../../../Return-Codes/Common-errors.md) is returned.


