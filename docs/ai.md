[toc]

# 基础

## 文件格式

gguf
Safetensors

## 模型平台

ollama
xinference

## 推理引擎

vllm: linux优先推荐使用，是一个支持高并发的高性能大模型推理引擎。是基于pytorch
sglang: linux优先推荐使用。多模态优先推荐使用
llama.cpp: 资源有限情况下推荐使用，比如一些边缘设备上，比如嵌入式设备或移动终端。在vllm、sglang、MLX不支持的情况下推荐使用
transformers: 对于其它都不支持的情况下使用
MLX: mac上优先推荐使用，MLX-lm 用来在苹果 silicon 芯片上提供高效的 LLM 推理

## 量化

# 平台

## xinference

https://inference.readthedocs.io/zh-cn/latest/getting_started/using_xinference.html

```sh
docker pull registry.cn-hangzhou.aliyuncs.com/xprobe_xinference/xinference

docker tag registry.cn-hangzhou.aliyuncs.com/xprobe_xinference/xinference xprobe/xinference

# XINFERENCE_MODEL_SRC 指定模型仓库，默认是 HuggingFace ，当然也可以不指定后续通过webui界面选择
docker run -itd --name xi -v D:/dockermount/xinference:/root/.xinference -e XINFERENCE_HOME=/root/.xinference -e XINFERENCE_MODEL_SRC=modelscope -p 9998:9997 --gpus all xprobe/xinference xinference-local -H 0.0.0.0 --log-level debug

http://127.0.0.1:9998/ui
http://127.0.0.1:9998/docs

docker exec -it xi
```

## ollama

```sh
docker pull ollama/ollama
docker run --rm -it --gpus=all ollama/ollama
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

# 硬件与编码

## nvidia

```sh
nvidia-smi -l 3
```

## cuda & torch版本

```sh
# 稳定版看stable，其它可以看preview
https://pytorch.org/get-started/locally/s
```

```python
import torch
torch.device("cuda" if torch.cuda.is_available() else "cpu")
```