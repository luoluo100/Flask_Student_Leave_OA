# Flask_Student_Leave_OA
This is a simple falsk project,on completing the work of leaving students and Teachers

## 项目要求
* 学生能够在系统上完成请假，请求销假，以及撤销请假的操作
* 老师能够在系统上完成批假，销假的功能
* 管理员能够添加学生
* 学生老师共用一个登陆界面和URL,通过权限管理来限制访问内容


## 实现思路
* 定义3个模型类，学生，老师，管理员，模型之间不设表间关系，每个模型对应不同权限，grant:0,1,2
* 视图中根据调整学生当前状态，正常，等待批假，已请假，等待销假
* 后端根据登录信息识别用户身份，并设置用户cookie，session信息，过期时间设为7\*24\*3600
* 前端js根据views返回的参数，确定要显示的内容


## 注意的问题
* flask的jinja2模板不能导入静态文件，但是能继承基础模板
* 登出时，一定要清除掉用户的cookie信息
* 理清学生请假与老师批假之间的关系，做到不重复请假


## js函数代码展示

```html
    <script type="text/javascript">
        var foo = "{{ student }}";
        f(foo);
        function f(foo){
            if(foo==1){
            document.getElementById("collapseTwo").style.display="none";
            document.getElementById("hhh").style.display="none";
        }else if(foo==0){
            document.getElementById("collapseUtilities").style.display="none";
            document.getElementById("hhh").style.display="none";
        }
        }
    </script>
```
