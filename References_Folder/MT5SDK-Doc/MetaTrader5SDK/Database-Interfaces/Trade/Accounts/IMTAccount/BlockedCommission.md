[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / BlockedCommission

[Previous](SOMargin.md) | [Next](BlockedProfit.md)

# IMTAccount::BlockedCommission

Get the amount of the standard commission locked on the account, which has been accumulated during the day/month.

C++
    
    
    double  IMTAccount::BlockedCommission()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTAccount.BlockedCommission()

### Return Value

The amount of the standard commission locked on the account.

### Note

If standard commission ([IMTConCommission::COMM_STANDARD (#encommmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode)) is charged in the [IMTConCommission::COMM_CHARGE_DAILY or IMTConCommission::COMM_CHARGE_MONTHLY (#encommchargemode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommchargemode)mode, the commission amount for trade operations is blocked on the account during one month or day and is accumulated in the BlockedCommission field. At the end of the day/month, the accumulated amount is debited from the account in a separate balance operation (a deal of type [DEAL_COMMISSION_DAILY or DEAL_COMMISSION_MONTHLY (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction)). After that the value of the BlockedCommission field is reset.

# IMTAccount::BlockedCommission

Set the amount of the standard commission locked on the account, which has been accumulated during the day/month.

C++
    
    
    MTAPIRES  IMTAccount::BlockedCommission(
       const double  commission      // The amount of commission locked
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.BlockedCommission(
       double        commission      // The amount of commission locked
       )

### Parameters

**commission**  
[in] The amount of the standard commission locked on the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If standard commission ([IMTConCommission::COMM_STANDARD (#encommmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode)) is charged in the [IMTConCommission::COMM_CHARGE_DAILY or IMTConCommission::COMM_CHARGE_MONTHLY (#encommchargemode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommchargemode)mode, the commission amount for trade operations is blocked on the account during one month or day and is accumulated in the BlockedCommission field. At the end of the day/month, the accumulated amount is debited from the account in a separate balance operation (a deal of type [DEAL_COMMISSION_DAILY or DEAL_COMMISSION_MONTHLY (#endealaction)](../../Deals/IMTDeal/Enumerations.md#endealaction)). After that the value of the BlockedCommission field is reset.
