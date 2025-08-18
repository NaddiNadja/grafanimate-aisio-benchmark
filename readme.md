# Grafana dashboard for benchmark results

This is a small setup for animating a benchmarking dashboard for AiSiO, GDS, POSIX and
BaM. The `docker-compose.yaml` hosts a dockerised version of Grafana and a dockerised
dashboard server, which provides the local data-sources and a web interface embedding the
provided dashboard. It is all behind a reverse proxy and can be accessed at
`http://localhost`.

## Data sources

The dashboard expects three data sources, which are three independent processes running
the Flask server in `./data-server/server.py`. If run locally, nginx expects the servers
to be hosted on ports 4000 (POSIX), 4001 (GDS) and 4002 (AiSiO). If run on external
hosts, nginx expects the servers to be hosted on port 4000 for each.

The server can be run with:

```sh
usage: server [-h] [--data-path DATA_PATH]
              [--time-column TIME_COLUMN]
              [--port PORT]

options:
  -h, --help            show this help message
                        and exit
  --data-path DATA_PATH, -d DATA_PATH
                        Path to to the data
                        source CSV (default:
                        data.csv)
  --time-column TIME_COLUMN, -t TIME_COLUMN
                        Name of the CSV column
                        indicating time in
                        milliseconds (default:
                        Time)
  --port PORT, -p PORT  Port to host the Flask
                        server on (default:
                        4000)
```

### Run on external hosts

Change the config `./nginx/nginx.conf` under locations `/posix`, `/gds` and `/aisio` to
use the outcommented `proxy_pass`es, e.g. `proxy_pass http://aisio:4000/data`. In a
`.env` file define the variables `POSIX_HOST`, `GDS_HOST`, and `AISIO_HOST` with the IP
address for each. The provided script `run-server.py` can be used to provision a host on
a specific port (default: 4000).

```sh
./run-server POSIX
# or
./run-server GDS 4001
```

The `./run-benchmark.sh` script is WIP, but should start the sil benchmarking tool on the
hosts defined in `.env`. The commands necessary to run on the hosts are:

```sh
echo 3 > /proc/sys/vm/drop_caches # clear cache
stdbuf -oL sil <drive> --root-dir train --mnt /mnt/nvme --batch-size 888 --batches 1000 --backend <gds or posix> > /tmp/data-server/data.csv
```

### Run locally

To run locally (e.g. for testing), the `generate-logs.py` helper script can be used to
generate artificial logs in a `./data` subdirectory. Run the following commands in each
their own command line.

```sh
python generate-logs.py
python server.py --data-path ./data/posix.csv --port 4000
python server.py --data-path ./data/gds.csv --port 4001
python server.py --data-path ./data/aisio.csv --port 4002
```

The `generate-logs.py` script can be used to restart the simulation of running the
benchmarks while viewing the dashboard.

## Run

To view the dashboard, run

```sh
docker compose up --build
```

and go to `http://localhost`.
