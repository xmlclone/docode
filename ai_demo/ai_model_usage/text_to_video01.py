"""
pip install modelscope==1.4.2
pip install open_clip_torch
pip install pytorch-lightning
pip install opencv-python
pip install tensorflow

https://huggingface.co/ali-vilab/modelscope-damo-text-to-video-synthesis
"""


from huggingface_hub import snapshot_download

from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys
import pathlib
import torch
import paramiko


# 由于本地没有GPU，使用的是远程GPU，远程无法链接终端，需要把生成的视频传输到本地一个可以链接终端的服务器后使用
hostname = '47.109.110.64'
username = 'root'
password = 'win@xp@1'


model_dir = pathlib.Path('weights')
snapshot_download('damo-vilab/modelscope-damo-text-to-video-synthesis',
                   repo_type='model', local_dir=model_dir)
pipe = pipeline('text-to-video-synthesis', model_dir.as_posix(), map_location=torch.device('cpu'))
test_text = {
        'text': '一个人在打篮球.',
    }
output_video_path = pipe(test_text,)[OutputKeys.OUTPUT_VIDEO]
print('output_video_path:', output_video_path)


with paramiko.SSHClient() as client:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, username=username, password=password)
    with client.open_sftp() as sftp:
        sftp.put(output_video_path, output_video_path)