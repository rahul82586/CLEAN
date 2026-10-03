[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Trade](../Trade.md) / Request Processing

[Previous](Trade-Requests/Requests-AccountSet.md) | [Next](Request-Processing/DealerStart.md)

# Processing of requests

MetaTrader 5 Server API allows connecting to a queue of requests of a trade server, capture requests from this queue and process them on behalf of a manager account, similar to [Manager API](../../../Manager-API/Manager-Interface/Trade-Activity/Dealing.md).

To start operation, you need to call the [IMTServerAPI::DealerStart](Request-Processing/DealerStart.md) method, specifying the login of the manager, on whose behalf trade requests will be processed. You can connect multiple manager accounts by calling this method for each of them. These accounts must have the [IMTConManager:RIGHT_TRADES_DEALER (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission.

After that, the plugin downloads the queue of requests for the manager (or managers) and calls the [IMTRequestSink::OnRequestSync](../../../Database-Interfaces/Trade/Trade-Requests/IMTRequestSink/Requests-OnRequestSync.md) event, which means that the queue has been downloaded. After that the plugin starts receiving events of changes in its queue: addition, update or deletion of requests ([IMTRequestSink](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestSink.md) methods).

  * The plugin does not have access to the entire queue of a trade server. Each plugin works with its own queue, which receives only those requests, which are available to connected managers. Each manager can only access the requests from clients from allowed groups ([IMTConManager::Group*](../../../Configuration-Interfaces/Managers/IMTConManager/GroupAdd.md)) and only those requests, which are routed to him according to [routing rules](../../../Configuration-Interfaces/Routing/IMTConRoute.md). Also, the manager only receives events related to available requests.
  * The queue of requests is available to the plugin until the call of [IMTServerAPI::DealerStop](Request-Processing/DealerStop.md) for each of the dealers, who were previously connected via [IMTServerAPI::DealerStart](Request-Processing/DealerStart.md). For example, if the plugin starts processing requests on behalf of four different dealers, and then completes the operation of three of them, the plugin will continue to receive events.
  * Application of transactions associated with changes in the general server queue to the plugin queue, as well as notification of connected managers about these events are performed in one thread. In this regard, too long processing of events can cause a delay in the plugin queue. The longer the plugin returns control from events, the greater can be the difference between the status of the plugin queue and the general server queue. However, this will not slow down the operation of other plugins, because each plugin uses its own thread.

  
---  
  
To capture a request for processing use [IMTServerAPI::DealerGet](Request-Processing/DealerGet.md) or [IMTServerAPI::DealerLock](Request-Processing/DealerLock.md). After that call [IMTServerAPI::DealerAnswer](Request-Processing/DealerAnswer.md) to respond to a captured request. The object of the confirmation [IMTConfirm](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) is passed in this method, where it is specified how the request should be executed. For details on how to fill IMTConfirm for each type of request please see the [separate section (#fill-confirmation)](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md#fill-confirmation). 

Requests are processed asynchronously. Once confirmed by a plugin, the request appears on the execution queue of the server. Use the [IMTRequestSink::OnRequestUpdate](../../../Database-Interfaces/Trade/Trade-Requests/IMTRequestSink/Requests-OnRequestUpdate.md) handler to get the execution result. Request execution results are written to [IMTRequest::Result*](../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ResultRetcode.md) fields. To search for a required request, use its ID ([IMTRequest::ID](../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ID.md)).

> Such a request must be processed within three minutes. Otherwise, the server will automatically delete it, and the client will receive a rejection.

The following request processing methods are available in MetaTrader 5 Server API:

Features | Purpose  
---|---  
[DealerStart](Request-Processing/DealerStart.md) | Starts processing requests on behalf of the specified manager account.  
[DealerStop](Request-Processing/DealerStop.md) | Stops processing requests via the specified manager account.  
[DealerGet](Request-Processing/DealerGet.md) | Gets the next request for processing. The method captures requests from the queue in the same order they are received from clients.  
[DealerLock](Request-Processing/DealerLock.md) | Gets a request with the specified ID for processing.  
[DealerAnswer](Request-Processing/DealerAnswer.md) | A response to a trade request, which [IMTServerAPI::DealerGet](Request-Processing/DealerGet.md) or [IMTServerAPI::DealerLock](Request-Processing/DealerLock.md) has received for processing.  
[DealerExecution](Request-Processing/DealerExecution.md) | Applies a [trade execution](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md).  
[DealerRequestTotal](Request-Processing/DealerRequestTotal.md) | Gets the total number of requests in the trade queue available to the specified manager account.  
[DealerRequestNext](Request-Processing/DealerRequestNext.md) | Gets a trade request with the specified index.  
[DealerRequestGet](Request-Processing/DealerRequestGet.md) | Gets a trade request with the specified identifier.  
[DealerRequestGetAll](Request-Processing/DealerRequestGetAll.md) | Gets all trade requests from the trade queue available to the specified manager account.
