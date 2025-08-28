



# GIT Study Record

## 一、常见命令操作

~~~ shell
# 创建特性分支
git checkout -b feature/login-page

# 提交代码
git add .
git commit -m "feat: 添加登录页面基础结构"

# 推送分支到远程
git push origin feature/login-page

# 创建PR
gh pr create --title "登录功能开发" --body "完成基础UI和API对接"

# 合并后删除分支
git branch -d feature/login-page
git push origin --delete feature/login-page
~~~

Github pr 通过，merge完后 建议勾选删除分支，然后在本地输入命令

~~~bash
merge完后 勾选删除分支 ==
git push origin --delete <branch>

# 1. 保存当前修改（如有）
git add . && git commit -m "临时保存"  # 或 git stash

# 2. 切换到主分支
git checkout main

# 3. 同步远程信息并清理无效引用
git fetch --prune

# 4. 删除本地分支A
git branch -d branchA  # 或 git branch -D branchA

# 5. 验证结果
git branch -a










切换到主分支（如main）并拉取最新代码：
git checkout main  
git pull origin main
删除本地已合并分支：
git branch -d feature/xxx  # 安全删除（仅合并后）  
git branch -D feature/xxx  # 强制删除（未合并时）（谨慎使用）
删除远程分支后，本地需更新引用
git fetch -p  # 修剪已删除的远程分支引用
git branch -d 仅删除本地分支，与远程分支无关。
git fetch -p 用于同步远程分支状态，清理本地无效的远程引用。

是否需要立即执行 git fetch -p：取决于远程分支是否已被删除，若已删除则建议执行，否则无需强
git fetch origin	获取远程分支列表（不修改本地文件）
git checkout -b xxx origin/xxx	创建本地分支并跟踪远程分支
git push -u origin xxx	首次推送并设置上游跟踪（后续直接 git push）
git pull --rebase	拉取远程变更并保持线性提交历史
~~~

