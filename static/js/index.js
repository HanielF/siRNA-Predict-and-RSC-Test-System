//===================================前端部分=================================
window.onload = function () {
    var tableSirna = document.querySelector('#table-sirna');
    function scrollHandle (e){
        console.log(this);
        var scrollTop = this.scrollTop;
        console.log(scrollTop);
        this.querySelector('thead').style.transform = 'translateY(' + scrollTop + 'px)';
    }

    tableSirna.addEventListener('scroll',scrollHandle);
}

//$(function(){
//    /* 给表格里面每一个td添加一个dblclick事件 */
//    $("td").dblclick(function(){
//        /* 1.先拿到这个td原来的值，然后将这个td变成一个input:text,并且原来的值不动 */
//        var tdVal = $(this).text();
//        var oInput = $("<input type='text' class='tdput' value='"+tdVal+"'/>");
//        $(this).html(oInput);
//        oInput.focus();
//
//        /* 2.失去焦点，这个td变为原来的text，value为修改过后的value */
//        oInput.blur(function(){
//            oInput.parent().html(oInput.val());
//        });
//    });
//});

//页面加载完毕后执行
$(function(){
    $("#clear_bt").click(function () {
        var text = "";
        for (i = 0; i < 8; i++) {
            text += "<tr><td contentEditable='true'></td><td></td></tr>";
        }
        document.getElementById("table-sirna-tbody").innerHTML = text;
    });
});


//===================================WebSocket部分=================================
//定义变量
var remoteHref = getRemoteIp();
var ws = new WebSocket("ws://"+remoteHref+'/predict');
ws.onopen = function(e) {
    console.log("Open ws successfully");
}
ws.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var res = [];
    if(data.result){
       res=data.result;
    }
    fillTableVals(res, "table-sirna-tbody", 1);
    console.log("Receive message:");
    console.log(res);
}

//获取服务器ip
function getRemoteIp(){
  var urlPath = window.document.location.href;  //浏览器显示地址 http://192.168.137.1:5555/demo
  var serverPath = urlPath.substring(7, urlPath.length-1);//服务器ip 192.168.137.1
  return serverPath;
}

//发送消息函数
function sendMessage(uData) {
  var data = {
    seqs: uData,
  }
  if(data.seqs)
    ws.send(JSON.stringify(data));
  else
    alert("序列数据为空!");
  console.log("Send message:");
  console.log(data);
  return false;
}

//预测函数
function predict(){
    var uData = getTableVals("table-sirna-tbody", 0);
    //若有不合法序列，或者列表为空，则不发送消息
    if (uData == null) return;
    sendMessage(uData);
}

function getTableVals(id, col) {
    var id = arguments[0] ? arguments[0] : "table-sirna-tbody";
    var col = arguments[1] ? arguments[1] : 0;
    var seqs = ""
    var tb = document.getElementById(id);
    var rows = tb.rows;
    for(var i = 0; i<rows.length; i++ ){
        var htm = rows[i].cells[col].innerHTML;
        if (htm && htm.length != 21) {
            alert("序列长度必须为21bp")
            console.log("此序列长度为：")
            console.log(htm.length)
            console.log("此序列为：")
            console.log(htm)
            return;
        }
        if (htm && htm.length==21) {
            seqs += htm + ',';
        }
    }
    return seqs;
}

function fillTableVals(data, tbid, col) {
    var tbid = arguments[1] ? arguments[1] : "table-sirna-tbody";
    var col = arguments[2] ? arguments[2] : 0;
    var tb = document.getElementById(tbid);
    var rows = tb.rows;
    for(var i = 0; i<data.length; i++ ){
        rows[i].cells[col].innerText = data[i];
    }
}