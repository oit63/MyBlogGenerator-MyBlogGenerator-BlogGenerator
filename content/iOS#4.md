Title: iOS Core Data
Date:2015-08-26
Tag:Life
今天看了三本书，两本 Pro，一本 BigNerd。
不过好在还是 BigNerd讲得清楚，配套了源码，还有社区的 [Challenge解决方案](http://forums.bignerdranch.com/viewtopic.php?f=504&t=8393), 我才能把 Core Data 在这四天内搞得差不多。

将 Core Data 搞定以后，我的数据结构就好了一大半了，之后就是配合 View 做相关的显示，以及相关操作了。

之后就是注册页面的实现， 好在有一本 Pro可以参照， 还有之前实习时候的工程也可借鉴了，比如 KeyChain部分。

再接着就是整合多种特效了，将各种需要的效果整合在一起，最后就是REST的相关工作了。

做好这几块再将Socket整合进来，使应用可以工作就行啦。

另外模型设置上，明天还需要就这一点与家门讨论一下，对于监控信息的展示也是一个问题。

比如监控信息也是一种model，一个item可以对应有多个监控信息，就是many to one 类型啦。

这样一来它的关系和item与assetType就类似啦。