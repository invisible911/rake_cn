# rake_cn
---
RAKE keyword extraction implentation in Chinese Language.
In python.

## originate 
  https://github.com/aneesha/RAKE in English
  which based on 
  > Rose, S., Engel, D., Cramer, N., & Cowley, W. (2010). Automatic Keyword Extraction from Individual Documents. In M. W. Berry & J. Kogan (Eds.), Text Mining: Theory and Applications: John Wiley & Sons.

## example
* text

>美媒称，中国房地产市场已然过热。近月来，一些城市的房价同比涨幅高达两位数，而投资者尚未找到另一个收益上涨的市场。
>美国《福布斯》双周刊10月11日一期刊登题为《中国房地产泡沫终于如期而至》的文章称，据中国国家统计局统计，全国70座大城市新建住房价格平均同比上涨9.2%，上海房价同比上涨了31.2%，二线城市厦门的房价一年来上涨了43.8%。针对这一情况，地方政府试图通过调控措施抑制房价过度上涨。
>最近，北京、深圳、苏州及其他城市不同程度地提高了购房首付。广东省的珠海和东莞市以及福建省的福州市都将购房限制在两套以内。安徽省合肥市规定：登记备案后六个月内不得变更房价。天津、郑州、成都、济南、无锡、南昌、南宁、广州、厦门和武汉也都出台了冷却房地产市场的措施，比如提高首付比例，减少居民购房套数。中国各大城市仍在出台新的调控措施。
>文章称，有趣的是，此前连续数年，一旦房地产热崩溃，政府就放宽限制，刺激住房市场。
>从2014年9月起，央行放宽了二套房抵押贷款限制，降低了首付比例和抵押贷款利率。2015年8月，在华工作和生活的外国人以及外国公司在中国的分公司都可以购房。2015年9月，中国人民银行继续降低首次购房的首付比例，从30%降至25%。今年2月，第一套和第二套住房的首付比例再次降低至20%。
>中国房地产大亨王健林曾暗示今天的房价上涨是一个“大泡沫”。他说意在冷却市场活动的调控措施没有什么效果，野村首席经济学家张志伟认为有证据表明土地拍卖存在泡沫。
>文章称，泡沫并不特别，也并非意料之外。随着投资者寻找安全且可以赚到钱的投资渠道，“泡沫”——或称为资产价格上涨，比如房地产、股市或影子银行市场——在中国经常发生。金融调控放宽时，资产价格就上涨，收紧时就下降，这既说明金融市场不够健全，也反映了中国独一无二的国家与市场混合型金融体制。
>储蓄者根本没有可以赚钱的充分的渠道进行投资：股票和债券市场并不始终如一地准确反映公司的风险与收益，房价可能被剥夺，诸如影子银行部门的财富管理和信托产品这样的投资产品不透明，并可能充满风险——包括证券化了的不良贷款或其他不合格产品。
>文章称，之所以出现问题，也是因为中国为了应对经济下滑采取了宽松的货币政策。过度的流动性，加上资产价位低，投资渠道少而空泛，这些因素共同导致了各种融资泡沫。货币供应量（或称M2）不断增加，尤其是2008年和2009年发生全球金融危机之后。资金先是注入了为房地产部门和基础设施投资进行融资的影子银行部门，然后又涌入股市、公司债券市场，最后又回到房地产部门。所有这些资产价格泡沫都伴随着相应暴跌，资产价格迅速下降，政府介入，出台调控措施或注入资本，为暴跌的市场托底，这就是中国房地产市场今天的实情。
>【相关图集】
>揭秘房价崩溃后的日本：自杀破产集中爆发

*keywords (top 5)
英镑兑美元汇率跌
允许中国游客申请
达成优惠交易
英国脱欧英镑贬值
享英伦礼遇

## to use
  you need a tokenizing service through py4j in java, which can be one of the most popular tokenizer in Chinese word.eg.[中科院分词器](http://ictclas.nlpir.org/),[IK分词器](https://github.com/wks/ik-analyzer)
  
  
  or
  
  you could have a python-implemented one with the specified interface defined in segment_service.py.
  
  **Viewing demo in Ipython notebook**

## moderfications
  1. spliting sentence into phrase using non-real words (nature in ['m','d','ad','p','b','r','w','f','AMBIGUOUS'] ) ,in addition to words in stopwords list.
  2. using hand-crafted rules to filter inappropriate words and to form keywords with desired nature combinations (could be improved)
  
