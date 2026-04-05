import nmap
import json

#Setup is in venv
nmaptest = nmap.PortScanner()

target = "45.33.32.156" # scanme.nmap.org
nmaptest.scan(target, arguments="-sV -sC")

protocolDictionary = {} # Dynamic adjustment when looping through protocols
hostDictionary = {
    "HostName": target,
    "State": nmaptest[target].state(),
    "Protocols": protocolDictionary,
}

for protocol in nmaptest[target].all_protocols():
    ports = {}
    for port, state in nmaptest[target][protocol].items():
        port_info = {
            "state": state.get("state", ""),
            "name": state.get("name", ""),
            "product": state.get("product", ""),
            "version": state.get("version", "")
        }

        if "script" in state and state["script"]:
            port_info["script"] = state["script"]
        ports[port] = port_info #Add ports and port info dynamically to the dictionary

    protocolDictionary[protocol] = ports

with open("scan_res.json", "w") as f:
    json.dump(hostDictionary, f, indent=2) #Dump the whole filtered information to JSON

print(hostDictionary)

#Example data structure to store the data gathered (this is just make a mental sketch on how should it look like)
'''
dictionary = {
    "Hostname": "host",
    "State" : value,
    "Protocols": {
        "Udp": {
            "PortNumber": {
                "otherDetail" : value
            }
        }
        "Tcp": {
            "PortNumber": {
                #same stuff
            }
        }
    }
}
'''