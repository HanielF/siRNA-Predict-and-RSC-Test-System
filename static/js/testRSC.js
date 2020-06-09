var packageName = 'data_util';
var curItemName = 'char_remove';
var outerShow = $("#"+packageName)
var divShow = $("#"+curItemName);
var preShow = $("#code_char_remove");

$(function () {
    //获取点击事件的对象
    $("li.item").click(function(){
      //获取点击的对象名
      curItemName = $(this).text();
      //获取要显示或隐藏的对象
      divShow = $("#"+curItemName)
      packageName = divShow.parent().attr("id")
      outerShow = $("#"+packageName)
      preShow = $("#code_"+curItemName)
      funcName = $("#funcName")
      //显示当前对象并隐藏其他对象
      outerShow.show()
      outerShow.siblings().hide();
      divShow.show();
      divShow.siblings().hide();
      preShow.show();
      preShow.siblings("pre").hide();
      funcName.text(packageName + "." + curItemName);
      console.log("packageName: "+packageName);
      console.log("curItemName: "+curItemName);
    });
});


//===================================WebSocket部分=================================
//定义变量
var remoteHref = getRemoteIp();
var ws = new WebSocket("ws://"+remoteHref+"testrsc");
ws.onopen = function (e) {
  console.log("ws was opened successfully");
  console.log(ws)
}

ws.onmessage = function (e) {
  var data = JSON.parse(e.data);
  var res = "Return: None";
  if(data.result){
     res=data.result;
  }
  // var resArea = $("#res")
  // resArea.append(res + "\n\n")
  if (curItemName == 'make_plot' || curItemName == 'make_scatter') {
    var idx = res.indexOf("'");
    var baseImg = res.substring(idx + 1, res.length-1);
    var imgArea = document.getElementById("res-pic");
    imgArea.src = "data:image/jpg;base64," + baseImg;
    console.log("base64:")
    console.log(imgArea.src)
  }
  var resArea = document.getElementById("res");
  resArea.value += (curItemName.charAt(0).toUpperCase() + curItemName.slice(1) + " " + res + "\n\n");
  resArea.scrollTop = resArea.scrollHeight;
  console.log("Received message:");
  console.log(res);
}

//获取服务器ip
function getRemoteIp(){
  var urlPath = window.document.location.href;  //浏览器显示地址 http://127.0.0.1:8000/test
  var serverPath = urlPath.substring(7, urlPath.length-4);//服务器ip 127.0.0.1
  console.log("serverPath: " + serverPath)
  return serverPath;
}

//发送消息函数
function sendMessage(uData) {
  var data = {
    packageName: packageName,
    funcName: curItemName,
    paras: uData,
  }
  if(data.paras)
    ws.send(JSON.stringify(data));
  else
    alert("参数为空!");
  var resArea = document.getElementById("res");
  resArea.value += ("parameter list: " + data.paras.join("; ") + "\n");
  resArea.scrollTop = resArea.scrollHeight;
  console.log("send message:");
  console.log(data);
  return false;
}

function testRSC() {
    var paras = divShow.find("input");
    var paraList = new Array();
    paras.each(function () {
        paraList.push($(this).val());
    })
    console.log("paraList:")
    console.log(paraList);
    sendMessage(paraList);
}
