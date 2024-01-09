from transformers import pipeline, AutoModel, AutoTokenizer
from transformers import (
    AutomaticSpeechRecognitionPipeline,
    TextGenerationPipeline,
    QuestionAnsweringPipeline,
    DistilBertModel,
    DistilBertTokenizerFast,
    DistilBertForQuestionAnswering,
)
import torch
from torch import nn


# transcriber: AutomaticSpeechRecognitionPipeline = pipeline(task="automatic-speech-recognition")
# ret = transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
# print(ret)


# transcriber: AutomaticSpeechRecognitionPipeline = pipeline(model="openai/whisper-large-v2")
# ret = transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac")
# print(ret)


# 根据提示内容补充完整后输出
# pipe: TextGenerationPipeline = pipeline(model="gpt2")
# ret = pipe("你好，请用中文")
# print(ret[0]['generated_text'])


# 根据上下文的提示信息回答问题
# context = r"""My name is Wolfgang and I live in Berlin"""
# pipe: QuestionAnsweringPipeline = pipeline(task="question-answering")
# ret = pipe(question="Where do I live?", context=context)
# print(ret)


# 直接指定model和tokenizer
# model: DistilBertModel = DistilBertForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")
# tokenizer: DistilBertTokenizerFast = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
# context = r"""My name is Wolfgang and I live in Berlin"""
# pipe: QuestionAnsweringPipeline = pipeline(task="question-answering", model=model, tokenizer=tokenizer)
# ret = pipe(question="Where do I live?", context=context)
# print(ret)


# question, context = "Where do I live?", "My name is Wolfgang and I live in Berlin"
# model: DistilBertModel = DistilBertForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")
# tokenizer: DistilBertTokenizerFast = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
# inputs = tokenizer(question, context, return_tensors="pt")
# print(inputs) # 输出 'input_ids' 'attention_mask'等
# print(tokenizer.decode(inputs["input_ids"][0])) # 反编码为我原始数据
# outputs = model(**inputs)
# print(outputs)
# pt_predictions = nn.functional.softmax(outputs.end_logits, dim=-1)
# print(pt_predictions)
# with torch.no_grad():
#     outputs = model(**inputs)
# print(outputs)

# 上面微调后保存我们的模型，后续可以直接加载我们的模型进行使用
# pt_save_directory = "./pt_save_pretrained"
# tokenizer.save_pretrained(pt_save_directory)
# model.save_pretrained(pt_save_directory)

# 直接加载我们的模型进行使用
# model: DistilBertModel = DistilBertForQuestionAnswering.from_pretrained("./pt_save_pretrained")
# tokenizer: DistilBertTokenizerFast = AutoTokenizer.from_pretrained("./pt_save_pretrained")
# context = r"""My name is Wolfgang and I live in Berlin"""
# pipe: QuestionAnsweringPipeline = pipeline(task="question-answering", model=model, tokenizer=tokenizer)
# ret = pipe(question="Where do I live?", context=context)
# print(ret)


# pipe = pipeline(model="THUDM/chatglm-6b", trust_remote_code=True)
# print(pipe)