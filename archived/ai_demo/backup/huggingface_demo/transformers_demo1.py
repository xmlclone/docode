from transformers.pipelines.pt_utils import KeyDataset
from transformers import pipeline
from datasets import load_dataset


pipe = pipeline(model="hf-internal-testing/tiny-random-wav2vec2")
dataset = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation[:10]")

for out in pipe(KeyDataset(dataset, "audio")):
    print(out)