> git操作使用手册
****
远程仓库

本地生成ssh   （创建rsa密钥）
-
    git-keygen -t rsa


github创建ssh
-
	1，个人中心----setting----SSH and GPGkeys
	2，复制本地生成的key



github 创建项目
-
	
  	New repository

本地创建版本库
-
	本地创建临时版本库
	git init   	    		---创建信息的版本库
	git clone @git地址    	---克隆版本库到本地
	

本地提交
- 
	git add *  	---提交代码
	git commit -m '' ---提交代码信息	
	git push origin master  ---上传至远程库

删除远程库信息
-
	git rm file		---删除代码
	git commit -m ''	---提交删除信息
	git push origin master  --上传至远程版本库