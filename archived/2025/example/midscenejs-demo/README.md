# 常用命令

```sh
set PUPPETEER_SKIP_DOWNLOAD=true
npm i -g @midscene/cli

npm init playwright@latest
npm install @midscene/web --save-dev

set OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
set OPENAI_API_KEY=......
set MIDSCENE_MODEL_NAME=qwen-vl-max-latest
set MIDSCENE_USE_QWEN_VL=1

npx playwright test
```

# 安装与使用

```sh
# 安装
npm i -g @midscene/cli

# 如果安装过程中，出现PUPPETEER网络异常的情况，可以先临时屏蔽重新执行上面的安装命令，后续再安装PUPPETEER，屏蔽命令如下：
set PUPPETEER_SKIP_DOWNLOAD=true
```

# playwright集成

```sh
# playwright初始化，进入对应的工程目录，如playwright-demo1后执行以下命令：
npm init playwright@latest

# 如果暂时不需要安装playwright带的浏览器，可以先跳过，后续用以下命令重新安装即可：
npx playwright install

# 安装依赖
npm install @midscene/web --save-dev

# 配置大模型(linux下用export, 并注意用引号把值包含在内)
set OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
set OPENAI_API_KEY=......
set MIDSCENE_MODEL_NAME=qwen-vl-max-latest
set MIDSCENE_USE_QWEN_VL=1

# 执行demo
npx playwright test
```