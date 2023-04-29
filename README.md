# dcdatabase_is
本软件为粉丝向软件。

适用于美国漫画，DC漫画，超级英雄爱好者。用于爬取[dcdatabase](https://dc.fandom.com/wiki/DC_Comics_Database)上的角色出场数据，并求出多名角色在同一期刊出场的交集。

(没错是作者补漫的时候顺路写的)

使用Python3.7在Windows10上开发并简单打包为exe，未进行进一步测试

# 使用方式
双击exe即可使用

![四个选项](https://tvax1.sinaimg.cn/large/008vOhrAly1hdgu9j1kifj30ie09nq4b.jpg)

①爬取dcdatabase的角色出场数据，以html文件形式保存在本地

②比较多个本地html文件，生成其交集

③比较多个本地html文件，生成其并集

④比较多个本地html文件，生成补集

![选项1](https://tvax1.sinaimg.cn/large/008vOhrAly1hdgubau8j2j30ib09u769.jpg)

选项1如图

输入网址url —— 从网站上面把单人出场爬下来。

1000items大约要爬两分钟。网址一定要准确，否则会报错(比如dcdatabase网址将超人写为卡尔艾尔而不是克拉克肯特，那么输入克拉克肯特是查不到的)。

dcdatabase将p52写为New Eart，将n52写为Prime Earth

![选项2/3](https://tvax1.sinaimg.cn/large/008vOhrAly1hdgucs685hj30l60a1q4m.jpg)

![选项4](https://tvax1.sinaimg.cn/large/008vOhrAly1hdgupy3k6ej30ih06w3z9.jpg)

选项2/3/4如图

依次输入多个html文件名 —— 输出其交集/并集/补集。

exe会自动查询本地所有html文件名，将自己想要查询的html复制粘贴输入列表，一次输入一个。全部输入完成后，输入ok即可。

![生成html示范](https://tvax1.sinaimg.cn/large/008vOhrAly1hdgalbi6itj30yw0k6gzr.jpg)

生成html如图

链接点进去是dcdatabase相应期数刊物的网址


# 更新日志
1.2 增加并集功能，修复闪退

1.2.1 轻度优化依旧简陋的界面，修复闪退

1.3 修改命名方式

1.4 文件转移到子文件夹并附带统计条数

1.4.1 修复合并计数错误的问题

1.5 加入减法补集功能

1.5.5 功能没变换了种写法

1.5.6 修复选择列表又取消后文件名重复的问题

