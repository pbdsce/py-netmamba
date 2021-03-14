# NetMamba
Scan for hosts in a network.

## Basic Information
NetMamba scans for hosts connected to a network by creating an ARP packet that is broadcasted to the network. Sudo privilege is required to broadcast this.
The devices connected to the network respond back with their IP and MAC addresses.

## How to run

- Using `curl`:
    ```bash
    #From github
    curl https://raw.githubusercontent.com/hariomch/py-netmamba/main/netscan.py -o netscan.py
    sudo python3 netscan.py -t [NETWORK-IP]
    ```
- Cloning Repo:

    ```bash
    # Clone repo
    git clone 'https://github.com/hariomch/py-netmamba.git'
    cd py-netmamba
    sudo python3 netscan.py -t [NETWORK-IP]
    ```
    another way:
    ```bash
    git clone 'https://github.com/hariomch/py-netmamba.git'
    cd py-netmamba
    chmod +x netscan.py
    sudo ./netscan.py -t [NETWORK-IP]
    ```

## Usage

| Flag | Description |
|-|-|
| -h (--help) | Displays the usage of NetMamba |
| -t (--target) | Accepts the network IP in CIDR format to be scanned. |
