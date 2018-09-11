/**
 * Created by tarena on 18-9-6.
 */

function checkLogin() {
    $.ajax({
        url:"/checkLogin/",
        type:"post",
        data:{
            csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()
        },
        dataType:"json",
        async:false,
        success:function (data) {
            if(data.status==0){
                html = "<a href='/login/'>登录</a>， ";
                html += "<a href='/exit/'>注册有惊喜</a>";
            }else {
                var user = JSON.parse(data.txt);
                html = '<span>欢迎：'+user.uname+'</span>'+"&nbsp;&nbsp;"
                html += "<a href='/exit/' id='myCart'>退出</a>";
                html += " <a href='#'>我的购物车</a>"
            }
            $("#headline").html(html)
        }
    })
}

function loadGoods() {
    $.ajax({
        url:"/loadGoods/",
        type:"get",
        dataType:"json",
        async:false,
        success:function (data) {
            var html = ''
            $.each(data,function (i,obj) {
                var type = JSON.parse(obj);
                console.log(type);
                var goods = JSON.parse(type.goods);
                console.log(type.type_picture);
                console.log(goods);
                $.each(goods,function (j,good) {
                    var thegood = JSON.parse(good);
                    console.log(thegood)
                })
            });
            $("#main").html(html)
        }
    })
    $.get('/loadGoods/',function(data){
        var html="";
        //循环遍历data,得到类别以及对应的商品JSON
        $.each(data,function(i,obj){
            html+="<div class='item'>";
            var typeObj = JSON.parse(obj);
              html+="<p class='title'>";
                html+="<a href='#'>更多</a>";
                html+="<img src='/"+typeObj.type_picture+"'>";
              html+="</p>";
              html+="<ul>";
                //将obj.goods转换成JSON数组
                var goodsArr = JSON.parse(typeObj.goods);
                $.each(goodsArr,function(i,goods){
                  //goods表示的是每一个商品
                    var good = JSON.parse(goods);
                  html+="<li ";
                  if((i+1) % 5 == 0)
                    html+="class='no-margin'";
                  html+=">";
                    //加载商品图片
                    html+="<p>";
                      html+="<img src='/"+good.picture+"'>";
                    html+="</p>";
                    //加载商品内容
                    html+="<div class='content'>";
                      //加载购物车标识
                      html+="<a href='javascript:AddCart("+good.id+"') class='cart'>";
                        html+="<img src='/static/images/cart.png'>";
                      html+="</a>";
                      //加载商品标题
                      html+="<p>"+good.title+"</p>";
                      //加载商品价格以及规格
                      html+="<span>&yen;"+good.price+"/"+good.spec+"</span>";
                    html+="</div>";
                  html+="</li>";
                });
              html+="</ul>";
            html+="</div>";
        });

        $("#main").html(html);
    },'json');
}

function AddCart(goodsid) {
    $.ajax({
        url:"/checkLogin/",
        type:"post",
        data:{
            csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val()
        },
        dataType:"json",
        async:false,
        success:function (data) {
            if(data.status==0){
                alert('请先登录')
            }else {

            }
        }
    })
}

//加载当前购物车的商品数量
function load_count() {
    $.get('/cart_count/',function (data) {
        $("#myCart").html("我的购物车("+data.count+")")
    },'json')
}

$(function () {
    checkLogin();
    loadGoods();
    load_count();
});