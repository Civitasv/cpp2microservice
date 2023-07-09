# 算法到微服务到 k8s

## 算法到微服务

### 1. 环境

1. 安装 conda: <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>
2. 激活 conda 环境: conda activate `<your-env>`
3. 安装 flask: conda install flask

### 2. 算法定义与实现

算法的定义和实现见 [cpp](./cpp)。

#### 2.1 Python wrapper

使用 C++ 定义和实现算法后，为简化 Python 侧的调用，使用 Python 代码进行封装，见 [plugin](./python/plugin/)。

提供了三个例子：

- 对简单 C 语言程序的调用
- 对类函数的调用
- 对复杂类对象参数的传递

### 3. 服务注册

在 [routes](./python/app/routes.py) 中进行服务的注册，每个算子注册为一个服务。

## 微服务到 k8s

1. k8s 用于容器编排和管理，它的主要作用是简化容器化应用程序的部署、扩展和管理，并提供高可用性、可伸缩性和自动化的容器化环境
2. Kubernetes的优势在于能够在多台机器、集群环境和云端进行部署。通过在多个节点上运行容器，Kubernetes可以提供高可用性和可伸缩性。它可以自动管理容器的调度、故障恢复和负载均衡，从而确保应用程序的稳定性和可靠性。因此，在充分利用Kubernetes的能力之前，需要有多节点、集群环境或云基础设施的支持，否则意义不大。

所以，k8s 的关键点在于集群，对于单机服务器，其实没有必要使用 k8s，不过也是可行的。

### 1. 将 Flask 应用容器化

创建 Docker，并将 Flask 应用程序及其依赖项打包为一个可执行的容器。

### TODO

## Reference

1. [Flask](https://flask.palletsprojects.com/en/latest/quickstart/)
2. [Ctypes: 用于 Python 调用 C](https://docs.python.org/3/library/ctypes.html)
3. [k8s](https://kubernetes.io/)
