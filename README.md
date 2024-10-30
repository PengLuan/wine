# 文档地址
#### https://wh5cnpcn77.feishu.cn/docx/P3OHdFHQRoJd2mxTA1CckTTLnVc?from=from_copylink

# 部署方式
- 1、准备python3.10 环境
- 2、下载 cc.zh.300.bin 并放到 data目录 下载地址 https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.zh.300.bin.gz
- 3、下载 classification.model 并放到 data 目录 下载地址 https://luanpeng-file.oss-cn-beijing.aliyuncs.com/classification.model
- 4、如下代码安装依赖并执行服务

```schell
pip install -r requirements.txt
python server.py
```

- 5、打开test中的robot_text.html 进行交互测试
- 
