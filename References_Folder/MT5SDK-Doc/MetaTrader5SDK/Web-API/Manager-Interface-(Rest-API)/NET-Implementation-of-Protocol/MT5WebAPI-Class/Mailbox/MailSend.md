[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Mailbox](../Mailbox.md) / MailSend

[Previous](../Mailbox.md) | [Next](../News-Event.md)

# MT5WebAPI.MailSend

Send mails via the internal mailing system of the trading platform.
    
    
    MTRetCode  MT5WebAPI.MailSend(
       string          to,              // Recipients
       string          subject,         // Subject
       string          text             // Mail text
       )

### Parameters

**to**  
[in] The login of the email recipient. You may use the mask "*" as well as specify login ranges in this parameter. For example:

**subject**  
[in] Subject of an email.

**text**  
[in] Mail body. You may use HTML to format mails.

  * TO=* — the mail will be sent to all clients
  * TO=demo*,preliminary — the mail will be sent to all clients from groups "demo" and "preliminary".
  * TO=100-250,5000-7500 — the mail will be sent to all clients from groups "demo" and "preliminary".



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

You can use macros in the email body, which allow substituting relevant data depending on the email recipient:

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


