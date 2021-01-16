#!/bin/bash
# Author:        Andrew St Clair
# Usage:         ./routes-add.sh [interface]
# Example:       ./routes-add.sh wlan0
# Description:   add ip routes for ip addresses that resolve for a domain name to a specific interface

# Check if script is being run as root. we need root permissions to add routes
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

# Define function to add routes to kernel routes table
function add-route() {
    nslookup $1 | sed -n -e '/Non-authoritative/,$p' | grep Address | cut -d " " -f 2 | while read line ; do ip route add $line dev $2 ; done
}

# Finally run function for domain (or multiple domains if you wish, just duplicate the line changing the domain)
add-route www.example.com $1