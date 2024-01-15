from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

encoded_input = tokenizer([
    "ni hao",
    "wo hao",
    "dajia hao",
    "feichang hao"
], return_tensors="pt", padding=True)
print(encoded_input)

output = tokenizer.decode(encoded_input["input_ids"][0])
print(output)