Title:iOS 开发环境配置
Date:2015-09-01
Tags:Emacs

其实 Xcode 还是挺好使用的， 所有的功能挺齐全的， 导航也很方便， 不过它在编辑器上没有什么作为， 所以作为一个臻于完美主义者， 总是希望再全面一点， 所以尝试了 Vim， 不过我在YouCompleteMe插件上遇到了错误， 各种找不到资料， 最后听说需要重装系统， 那我就只有呵呵了， 公司的电脑是黑苹果， 重装， 呵呵。



	make[3]: *** [BoostParts/CMakeFiles/BoostParts.dir/libs/chrono/src/process_cpu_clocks.cpp.o] Error 1
	error: invalid deployment target for -stdlib=libc++ (requires OS X 10.7 or later)
	clang: error: invalid deployment target for -stdlib=libc++ (requires OS X 10.7 or later)
	make[3]: *** [BoostParts/CMakeFiles/BoostParts.dir/libs/chrono/src/process_cpu_clocks.cpp.o] Error 1
	make[3]: *** [BoostParts/CMakeFiles/BoostParts.dir/libs/chrono/src/chrono.cpp.o] Error 1
	make[3]: *** [BoostParts/CMakeFiles/BoostParts.dir/libs/chrono/src/thread_clock.cpp.o] Error 1
	make[2]: *** [BoostParts/CMakeFiles/BoostParts.dir/all] Error 2
	make[1]: *** [ycm/CMakeFiles/ycm_support_libs.dir/rule] Error 2
	make: *** [ycm_support_libs] Error 2
	
所以我来配置Emacs吧。
Emacs非常好用。但是配置是一个 Challenge ， 不过好在集成了包管理工具， 添加源以后， 就可以直接搜索安装了， 也非常方便。

老外发明的东西还是他们玩得6啊， 来看[Aaron Bieber的博客](http://blog.aaronbieber.com)

再看[陈斌的Github](https://github.com/redguardtoo/mastering-emacs-in-one-year-guide/blob/master/guide-zh.org)

org-mode 用于写文章，
evil-mode 可以在 emacs 里使用 Vim 


Allan Perlis曾经说过：“一个无法改变你思维方式的编程语言是不值得学习的。"
我想说编辑器也是这样。


![十年磨一剑 Peter Norvig](http://jbcdn2.b0.upaiyun.com/2012/08/peter-norvig.jpg)
Peter Norvig

