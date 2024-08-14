from transformers import (
    pipeline, 
    TextClassificationPipeline,
    DistilBertForSequenceClassification,
    DistilBertTokenizerFast
)
from transformers.pipelines import SUPPORTED_TASKS
import torch


# pipeline第一个参数是task，其它参数都可以不用传，model和tokenizer会自动加载默认的
# sentiment-analysis 和 text-classification一样，返回一个 TextClassificationPipeline
# SUPPORTED_TASKS 里面定义了默认的task和model关联关系
# 比如下面这个情感分析任务的默认model用的就是: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
# pipeline会初始化TextClassificationPipeline，传递了DistilBertForSequenceClassification模型，DistilBertTokenizerFast分词器
classifier: TextClassificationPipeline = pipeline("sentiment-analysis")
# 在调用classifier时，其实也是调用了tokenizer和model进行处理，然后传递给model，最后输出可阅读的数据
result = classifier('I like the dog.')
print(f"{result=}\n")


# 上面的pipeline基本等同于下面的代码
model: DistilBertForSequenceClassification = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
tokenizer: DistilBertTokenizerFast = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
inputs = tokenizer('I like the dog.', return_tensors="pt")
print(f"{inputs=}\n")
with torch.no_grad():
    logits = model(**inputs).logits
    print(f"{logits=}\n")
argmax = logits.argmax()
print(f"{argmax=}\n")
predicted_class_id = argmax.item()
print(f"{predicted_class_id=}\n")
label = model.config.id2label[predicted_class_id]
print(f"{label=}\n")


# 也可以结合使用
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
print(classifier('I like the dog.'))
