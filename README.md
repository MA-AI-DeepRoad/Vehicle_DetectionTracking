# Vehicle_DetectionTracking

> folder: object_tracking: 실행전 작업: "/Yolov5_StrongSORT_OSNet/strong_sort/configs" 경로의 strong_sort.yaml 수정 필요.
STRONGSORT:
  ECC: True              # activate camera motion compensation
  MC_LAMBDA: 0.995       # matching with both appearance (1 - MC_LAMBDA) and motion cost
  EMA_ALPHA: 0.9         # updates  appearance  state in  an exponential moving average manner
  MAX_DIST: 0.15          # The matching threshold. Samples with larger distance are considered an invalid match
  MAX_IOU_DISTANCE: 0.7  # Gating threshold. Associations with cost larger than this value are disregarded.
  MAX_AGE: 15            # Maximum number of missed misses before a track is deleted
  N_INIT: 3              # Number of frames that a track remains in initialization phase
  NN_BUDGET: 100         # Maximum size of the appearance descriptors gallery
