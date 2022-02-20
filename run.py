import os

with open("/model/run.sh", "w") as f:
    videos = os.listdir("/dataset")
    for video in videos:
        f.write(f"mkdir /results/{video}\n")
        f.write(f"python3 main_test_vrt.py --task 001_VRT_videosr_bi_REDS_6frames --folder_lq /dataset/{video} --results /results/{video} --tile 6 128 128 --tile_overlap 2 20 20\n")

os.system("sh /model/run.sh")
