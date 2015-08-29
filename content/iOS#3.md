Title:CoreData 还真是不好学呢
Date:2015-08-25
Tags:iOS
> CoreData
CoreData 一句话真是无语了，封装了半天还是那么多乱七八糟的东西，什么一会儿有
 context 了，一会儿又 objectModel 了，一会儿又 manager 了，你没妹啊？！

不能好好写个协议调用就好了啊，还选择目录保存，还用 url，还找目录，还需要转换属性的类型，要做这么复杂吗？真是的，没意思。Apple 的天才们都死哪里去了？

搞来存储个东西尼玛还需要获取个 context，然后增删改都要调它的 save：，不调用要死呀？不能写个封装类呀？

查询也是够了，还要写个 request 请求类，
什么 acsend 都要加在上面，取回的还是一个数组，这有没有啊？

好了，然后写个 Singleton 搞定这些，把它们统统封装起来，对吧？

然后在 AppDelegate 的两个回调方法里也要写上保存噢，对吧？

不要害怕噢，core data 就这些东西，对吧？

什么 .xcdatamodeld 什么 Entity， 什么 Property， 什么 Relationship， 生成 NSManagedObjectModel subclass 也很简单， 对吧？

哈哈，当然 relationship这里我还不大明白， 等会儿看了BNR的书再来回答吧。
总之CoreData入门就这些啦。

明天写个KeyChain的注册页面，还要和老板讨论服务器的问题呢。



