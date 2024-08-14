from datasets import (
    load_dataset,
    load_dataset_builder,
    get_dataset_config_names,
    get_dataset_split_names,
)
import time

ds_name = "PolyAI/minds14"

ds_builder = load_dataset_builder(ds_name, "all")
# features其实就是每列的列信息，是一个字典，key是列名，指表示数据类型等信息
print(f"{ds_builder.info.description=}\n{ds_builder.info.features=}\n")

# config name类似于上面的features，如果数据集存在config name，部分函数是必须要传递这个参数的，比如下面的get_dataset_split_names和load_dataset
# 就是网页上subset字段下可选值
cp_name = get_dataset_config_names(ds_name)
print(f"{cp_name=}\n")

# 就是网页上split字段下的可选值
sp_name = get_dataset_split_names(ds_name, "all")
print(f"{sp_name=}\n")

# 如果上面的config存在，则必须传递，比如zh-CN all等
# 如果不传递split参数，则会返回所有，但是会以字典形式返回，否则只返回传递了split的实际内容
dataset = load_dataset(ds_name, "zh-CN")
print(f"{dataset=}\n")

dataset = load_dataset(ds_name, "zh-CN", split="train")
# 注意，如果没有使用split，下面是无法使用dataset[0]的，因为返回的是一个字典，类似{test: value, train: value}，即DatasetDict对象
# 如果指定了train，则返回的是字典train对应的value，才可以使用dataset[0]的方式进行访问，即Dataset对象
print(f"{dataset=}\n{dataset[0]=}\n{dataset[0]['transcription']=}\n")
# print(f"{dataset['transcription']=}\n")

# 对比两种访问数据的耗时(注意第一个耗时如果前面没有对数据进行访问，可能会有其它耗时，故前面一定有其它数据访问后，在进行对比，否则对比没有意义)
start_time = time.time()
print(dataset[0]['transcription'])
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.4f} seconds")
# 不建议用下面的方式，耗时较长
start_time = time.time()
print(dataset['transcription'][0])
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.4f} seconds")