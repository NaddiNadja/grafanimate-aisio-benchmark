import os
from grafanimate.animations import AnimationSequence
from grafanimate.scenarios import AnimationScenario, SequencingMode

def play():
    host = os.getenv("GRAFANA_HOST") or "localhost"
    start = int(os.getenv("ANIMATION_START") or -20)
    end = 92

    return AnimationScenario(
        grafana_url=f"http://{host}:3000/",
        dashboard_uid="c83d24b6-3bf5-4963-9a71-6f1676d75f0e",
        sequences=[
            AnimationSequence(
                start=start,
                stop=end,
                every="1sec",
                mode=SequencingMode.WINDOW,
            ),
        ],
    )