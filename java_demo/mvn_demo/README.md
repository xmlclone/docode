# 基础命令

```shell
# 创建项目
mvn archetype:generate -DgroupId=com.example -DartifactId=myproject -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# 编译项目
cd myproject
mvn clean package

# 运行
java -jar target\myproject-1.0-SNAPSHOT.jar
```