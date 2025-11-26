# 作者：薛丰坤
# 2025年11月26日12时45分20秒
# 2634661037@qq.com
import subprocess
import sys

def run_cmd(cmd):
    """执行命令并返回输出"""
    try:
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def check_account():
    name = run_cmd("git config user.name")
    email = run_cmd("git config user.email")
    if name and email:
        print("账户校验成功")
        return True
    else:
        print("账户校验失败")
        return False

def check_remote():
    url = run_cmd("git remote get-url origin")
    if url:
        print("远程仓库校验成功")
        return True
    else:
        print("远程仓库校验失败")
        return False

def check_commit_msg():
    msg = run_cmd("git log -1 --pretty=%B")
    expected_msg = "Add README.md with my OSS contribution plan"
    if msg and msg.strip() == expected_msg:
        print("commit信息校验成功")
        return True
    else:
        print("commit信息校验失败")
        return False

def check_commit_content():
    files = run_cmd("git diff --cached --name-only")
    # 检查最近一次提交是否有修改文件
    if files or run_cmd("git log -1 --name-only"):
        print("git 提交内容校验成功")
        return True
    else:
        print("git 提交内容校验失败")
        return False

if __name__ == "__main__":
    success = True
    if not check_account():
        success = False
    if not check_remote():
        success = False
    if not check_commit_msg():
        success = False
    if not check_commit_content():
        success = False

    if not success:
        sys.exit(1)
