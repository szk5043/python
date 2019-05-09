**问题1：无法启用插件安装**
Sublime包管理package control 报错 There are no packages available for installation
编辑  首选项--> package-settings  ---> package contral ---> settings user

```shell
{
	"bootstrapped": true,
	"channels":
	[
		"https://raw.githubusercontent.com/HBLong/channel_v3_daily/master/channel_v3.json"
	],
	"in_process_packages":
	[
	],
	"installed_packages":
	[
		"Chinese-English Bilingual Dictionary",
		"ChineseLocalizations",
		"MarkdownEditing",
		"Package Control"
	]
}
```
**问题2：无法安装emmet插件**
手动安装emmet插件：
克隆或[下载](https://github.com/sergeche/emmet-sublime/archive/master.zip) git repo到你的包文件夹中（在ST中，找到首选项-->浏览插件目录 ...菜单项打开这个文件夹）
重启ST编辑器
[https://github.com/sergeche/emmet-sublime#readme](https://github.com/sergeche/emmet-sublime#readme)

