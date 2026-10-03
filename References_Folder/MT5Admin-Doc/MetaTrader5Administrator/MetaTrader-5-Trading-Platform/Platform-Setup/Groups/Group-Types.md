[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Groups](../Groups.md) / Group Types

[Previous](Commission-Settings/Commission-Examples.md) | [Next](Import-of.md)

<a id="group-types"></a>

# Group Types (#group-types)

The trading platform allows to work with different types of [groups of accounts](../Groups.md). The system determines the types of groups by their names and processes them respectively. There are following types of groups:

<a id="demo"></a>

## Demo Groups (#demo)

Demo groups contain demo [accounts](../Accounts.md). They allow to work in a training mode without real money to perfect a trading strategy. This kind of accounts offer the same possibilities as the real ones. The difference is that the demo accounts can be opened without corresponding investment, however such accounts cannot be used for earning real money. Demo accounts can be opened directly from the client terminal, and the real ones are only opened from the manager and administrator terminals.

A created group is considered a demo one if its [name](Group-Settings.md) (including path) includes "demo" symbols (case sensitive). For example, the "demo\forex", "demo-USD" and "real\demoforex-USD" groups are demo and the "Demoforex" "fx-USD" groups are not.

> Add demo groups to the "[Account allocation](../Accounts/Account-Allocation-Settings.md)" section to enable your clients to open accounts in these groups directly via client terminals.

<a id="manager"></a>

## Manager Groups (#manager)

Groups are considered manager ones if their names (including path) include "manager" symbols (case sensitive). For example, "manager_CFD" or "manager_real". Only accounts that belong to the manager groups are able to connect to the trade servers using the manager and administrator terminals and the corresponding APIs. [Manager](../Managers.md) accounts can only be created on the basis of accounts that belong to the manager groups.

<a id="contest"></a>

## Contest Groups (#contest)

This type is intended for conducting contests among traders. Groups are considered contest ones if their names (including path) include "contest" symbols (case sensitive). For example, "contest_forex" or "contest\USD".

Contest accounts cannot be opened from terminals, as they can only be created by the broker.

Contest accounts are marked with a blue icon in client terminals. When a trader is connected to such an account, the "Contest account" title is displayed in the terminal window header. In some of the [reports](../Reports.md) contest accounts are shown in separate groups. Contest accounts operate similarly to demo ones.

<a id="preliminary"></a>

## Preliminary Group (#preliminary)

One preliminary group called "preliminary" is automatically created on the server. [Preliminary accounts](../Accounts/Preliminary.md) are created in it when requests for opening real accounts are sent from the client terminals. Managers can track such accounts and contact the clients using contact details specified during the registration. As soon as an official agreement with a client is made, a manager can move the account to one of the reals groups, what allows the client to start working immediately.

- [Trading is prohibited (#symbols)](Group-Settings.md#symbols) for all symbols in the preliminary group.
- All accounts are created with zero balance in the preliminary group.
- When opening an account in such a group, a client receives an email based on the [special template](../../Platform-Components/Trade-Server/Mail-Templates.md).

- Add preliminary groups to the "[Account allocation](../Accounts/Account-Allocation-Settings.md)" section to enable your clients to request live accounts directly via client terminals.

---

<a id="hedge"></a>

## Coverage Groups (#hedge)

Groups are considered as coverage ones if their names (including path) include "coverage" symbols (case sensitive). For example, "coverage\forex". This type of groups is intended for creating accounts that are used for covering client positions. Summary rates by such accounts are displayed in the manager terminal. A more detailed information is given in a [separate section (#coverage)](../../Platform-Components/Gateways/MetaTrader-5.md#coverage).

<a id="real"></a>

## Real Groups (#real)

This kind of groups contain account for working with real money. If a group doesn't fall into any category by its name among the ones mentioned above, then the system considers it a real one.

- If the groups in the system have certain hierarchy then their [names (#name)](Group-Settings.md#name) contain the corresponding paths to them. That path is an essential part of a group name and it is considered when determining its type. For example, all the sub-groups of the "manager" group will be considered as manager ones.

- Do not use indications of different group types within the name of a group. For example, managers\demo.

---

<a id="recommendations-on-naming-groups"></a>

## Recommendations on Naming Groups (#recommendations-on-naming-groups)

For making the work with groups convenient it is recommend to follow several rules when giving the names to groups:

- It is recommended to give sensible names to the demo groups because they will be visible to the clients when opening demo accounts from the client terminals. Only lower-case and upper-case letters, digits and "\_" (underline), "-" (hyphen) symbols are allowed in the group names;
- Names of user groups of company offices should end with a certain combination of symbols and should not end with '\_' symbol. For example, '\_kzn';
- It is possible to unite the groups by their regional (country) belonging. For example, one can add certain symbol combinations to the group names. For example, '_ru_'.
