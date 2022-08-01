## 数据说明：
  1. id: 编号，作为识别该条数据唯一key。
   
  2. Case_A：输入案例A，经过分句处理。
  
  3. Case_B：输入案例B，经过分句处理。
  
  4. Case_A_rationales: 案例A中司法特征句，人工标注证据，在提供给参赛者的测试文件中不含该字段。
   	
  5. Case_B_rationales: 案例B中司法特征句，人工标注证据，在提供给参赛者的测试文件中不含该字段。
  
  6. relation: 支持匹配句子对，人工标注证据，在提供给参赛者的测试文件中不含该字段。
  
  7. label: 2 匹配/ 1 部分匹配/ 0 不匹配 人工标注结果，在提供给参赛者的测试文件中不含该字段。

## 提交格式说明：

1、每行为一个案例对的预测结果：

2、每行包含6列内容，分别为输入数据id（必需字段）、匹配预测label（必需字段）、Case_A_rationales（必需字段），
Case_B_rationales（必需字段）， relation（必需字段），以table键隔开。其中，输入id来自测试集文件，
匹配预测label是模型对案例匹配标签的预测结果，Case_A_rationales 与 Case_B_rationales 中包含句子id使用英文逗号隔开， 
Case_A_B_rationales 使用[Case_A句子id,Case_B句子id] 的形式，间隔符号均为英文输入状态。请注意，证据的句子 id要跟输入文件中给出的句子 id对齐。
结果评估时，基于的是我们提供的分句进行的，句子编号从0开始。