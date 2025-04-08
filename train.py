import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
 
if __name__ == '__main__':
    model = YOLO(r'/root/autodl-tmp/UAVD-Mamba/UAVD-Mamba/datasets/UAVD-Mamba.yaml') 
    model.train(data=r'/root/autodl-tmp/UAVD-Mamba/UAVD-Mamba/datasets/single.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                single_cls=False, 
                batch=8,
                close_mosaic=10,
                workers=16,
                device='0',
                optimizer='SGD',
                amp=True,
                project='runs/train',
                name='exp',
                )
