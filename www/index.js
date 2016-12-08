run_dir = null;

tmr = { 'pan': [] , 'act': [], 'sw_m': [], 'dist': null, 'sw_a': [] };

function resize(){
	w = $('body').width();
	h = $('body').height();
	f = h / 20 > w / 20 ? w / 20 : h / 20;
	$('div.b').css({'padding': f / 3});
	$('div.b div.t').height(f).css({'font-size': f, 'margin-bottom': f / 3});
	$('div.b ck-btn').height(h / 40)/*.css('font-size', f)*/;
	$('div.b span').css('font-size', f);
}
// Live Video Functions
function tmr_pan(){
	if (tmr.pan[0]) $.get(run_dir + tmr.pan[0], function(){
//		if (!tmr.pan[0]) clearInterval(tmr.pan[2]);
		if (tmr.pan[0]) setTimeout(tmr_pan, tmr.pan[1]);
	});
}
// Movement Control Functions
function tmr_act(){
	if (tmr.act[0]) $.get(run_dir + tmr.act[0], function(){
		if (tmr.act[0]) setTimeout(tmr_act, tmr.act[1]);
		else $.get(run_dir + 'act_a');
	});
	else $.get(run_dir + 'act_a');
/*
	else $.get(run_dir + 'act_a', function(){
		if (!tmr.act[0]) clearInterval(tmr.act[2]);
	});
*/
}
function tmr_sw_m(){
	if (tmr.sw_m[0]) $.get(run_dir + 'sw_m', function(){
//		if (!tmr.sw_m[0]) clearInterval(tmr.sw_m[2]);
		if (tmr.sw_m[0]) setTimeout(tmr_sw_m, tmr.sw_m[1]);
	});
}
function dist(){
	$.get(run_dir + 'dist', function(data){
		a = data.split(",");
		if (a[0]){
			$('.b#b4 div#dist_l span.l').text(parseFloat(a[0]).toFixed(4));
			$('.b#b4 div#dist_l span.l').slideDown(0);
			$('.b#b4 div#dist_l span:not(.l)').slideUp(0);
		}else{
			$('.b#b4 div#dist_l span:not(.l)').slideDown(0);
			$('.b#b4 div#dist_l span.l').slideUp(0);
		}
		if (a[1]){
			$('.b#b4 div#dist_r span.l').text(parseFloat(a[1]).toFixed(4));
			$('.b#b4 div#dist_r span.l').slideDown(0);
			$('.b#b4 div#dist_r span:not(.l)').slideUp(0);
		}else{
			$('.b#b4 div#dist_r span:not(.l)').slideDown(0);
			$('.b#b4 div#dist_r span.l').slideUp(0);
		}
	});
}
function tmr_sw_a(){
	if (tmr.sw_a[0]) $.get(run_dir + 'sw_a', function(){
//		if (!tmr.sw_a[0]) clearInterval(tmr.sw_a[2]);
		if (tmr.sw_a[0]) setTimeout(tmr_sw_a, tmr.sw_a[1]);
	});
}
$().ready(function(){
	run_dir = $('#ip').text();
	$('.b#b1 div[id]').mousedown(function(){
//		if (tmr.pan.length) clearInterval(tmr.pan[2]);
		tmr.pan = [ $(this).attr('id'), $(this).attr('t') | 0 ];
		tmr_pan();
//		tmr.pan[2] = setInterval(tmr_pan, tmr.pan[1]);
	}).mouseup(function(){
		tmr.pan[0] = '';
	});
	$('.b#b2 div[id]').mousedown(function(){
//		if (tmr.act.length) clearInterval(tmr.act[2]);
		tmr.act = [ $(this).attr('id'), $(this).attr('t') | 0 ];
		tmr_act();
//		tmr.act[2] = setInterval(tmr_act, tmr.act[1]);
	}).mouseup(function(){
		tmr.act[0] = '';
	});
	$('.b#b3 div#sw_m').click(function(){
		if ($(this).hasClass('chk')){
			$(this).removeClass('chk');
			tmr.sw_m[0] = '';
		}else{
			$(this).addClass('chk');
//			if (tmr.sw_m.length) clearInterval(tmr.sw_m[2]);
			tmr.sw_m = [ 'sw_m', $(this).attr('t') | 0 ];
			tmr_sw_m();
//			tmr.sw_m[2] = setInterval(tmr_sw_m, tmr.sw_m[1]);
		}
	});
	$('.b#b3 div:not(.left)').click(function(){
		$.get(run_dir + $(this).attr('id'));
		window.location.assign($(this).attr('href'));
	});
	dist();
	tmr.dist = setInterval(dist, 1000);
	$('.b#b4 div#sw_a').click(function(){
		if ($(this).hasClass('chk')){
			$(this).removeClass('chk');
			tmr.sw_a[0] = '';
		}else{
			$(this).addClass('chk');
//			if (tmr.sw_a.length) clearInterval(tmr.sw_a[2]);
			tmr.sw_a = [ 'sw_a', $(this).attr('t') | 0 ];
			tmr_sw_a();
//			tmr.sw_a[2] = setInterval(tmr_sw_a, tmr.sw_a[1]);
		}
	});
	resize();
	$(window).resize(resize);
});