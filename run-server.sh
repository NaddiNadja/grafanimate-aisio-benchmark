#! /bin/bash

source .env

backend=$1

if [ "$backend" != "POSIX" ] && [ "$backend" != "GDS" ] && [ "$backend" != "AISIO" ]; then
    echo "Error: First argument must be either POSIX, GDS or AISIO"
    echo "Usage: $0 {POSIX,GDS,AISIO} <port>"
    exit 1
fi

host="${backend}_HOST"
port=${2:-"4000"}

echo "Provisioning host at ${!host}"
ssh root@${!host} "mkdir /tmp/data-server"
scp ./data-server/server.py root@${!host}:/tmp/data-server
scp ./data-server/requirements.txt root@${!host}:/tmp/data-server
# we need to also provision the necessary git repositories and install sil.

ssh root@${!host} "cd /tmp/data-server; python3 -m venv .venv; source .venv/bin/activate; python3 -m pip install --upgrade pip; python3 -m pip install -r requirements.txt; python3 server.py --data-path /tmp/data-server/data.csv --port $port"

kill_server() {
    ssh root@${!host} "pkill -f server.py"
}

trap kill_server EXIT INT TERM
