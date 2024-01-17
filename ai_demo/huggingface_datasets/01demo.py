from datasets import load_dataset
from transformers import AutoTokenizer


dataset = load_dataset("rotten_tomatoes", split="train")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


print(f"{tokenizer(dataset[0]['text'])=}\n")


# 可以使用map对数据集进行批量处理
def tokenization(data):
    return tokenizer(data['text'])
dataset = dataset.map(tokenization, batched=True)
print(f"{dataset=}\n{dataset[0]=}\n")


# 上面通过tokenizer转换后，其实是python格式的数据，比如字典+列表格式
# 需要把数据转换为对应框架(比如pytorch tensorflow)等可以识别的格式
# 并且只保留指定的数据，经过下面方式处理后的数据才可以被对应的框架进行训练
# set_format改变的是原始dataset，可以使用with_format返回一个新的dataset而不影响原始的dataset
# 如果使用set_format后想恢复原始的，可以通过dataset.reset_format()恢复
dataset.set_format(type="torch", columns=["input_ids", "token_type_ids", "attention_mask", "label"])
print(f"{dataset=}\n{dataset[0]=}\n")