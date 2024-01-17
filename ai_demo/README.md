# 安装

```sh
# 如果无法安装，请确认python版本，比如我安装时，torch还不支持Python3.12
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118x

pip install transformers
pip install datasets
pip install soundfile
pip install librosa

pip install matplotlib

pip install torchtext
pip install portalocker
```

# 基础目录

1. windows下自动下载的模型等数据一般在`C:\Users\<username>\.cache\huggingface`目录下，可以通过设置环境变量`HF_HOME`来配置目录

# 基础名词

1. `Tokenizers`，分词器，是`NLP`的重要概念，把连续的字符分割为离散的单元的一种算法或工具。Tokenizer的作用是将文本转化为模型能够理解和处理的离散编码序列，可以进行分词、建立词表、编码和反编码。

# repo

You can create a repository from the CLI (skip if you created a repo from the website)

```sh
$ pip install huggingface_hub
# You already have it if you installed transformers or datasets

$ huggingface-cli login
# Log in using a token from huggingface.co/settings/tokens
# Create a model or dataset repo from the CLI if needed
$ huggingface-cli repo create repo_name --type {model, dataset, space}
```

Clone your model, dataset or Space locally

```sh
# Make sure you have git-lfs installed
(https://git-lfs.github.com)
$ git lfs install
$ git clone https://huggingface.co/username/repo_name
```

Then add, commit and push any file you want, including larges files

```sh
# save files via `.save_pretrained()` or move them here
$ git add .
$ git commit -m "commit from $USER"
$ git push
```

In most cases, if you're using one of the compatible libraries, your repo will then be accessible from code, through its identifier: username/repo_name

For example for a transformers model, anyone can load it with:

```python
tokenizer = AutoTokenizer.from_pretrained("username/repo_name")
model = AutoModel.from_pretrained("username/repo_name")
```

# 参考链接

## huggingface

1. [环境变量](https://huggingface.co/docs/huggingface_hub/main/en/package_reference/environment_variables)

## modelscope

1. [魔搭](https://www.modelscope.cn/home)
2. [魔搭github](https://github.com/modelscope/modelscope)