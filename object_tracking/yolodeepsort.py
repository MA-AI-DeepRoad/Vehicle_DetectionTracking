#영상의 경로를 입력한 뒤->yolo관련 폴더로 이동시켜서 분석하기
def yolo_deepsort(img_route):
    !git clone --recurse-submodules https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet.git  # clone repo
    %pip install -qr requirements.txt  # install dependencies

    import torch
    from IPython.display import Image, clear_output  # to display images

    clear_output()
    print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

    #Download data
    from google.colab import drive
    drive.mount('/content/drive')

    %cd /content/Yolov5_StrongSORT_OSNet

    #비디오 경로 변경
    import shutil
    shutil.copy(img_route, '/content/Yolov5_StrongSORT_OSNet/out.avi')
    #!yes | ffmpeg -ss 00:00:01 -i nayoung.avi -t 00:00:15 -c copy out.avi

    #module 'yaml' has no attribute 'FullLoader'
    !pip install -U PyYAML

    #run github algorithm
    !python track.py --img 1280 --yolo-weights /content/Yolov5_StrongSORT_OSNet/yolov5/yolov5m.pt --strong-sort-weights osnet_x0_25_msmt17.pt --source out.avi --conf-thres 0.5 --save-vid --save-crop
