- [ollama](https://ollama.com/search)
- [ollama-github](https://github.com/ollama/ollama)

# 常用命令

```sh
ollama pull deepseek-r1
ollama run deepseek-r1

ollama ps
ollama list
```

# 常用配置

```sh
# 可以通过配置下面的环境变量，设定 ollama 下载模型的路径
OLLAMA_MODELS
```

# docker

```sh
docker pull ollama/ollama
docker run --rm -it --gpus=all ollama/ollama
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# 如果通过 docker 启动的, ollama 服务一般配置为如下url：
http://host.docker.internal:11434
```

# 进阶

```sh
# 导出配置，修改里面 FROM 指令对应的路径，可以指定为gguf文件路径
ollama show --modelfile qwq > Modelfile
# 比如gguf文件下载： https://www.modelscope.cn/models/modelscope/Qwen2.5-7B-Instruct-1M-GGUF/files

# 自定义模型
ollama create Qwen2.5-7B-Instruct-1M-FP16 -f Modelfile
```