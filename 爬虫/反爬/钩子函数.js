# 参考地址：https://zhuanlan.zhihu.com/p/108207751?from_voters_page=true

1.用于定位cookie中关键参数生成位置

var code = function(){
    var org = document.cookie.__lookupSetter__('cookie');
    document.__defineSetter__("cookie",function(cookie){
        if(cookie.indexOf('TSdc75a61a')>-1){
            debugger;
        }
        org = cookie;
    });
    document.__defineGetter__("cookie",function(){return org;});
}
var script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head||document.documentElement).appendChild(script);
script.parentNode.removeChild(script);
当cookie中匹配到了 TSdc75a61a， 则插入断点。

2 请求钩子

var code = function(){
var open = window.XMLHttpRequest.prototype.open;
window.XMLHttpRequest.prototype.open = function (method, url, async){
    if (url.indexOf("MmEwMD")>-1){
        debugger;
    }
    return open.apply(this, arguments);
};
}
var script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head||document.documentElement).appendChild(script);
script.parentNode.removeChild(script);
当请求的url里包含MmEwMD时，则插入断点

3 header钩子
var code = function(){
var org = window.XMLHttpRequest.prototype.setRequestHeader;
window.XMLHttpRequest.prototype.setRequestHeader = function(key,value){
    if(key=='Authorization'){
        debugger;
    }
    return org.apply(this,arguments);
}
}
var script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head||document.documentElement).appendChild(script);
script.parentNode.removeChild(script);

当header中包含Authorization时，则插入断点
