import pandas as pd


df = pd.read_csv('test_data.csv')
print(f"{df=}\n{df['img']=}\n{df.img.tolist()=}")