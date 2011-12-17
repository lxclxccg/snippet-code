#!/usr/bin/env python
#coding:utf-8

#项目相关的信息
GLOBAL_PROJECT = "snippet-code"
GLOBAL_PROJECT_MAJOR_VERSION = "0"
GLOBAL_PROJECT_MINOR_VERSION = "1"
GLOBAL_PROJECT_AUTHOR = "Zimilo"
GLOBAL_PROJECT_AUTHOR_EMAIL = "zimilo@code-trick.com"


#数据库相关的配置
GLOBAL_DB_HOST        = "localhost"
GLOBAL_DB_PORT        = 3306
GLOBAL_DB_USER        = "zJiXU"
GLOBAL_DB_PASSWD      = "iUpIUY"
GLOBAL_DB_DB          = "snippet"
GLOBAL_DB_PRE         = "snippet_"
GLOBAL_DB_POSTS_TABLE = "posts"



#系统支持的语言类型的配置
GLOBAL_LANGUAGES = [
    #ID, Type, DisplayName
    [1,   "TXT",    "纯文本"],
    [2,   "Python", "Python"],
    [3,   "PHP",    "PHP"],
    [4,   "Erlang", "Erlang"],
    [999, "Others", "其它" ]
    ]



#系统发布的权限
GLOBAL_PRIVILIEDGE_PUBLIC = 1
GLOBAL_PRIVILIEDGE_PRIVATE = 0


#POST的相关配置
GLOBAL_DEFAULT_POST_TITLE = "未命名代码片段"
