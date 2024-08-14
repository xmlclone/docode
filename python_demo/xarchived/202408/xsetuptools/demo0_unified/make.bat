@REM 仅删除本项目打包的内容，其它内容不删除(比如有其它依赖)
del /q dist\xmltest* 2>nul

@REM 重新构建 pyc 文件，加密模块不想打包
@REM 需要配合 MANIFEST.in 文件使用
del /q xmltest\sec\__pycache__\*.pyc 2>nul
del /q xmltest\sec\*.pyc 2>nul
python -m compileall xmltest\sec\api.py
move xmltest\sec\__pycache__\api*.pyc xmltest\sec\api.pyc

python -m build .