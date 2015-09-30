Title: 开头一周
Date: 2015-09-28
Tags: WorkDay 

以后真的要制作一个 snippet，来生成 pelican 的格式，每次写作之前都要花时间来写开头的格式，确实也是个麻烦事。

这一周开头挺好， 早上6:06 的时候，我和父母去把家里装修开了个头，就算是要正式开工了。

然后回家吃了个丰富的早饭， 在8:13 的时候就来到了公司。

因为没有带book 的电源线， 于是正好开始重新利用公司的电脑。 之前因为公司电脑内存太小， CPU一般，硬盘是机械的种种原因， 我就用了一段时间自己的电脑， 到了现在，因为带自己电脑上下班不太方便， 所以还是决定启用公司的电脑。

自己带了一把 Kinesis Advantage， 写字就没那么累了。

来了公司第一件事就是把 Xcode 更新到 7.0， 然后安装各种插件。 

先安装 package manager : [Alcatraz](https://github.com/supermarin/Alcatraz)

如果没有在 Windows 看到 Package Manager 菜单项。 
则执行：

find ~/Library/Application\ Support/Developer/Shared/Xcode/Plug-ins -name Info.plist -maxdepth 3 | xargs -I{} defaults write {} DVTPlugInCompatibilityUUIDs -array-add `defaults read /Applications/Xcode.app/Contents/Info DVTPlugInCompatibilityUUID`

sudo xcode-select --reset
 
如果该没有出现那个菜单项目，则再执行

defaults delete com.apple.dt.Xcode DVTPlugInManagerNonApplePlugIns-Xcode-7.0


Xvim  

	替代 
	JumpMarks，
	jumper，
	SFJumpToLine
	XcodeBookmark
	XcodePlus Delete Line
	

blockJump
MLAutoReplace
	
	替代ATProperty，
		CComment  /*/, /,*/，
		QuickLocalization  Convert @"content" to NSLocalizedString(@"content", @"content")
		SCXcodeSwitchExpander
	

Auto－importer 或者是 Peckham


changemarks
ColorSenseRainbow 或者 OMColorSense

DBSmartPanels

DCLazyInstantiate

ESJsonFormat


FuzzyAutocomplete

HCTAutoFolding

Helmet

HighlightSelectedString

HOStringSense

HTYCopyIssue

IconMaker

Injection plugin

	Injection for Xcode

intelliPaste
	
	或者 
XcodeBoost	
![fs](https://github.com/fortinmike/XcodeBoost/raw/master/Images/menu.png)

JDPluginManager

JKBlockCommenter   ⌘⌥/ 

KKHighlightRecentPlugin

KPRunEverywhereXcodePlugin  Run Everywhere ⌃ + ⌥ + ⌘ + R  Stop Everywhere ⌃ + ⌥ + ⌘ + .

KSImageNamed

OpenQuiklyCtrlNP
PrettyPrintJSON
Polychromatic  安装好以后去主题页面调色 ，不然默认是黑色 

PuncoverPlugin

QuickFind

	Now with QuickFind, you just need to select something, and press CMD + F,
	QuickFind will open the find bar, put what you selected in the find bar 
	and start to find the next one. You can also press CMD + F again and again
	to find the next one (just forget CMD + E and CMD + G, you may only need 
	CMD + F )
	
QuickJump 

	Go to System Preferences > Keyboard > Shortcuts > App shortcuts and press the + button

RegX 

	Pretty alignment ⌘ + F1 F2 F3 F4
	或者XAlign 只有一种风格 ⌥ + ⌘ + X
	
SCXcodeEditorInset

SCXcodeMinimap

SCXcodeTabSwitcher

ShowInGithub

SketchExporter

SwipeGestureSwitcher   shortcut (cmd+ctrl+← and cmd+ctrl+→,

TOCAssetCatalogBackground

Tuna 
	
	Log 神器

Waka Time

	或者 XContract for localuse

WarmingLightXcodePlugin

WindowFlex

XCActionBar
	
	神器  Double tap CMD or press CMD+SHIFT+8
	
XcAddedMarkup
	
	变身图文编辑器	

Xcode_beginning_of_line
	
	nice for kinesis advantage
	
Xcode_copy_line

[XcodeColors](https://github.com/robbiehanson/XcodeColors)
	NSLog(XCODE_COLORS_ESCAPE @"fg0,0,255;" @"Blue text" XCODE_COLORS_RESET);

	NSLog(XCODE_COLORS_ESCAPE @"bg220,0,0;" @"Red background" XCODE_COLORS_RESET);

	NSLog(XCODE_COLORS_ESCAPE @"fg0,0,255;"
      XCODE_COLORS_ESCAPE @"bg220,0,0;"
      @"Blue text on red background"
      XCODE_COLORS_RESET);

	NSLog(XCODE_COLORS_ESCAPE @"fg209,57,168;" @"You can supply your own RGB values!" XCODE_COLORS_RESET);

XcodeMediaLibraryTweak

Xcode Refactoring Plus

	Delete Line (cmd+D)
	Delete the line or current selected lines.
	Duplicate Line (alt+cmd+down
	Duplicate the line or current selected lines.
	Move Line (alt+down | alt+up)
	Move the line or current selected lines
	Extract Local Variable (alt+cmd+l)
	Extract the inline code into local variable within the method
	
XcodeWay
![xcw](https://camo.githubusercontent.com/5b08e1707f962d315fce7364be90beb5aa0f7b1e/687474703a2f2f6935392e74696e797069632e636f6d2f62666d6579392e706e67)

XCommentWrap

infer
	static analysis tool
	
LXCXcodeAssist 
	
	Smarter ⌘+← and ⌘ + ⇧ + ←

    Move/Select cursor to position before first non-white space character instead of very beginning of the line

XLocation
	
	for ui pick location
	
Xprop 

	will hide all garbage from the Document Items menu. As result, no more distraction.  when ctr-6 
	
XQuit
	
	ask you whether quit Xcode
	
XReset 
	reset iOS Simulators Content and Settings
	
XToDo
	
	神器 准确标记目标

XTrello
	
	for trello

[XWJsonToCode](https://github.com/boyXiong/XWJsonToCode)
![c](https://camo.githubusercontent.com/eecdbb902060ecb7dae7315dfdc90c5a64521460/687474703a2f2f696d672e626c6f672e6373646e2e6e65742f3230313530373331303032313534303432)

ZKKeyBindingsTeacher
	
	神器，教一些常用的按键绑定

ZLCheckFilePlugin-Xcode
	
	 检查多余的文件 File -> Look check

ZLGotoSandbox 
	
	较快去sanbox
	Support When running the simulator shortcut keys ('Shift + Common + w') Jump Sandbox.

ZLXCodeLine
	
	统计代码行数

ZMDocItemInspector
	
	 converts the Quick Help inspector into an always visible Document Items inspector. 
	 
WCGitTagsPlugin
SuggetsedColors
Snapshots
RSImageOptimPlugin
RRConstraintsPlugin
RevealPlugin 
Remote	
RealmBrowser
KSHObjcUML
Open With Application
OFXcodeMenu
ObjectGraph-Xcode

	KSHObjcUML
	Xprobe  或许更好， 可以动态显示

NJHMultiTheme
NCSimulatorPlugin
MCLog
MarvinPlugin show collection of commands
instaCodesPlugin
coPilot
Distraction free mode zen
DerivedData Exterminator
CocoaControls
AutoIndentWithSave
BTGistPost
	
	或者 XCSnippetr
AutoImporter
ACCCodeSnippetRespository
AMMethod2Implement

PluginConsole
PluginPannel with TimePlugin
RedXcode

unknown 
seguecode
Stencil
SYConfigurableVariable
SymbolicationPlugin
unTrashed-Files
VariablesViewFullCopy
XCFixin_CustomizeWarningErrorHighlights
XcodeAutoBasher
XCoverage

swift
https://github.com/burczyk/XcodeSwiftSnippets


gem install
fui  and xcodeproj
	for xcfui
	如果 安装失败，就添加淘宝源 
	sudo gem sources -r https://rubygems.org
	sudo gem sources -a http://ruby.taobao.org
	
maybe tasty
Xcode Explorer

63 code bundles

links

wakatime.com