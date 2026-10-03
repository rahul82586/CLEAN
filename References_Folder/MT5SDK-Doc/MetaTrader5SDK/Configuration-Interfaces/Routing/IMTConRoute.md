[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Routing](../Routing.md) / IMTConRoute

[Previous](../Routing.md) | [Next](IMTConRoute/Enumerations.md)

# IMTConRoute

The IMTConRoute class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTConRoute/Release.md) | Deletes the current object.  
[Assign](IMTConRoute/Assign.md) | Assigns a passed object to the current one.  
[Clear](IMTConRoute/Clear.md) | Clears an object.  
[Name](IMTConRoute/Name.md) | Gets and sets the name of a routing rule.  
[Mode](IMTConRoute/Mode.md) | Gets and sets the state of a routing rule.  
[Request](IMTConRoute/Request.md) | Gets and sets the types of requests for which the rule is applicable.  
[Type](IMTConRoute/Type.md) | Gets and sets the types of orders for which the rule is applicable.  
[Action](IMTConRoute/Action.md) | Gets and sets the type of action that is applied to a request in accordance with a rule.  
[ParamType](IMTConRoute/ParamType.md) | Gets the type of an additional parameter for a routing rule.  
[ParamInt](IMTConRoute/ParamInt.md) | Gets and sets the value of an additional parameter of the INT type.  
[ParamUInt](IMTConRoute/ParamUInt.md) | Gets and sets the value of an additional parameter of the UINT type.  
[ParamDouble](IMTConRoute/ParamDouble.md) | Gets and sets the value of an additional parameter of the double type.  
[ParamString](IMTConRoute/ParamString.md) | Gets and sets the value of an additional parameter of the string type.  
[ParamColor](IMTConRoute/ParamColor.md) | Gets and sets the value of an additional parameter of the colorref type.  
[ParamMoney](IMTConRoute/ParamMoney.md) | Gets and sets the value of an additional parameter that expresses the amount of money.  
[ParamVolume](IMTConRoute/ParamVolume.md) | Gets and sets the value of an additional parameter that expresses the volume.  
[ParamVolumeExt](IMTConRoute/ParamVolumeExt.md) | Gets and sets the value of an additional parameter that expresses the volume with extended accuracy.  
[ParamDatetime](IMTConRoute/ParamDatetime.md) | Gets and sets the value of an additional parameter that expresses date and time.  
[ParamLeverage](IMTConRoute/ParamLeverage.md) | Gets and sets the value of an additional parameter that expresses the leverage.  
[ParamBool](IMTConRoute/ParamBool.md) | Gets and sets the value of an additional parameter of the bool type.  
[ParamTime](IMTConRoute/ParamTime.md) | Gets and sets the value of an additional parameter that expresses the time.  
[ConditionAdd](IMTConRoute/ConditionAdd.md) | Adds an additional condition to apply a rule.  
[ConditionUpdate](IMTConRoute/ConditionUpdate.md) | Changes an additional condition to apply a rule at the specified position.  
[ConditionDelete](IMTConRoute/ConditionDelete.md) | Deletes an additional condition to apply a rule at the specified position.  
[ConditionClear](IMTConRoute/ConditionClear.md) | Clears the list of all additional conditions to apply a rule.  
[ConditionShift](IMTConRoute/ConditionShift.md) | Moves an additional condition of rule application in the list.  
[ConditionTotal](IMTConRoute/ConditionTotal.md) | Gets the number of additional conditions for applying a routing rule.  
[ConditionNext](IMTConRoute/ConditionNext.md) | Gets an additional condition to apply a rule by its index.  
[DealerAdd](IMTConRoute/DealerAdd.md) | Adds a dealer to whom requests under the conditions of this rule will be sent for processing.  
[DealerUpdate](IMTConRoute/DealerUpdate.md) | Updates a dealer to whom requests under the conditions of this rule will be sent for processing.  
[DealerDelete](IMTConRoute/DealerDelete.md) | Deletes an entry of a dealer to whom requests under the conditions of this rule will be sent for processing.  
[DealerClear](IMTConRoute/DealerClear.md) | Clears the list of dealers to whom requests under the conditions of this rule will be sent for processing.  
[DealerShift](IMTConRoute/DealerShift.md) | Moves an entry of a dealer to whom requests under the conditions of this rule will be sent for processing.  
[DealerTotal](IMTConRoute/DealerTotal.md) | Gets the total number of entries of dealers to whom requests under the conditions of this rule will be sent for processing.  
[DealerNext](IMTConRoute/DealerNext.md) | Gets a dealer entry in a routing rule by the index.  
[DealerGet](IMTConRoute/DealerGet.md) | Gets a dealer entry in a routing rule by the login.  
  
The IMTConRoute class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnRouteMode (#enroutemode)](IMTConRoute/Enumerations.md#enroutemode) | State of the rule.  
[EnRouteFlags (#enrouteflags)](IMTConRoute/Enumerations.md#enrouteflags) | Conditions of the request type.  
[EnTypeFlags (#entypeflags)](IMTConRoute/Enumerations.md#entypeflags) | Conditions of the order type.  
[EnRouteAction (#enrouteaction)](IMTConRoute/Enumerations.md#enrouteaction) | Types of actions applicable to the requests.
