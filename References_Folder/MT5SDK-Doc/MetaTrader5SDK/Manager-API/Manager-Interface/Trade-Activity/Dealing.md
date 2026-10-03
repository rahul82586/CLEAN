[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Trade Activity](../Trade-Activity.md) / Dealing

[Previous](../Trade-Activity.md) | [Next](Dealing/DealerConfirmCreate.md)

# Dealing

The MetaTrader 5 Manager API allows performing dealing using a special set of functions. Functions described in this section allow to connect to a queue of requests of a trade server, select requests from it and process them in accordance with the encoded algorithms.

Functions | Purpose  
---|---  
[DealerConfirmCreate](Dealing/DealerConfirmCreate.md) | Create request confirmation interface object.  
[DealerUnsubscribe](Dealing/DealerUnsubscribe.md) | Unsubscribe from waiting for results of trading operations executed by DealerSend commands.  
[DealerStart](Dealing/DealerStart.md) | Start dealing.  
[DealerStop](Dealing/DealerStop.md) | Stop dealing.  
[DealerGet](Dealing/DealerGet.md) | Get the first request in the queue of requests for processing.  
[DealerLock](Dealing/DealerLock.md) | Get a request with a specified ID for processing.  
[DealerAnswer](Dealing/DealerAnswer.md) | Respond to a trade request received for processing using the DealerGet or DealerLock method.  
[DealerSend](Dealing/DealerSend.md) | Send a trade request to the server.  
[DealerBalance](Dealing/DealerBalance.md) | Conduct balance operations on an account.  
[DealerBalanceRaw](Dealing/DealerBalanceRaw.md) | Conduct balance operation on a user account without checking the free margin and the current balance on the account.
