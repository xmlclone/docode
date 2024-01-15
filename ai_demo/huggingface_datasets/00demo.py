from datasets import (
    load_dataset,
    load_dataset_builder,
    get_dataset_config_names,
    get_dataset_split_names,
)
import time

ds_name = "PolyAI/minds14"

ds_builder = load_dataset_builder(ds_name, "all")
print(f"{ds_builder.info.description=}\n{ds_builder.info.features=}\n")

cp_name = get_dataset_config_names(ds_name)
print(f"{cp_name=}\n")

sp_name = get_dataset_split_names(ds_name, "all")
print(f"{sp_name=}\n")

dataset = load_dataset(ds_name, "zh-CN")
print(f"{dataset=}\n")

dataset = load_dataset(ds_name, "zh-CN", split="train")
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