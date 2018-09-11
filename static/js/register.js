/**
 * Created by tarena on 18-9-5.
 */
function checkUphone() {
    var value = $("[name='numb']").val();
    //向window对象中增加一个变量flag，默认值为false
    window.flag = false;
    if(value.trim().length==11){
        $.ajax({
            url:"/01_server/",
            type:"post",
            data:{
                uphone:value,
                csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()
            },
            dataType:"json",
            async:false,
            success:function (data) {
                $("#uphoneshow").html(data.text);
                if(data.status == 1)
                    window.flag = true;
                else
                    window.flag = false;
            }
    })
    }else {
        $("#uphoneshow").html('手机号码位数不正确');
        window.flag = false;
    }
    return window.flag
}

function checkRepeat() {
    var flag = false
    var value = $("[name='repeat']").val();
    if(value != $("[name='passwd']").val()){
        $("#repeatshow").html('两次密码不一致')
        flag = false
    }else{
         $("#repeatshow").html('验证通过')
        flag = true
    }
    return flag
}

function checkUpwd() {
    var flag = false
    var value = $("[name='passwd']").val();
    if(value.length < 6){
        $("#upwdshow").html('密码不符合规范')
        flag = false
    }else{
         $("#upwdshow").html('验证通过')
        flag = true
    }
    return flag
}

$(function () {
    $("[name='numb']").blur(function () {
        checkUphone();
    })
    $("[name='repeat']").blur(function () {
        checkRepeat();
    })
    $("[name='passwd']").blur(function () {
        checkUpwd();
    })
//    为 #femRegister 绑定 submit 事件
    $("#frmRegister").submit(function () {
        return checkUphone() && checkUpwd() && checkRepeat()
    })
});