# 安装

```sh
# 如果无法安装，请确认python版本，比如我安装时，torch还不支持Python3.12
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118x

pip install transformers
pip install datasets
pip install soundfile
pip install librosa

pip install matplotlib
```

# 基础目录

1. windows下自动下载的模型等数据一般在`C:\Users\<username>\.cache\huggingface`目录下

# 基础名词

1. `Tokenizers`，分词器，是`NLP`的重要概念，把连续的字符分割为离散的单元的一种算法或工具。