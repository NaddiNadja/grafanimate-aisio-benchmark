# Grafana dashboard for benchmark results

This is a small setup for animating a benchmarking dashboard for AiSiO, GDS, POSIX and
BaM. The `docker-compose.yaml` hosts a dockerised version of Grafana and a dockerised
dashboard server, which provides the local data-sources and a web interface embedding the
provided dashboard. It is all behind a reverse proxy and can be accessed at
`http://localhost`.

## Data sources

The data sources should be provided as `.csv` in the `./dashboard/data` directory with
three named columns: `epoch,value`. The `./dashboard/generate-logs.py` script is
provided to generate "dummy data" for the dashboard.

## Run

To view the dashboard, run

```sh
docker compose up --build
```

and go to `http://localhost`.
