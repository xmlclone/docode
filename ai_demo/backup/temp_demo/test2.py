import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 读取CSV文件
data = pd.read_csv('text_training_data.csv')

# 划分训练集和测试集
X = data['text']  # 特征
y = data['label']  # 标签
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特征提取
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# 训练模型
model = RandomForestClassifier()
model.fit(X_train_vectorized, y_train)

# 预测并计算准确率
y_pred = model.predict(X_test_vectorized)
print(y_pred)
accuracy = accuracy_score(y_test, y_pred)
print("准确率:", accuracy)