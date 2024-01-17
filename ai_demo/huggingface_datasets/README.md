# 加载数据的方式

`load_dataset`加载huggingface上的dataset时，huggingface上可以是原始数据，也可以是一个脚本文件

```python
# 可以参考以下几个dataset的不同加载方式
# https://huggingface.co/datasets/allenai/c4     纯数据
# https://huggingface.co/datasets/eli5/tree/main 加载脚本
load_dataset(
    path, #huggingface或本地的dataset名称，下面基本一致，都是huggingface或本地 (还可以是一个py加载脚本或路径)
    data_dir, #加载数据集的路径
    data_files, #加载数据集的文件，可以是直接的文件名，也可以是 {train: file, test: file}格式的字典
    splite,
    trust_remote_code=True
)
```