[🏠 Document Start](..\README.md) / Stale Prices

# Stale Prices

Overview
Failover Makers is used to seamlessly and automatically switch to another stream of prices when the primary stream of prices fails due to
various reasons. This can also help to redirect trades in case of primary makers unavailability. This can be achieved through the use of the
“Stale Prices” module.
In its operations, the system captures the time of a symbol’s latest tick from a Maker and starts counting based on Warning and Error
Timeout, the following logic will be followed:
If no new quote has been received and the time exceeds the Warning Timeout, A Warning Alert will be triggered and sent by the
bridge.
If no new quote has been received and the time exceeds the Error Timeout, one of the following will happen:
If Switch to Failover is disabled, An Error Alert will be triggered.
If Switch to Failover is enabled, An Error Alert will be triggered, and one of the following can happen:
If Check LM is disabled, the system will immediately switch to Failover Maker and it will ignore the other makers available in the
Liquidity model.
If Check LM is enabled, the system will check first the other Makers in the Liquidity Model and one of the following can happen:
If the other Makers in the Liquidity Model are not streaming, the system will switch to Failover Maker.
If the other Makers in the Liquidity Model are streaming, the system will not switch to Failover Maker.
Setting up an Auto-failover
To setup an Auto-Failover we need to


1. Create a Symbol Profile → Refer to the Symbol Profile component for comprehensive documentation.
2. Create a Stale Rule → Refer to the Stale Rule component for comprehensive documentation.
3. Add a Failover Maker to the Liquidity Model → Refer to the Liquidity Model for comprehensive documentation.

