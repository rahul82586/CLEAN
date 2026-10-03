[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Gateways](../../Gateways.md) / [IMTConGatewayModule](../IMTConGatewayModule.md) / Enumerations

[Previous](../IMTConGatewayModule.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The IMTConGatewayModule class contains one enumeration:

<a id="engatewayfieldmask"></a>
## IMTConGatewayModule::EnGatewayFieldMask (#engatewayfieldmask)

The editable fields of the gateway configuration are listed in IMTConGatewayModule::EnGatewayFieldMask.

ID | Value | Description  
GATEWAY_FIELD_SERVER | 1 | The "Server" field.  
GATEWAY_FIELD_LOGIN | 2 | The "Login" field.  
GATEWAY_FIELD_PASS | 4  | The "Password" field.  
GATEWAY_FIELD_PARAM | 8 | The "Parameters" field.  
GATEWAY_FIELD_NONE | 0 | Beginning of enumeration. It corresponds to the absence of editable fields.  
GATEWAY_FIELD_ALL |  | End of enumeration. It corresponds to the fact that all fields are editable.  
  
This enumeration is used in the [IMTConGatewayModule::Fields](Fields.md) method.
