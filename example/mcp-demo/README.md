# MCP

- https://modelcontextprotocol.io/introduction
- https://github.com/modelcontextprotocol/inspector

# Python

- https://pypi.org/project/mcp/

```sh
pip install "mcp[cli]"

set DANGEROUSLY_OMIT_AUTH=true
mcp dev server.py

# 启动后访问http://localhost:6274/
# 在command填入：mcp
# 在Arguments填入：run sercer.py
# 最后点击connect即可
```