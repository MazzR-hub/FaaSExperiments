# FaaSExperiments
A series of workflows and testing scripts for use with Microsoft Azure.

---

## Installation
Requires: Visual Studio Code, Azure Functions Extension, Python3

Each of the workflows needs to be deployed directly from Visual Studio Code in order to work. To do this, select the folder of the workflow you want to deploy, right click, and select
`open with code`

---
***Project folders***

Workflow One: FaaSExperiments

Workflow Two: Workflow_Two

Workflow Three: Workflow_Three

Workflow Five: Workflow_Five

Workflow Six: Workflow_Six

---
Once inside Azure, select the Azure Functions Extension, navigate to the "Local Project" to see the functions contained within the Project.

_Testing Locally_
Within the azure terminal, run:

Windows
`.venv\scripts\activate`

Linux
`source .venv/bin/activate`

Then run the following:

`python -m pip install -r requirements.txt`

Once this is complete, you should be able to run the function locally from inside the Functions Extension


## Using ClientScripts

Both the send_azure_requests.py and send_instance_requests.py can be used to send requests to a test function as required.

If running locally, the URL can be fetched from the terminal once the function has been deployed in VSCode.

Edit the function with the number of the workflow you would like to test, and update the URL to be that of the local function.