import os

with open("/model/run.sh", "w") as f:
    f.write(f"python3 /model/main_test_vrt.py --task 001_VRT_videosr_bi_REDS_6frames --folder_lq /dataset --results /results --tile 6 128 128 --tile_overlap 2 20 20\n")

os.system("sh /model/run.sh")
