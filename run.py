import os
import json

if os.path.isfile("/model/config.json"):
    with open("/model/config.json", "r") as f:
        data = json.load(f)
    options = data['options']
else:
    options = "--tile 6 128 128 --tile_overlap 2 20 20"

with open("/model/run.sh", "w") as f:
    f.write(f"python3 /model/main_test_vrt.py --task 001_VRT_videosr_bi_REDS_6frames --folder_lq /dataset --results /results {options}\n")

os.system("sh /model/run.sh")
