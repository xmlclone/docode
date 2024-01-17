from datasets import load_dataset, load_from_disk
from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")


# 如果数据量较大，建议使用 parquet 文件格式进行存储，处理起来会更高效

# 可以直接加载本地csv文件
dataset = load_dataset('csv', data_files='train.csv')
# 是一个DatasetDict对象
print(f"{dataset=}\n")

dataset = load_dataset('csv', 'train.csv', split='train')
# 是一个Dataset对象
print(f"{dataset=}\n{dataset[0]=}\n")
print(f"{dataset.split=}\n{dataset.features=}\n")


# 处理数据
def tokenization(data):
    return tokenizer(data['text'])
dataset = dataset.map(tokenization)
dataset.set_format(type="torch", columns=["input_ids", "token_type_ids", "attention_mask", "label"])
print(dataset)
# 保存数据
dataset.save_to_disk("dataset")

# 重新加载数据
dataset = load_from_disk("dataset")
print(f"{dataset=}\n{dataset[0]=}\n")

# 还可以导出为csv文件
dataset.to_csv("dataset/dataset.csv")

# 重新从csv文件导入
# 这里演示了另一种导入csv的方式
dataset = load_dataset('csv', data_dir='dataset', data_files={'train': 'dataset.csv'})
# 注意，这里仍然是一个DatasetDict对象
print(f"{dataset=}\n")