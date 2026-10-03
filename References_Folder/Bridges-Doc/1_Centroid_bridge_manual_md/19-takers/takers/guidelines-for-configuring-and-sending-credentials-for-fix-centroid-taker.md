[🏠 Document Start](..\..\README.md) / [Takers](..\README.md) / [Takers](README.md) / Guidelines for Configuring and Sending Credentials for FIX Centroid Taker

# Guidelines for Configuring and Sending Credentials for FIX Centroid Taker

Overview
This guide covers the setup of a Centroid Taker on the specified bridge, detailing the steps needed to configure and activate it as part of
the centroid-to-centroid connection process.
Provisioning Fix Taker and Related Components
For provisioning steps related to the Fix Taker, Taker Feed, and Execution Model, please refer to the documentation at [insert path or
link].
Instructions for Sending Maker Credentials to FIX Takers
After adding your FIX Taker, follow these steps to send the necessary credentials:
1. Locate the Mailbox Icon
Find the small mailbox icon in the interface. Clicking it will open a pop-up window requesting the following information:
Your Company: This field is auto-filled based on your Bridge configuration. You can edit it if necessary.
Client Name: Enter the name of the FIX Taker (typically your client's name).
Client Email: Provide the client's email address where the credentials will be sent. Ensure this email is correct and active.
Ensure that Tag1 is correctly configured, as the absence of Tag1 will prevent the email from being sent.
Once you click the Proceed button, your taker client will receive an email with the subject: Maker Credentials from "Your Company Name".


Upon completing these steps, your Taker client will receive an email containing the required credentials. The next phase will be managed
on their end, where they will proceed to add you as a Maker. For further assistance, they can refer to the relevant documentation or reach
out to support.
Note: A bridge restart is required to activate the Taker
Note: Whitelisting is not required for Centroid-to-Centroid connections

