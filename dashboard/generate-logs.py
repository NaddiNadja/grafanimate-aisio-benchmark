import random, time
from pathlib import Path


def generate_logs():
  """Generate synthetic logs to use for testing the Grafana dashboard"""

  def gettime(start):
    if not start:
      return time.time()
    
    epoch = int((time.time() - start) * 1000) / 1000
    return epoch
  
  ds = Path(__file__).parent / "data"
  Path.mkdir(ds, exist_ok=True)

  for source, mn, mx in [("aisio", 80, 85), ("gds", 20, 25), ("posix", 10, 12)]:
    with open(ds / f"{source}.log.csv", "w") as file:
      file.write("time,batches,iops,mib/s\n")

      start = gettime(0)
      i = 0
      while i < 1000:
        t = gettime(start)
        file.write(f"{t},{i},100,{i/(t or 0.000001)}\n")
        time.sleep(0.5)
        i += random.randint(mn,mx)

      t = gettime(start)
      file.write(f"{t},1000,100,{1000/t}\n")


if __name__ == "__main__":
  generate_logs()
