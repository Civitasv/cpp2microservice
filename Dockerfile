# 使用基础 Python 3.9 镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到镜像
COPY . .

# 安装依赖项
RUN pip install -r python/requirements.txt

# 暴露端口
EXPOSE 5000

# 定义启动命令
CMD [ "./start.sh" ]
