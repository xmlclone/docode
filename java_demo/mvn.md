# 基础

package命令完成了项目编译、单元测试、打包功能，但没有把打好的可执行jar包（war包或其它形式的包）布署到本地maven仓库和远程maven私服仓库
install命令完成了项目编译、单元测试、打包功能，同时把打好的可执行jar包（war包或其它形式的包）布署到本地maven仓库，但没有布署到远程maven私服仓库
deploy命令完成了项目编译、单元测试、打包功能，同时把打好的可执行jar包（war包或其它形式的包）布署到本地maven仓库和远程maven私服仓库

# maven配置

1. 下载maven(https://maven.apache.org/download.cgi)，并且配置环境变量，输入mvn -v查看版本
2. 配置，文件在conf\settings.xml
3. 找到 `<localRepository>/path/to/local/repo</localRepository>` 这行，大概在52行，路径修订为期望的路径，就是下载的本地仓库保存地址，注意这里的路径是/
4. 另外镜像可以配置为国内的，大概在160行

```xml
<!-- 阿里云仓库 建议这个-->
<mirror>
    <id>alimaven</id>
    <mirrorOf>central</mirrorOf>
    <name>aliyun maven</name>
    <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
</mirror>
 或者
  <mirror>
    <id>nexus-aliyun</id>
    <mirrorOf>*</mirrorOf>
    <name>Nexus aliyun</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public</url>
 </mirror>
```

5. 配置java版本

```xml
<profile>
  <id>jdk-1.8</id>
  <activation>
    <activeByDefault>true</activeByDefault>
    <jdk>1.8</jdk>
  </activation>

  <properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
    <maven.compiler.compilerVersion>1.8</maven.compiler.compilerVersion>
  </properties>
</profile>
```

6. 最后通过命令`mvn help:system`看是否提示从阿里云下载

# maven常用命令

```shell
# 创建项目
# DarchetypeArtifactId 可以简单理解为我们创建的项目模板，有下面一些常用的可选：
# maven-archetype-quickstart：一个简单的Java应用程序项目，包含一个类和一个测试类。
# maven-archetype-webapp：一个Web应用程序项目，包含Web应用程序基本结构和配置文件。
# maven-archetype-j2ee-simple：一个标准的Java企业级应用程序（JavaEE）项目，包含基本的JavaEE应用程序结构和配置文件。
# maven-archetype-jersey：一个创建RESTful Web服务的项目，使用了Jersey框架。
# maven-archetype-spring-boot：一个Spring Boot应用程序项目，包含了Spring Boot的基本结构和配置文件，并且可以用于快速开发Spring Boot应用程序。
mvn archetype:generate -DgroupId=com.example -DartifactId=myproject -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# 清理项目
mvn clean

# 生成jar
mvn package (一般生成在target下，有个jar文件，通过java -jar target\xxx.jar执行)

# 先清理在打包
mvn clean package

# 先清理在打包，跳过测试类
mvn clean package -Dmaven.test.skip=true

# 编译测试源代码
mvn test-compile

# 运行应用程序中的单元测试
mvn test

# 编译源代码
mvn compile

# 在本地Repository中安装jar
mvn install

# 发布项目
mvn deploy

# 把maven库服务器中中没有第三方jar包安装到到本地Repository中的命令
mvn install:install-file -DgroupId=org.csource -DartifactId=fastdfs-client-java -Dversion=${version} -Dpackaging=jar -Dfile=fastdfs-client-java-${version}.jar

# 创建maven项目，输入groupId和artifactId即可
mvn archetype:generate
```

## 异常

### mvn package等命令报错类似: 不再支持源选项 5。请使用 7 或更高版本

可以尝试以下两种方式:

1. 修改maven的setting.xml配置文件(全局生效)

```xml
<profiles>
      <id>jdk-18</id>
      <activation>
        <activeByDefault>true</activeByDefault>
        <jdk>18</jdk>
      </activation>

      <properties>
        <maven.compiler.source>18</maven.compiler.source>
        <maven.compiler.target>18</maven.compiler.target>
        <maven.compiler.compilerVersion>18</maven.compiler.compilerVersion>
      </properties>
</profiles>
```

2. 修改项目的pom.xml配置文件(项目生效)

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.target>18</maven.compiler.target>
    <maven.compiler.source>18</maven.compiler.source>
</properties>
```

### java -jar执行提示: xxx.jar中没有主清单属性

在pom.xml中增加如下配置

```xml
<build>
  <plugins>
      <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.2.2</version>
          <configuration>
              <archive>
                  <manifest>
                      <addClasspath>true</addClasspath>
                      <mainClass>com.xmlclone.demo.App</mainClass> <!-- 此处为主入口-->
                  </manifest>
              </archive>
          </configuration>
      </plugin>
  </plugins>
</build>
```

## 参考

1. [Eclipse+Spring boot开发教程](https://www.cnblogs.com/lsdb/p/9783435.html)
2. [Maven的安装与配置](https://blog.csdn.net/a805814077/article/details/100545928)

# 本地jar包导入

## 方式一

直接通过`mvn install进行安装`，比如:

```
mvn install:install-file -DgroupId=com.xx.yy -DartifactId=xx-overload-interface -Dversion=0.0.1-SNAPSHOT -Dpackaging=jar -Dfile=xx-overload-interface-0.0.1-SNAPSHOT.jar
```

## 方式二

修改mvn的settings.xml，增加如下配置:

```xml
<localRepository>C:\\Users\\xxx\\Desktop\\APP\\apache-maven-3.8.6\\localRepository</localRepository>
```

然后把jar包，放到对应的目录下，一般在这个目录下的com/xx/yy/xx-overload-interface/0.0.1-SNAPSHOT目录下即可