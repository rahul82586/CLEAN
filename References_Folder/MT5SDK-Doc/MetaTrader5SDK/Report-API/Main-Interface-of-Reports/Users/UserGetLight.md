[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Users](../Users.md) / UserGetLight

[Previous](UserGet.md) | [Next](UserLogins.md)

# IMTReportAPI::UserGetLight

Get the client record brief description.
    
    
    MTAPIRES  IMTReportAPI::UserGetLight(
       const UINT64  login,     // Client login
       IMTUser       *user      // An object of the client record
       )

### Parameters

**login**  
[in] The login of a user.

***user**  
[out] An object of the client login. The user object must first be created using theIMTReportAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Request for eased record allows to save resources. This method transfers the following user parameters:

  * [IMTUser::Login](../../../Database-Interfaces/Users/IMTUser/Login.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Group](../../../Database-Interfaces/Users/IMTUser/Group.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Rights](../../../Database-Interfaces/Users/IMTUser/Rights.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Registration](../../../Database-Interfaces/Users/IMTUser/Registration.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[LastAccess](../../../Database-Interfaces/Users/IMTUser/LastAccess.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[LastIP](../../../Database-Interfaces/Users/IMTUser/LastIP.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Name](../../../Database-Interfaces/Users/IMTUser/Name.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Language](../../../Database-Interfaces/Users/IMTUser/Language.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Leverage](../../../Database-Interfaces/Users/IMTUser/Leverage.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Balance](../../../Database-Interfaces/Users/IMTUser/Balance.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Credit](../../../Database-Interfaces/Users/IMTUser/Credit.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[InterestRate](../../../Database-Interfaces/Users/IMTUser/InterestRate.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[CommissionDaily](../../../Database-Interfaces/Users/IMTUser/CommissionDaily.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[CommissionMonthly](../../../Database-Interfaces/Users/IMTUser/CommissionMonthly.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[CommissionAgentDaily](../../../Database-Interfaces/Users/IMTUser/CommissionAgentDaily.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[CommissionAgentMonthly](../../../Database-Interfaces/Users/IMTUser/CommissionAgentMonthly.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[BalancePrevDay](../../../Database-Interfaces/Users/IMTUser/BalancePrevDay.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[BalancePrevMonth](../../../Database-Interfaces/Users/IMTUser/BalancePrevMonth.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[EquityPrevDay](../../../Database-Interfaces/Users/IMTUser/EquityPrevDay.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[EquityPrevMonth](../../../Database-Interfaces/Users/IMTUser/EquityPrevMonth.md)
  * [IMTUser::](../../../Database-Interfaces/Users/IMTUser/Login.md)[Agent](../../../Database-Interfaces/Users/IMTUser/Agent.md)
  * [IMTUser::ExternalAccount](../../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md)
  * [IMTUser::MQID](../../../Database-Interfaces/Users/IMTUser/MQID.md)
  * [IMTUser::PasswordHash](../../../Database-Interfaces/Users/IMTUser/PasswordHash.md)
  * [IMTUser::CertSerialNumber](../../../Database-Interfaces/Users/IMTUser/CertSerialNumber.md)


