[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Users](../Users.md) / IMTUser

[Previous](../Users.md) | [Next](IMTUser/Enumerations.md)

# IMTUser

The IMTUser class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTUser/Release.md) | Delete the current object.  
[Assign](IMTUser/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTUser/Clear.md) | Clear an object.  
[Login](IMTUser/Login.md) | Get and set the login of a user.  
[Group](IMTUser/Group.md) | Get and set the group of a user.  
[CertSerialNumber](IMTUser/CertSerialNumber.md) | Get the number of the certificate that was used last by the client for authorization.  
[Rights](IMTUser/Rights.md) | Get and set user permissions.  
[Registration](IMTUser/Registration.md) | Get the client record creation date.  
[RegistrationSet](IMTUser/RegistrationSet.md) | Set the client record creation date.  
[LastAccess](IMTUser/LastAccess.md) | Get the date of the last connection using the account.  
[LastIP](IMTUser/LastIP.md) | Get the IP address from which the user last connected to the server.  
[Name](IMTUser/Name.md) | Get and set the client's first name. The method is obsolete.  
[FirstName](IMTUser/FirstName.md) | Get and set the client's first name.  
[LastName](IMTUser/LastName.md) | Get and set the client's last name.  
[MiddleName](IMTUser/MiddleName.md) | Get and set the client's middle name.  
[Company](IMTUser/Company.md) | Get and set the name of a client's company.  
[Account](IMTUser/Account.md) | Get and set the number of a client's account in an external trading system.  
[Country](IMTUser/Country.md) | Get and set a client's country of residence.  
[Language](IMTUser/Language.md) | Get and set the language of a user.  
[City](IMTUser/City.md) | Get and set a client's city of residence.  
[State](IMTUser/State.md) | Get and set a client's state (region) of residence.  
[ZIPCode](IMTUser/ZipCode.md) | Get and set a client's zip code.  
[Address](IMTUser/Address.md) | Get and set a client's address.  
[Phone](IMTUser/Phone.md) | Get and set a client's phone number.  
[EMail](IMTUser/EMail.md) | Get and set a client's email address.  
[ID](IMTUser/ID.md) | Get and set the number of a client's identity document.  
[MQID](IMTUser/MQID.md) | Get the client's MetaQuotes ID.  
[ClientID](IMTUser/ClientID.md) | Get and set the client ID with which the trading account is associated.  
[VisitorID](IMTUser/VisitorID.md) | Get a unique identifier assigned to a user when he/she installs your terminal or visits your site, if a Finteza tracker is installed in it.  
[Status](IMTUser/Status.md) | Get and set a client's status.  
[Comment](IMTUser/Comment.md) | Get and set a comment to a client.  
[Color](IMTUser/Color.md) | Get and set a client's color.  
[PhonePassword](IMTUser/PhonePassword.md) | Get and set a client's phone password.  
[LastPassChange](IMTUser/LastPassChange.md) | Get the date of the last change of the user's password.  
[PasswordHash](IMTUser/PasswordHash.md) | Get the password hash of a client record. This method is used only in the MetaTrader 5 Server API.  
[OTPSecret](IMTUser/OTPSecret.md) | Get and set a secret key which links a trading account and a one-time password generator.  
[Leverage](IMTUser/Leverage.md) | Get and set the size of a client's leverage.  
[LeadSource](IMTUser/LeadSource.md) | Get and set a lead source — a website a client has come from.  
[LeadCampaign](IMTUser/LeadCampaign.md) | Get and set a lead campaign — name of a marketing campaign a client was attracted by.  
[InterestRate](IMTUser/InterestRate.md) | Get the amount accrued for the current month calculated based on the annual interest rate.  
[CommissionDaily](IMTUser/CommissionDaily.md) | Get the amount of commissions from a client for a day.  
[CommissionMonthly](IMTUser/CommissionMonthly.md) | Get the total amount of commissions charged from a client for the current month.  
[CommissionAgentDaily](IMTUser/CommissionAgentDaily.md) | Get the size of agent commissions charged from a client's trade operations for a day.  
[CommissionAgentMonthly](IMTUser/CommissionAgentMonthly.md) | Get and the amount of agent commission charged for a client's trade operations for the current month.  
[Agent](IMTUser/Agent.md) | Get and set the number of a client's agent account.  
[Balance](IMTUser/Balance.md) | Get the current balance of a client.  
[BalancePrevDay](IMTUser/BalancePrevDay.md) | Get the value of a client's balance as of the end of the previous day.  
[BalancePrevMonth](IMTUser/BalancePrevMonth.md) | Get the value of a client's balance as of the end of the previous trading month.  
[EquityPrevDay](IMTUser/EquityPrevDay.md) | Get the value of a client's equity as of the end of the previous day.  
[EquityPrevMonth](IMTUser/EquityPrevMonth.md) | Get the value of a client's equity as of the end of the previous trading month.  
[Credit](IMTUser/Credit.md) | Get the current amount of funds credited to a client.  
[LimitOrders](IMTUser/LimitOrders.md) | Get and set the maximum number of active (placed) pending orders allowed on the account.  
[LimitPositionsValue](IMTUser/LimitPositionsValue.md) | Get and set the maximum value of open positions allowed on the account.  
[ApiDataSet](IMTUser/APIDataSet.md) | Set the user parameter for a client record.  
[ApiDataGet](IMTUser/APIDataGet.md) | Get the value of the user parameter of a client record.  
[APIDataUpdate](IMTUser/APIDataUpdate.md) | Update a custom parameter for a client record.  
[APIDataNext](IMTUser/APIDataNext.md) | Get a custom parameter of a client record by position.  
[ApiDataClear](IMTUser/APIDataClear.md) | Clear all user parameters set by an application.  
[ApiDataClearAll](IMTUser/APIDataClearAll.md) | Clear all custom parameters of client records.  
[ExternalAccountAdd](IMTUser/ExternalAccountAdd.md) | Add the number of a client's trading account in the external system, with which the platform interacts via the specified gateway.  
[ExternalAccountUpdate](IMTUser/ExternalAccountUpdate.md) | Update the number of a client's trading account in the external system, with which the platform interacts via the specified gateway.  
[ExternalAccountDelete](IMTUser/ExternalAccountDelete.md) | Delete the number of a trading account in the external trading system by position.  
[ExternalAccountClear](IMTUser/ExternalAccountClear.md) | Clear client account numbers in external trading systems.  
[ExternalAccountTotal](IMTUser/ExternalAccountTotal.md) | Get the number of client's trading accounts in external trading systems.  
[ExternalAccountNext](IMTUser/ExternalAccountNext.md) | Get the number of a client's trading account in the external system and the ID of the gateway, through which the platform interacts with the system.  
[ExternalAccountGet](IMTUser/ExternalAccountGet.md) | Get the number of a client's trading account in the external system by the ID of the gateway, through which the platform interacts with the system.  
  
The IMTUser class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnUsersRights (#enusersrights)](IMTUser/Enumerations.md#enusersrights) | Flags of user permissions.  
[EnUsersPasswords (#enuserspasswords)](IMTUser/Enumerations.md#enuserspasswords) | Types of passwords.  
[EnUsersConnectionTypes (#enusersconnectiontypes)](IMTUser/Enumerations.md#enusersconnectiontypes) | Types of connections.
