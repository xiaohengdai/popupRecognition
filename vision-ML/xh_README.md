>  训练不同场景下的模型
```
一、处理弹窗中"x"关闭按钮的模型，x_v1_trained_model_1.h5
1、在用框架中自带的模型去识别苏宁app中的x弹窗时，识别不出来
解决：
在image目录下补充正、负样本，将弹窗样式进行截图补充到正样本中，以x弹窗附近的区域及将识别成非x弹窗的位置截图补充到负样本中


```