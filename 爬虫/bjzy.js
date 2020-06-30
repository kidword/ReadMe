// ==UserScript==
// @name         北京职业技能
// @namespace   https://www.bjjnts.cn/lessonStudy/2/34
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match       https://www.bjjnts.cn/lessonStudy/2/34
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    setInterval(function(){
     //
        //console.log($('.new_demotop').html())
	// 获取弹窗元素，存在就点击
	if ($('.layui-layer-btn0').attr('class')) {
            console.log('弹出窗口了')
		    $('.layui-layer-btn0').click()
	    } else{
            console.log('未获取到layer元素')
        };
    }, 2000)
})();
