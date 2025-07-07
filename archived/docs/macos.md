# clouddrive

```sh
# 确保你的macOS已安装Homebrew，https://github.com/Homebrew/brew
# 运行前请确保系统已安装macFUSE，并已按照提示正确设置权限。或者通过brew命令安装macFUSE
brew install --cask macfuse

# 运行以下命令安装CloudDrive：
brew tap cloud-fs/clouddrive2
brew install clouddrive2

# 运行以下命令启动CloudDrive：
brew services start clouddrive2

# 运行成功后将会自动创建后台服务并且下次登录会自动运行
# 启动成功后用浏览器打开http://localhost:19798进入管理配置界面

# 运行以下命令停止CloudDrive：
brew services stop clouddrive2

# 运行以下命令卸载CloudDrive：
brew services stop clouddrive2
brew uninstall clouddrive2

# 运行以下命令更新CloudDrive：
brew services stop clouddrive2
brew update
brew upgrade clouddrive2
brew services start clouddrive2
```