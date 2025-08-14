# Grafana dashboard animation

This is a small setup for animating a benchmarking dashboard for AiSiO, GDS, POSIX and
BaM. The `docker-compose.yaml` hosts a dockerised version of Grafana, which is available
at `localhost:3000`, and a dockerised server, which provides the local data-sources.

## Data sources

The data sources should be provided as `.csv` in the `./data-source/data` directory with
three named columns: `epoch,value`. The `./data-souce/generate-logs.py` script is
provided to generate "dummy data" for the dashboard.

It is expected that all data sources, except `synthetic.log.csv`, start at epoch 0.

Ensure that the `end` variable in `./grafanimate/grafana-play.py` is at least equal to
the largest time value in your data sources.

## Running grafanimate

You can create the animation in two ways: (a) Running the `docker-compose.yaml` and waiting
for the grafanimate container to have produced the animation, or (b) by running the
`docker-compose.yaml` and running the grafanimate scenario locally.

### Using Docker

This is the easiest, but the animation is not smooth. It is just a sequence of screenshots.

1. Run:

    ```sh
    docker compose up --build
    ```

1. Wait until grafanimate exits. The animation will be placed in 
   `./grafanimate/animations`.

### Running grafanimate locally

By running it locally, the created animation will still be a sequence of screenshots,
but you will be able to a screen recording of the smooth transitions.

#### Prerequisites

1. [FFmpeg](https://ffmpeg.org/)

1. [Firefox](https://www.firefox.com/da/)

    - If grafanimate cannot find Firefox, you need to set the `FIREFOX_BIN` environment
      variable.

1. My fixed version of [grafanimate](https://github.com/naddinadja-forks/grafanimate).

    - Clone the git repo, switch to branch `fixes` and run

        ```sh
        pip install .
        ```

#### Run

1. (Optional) Start some kind of screen recording software if you wish to record
   the screen.

1. Use the following command to create the animation.

    ```sh
    grafanimate --scenario=./grafanimate/grafana-play.py:play --output=./grafanimate/animations
    ```

    - As default, the `./grafanimate/grafana-play.py` script includes 20 seconds of
      "nothing" before the animation begins. This time can be used to set the right
      window size and start the recording software.
