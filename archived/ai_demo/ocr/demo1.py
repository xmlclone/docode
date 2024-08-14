"""
# 如果无法安装，请确认python版本，比如我安装时，torch还不支持Python3.12
pip3 install torch==1.11.0 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
pip install modelscope
pip install opencv-python
pip install tf_slim
pip install --upgrade tensorflow==2.13.0
pip install pyclipper
pip install shapely
pip install keras


docker run --rm -it -v .:/opt/ws registry.cn-hangzhou.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-py310-torch2.1.2-tf2.14.0-1.13.1 /bin/bash

"""


from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
import cv2


ocr_recognition = pipeline(Tasks.ocr_recognition, model='damo/cv_convnextTiny_ocr-recognition-general_damo', device='cpu')
ocr_detection = pipeline(Tasks.ocr_detection, model='damo/cv_resnet18_ocr-detection-line-level_damo', device='cpu')

img_path = '1.png'
img = cv2.imread(img_path)


result = ocr_recognition(img)
print(result)

result = ocr_detection(img)
print(result)