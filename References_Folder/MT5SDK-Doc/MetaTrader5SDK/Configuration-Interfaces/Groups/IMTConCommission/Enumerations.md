[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / Enumerations

[Previous](../IMTConCommission.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConCommission](../IMTConCommission.md) class contains the following enumerations:

  * [IMTConCommission::EnCommMode (#encommmode)](Enumerations.md#encommmode)
  * [IMTConCommission::EnCommRangeMode (#encommrangemode)](Enumerations.md#encommrangemode)
  * [IMTConCommission::EnCommChargeMode (#encommchargemode)](Enumerations.md#encommchargemode)
  * [IMTConCommission::EnCommEntryMode (#encommentrymode)](Enumerations.md#encommentrymode)
  * [IMTConCommission::EnCommActionMode (#encommactionmode)](Enumerations.md#encommactionmode)
  * [IMTConCommission::EnCommProfitMode (#encommprofitmode)](Enumerations.md#encommprofitmode)
  * [IMTConCommission::EnCommReasonFlags (#encommreasonflags)](Enumerations.md#encommreasonflags)



<a id="encommmode"></a>
## IMTConCommission::EnCommMode (#encommmode)

Commission types are enumerate in IMTConCommission::EnCommMode.

ID | Value | Description  
COMM_STANDARD | 0 | Standard commission. This type of commission is charged by a broker for the clients' trades.  
COMM_AGENT | 1 | Agent commission. This commission is charged by agents. Each account has the [IMTUser::Agent](../../../Database-Interfaces/Users/IMTUser/Agent.md) field, in which the number of the appropriate agent account can be specified. Commissions of all trades conducted on this trading account will be transfered to the Agent account in accordance with the commission settings.  
COMM_FEE | 2 | Fee. The fee is similar to standard commission: it is also charged by a broker per traders deals and has the same settings and the calculation principle. The differences are as follows:

  * Fees can only have [the "IMTConCommission::COMM_CHARGE_INSTANT" calculation mode (#encommchargemode)](Enumerations.md#encommchargemode).
  * The amount is written to deals as a separate field â [IMTDeal::Fee](../../../Database-Interfaces/Trade/Deals/IMTDeal/Fee.md), while the standard commission appears in the [IMTDeal::Commission](../../../Database-Interfaces/Trade/Deals/IMTDeal/Commission.md) field.

Fees allow splitting deal commissions for a separate accounting. For example, this option can be used when part of commission is charged by the brokerage company, and the other part is payable to an external system (exchange) the broker is integrated with.  
COMM_FIRST |  | Beginning of enumeration. It corresponds to COMM_STANDARD.  
COMM_LAST |  | End of enumeration. It corresponds to COMM_FEE.  
  
This enumeration is used in the [IMTConCommission::Mode](Mode.md) method.

<a id="encommrangemode"></a>
## IMTConCommission::EnCommRangeMode (#encommrangemode)

Types of commission levels are listed in IMTConCommission::EnCommRangeMode.

ID | Value | Description  
COMM_RANGE_VOLUME | 0 | Commission levels by volume.  
COMM_RANGE_TURNOVER_MONEY | 1 | Commission levels by turnover in money. The turnover calculation period is set via [IMTConCommission::ChargeMode](ChargeMode.md). By default, the money turnover is calculated in the [group deposit currency](../IMTConGroup/Currency.md): the price of each trade is calculated and converted into the deposit currency. For example, the price of Buy 1 lot EURUSD with a contract size of 100,000 is 100,000 EUR. If the client's deposit currency is USD, the position price is converted at EURUSD at the time of the transaction (in this case, it is the transaction price). If commission is to be charged on the turnover in some certain currency regardless of the group deposit, set it using [IMTConCommission::TurnoverCurrency](TurnoverCurrency.md). Commission ranges will be based on the turnover in the specified currency. When calculating commissions, the deal price is also converted into that currency.  
COMM_RANGE_TURNOVER_VOLUME | 2 | Commission levels by turnover in lots. The turnover calculation period is set via [IMTConCommission::ChargeMode](ChargeMode.md).  
COMM_RANGE_FIRST |  | Beginning of enumeration. It corresponds to COMM_RANGE_VOLUME.  
COMM_RANGE_LAST |  | End of enumeration. It corresponds to COMM_RANGE_TURNOVER_VOLUME.  
  
This enumeration is used in the [IMTConCommission::RangeMode](RangeMode.md) method.

<a id="encommchargemode"></a>
## IMTConCommission::EnCommChargeMode (#encommchargemode)

Commission charging modes are listed in IMTConCommission::EnCommChargeMode.

ID | Value | Description  
COMM_CHARGE_DAILY | 0 | Charging at the end of the day. During the day, the standard commissions for trade operations are blocked on in the account and are accumulated in the [IMTAccount::BlockedCommission](../../../Database-Interfaces/Trade/Accounts/IMTAccount/BlockedCommission.md) field. At the end of the day this amount is debited from an account in a separate balance operation (a deal of type [IMTDeal::DEAL_COMMISSION_DAILY (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction)). After that the value of the IMTAccount::BlockedCommission field is reset. Agent commissions are charged in a similar way. The commissions are accumulated during the day, and then credited to an agent's account in a separate balance operation (a deal of type IMTDeal::DEAL_AGENT_DAILY).  
COMM_CHARGE_MONTHLY | 1 | Charging at the end of the month. During the month, the standard commissions for trade operations are blocked on in the account and are accumulated in the [IMTAccount::BlockedCommission](../../../Database-Interfaces/Trade/Accounts/IMTAccount/BlockedCommission.md) field. At the end of the month this amount is debited from an account in a separate balance operation (a deal of type [IMTDeal::DEAL_COMMISSION_MONTHLY (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction)). After that the value of the IMTAccount::BlockedCommission field is reset. Agent commissions are charged in a similar way. The commissions are accumulated during the month, and then credited to an agent's account in a separate balance operation (a deal of type IMTDeal::DEAL_AGENT_MONTHLY).  
COMM_CHARGE_INSTANT | 2 | Immediate commission charging during a trade operation execution. The value of the instantly charged standard commission is displayed in the [IMTDeal::Commission](../../../Database-Interfaces/Trade/Deals/IMTDeal/Commission.md) field. Agent commissions are charged as separate balance operations ([IMTDeal::DEAL_AGENT (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction)). In case of an instant charge, commission levels can be specified only in volume ([IMTConCommission::COMM_RANGE_VOLUME (#encommrangemode)](Enumerations.md#encommrangemode)).  
COMM_CHARGE_FIRST |  | Beginning of enumeration. It corresponds to COMM_CHARGE_DAILY.  
COMM_CHARGE_LAST |  | End of enumeration. Corresponds to COMM_CHARGE_INSTANT.  
  
This enumeration is used in the [IMTConCommission::ChargeMode](ChargeMode.md) method.

<a id="encommentrymode"></a>
## IMTConCommission::EnCommEntryMode (#encommentrymode)

Commission charging modes depending on the deal direction are enumerated in IMTConCommission::EnCommEntryMode.

Identifier | Meaning | Description  
COMM_ENTRY_ALL | 0 | The commission is charged irrespective of the direction of deals. No commission is charged on Close Buy deals, since the commission is charged on two original deals.  
COMM_ENTRY_IN | 1 | The commission is only charged on entry deals. For reversal deals with the in/out type, commission is only charged on the volume of the newly opened position. No commission is charged on Close Buy deals, since the commission is charged on two original deals. For example, a commission of 1 USD is charged on each deal. When a trader performs an entry Buy 1.00 EURUSD deal and an entry Sell 1.00 EURUSD deal, a commission of 2 USD will be charged. When the 1.00 EURUSD position is closed by the Sell 1.00 EURUSD position, the client will not be charged additional commission.  
COMM_ENTRY_OUT | 2 | The commission is only charged on exit deals. For reversal deals with the in/out type, commission is only charged on the closed volume. For Close By deals, commission is charged on both deals. The total commission value is written to the main exit deal (in which profit/loss is specified). For example, a commission of 1 USD is charged on each deal. When a trader performs an entry Buy 1.00 EURUSD deal and an entry Sell 1.00 EURUSD deal, no commission will be charged. When the 1.00 EURUSD position is closed by the Sell 1.00 EURUSD position, a commission of 2 USD will be charged. A commission of 2 USD will be specified in the first 'out by' deal, and a zero commission will be specified in the second deal.  
COMM_ENTRY_FIRST |  | Beginning of enumeration. Corresponds to COMM_ENTRY_ALL.  
COMM_ENTRY_LAST |  | End of enumeration. Corresponds to COMM_ENTRY_OUT.  
  
The enumeration is used in the [IMTConCommission::EntryMode](EntryMode.md) method.

<a id="encommactionmode"></a>
## IMTConCommission::EnCommActionMode (#encommactionmode)

IMTConCommission::EnCommEntryMode contains commission charging modes depending on the deal type.

ID | Value | Description  
COMM_ACTION_ALL | 0 | All transactions, regardless of type.  
COMM_ACTION_BUY | 1 | Only Buy deals.  
COMM_ACTION_SELL | 2 | Only sell deals.  
COMM_ENTRY_FIRST |  | Beginning of enumeration. Corresponds to COMM_ACTION_ALL.  
COMM_ENTRY_LAST |  | Enumeration end. Corresponds to COMM_ACTION_SELL.  
  
The enumeration is used in the [IMTConCommission::ActionMode](ActionMode.md) method.

<a id="encommprofitmode"></a>
## IMTConCommission::EnCommProfitMode (#encommprofitmode)

Commission charging modes depending on the deal profit are enumerated in IMTConCommission::EnCommProfitMode.

ID | Value | Description  
COMM_PROFIT_ALL | 0 | All deals.  
COMM_PROFIT_PROFIT | 1 | Only profitable deals.  
COMM_PROFIT_LOSS | 2 | Only losing deals.  
COMM_PROFIT_FIRST |  | Beginning of enumeration. Corresponds to COMM_PROFIT_ALL.  
COMM_PROFIT_LAST |  | End of enumeration. Corresponds to COMM_PROFIT_LOSS.  
  
The enumeration is used in the [IMTConCommission::ProfitMode](ProfitMode.md) method.

<a id="encommreasonflags"></a>
## IMTConCommission::EnCommReasonFlags (#encommreasonflags)

Commission charging modes depending on the reason for the deal execution are enumerated in IMTConCommission::EnCommReasonFlags.

ID | Value | Description  
COMM_REASON_FLAG_NONE | 0x00000000 | No commission will be charged for any transactions.  
COMM_REASON_FLAG_CLIENT | 0x00000001 | The deal is performed by the client manually, through the client terminal.  
COMM_REASON_FLAG_EXPERT | 0x00000002 | The deal is performed by the client using an Expert Advisor.  
COMM_REASON_FLAG_DEALER | 0x00000004 | The deal is performed by a dealer through the manager terminal.  
COMM_REASON_FLAG_EXTERNAL_CLIENT | 0x00000008 | The deal is performed from an external trading system.  
COMM_REASON_FLAG_MOBILE | 0x00000010 | The deal is performed via the MetaTrader 5 mobile terminal for Android or iPhone.  
COMM_REASON_FLAG_WEB | 0x00000020 | The deal is performed via the web terminal.  
COMM_REASON_FLAG_SIGNAL | 0x00000040 | The deal is performed as a result of copying a [trading signal](https://www.mql5.com/ru/signals), in accordance with the subscription, in the client terminal.  
COMM_REASON_FLAG_ALL |  | End of enumeration. Enables commissions for all deals with any deal reason.  
  
The enumeration is used in the [IMTConCommission::ReasonFlags](ReasonFlags.md) method.
