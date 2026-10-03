[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Mail Database](../Mail-Database.md) / MailSend

[Previous](MailUnsubscribe.md) | [Next](../News-Database.md)

# IMTServeAPI::MailSend

Send emails via the internal mail system.
    
    
    MTAPIRES  IMTServerAPI::MailSend(
       IMTMail*  mail      // Mail object
       )

### Parameters

**mail**  
[in] An object of the email.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Before sending an email, its correctness is checked (presence of its [subject](../../../Database-Interfaces/Mail-Database/IMTMail/Subject.md), [recipient](../../../Database-Interfaces/Mail-Database/IMTMail/To.md) and [sender](../../../Database-Interfaces/Mail-Database/IMTMail/From.md)).

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


