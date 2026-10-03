[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Reopen Order

[Previous](Restore-from-Backup.md) | [Next](../Deals.md)

# Reopen an Order

The request allows reopening a pending order from the account history.

## Rest API

Request Format
    
    
    GET /api/order/reopen?ticket=ticket
    POST /api/order/reopen?ticket=ticket

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/order/reopen?ticket=12832917
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Order" : "12832917",
        "ExternalID" : "",
        "Login" : "104366",
        ...
      }
    }

## Raw API

Request Format
    
    
    ORDER_REOPEN|TICKET=ticket|\r\n

Response Format
    
    
    ORDER_REOPEN|RETCODE=code description|\r\n
    Description of the reopened order in JSON format

## Request Parameters

  * ticket — the ticket of the order to be reopened.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — recovered order parameters in JSON format. The full description of order parameters is available under the [Data Structure](Data-Structure.md) section.



## Note

Only [Limit, Stop and Stop Limit orders can be reopened (#enordertype)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enordertype). The order you want to reopen must exist in the client's history.

The request finds an order in the account history and moves it to open orders while updating its [parameters](Data-Structure.md):

  * Changes the order state to Placed (State)
  * Deletes the execution date (TimeDone, TimeDoneMsc)
  * Deletes the trigger price (PriceTrigger)
  * Resets the current volume (VolumeCurrent) to the initial (VolumeInitial)
  * Zeroes PositionID
  * Resets activation signs: ActivationTime, ActivationPrice and ActivationMode



Before reopening a previously triggered order, you should properly correct the state of the client's trading positions and account:

  * Delete the [trade](../Deals.md), which was opened in accordance with the order. If several trades were performed in connection with the order, delete all of them.
  * Correct the client's positions ([/api/position/fix](../Positions/Fix-Position.md)).
  * Correct the client's balance ([/api/user/check_balance](../../Users/Check-Balance.md)).



After the above actions, the client's state will correspond to the history of orders.
