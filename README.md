# mse24.ml.aipc
home work for mse24 ml aipc

## 项目介绍

1. 第一文件llm_rerank.ipynb在使用GPU的情况下将模型直接转为openvino 然后输出
2. 第二个文件llm_rerank.ipynb 在使用文件1的基础之上增加量化操作，量化为8bit
3. SearchApps.py 为搜索google play内容的模块请注意， 因使用了付费api，所以我们在github中隐去了具体的key， 如果有需要，请自行申请[rapidpi](https://rapidapi.com/)或联系作者获取

## 整体工作流程

1. 从google play中获取对应query的搜索结果
2. 根据google play的搜索结果， 将其输入到大模型中，获得相关系数得分， 
3. 根据step2的得分对结果进行重排

## 项目出发点

1. 根据过往项目经验，传统RAG模型对于通用搜索，具有较强的表达效果，
2. 相比较于通用搜索， 垂直搜索具有更多挑战，通常， 垂直搜索更具有目的性，更注重于查找而非答案
3. 传统搜索流程 召回=》粗排=》精排， 排序在搜索中占有重要定位
4. 例通用搜索中：用户输入“中国常用的支付app”，bing或者google 通常可以返回具有解释的答案，而在google play中，这种方式不被采纳，用户期求返回具体的app下载链接
5. 因此在垂直搜索领域， rerank相比较于rag具有更高的应用价值

## 项目中遇到的问题

1. 对于模型预测中，一次性输入搜索候选集会出现内存溢出错误， 为解决这个问题， 我们采用逐次输入的方式
2. 排序得分是一个相对得分， 经过测试发现不同pairs中的同一app会出现不同的分数， 为解决该问题，采用固定pairs中的第一个item， 然后根据相除得到相对得分进行排序。

## 项目改进方向
1. 如果有app store的具体行为信息，那么就可以构建具体的 “问-答” pairs，可以对模型进行进一步的调整fine tune

## 所引用模型与生成模型
+ [base model : bge reranker](https://huggingface.co/BAAI/bge-reranker-v2-m3)
+ [base model's github](https://github.com/FlagOpen/FlagEmbedding)
+ [openvino(generate by this project)](https://huggingface.co/NumberEight/bge-reranker-v2-m3-openvino)
## 团队成员

+ [Hao Ba](674248666@qq.com)
+ [YiLai Sheng]()
+ [YingJie Jin]()
+ [DaHong Xu]()
+ [YunWei Li]()


