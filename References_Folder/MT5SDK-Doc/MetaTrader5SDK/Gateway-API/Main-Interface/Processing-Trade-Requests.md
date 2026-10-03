[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Main Interface](../Main-Interface.md) / Processing Trade Requests

[Previous](Gateway-Symbols/GatewaySymbolGet.md) | [Next](Processing-Trade-Requests/DealerConfirmCreate.md)

# Processing Trade Requests

In accordance with the ideology of the MetaTrader 5 trading platform, customer request management is carried out through a queue of trade requests. A gateway written with the help of the Gateway API acts as a dealer, who works with the queue, receiving the queue status, capturing and processing trade requests, and then reporting the results of their processing.

  * All the functions described in this section are used only for gateways.
  * Details of working with trade operations are described in the ["Trade Operations in Gateway API"](../Trade-Operations-in.md) section.

  
---  
  
The following dealer activity functions are available:

Functions | Purpose  
---|---  
[DealerConfirmCreate](Processing-Trade-Requests/DealerConfirmCreate.md) | Create request confirmation interface object.  
[DealerExecutionCreate](Processing-Trade-Requests/DealerExecutionCreate.md) | Create trade execution method of this object.  
[DealerStart](Processing-Trade-Requests/DealerStart.md) | Gateway connection to the trading platform as a dealer.  
[DealerStop](Processing-Trade-Requests/DealerStop.md) | DealerStart inverse method. After its successful execution the gateway will stop fulfilling the dealer functions.  
[DealerGetAsync](Processing-Trade-Requests/DealerGetAsync.md) | Capture the most early (old) request from the requests queue.  
[DealerLockAsync](Processing-Trade-Requests/DealerLockAsync.md) | Capture a request from the requests queue by ID.  
[DealerAnswerAsync](Processing-Trade-Requests/DealerAnswerAsync.md) | Return the results of the captured request processing.  
[DealerExecuteAsync](Processing-Trade-Requests/DealerExecuteAsync.md) | The platform notification on the order trade execution in the external system.
