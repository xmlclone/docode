import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# 读取CSV文件
data = pd.read_csv('text_training_data.csv')

# 分割特征和标签
X = data['text']
y = data['label']

# 创建TF-IDF向量化器
vectorizer = TfidfVectorizer()

# 将文本数据转换为特征向量
X = vectorizer.fit_transform(X)

# 创建支持向量机分类器
classifier = SVC()

# 训练模型
classifier.fit(X, y)

# 使用训练好的模型进行预测
user_input = "I love"
user_input_vector = vectorizer.transform([user_input])
predicted_label = classifier.predict(user_input_vector)

print("预测的标签为:", predicted_label)