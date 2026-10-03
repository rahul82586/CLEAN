[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Mail Database](../Mail-Database.md) / MailSend

[Previous](MailDeleteId.md) | [Next](MailBodyRequest.md)

# IMTAdminAPI::MailSend

Send emails via the internal mail system.

C++
    
    
    MTAPIRES  IMTAdminAPI::MailSend(
       IMTMail*  mail      // Mail object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.MailSend(
       CIMTMail  mail      // Mail object
       )

Python
    
    
    AdminAPI.MailSend(
       MTMail    mail      // Mail object
       )

### Parameters

**mail**  
[in] Mail object. The mail object must be first created using theIMTAdminAPI::MailCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Before sending an email, its correctness is checked (presence of its [subject](../../../Database-Interfaces/Mail-Database/IMTMail/Subject.md) and [recipient](../../../Database-Interfaces/Mail-Database/IMTMail/To.md)). [Sender](../../../Database-Interfaces/Mail-Database/IMTMail/From.md) field is automatically filled with the login of the manager account, which is used by the Manager API application to connect to the server.

  * #LOGIN# — the email recipient's account number.
  * #USERNAME# — the email recipient's name.
  * #CURRENCY# — the email recipient's deposit currency.
  * #BALANCE# — the email recipient's current balance.
  * #CREDIT# — the recipient's credit amount.
  * #EQUITY# — the current equity amount on the recipient's account.
  * #MARGIN# — the amount of funds required to cover current open positions.
  * #MARGIN_FREE# — the free margin amount.
  * #MARGIN_LEVEL# — the percent ratio of required margin and account equity.


  * #LEVERAGE# — the recipient's current leverage amount.


