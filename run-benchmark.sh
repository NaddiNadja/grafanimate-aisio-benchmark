#! /bin/bash

source .env

if [[ -z "$POSIX_HOST" ]]; then
  echo ""
else
  ssh root@$POSIX_HOST "echo 3 > /proc/sys/vm/drop_caches; stdbuf -oL sil /dev/nvme0n1 --root-dir train --mnt /mnt/nvme --batch-size 888 --batches 1000 --backend posix > /tmp/data-server/data.csv"
fi

if [[ -z "$GDS_HOST" ]]; then
  echo ""
else
  ssh root@$GDS_HOST "echo 3 > /proc/sys/vm/drop_caches; stdbuf -oL sil /dev/nvme0n1 --root-dir train --mnt /mnt/nvme --batch-size 888 --batches 1000 --backend gds > /tmp/data-server/data.csv"
fi

# and also AiSiO