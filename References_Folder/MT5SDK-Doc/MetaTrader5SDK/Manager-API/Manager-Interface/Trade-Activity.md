[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Manager Interface](../Manager-Interface.md) / Trade Activity

[Previous](News-Database/NewsSend.md) | [Next](Trade-Activity/Dealing.md)

<a id="trading-functions"></a>
# Trading Functions (#trading-functions)

This section contains descriptions of functions, using which you can implement trading activities from an application developed using the MetaTrader 5 Manager API.

Trading functions are divided into the following sections:

  * [Dealing](Trade-Activity/Dealing.md) — dealer activity functions.
  * [Trading requests](Trade-Activity/Trade-Requests.md) — functions for working with trading requests queue.
  * [Auxiliary Functions](Trade-Activity/Auxiliary-Functions.md) — functions for calculating profit, margin requirements and conversion rates.



<a id="dealer-supervisor"></a>
## Dealer and Supervisor Modes (#dealer-supervisor)

Depending on the [rights (#enmanagerrights)](../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) assigned to an account, a manager can perform the following activities related to trade operations on the server:

<a id="dealing"></a>
### Dealing (#dealing)

The Dealing permission ([IMTConManager:RIGHT_TRADES_DEALER (#enmanagerrights)](../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights)) allows a manager to handle trade requests received in accordance with the [routing rules](../../Configuration-Interfaces/Routing.md). Also, this right allows the manager the perform trade operations.

The dealing procedure:

  * After connecting to a server using the [IMTManagerAPI::Connect](Connection-to-the-Server/Connect.md) method with the required [pumping modes](Connection-to-the-Server/Pumping-Modes.md) (for orders, positions, accounts, groups and symbols) and starting dealing using the [IMTManagerAPI:DealerStart](Trade-Activity/Dealing/DealerStart.md) method, the manager receives the status of the queue of requests forwarded to the manager in accordance with the routing rules. Next, it will receive the changes of the queue (added, edited and deleted requests) using the methods of the [IMTRequestSink](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestSink.md) interface.
  * To capture a request from a queue for processing, methods [IMTManagerAPI:DealerGet](Trade-Activity/Dealing/DealerGet.md) and [IMTManagerAPI:DealerLock](Trade-Activity/Dealing/DealerLock.md) are used. A captured request must necessarily be processed by the dealer using the [IMTManagerAPI::DealerAnswer](Trade-Activity/Dealing/DealerAnswer.md) method. In this method, the object request confirmation [IMTConfirm](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) is passed, where the dealer specifies how the request should be executed.
  * Once confirmed by a dealer, the request appears on the queue to be executed by the server. The result of request execution can be received based on its identifier ([IMTRequest::ID](../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ID.md)) using the [IMTRequest::Result*](../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ResultRetcode.md) methods.



<a id="supervisor"></a>
### Supervisor (#supervisor)

The Supervisor right ([IMTConManager:RIGHT_TRADES_SUPERVIOSR (#enmanagerrights)](../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights)) allows a manager to view the entire queue of requests forwarded to him or her from available client groups, and track the process of request processing by other dealers.

Description of the Supervisor mode:

  * After connecting to a server using the [IMTManagerAPI::Connect](Connection-to-the-Server/Connect.md) method with the required [pumping modes](Connection-to-the-Server/Pumping-Modes.md) (for orders, positions, accounts, groups and symbols), the manager receives the status of the queue of requests, which the manager can view in accordance with the client group settings ([IMTConManager::Group*](../../Configuration-Interfaces/Managers/IMTConManager/GroupAdd.md)).
  * Then the manager will receive changes of the queue (added, edited and deleted requests) using the methods of the [IMTRequestSink](../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestSink.md) interface. Also, the manager will be able to get the results of request processing by other dealers using the [IMTRequest::Result*](../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ResultRetcode.md) methods.
  * When switching to the dealing mode using the [IMTManagerAPI:DealerStart](Trade-Activity/Dealing/DealerStart.md) method, the manager no longer sees the entire queue of requests from client groups available to him or her. Since then, the manager receives only the requests that are forwarded to him or her for processing in accordance with [routing rules](../../Configuration-Interfaces/Routing.md). Thus, the manager simply switches to the dealing mode described above.


