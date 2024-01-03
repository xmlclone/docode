# 下载

```sh
git clone https://github.com/THUDM/ChatGLM-6B.git

pip install -r requirements.txt

python web_demo.py

python cli_demo.py  # clear stop 
```

# 本地试用

```sh
# 在工程目录下创建THUDM目录，把下面代码克隆到此目录下
git clone https://huggingface.co/THUDM/chatglm-6b

# 配置离线参数
export TRANSFORMERS_OFFLINE=1
```

# py代码

```python
# 不管是cli还是web demo，py文件下均有以下代码，第一个参数其实就是模型文件的路径
# 指定为上面 git clone https://huggingface.co/THUDM/chatglm-6b 下载的路径即可(上面示例是按照下面路径配置的，所以这里不用变)
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
```

# cpu较弱

https://cloud.tsinghua.edu.cn/d/674208019e314311ab5c/?p=%2F&mode=list 这里下载 chatglm-6b-int4，修改上面py代码路径

> https://huggingface.co/THUDM/chatglm-6b-int4/tree/main 这里下载的才有config.json

```python
# 如果使用cpu(并且较弱的情况下)，代码需要改为如下
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4",trust_remote_code=True).float()
```


