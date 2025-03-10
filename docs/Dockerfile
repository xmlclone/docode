# docker build -t mrtcimage:v1.3 .

FROM python:3.9-bullseye

ENV TZ="Asia/Shanghai"

COPY msyh.ttc /usr/share/fonts

# COPY是可以把目录下所有(包括子目录)都copy过去的
# COPY dir /opt/workspace/dir  # 会把 dir 整个目录复制到 /opt/workspace 下，注意目的地也要有 dir，除非你想重命名
COPY chromedriver_102.0.5005.61 /usr/bin/chromedriver
WORKDIR /opt
RUN apt update
COPY google-chrome-stable_current_amd64_102.0.5005.115.deb /opt/google-chrome-stable_current_amd64.deb 
RUN dpkg -i google-chrome-stable_current_amd64.deb || true
RUN apt-get -y -f install
RUN dpkg -i google-chrome-stable_current_amd64.deb

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN sed 's/maxsize=1,/maxsize=100,/' -i /usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py

ADD entrypoint.sh /opt

WORKDIR /opt/mrtctest

ENTRYPOINT ["sh" ,"/opt/entrypoint.sh"]
CMD ["scripts/dory_case_demo.py", "--no-statis"]
