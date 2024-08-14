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
2. `Token`通常代表一个基本单元或被切割出来的一个片段，比如NLP里面，一个token一般就表示一个单词、字符、短语或任何被定义的文本单元；再比如情感分析中，某些厂商把整段文字作为一个token计费，而另外一个厂商会把文字分割后的单词，每个单词作为一个token计费，故并不是统一的标准。
3. `200K上下文`，即表示模型支持的上下文记忆/处理的`token`为`200,000个`
4. `6B` `8B`一般表示模型训练的参数数量，B表示Billion即10亿，比如6B代表有60亿个参数，更多的参数可以让模型具有更强的理解和生成能力。
5. `4bit量化`，即在神经网络中对权重和激活值位数影响的单位，通常使用32或64bit进行量化，但会占用较大的存储空间并增加计算量，通过降低量化值，可以在较少的设备上进行计算并提高推断速度，但是会损失精度。
6. `NLP` `AIGC` `LLM` `General Language Model (GLM)`
7. `LLM` Large Language Model，大语言模型，理解和生成人类语言

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
# (https://git-lfs.github.com)
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

## 模型

1. [视觉定位-可以根据描述在图片上的位置](https://www.modelscope.cn/models/damo/ofa_visual-grounding_refcoco_large_zh/summary/)
2. [文字识别-可解决图形文字验证码](https://www.modelscope.cn/models/damo/cv_convnextTiny_ocr-recognition-general_damo/summary)
3. [OFA介绍](https://modelscope.cn/docs/OFA_Tutorial)

## 模型评估

1. [中文基础模型评估套件 C-Eval](https://www.cevalbenchmark.com/index_zh.html)