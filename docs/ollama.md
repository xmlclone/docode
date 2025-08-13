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
# ollama服务地址，配置的模型名称，使用 ollama pull 时的名称即可，注意带上 tag（ latest 不用）
http://localhost:11434
http://127.0.0.1:11434
# 有一方通过 docker 启动，另外一方非 docker 启动的情况下，URL 配置如下：
http://host.docker.internal:11434

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