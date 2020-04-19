#!/perl/bin/perl
# ↑使用合乎服務器的路徑。

$this_script = 'game.cgi';
#require './jcode.pl';
require './cgi-lib.pl';
require './town_ini.cgi';
require './town_lib.pl';
&decode;
#維護檢查
	if($mente_flag == 1 && $in{'admin_pass'} eq "" && $in{'mode'} ne ""){&error("$mente_message")}
$seigenyou_now_time = time;
#限制時間檢查
		$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $access_byou);
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("暫時未能行動。請等候$ato_nanbyou秒以後")}
		
#條件分歧
	if($in{'mode'} eq "battle"){&battle;}
	elsif($in{'mode'} eq "doukyo"){&doukyo;}
	elsif($in{'mode'} eq "c_league"){&c_league;}
	elsif($in{'mode'} eq "new"){&new;}
	elsif($in{'mode'} eq "data_hozon"){&data_hozon;}
	else{&error("請用「返回」按鈕返回街");}
exit;
	
#############以下子程序
sub battle {
	open(IN,"$logfile") || &error("Open Error : $logfile");
	@aite_erabi = <IN>;
	close(IN);
#	srand(time^$$);
	$randed= int (rand($#aite_erabi));
	$aite_erabi=splice(@aite_erabi,$randed,1);
	($aite_id) = split(/<>/,$aite_erabi);
	if ($aite_id eq "$k_id"){&message("找不到對手。。","login_view");}
	&openAitelog ($aite_id);
	
	$aite_energy_max = int(($aite_looks/12) + ($aite_tairyoku/4) + ($aite_kenkou/4) + ($aite_speed/8) + ($aite_power/8) + ($aite_wanryoku/8) + ($aite_kyakuryoku/8));
	$aite_nou_energy_max = int(($aite_kokugo/6) + ($aite_suugaku/6) + ($aite_rika/6) + ($aite_syakai/6) + ($aite_eigo/6)+ ($aite_ongaku/6)+ ($aite_bijutu/6));
#如果圖標處於代入
	if ($kounyuu){$icon_hyouzi_a = "<img src=$kounyuu width=32 height=32 align=left>";}else{$icon_hyouzi_a = "";}
	if ($aite_kounyuu){$aite_icon_hyouzi_a = "<img src=$aite_kounyuu width=32 height=32 align=left>";}else{$aite_icon_hyouzi_a = "";}
	&header;
	print <<"EOM";
	<br><br><table width="600" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr align=center><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2 bgcolor=#ccff66 >
$icon_hyouzi_a$name君
</td></tr>
<tr><td align=right><span class=honbun3>頭腦力</span>：</td><td>$nou_energy</td></tr>
<tr><td align=right><span class=honbun3>身體力</span>：</td><td>$energy</td></tr>
<tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td align=center><span class=tyuu colspan=2>頭  腦</span></td></tr>
<tr><td align=right><span class=honbun3>國語</span>：</td><td>$kokugo</td></tr>
<tr><td align=right><span class=honbun3>數學</span>：</td><td>$suugaku</td></tr>
<tr><td align=right><span class=honbun3>理科</span>：</td><td>$rika</td></tr>
<tr><td align=right><span class=honbun3>社會</span>：</td><td>$syakai</td></tr>
<tr><td align=right><span class=honbun3>英語</span>：</td><td>$eigo</td></tr>
<tr><td align=right><span class=honbun3>音樂</span>：</td><td>$ongaku</td></tr>
<tr><td align=right><span class=honbun3>美術</span>：</td><td>$bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>身  體</span></td></tr>
<tr><td  align=right nowrap><span class=honbun3>容貌</span>：</td><td>$looks</td></tr>
<tr><td align=right><span class=honbun3>體力</span>：</td><td>$tairyoku</td></tr>
<tr><td align=right><span class=honbun3>健康</span>：</td><td>$kenkou</td></tr>
<tr><td align=right nowrap><span class=honbun3>速度</span>：</td><td>$speed</td></tr>
<tr><td align=right><span class=honbun3>力</span>：</td><td>$power</td></tr>
<tr><td align=right><span class=honbun3>腕力</span>：</td><td>$wanryoku</td></tr>
<tr><td align=right><span class=honbun3>脚力</span>：</td><td>$kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>其他</span></td>
<tr><td align=right><span class=honbun3>LOVE</span>：</td><td>$love</td></tr>
<tr><td align=right><span class=honbun3>興趣</span>：</td><td>$unique</td></tr>
<tr><td align=right><span class=honbun3>淫蕩</span>：</td><td>$etti</td></tr>
</table>
	</td><td>
	<div class=tyuu>在街遇到了$aite_name君！</div><br><br>
	<div class=dai>Fight start !!</div>
	</td><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2 bgcolor=#ffcc99>
$aite_icon_hyouzi_a$aite_name君
</td></tr>
<tr><td align=right><span class=honbun3>頭腦力</span>：</td><td>$aite_nou_energy_max</td></tr>
<tr><td align=right><span class=honbun3>身體力</span>：</td><td>$aite_energy_max</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td colspan=2 align=center><span class=tyuu>頭　腦</span></td></tr>
<tr><td align=right><span class=honbun3>國語</span>：</td><td>$aite_kokugo</td></tr>
<tr><td align=right><span class=honbun3>數學</span>：</td><td>$aite_suugaku</td></tr>
<tr><td align=right><span class=honbun3>理科</span>：</td><td>$aite_rika</td></tr>
<tr><td align=right><span class=honbun3>社會</span>：</td><td>$aite_syakai</td></tr>
<tr><td align=right><span class=honbun3>英語</span>：</td><td>$aite_eigo</td></tr>
<tr><td align=right><span class=honbun3>音樂</span>：</td><td>$aite_ongaku</td></tr>
<tr><td align=right><span class=honbun3>美術</span>：</td><td>$aite_bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>身　體</span></td></tr>
<tr><td  align=right nowrap><span class=honbun3>容貌</span>：</td><td>$aite_looks</td></tr>
<tr><td align=right><span class=honbun3>體力</span>：</td><td>$aite_tairyoku</td></tr>
<tr><td align=right><span class=honbun3>健康</span>：</td><td>$aite_kenkou</td></tr>
<tr><td align=right nowrap><span class=honbun3>速度</span>：</td><td>$aite_speed</td></tr>
<tr><td align=right><span class=honbun3>力</span>：</td><td>$aite_power</td></tr>
<tr><td align=right><span class=honbun3>腕力</span>：</td><td>$aite_wanryoku</td></tr>
<tr><td align=right><span class=honbun3>腳力</span>：</td><td>$aite_kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>其　他</span></td>
<tr><td align=right><span class=honbun3>LOVE</span>：</td><td>$aite_love</td></tr>
<tr><td align=right><span class=honbun3>有趣</span>：</td><td>$aite_unique</td></tr>
<tr><td align=right><span class=honbun3>淫蕩</span>：</td><td>$aite_etti</td></tr>
</table>
	</td></tr></table>
EOM

	if ($speed > $aite_speed){$turn =1;}
	$sentou_kaisuu =0;
	foreach (1..50){
			print "<br><br><table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"5\" align=center class=yosumi><tr><td colspan=2>";
			if ($turn == 1){&kougeki (1,$name);			#自己的攻擊
			}else{&kougeki (0,$aite_name);}			#對方的攻擊
			print <<"EOM";
			</td></tr>
			<tr><td align=left>
			<div class=tyuu>頭腦力：$nou_energy</div>
			<div class=tyuu>身體力：$energy</div>
			</td>
			<td align=right>
			<div class=tyuu>頭腦力：$aite_nou_energy_max</div>
			<div class=tyuu>身體力：$aite_energy_max</div>
			</td></tr></table>
EOM
			$sentou_kaisuu ++;
			if ($aite_energy_max <= 0){$win_flag=1;last;}
			if ($aite_nou_energy_max <= 0){$win_flag=2;last;}
			if ($energy <= 0){$win_flag=3;last;}
			if ($nou_energy <= 0){$win_flag=4;last;}
			if ($turn == 1){$turn = 0;} else {$turn = 1;}
	}
	print "<br><br>";
	if ($energy < 0){$energy = 0;}
	if ($nou_energy < 0){$nou_energy = 0;}
	$get_money=$sentou_kaisuu*30;
	if ($win_flag == 1) {
		$get_money *= 5;
		print "<div align=center style=\"color:#339933;font-size:14px;\">勝了！<br>從倒下的$aite_name君的錢包<r>奪走了$get_money元。</div>";
		$money += $get_money;
	}elsif($win_flag == 2){
		$get_money *= 5;
		print "<div align=center style=\"color:#339933;font-size:14px;\">勝了！<br>從精神崩潰的$aite_name君的錢包<br>奪走了$get_money元。</div>";
		$money += $get_money;
	}elsif($win_flag == 3){
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">輸了。。<br>從破破爛爛的$name君的錢包<br>被奪去了$get_money元。</div>";
		$money -= $get_money;
	}elsif($win_flag == 4){
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">輸了。。<br>從意識朦朧的$name君的錢包<br>被奪去了$get_money元。</div>";
		$money -= $get_money;
	}else{
		print "未能分出勝負。。";
	}
#データ更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
	&hooter("login_view","返回");
	exit;
}

sub kougeki {
#隨機選擇攻擊內容
		$battle_rand = int(rand(16))+1;
		print "<table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=center><tr align=center><td>";
##自己的攻擊的情況
		if (@_[0] == 1){
			print "<div style=\"color:#339933;font-size:12px;\" align=left>@_[1]的攻擊！<br>";
#攻擊內容
			&kougekinaiyou (1,$aite_name);
#結果表示
			if ($damage eq "no_d"){
					print "<div style=\"color:#ff3300;font-size:12px;\" align=right>$return_naiyou</div>\n";
			}else{
					print "<div style=\"color:#339933;font-size:12px;\" align=right>$return_naiyou</div>\n";
					if ($battle_rand <= 8 || $battle_rand == 14){
						$aite_nou_energy_max -= $damage;
					}else{
						$aite_energy_max -= $damage;
					}
			}
			
##對方的攻擊的情況
		}else {
			print "<div style=\"color:#ff3300;font-size:12px;\" align=right>@_[1]的攻擊！<br>";
			&kougekinaiyou (0,$name);
#結果表示
#不問自己的情況
			if ($damage eq "no_d"){
					print "<div style=\"color:#339933;font-size:12px;\" align=left>$return_naiyou</div>\n";
			}else{
#受到了損傷的情況
					print "<div style=\"color:#ff3300;font-size:12px;\" align=left>$return_naiyou</div>\n";
#頭腦損傷
					if ($battle_rand <= 8 || $battle_rand == 14){
						$nou_energy -= $damage;
					}else{
#肉體損傷
						$energy -= $damage;
					}
			}
		}
	print "</td></tr></table>";
}

###攻擊內容的損傷處理子程序
sub kougekinaiyou {
# @_[0]＝要是1自己的攻擊，要是0對方的攻擊
	if (@_[0] == 1){$align_settei = "align=left";}else{$align_settei = "align=right";}
#國語的攻擊
		if ($battle_rand ==1){
			print "你知道這個漢字怎樣讀嗎？@_[1]走近了！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],1);
			if ($damage eq "no_d"){$return_naiyou = "因為@_[1]擅長漢字，所以輕易地回答了。。";}
			else{$return_naiyou = "「喲，不曉得怎樣讀。。」@_[1] 受<span style=\"font-size:18px\">$damage</span> 精神損害！！";}
		}

		if ($battle_rand ==2){
			print "打算以難的數學問題使@_[1]感到困難！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],2);
			if ($damage eq "no_d"){$return_naiyou = "因為@_[1]擅長數學，所以沒有效果。。";}
			else{$return_naiyou = "完全無法理解，@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==3){
			print "以理科的題目使@_[1]動搖！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],3);
			if ($damage eq "no_d"){$return_naiyou = "因為@_[1]擅長理科，所以沒有效果。。";}
			else{$return_naiyou = "感到很混亂了的@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==4){
			print "向@_[1]質問有名的歷史事件的年號！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],4);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]歷史是大擅長。。";}
			else{$return_naiyou = "著急的@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==5){
			print "突然開始說英語！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],5);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]也用英語回答了。。";}
			else{$return_naiyou = "「明白應該更努力去學習英語。。」@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==6){
			print "擊打附近的鋼琴鍵盤！質詢這個音階是什麼？</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],6);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]簡單地對問題回答了。。";}
			else{$return_naiyou = "「哇，不知道。。」@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==7){
			print "流利地描畫景色對@_[1]顯示了！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],7);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]笑說「這個非常拙劣！」。。";}
			else{$return_naiyou = "「呀，很好。。」@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==8){
			print "以容貌取勝！向@_[1]逼近了！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],8);
			if ($damage eq "no_d"){$return_naiyou = "但@_[1]「勝了」吧。";}
			else{$return_naiyou = "「呀。。」@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==9){
			print "帶入了體力勝負</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],9);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]對體力很有自信。。";}
			else{$return_naiyou = "@_[1]受到了<span style=\"font-size:18px\">$damage</span>的肉體疲勞！";}
		}

		if ($battle_rand ==10){
			print "打算用快速的步法播弄@_[1]！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],11);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]很快速。。";}
			else{$return_naiyou = "被播弄的@_[1]受到了<span style=\"font-size:18px\">$damage</span>的肉體疲勞！";}
		}

		if ($battle_rand ==11){
			print "打算用力把@_[1]猛扔出去！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],12);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]更有力。。";}
			else{$return_naiyou = "被猛扔出去的@_[1]受到了 <span style=\"font-size:18px\">$damage</span>的肉體損傷！";}
		}

		if ($battle_rand ==12){
			print "向@_[1]打了拳！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],13);
			if ($damage eq "no_d"){$return_naiyou = "可是@_[1]及時地避開了。。";}
			else{$return_naiyou = "承受這拳的@_[1]受到了<span style=\"font-size:18px\">$damage</span>的肉體損傷！";}
		}

		if ($battle_rand ==13){
			print "踢到了@_[1]！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],14);
			if ($damage eq "no_d"){$return_naiyou = "可是@_[1]及時地避開了。。";}
			else{$return_naiyou = "這一踢令@_[1]受到了<span style=\"font-size:18px\">$damage</span>的肉體損傷！";}
		}

		if ($battle_rand ==14){
			print "開始說以愛的戀人引以為傲！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],15);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]說很愛自己戀人。。";}
			else{$return_naiyou = "「呀~ 真令人羨慕。。」@_[1]受到了<span style=\"font-size:18px\">$damage</span>的精神損害！";}
		}

		if ($battle_rand ==15){
			print "向@_[1]逗笑！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],16);
			if ($damage eq "no_d"){$return_naiyou = "「節省少少吧！」@_[1]一點反應也沒有。。";}
			else{$return_naiyou = "@_[1]笑到滾地，就在那時吃了一拳造成 <span style=\"font-size:18px\">$damage</span>的傷害！";}
		}
		
		if ($battle_rand ==16){
			print "披露平時色情培育出的秘密技能！</div><br>\n";
# iryoku_hantei (攻擊者,攻擊的內容)
			&iryoku_hantei (@_[0],17);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]也不示弱。。";}
			else{$return_naiyou = "被播弄的@_[1]受到了 <span style=\"font-size:18px\">$damage</span>的肉體損傷！";}
		}
}

#威力判斷子程序
sub iryoku_hantei {
#每攻擊的內容的能力值
	$iryoku_hanteiti = @_[1] + 5;
	if (@_[0] == 1){
		$hantei_kakkati = $nouryoku_suuzi_hairetu[$iryoku_hanteiti]  - $aite_nouryoku_suuzi_hairetu[$iryoku_hanteiti] ;
	}else{
		$hantei_kakkati = $aite_nouryoku_suuzi_hairetu[$iryoku_hanteiti]  - $nouryoku_suuzi_hairetu[$iryoku_hanteiti] ;
	}
	if ($hantei_kakkati <= 0){
			$damage = "no_d";
	}else{
			$damage = "$hantei_kakkati";
	}
}

####同居人
sub doukyo {
		if ($chara_x_size == "" && $chara_y_size == ""){
			$chara_gazou_size = "";
			$c_size_comment = "";
		}else{
			$chara_gazou_size = "width=$chara_x_size height=$chara_y_size";
			$c_size_comment = "畫像尺寸是橫$chara_x_size象素，縱$chara_y_size象素。";
		}
		$chara_settei_file="./member/$k_id/chara_ini.cgi";
			if (! -e $chara_settei_file){
				open(OIB,">$chara_settei_file") || &error("Write Error : $chara_settei_file");
				chmod 0666,"$chara_settei_file";
				close(OIB);
			}
		open(CSF,"$chara_settei_file") || &error("Open Error : $chara_settei_file");
			$chara_settei_data = <CSF>;
			($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_point,$ch_yuusyoukai,$ch_kokugo,$ch_suugaku,$ch_rika,$ch_syakai,$ch_eigo,$ch_ongaku,$ch_bijutu,$ch_looks,$ch_tairyoku,$ch_kenkou,$ch_speed,$ch_power,$ch_wanryoku,$ch_kyakuryoku,$ch_love,$ch_unique,$ch_etti,$ch_energy,$ch_nou_energy,$ch_sintai,$ch_zunou,$ch_me_kokugo,$ch_me_suugaku,$ch_me_rika,$ch_me_syakai,$ch_me_eigo,$ch_me_ongaku,$ch_me_bijutu,$ch_me_looks,$ch_me_tairyoku,$ch_me_kenkou,$ch_me_speed,$ch_me_power,$ch_me_wanryoku,$ch_me_kyakuryoku,$ch_me_love,$ch_me_unique,$ch_me_etti,$ch_k_yobi3,$ch_k_yobi4,$ch_k_yobi5)= split(/<>/,$chara_settei_data);
		close(CSF);
		
#造型設定處理的情況
		if ($in{'command'} eq "make_chara"){
			if (length($in{'ch_name'}) > 30) {&error("登場人物的名字是30字以內");}
			$cgi_lib'maxdata = 51200;
			$MaxW = 80;	# 橫幅
			$MaxH = 80;	# 縱幅
			if ($ch_k_id eq ""){$ch_k_id = $k_id;}
			if ($in{'ch_name'}){$ch_name = $in{'ch_name'};}
			if ($ch_oyaname eq ""){$ch_oyaname = $name;}
			if ($in{'ch_gazou'}){$ch_gazou = $in{'ch_gazou'};}
			if ($in{'ch_kokugo'} && $kokugo > $in{'ch_kokugo'}) { $ch_kokugo += $in{'ch_kokugo'}; $message_in .= "國語參數提高了$in{'ch_kokugo'}。<br>"; $hikukane += $in{'ch_kokugo'}; $kokugo -=$in{'ch_kokugo'}; }
			if ($in{'ch_suugaku'} && $suugaku > $in{'ch_suugaku'}) { $ch_suugaku += $in{'ch_suugaku'}; $message_in .= "提高了數學參數$in{'ch_suugaku'}。<br>"; $hikukane += $in{'ch_suugaku'}; $suugaku -=$in{'ch_suugaku'};}
			if ($in{'ch_rika'} && $rika > $in{'ch_rika'}) { $ch_rika += $in{'ch_rika'}; $message_in .= "提高了理科參數$in{'ch_rika'}。<br>"; $hikukane += $in{'ch_rika'}; $rika -=$in{'ch_rika'};}
			if ($in{'ch_syakai'} && $syakai > $in{'ch_syakai'}) { $ch_syakai += $in{'ch_syakai'}; $message_in .= "提高了社會參數$in{'ch_rika'}。<br>"; $hikukane += $in{'ch_syakai'}; $syakai -=$in{'ch_syakai'};}
			if ($in{'ch_eigo'} && $eigo > $in{'ch_eigo'}) { $ch_eigo += $in{'ch_eigo'}; $message_in .= "提高了英語參數$in{'ch_eigo'}。<br>"; $hikukane += $in{'ch_eigo'}; $eigo -=$in{'ch_eigo'};}
			if ($in{'ch_ongaku'} && $ongaku > $in{'ch_ongaku'}) { $ch_ongaku += $in{'ch_ongaku'}; $message_in .= "提高了音樂參數$in{'ch_ongaku'}。<br>"; $hikukane += $in{'ch_ongaku'}; $ongaku -=$in{'ch_ongaku'};}
			if ($in{'ch_bijutu'} && $bijutu > $in{'ch_bijutu'}) { $ch_bijutu += $in{'ch_bijutu'}; $message_in .= "提高了美術參數$in{'ch_bijutu'}。<br>"; $hikukane += $in{'ch_bijutu'}; $bijutu -=$in{'ch_bijutu'};}
			if ($in{'ch_looks'} && $looks > $in{'ch_looks'}) { $ch_looks += $in{'ch_looks'}; $message_in .= "提高了容貌參數$in{'ch_looks'}。<br>"; $hikukane += $in{'ch_looks'}; $looks -=$in{'ch_looks'};}
			if ($in{'ch_tairyoku'} && $tairyoku > $in{'ch_tairyoku'}) { $ch_tairyoku += $in{'ch_tairyoku'}; $message_in .= "提高了體力參數$in{'ch_tairyoku'}。<br>"; $hikukane += $in{'ch_tairyoku'}; $tairyoku -=$in{'ch_tairyoku'};}
			if ($in{'ch_kenkou'} && $kenkou > $in{'ch_kenkou'}) { $ch_kenkou += $in{'ch_kenkou'}; $message_in .= "提高了健康參數$in{'ch_kenkou'}。<br>"; $hikukane += $in{'ch_kenkou'}; $kenkou -=$in{'ch_kenkou'};}
			if ($in{'ch_speed'} && $speed > $in{'ch_speed'}) { $ch_speed += $in{'ch_speed'}; $message_in .= "提高了速度參數$in{'ch_speed'}。<br>"; $hikukane += $in{'ch_speed'}; $speed -=$in{'ch_speed'};}
			if ($in{'ch_power'} && $power > $in{'ch_power'}) { $ch_power += $in{'ch_power'}; $message_in .= "提高了力參數$in{'ch_power'}。<br>"; $hikukane += $in{'ch_power'}; $power -=$in{'ch_power'};}
			if ($in{'ch_wanryoku'} && $wanryoku > $in{'ch_wanryoku'}) { $ch_wanryoku += $in{'ch_wanryoku'}; $message_in .= "提高了腕力參數$in{'ch_wanryoku'}。<br>"; $hikukane += $in{'ch_wanryoku'}; $wanryoku -=$in{'ch_wanryoku'};}
			if ($in{'ch_kyakuryoku'} && $kyakuryoku > $in{'ch_kyakuryoku'}) { $ch_kyakuryoku += $in{'ch_kyakuryoku'}; $message_in .= "提高了腳力參數$in{'ch_kyakuryoku'}。<br>"; $hikukane += $in{'ch_kyakuryoku'}; $kyakuryoku -=$in{'ch_kyakuryoku'};}
			if ($in{'ch_love'} && $love > $in{'ch_love'}) { $ch_love += $in{'ch_love'}; $message_in .= "提高了LOVE參數$in{'ch_love'}。<br>"; $hikukane += $in{'ch_love'}; $love -=$in{'ch_love'};}
			if ($in{'ch_unique'} && $unique > $in{'ch_unique'}) { $ch_unique += $in{'ch_unique'}; $message_in .= "提高了有趣參數$in{'ch_unique'}。<br>"; $hikukane += $in{'ch_unique'}; $unique -=$in{'ch_unique'};}
			
			if ($in{'ch_etti'} && $etti > $in{'ch_etti'}) { $ch_etti += $in{'ch_etti'}; $message_in .= "提高了淫蕩參數$in{'ch_etti'}。<br>"; $hikukane += $in{'ch_etti'}; $etti -=$in{'ch_etti'};}
			
			if($hikukane =~ /[^0-9]/){&error("數值不妥");}
			if ($hikukane < 0){&error("數值不妥");}
			if ($hikukane != 0){
				$message_in .= "花費了$hikukane千元的錢。<br>";
			}
			if ($money < $hikukane*1000){&error("錢不夠");}
			
			if ($in{'ch_me_kokugo'}) { $ch_me_kokugo = "$in{'ch_me_kokugo'}";}
			if ($in{'ch_me_suugaku'}) { $ch_me_suugaku = "$in{'ch_me_suugaku'}";}
			if ($in{'ch_me_rika'}) { $ch_me_rika = "$in{'ch_me_rika'}";}
			if ($in{'ch_me_syakai'}) { $ch_me_syakai = "$in{'ch_me_syakai'}";}
			if ($in{'ch_me_eigo'}) { $ch_me_eigo = "$in{'ch_me_eigo'}";}
			if ($in{'ch_me_ongaku'}) { $ch_me_ongaku = "$in{'ch_me_ongaku'}";}
			if ($in{'ch_me_bijutu'}) { $ch_me_bijutu = "$in{'ch_me_bijutu'}";}
			if ($in{'ch_me_looks'}) { $ch_me_looks = "$in{'ch_me_looks'}";}
			if ($in{'ch_me_tairyoku'}) { $ch_me_tairyoku = "$in{'ch_me_tairyoku'}";}
			if ($in{'ch_me_kenkou'}) { $ch_me_kenkou = "$in{'ch_me_kenkou'}";}
			if ($in{'ch_me_speed'}) { $ch_me_speed = "$in{'ch_me_speed'}";}
			if ($in{'ch_me_power'}) { $ch_me_power = "$in{'ch_me_power'}";}
			if ($in{'ch_me_wanryoku'}) { $ch_me_wanryoku = "$in{'ch_me_wanryoku'}";}
			if ($in{'ch_me_kyakuryoku'}) { $ch_me_kyakuryoku = "$in{'ch_me_kyakuryoku'}";}
			if ($in{'ch_me_love'}) { $ch_me_love = "$in{'ch_me_love'}";}
			if ($in{'ch_me_unique'}) { $ch_me_unique = "$in{'ch_me_unique'}";}
			if ($in{'ch_me_etti'}) { $ch_me_etti = "$in{'ch_me_etti'}";}
			if  ($message_in eq ""){$message_in .= "變更了。";}

#			if ($in{'upfile'}) { &UpFile; }
#力的MAX值計算
	$ch_sintai = int(($ch_looks/10) + ($ch_tairyoku/10) + ($ch_kenkou/10) + ($ch_speed/10) + ($ch_power/10) + ($ch_wanryoku/10) + ($ch_kyakuryoku/10)+ ($ch_etti/10));
	$ch_zunou = int(($ch_kokugo/10) + ($ch_suugaku/10) + ($ch_rika/10) + ($ch_syakai/10) + ($ch_eigo/10)+ ($ch_ongaku/10)+ ($ch_bijutu/10)+ ($ch_love/10)+ ($ch_unique/10));
	
			$make_ch_temp ="$ch_k_id<>$ch_name<>$ch_oyaname<>$ch_gazou<>$ch_point<>$ch_yuusyoukai<>$ch_kokugo<>$ch_suugaku<>$ch_rika<>$ch_syakai<>$ch_eigo<>$ch_ongaku<>$ch_bijutu<>$ch_looks<>$ch_tairyoku<>$ch_kenkou<>$ch_speed<>$ch_power<>$ch_wanryoku<>$ch_kyakuryoku<>$ch_love<>$ch_unique<>$ch_etti<>$ch_energy<>$ch_nou_energy<>$ch_sintai<>$ch_zunou<>$ch_me_kokugo<>$ch_me_suugaku<>$ch_me_rika<>$ch_me_syakai<>$ch_me_eigo<>$ch_me_ongaku<>$ch_me_bijutu<>$ch_me_looks<>$ch_me_tairyoku<>$ch_me_kenkou<>$ch_me_speed<>$ch_me_power<>$ch_me_wanryoku<>$ch_me_kyakuryoku<>$ch_me_love<>$ch_me_unique<>$ch_me_etti<>$ch_k_yobi3<>$ch_k_yobi4<>$ch_k_yobi5";
	&lock;
	open(MTLO,">$chara_settei_file") || &error("Write Error : $chara_settei_file");
	print MTLO $make_ch_temp;
	close(MTLO);
	&unlock;
	$money -= $hikukane * 1000;
					&temp_routin;
					&log_kousin($my_log_file,$k_temp);
	&message("$message_in","doukyo","game.cgi");
		}		#作成處理的情況閉上
	
#評語的初始化
	if ($ch_me_kokugo eq ""){$ch_me_kokugo = "這個漢字能讀嗎？";}
	if ($ch_me_suugaku eq ""){$ch_me_suugaku = "明白這個數學的答案嗎？";}
	if ($ch_me_rika eq ""){$ch_me_rika = "考慮這個公式的誰知道嗎？";}
	if ($ch_me_syakai eq ""){$ch_me_syakai = "知不知道這個事件是何年發生？";}
	if ($ch_me_eigo eq ""){$ch_me_eigo = "知道這個英語單詞的意義嗎？";}
	if ($ch_me_ongaku eq ""){$ch_me_ongaku = "作了這個曲子是誰知道嗎？";}
	if ($ch_me_bijutu eq ""){$ch_me_bijutu = "請看看這個畫兒！";}
	if ($ch_me_looks eq ""){$ch_me_looks = "以容貌分勝負！";}
	if ($ch_me_tairyoku eq ""){$ch_me_tairyoku = "以體力取勝！";}
	if ($ch_me_kenkou eq ""){$ch_me_kenkou = "對健康有自信！";}
	if ($ch_me_speed eq ""){$ch_me_speed = "來比這個速度嗎？";}
	if ($ch_me_power eq ""){$ch_me_power = "以搶截分勝負！";}
	if ($ch_me_wanryoku eq ""){$ch_me_wanryoku = "以掰腕子是勝負！";}
	if ($ch_me_kyakuryoku eq ""){$ch_me_kyakuryoku = "踢踢踢！";}
	if ($ch_me_love eq ""){$ch_me_love = "愛的深度不輸！";}
	if ($ch_me_unique eq ""){$ch_me_unique = "這個噱頭怎麼？";}
	if ($ch_me_etti eq ""){$ch_me_etti = "色情不輸！";}
#画面表示
		if ($ch_gazou){$charaimage_gazou = "<img src=$ch_gazou $chara_gazou_size>";}
		else{$charaimage_gazou = "";}
		&header(item_style);
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td bgcolor=#ffffff>能在這裡製作自己登場人物。登場人物由自己的參數和投入錢的事增長。<br>製作最強的登場人物參加「Ｃ聯盟」吧。<br>(將來性自己的家造型的角能跟來訪者的交換)</td>
	<td  bgcolor=#333333 align=center width=200><img src="$img_dir/chara_tytle.gif"></td>
	</tr></table><br>
EOM
	if ($in{'command'} eq ""){
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="doukyo">
	<input type=hidden name=command value="make_chara">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	
		<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
		<tr><td>
		<div align=center>
		$charaimage_gazou<br>
		<div class=honbun2>$ch_name</div><br>
		頭腦能量：$ch_zunou<br>
		身體能力：$ch_sintai
		</div>
	
	</td><td>
	<div class=honbun2>●人物的名字(全角15個字以內)</div>※隨時能變更。<br>
	<input type=text size=30 name=ch_name value=$ch_name><br><br>
	
	<div class=honbun2>●登場人物畫像</div>（http://～開始的絕對URL。$c_size_comment ※即使無畫像構亦可。）<br>※隨時能變更。<br>
	<!--<input type=file name="upfile" size=30><br>-->
	<input type=text name="ch_gazou" size=60 value=$ch_gazou><br><br>
	
	<div class=honbun2>●參數提高</div>
	輸入了的數值的參數被自己設置，並且花費那個數值×1千元的費用。<br>
	登場人物被給予的數值的參數提高。<br>
	<table border="0"><tr>
	<td>國語</td><td><input type=text name="ch_kokugo" size=10></td></td>
	<td>數學</td><td><input type=text name="ch_suugaku" size=10></td>
	<td>理科</td><td><input type=text name="ch_rika" size=10></td>
	<td>社會</td><td><input type=text name="ch_syakai" size=10></td>
	<td>英語</td><td><input type=text name="ch_eigo" size=10></td></tr><tr>
	<td>音樂</td><td><input type=text name="ch_ongaku" size=10></td>
	<td>美術</td><td><input type=text name="ch_bijutu" size=10></td>
	<td>容貌</td><td><input type=text name="ch_looks" size=10></td>
	<td>體力</td><td><input type=text name="ch_tairyoku" size=10></td>
	<td>健康</td><td><input type=text name="ch_kenkou" size=10></td></tr><tr>
	<td>速度</td><td><input type=text name="ch_speed" size=10></td>
	<td>力</td><td><input type=text name="ch_power" size=10></td>
	<td>腕力</td><td><input type=text name="ch_wanryoku" size=10></td>
	<td>腳力</td><td><input type=text name="ch_kyakuryoku" size=10></td>
	<td>LOVE</td><td><input type=text name="ch_love" size=10></td></tr><tr>
	<td>有趣</td><td><input type=text name="ch_unique" size=10></td>
	<td>淫蕩</td><td><input type=text name="ch_etti" size=10>
	</tr></table>

	</td><td width=150>
	<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;" bgcolor=#ffffcc width=100%>
<td colspan=2 align=center><span class=tyuu>頭　腦</span></td></tr>
<tr><td align=right><span class=honbun5>國語</span>：</td><td align=right>$ch_kokugo</td></tr>
<tr><td align=right><span class=honbun5>數學</span>：</td><td align=right>$ch_suugaku</td></tr>
<tr><td align=right><span class=honbun5>理科</span>：</td><td align=right>$ch_rika</td></tr>
<tr><td align=right><span class=honbun5>社會</span>：</td><td align=right>$ch_syakai</td></tr>
<tr><td align=right><span class=honbun5>英語</span>：</td><td align=right>$ch_eigo</td></tr>
<tr><td align=right><span class=honbun5>音樂</span>：</td><td align=right>$ch_ongaku</td></tr>
<tr><td align=right><span class=honbun5>美術</span>：</td><td align=right>$ch_bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>身　體</span></td></tr>
<tr><td  align=right><span class=honbun5>容貌</span>：</td><td align=right>$ch_looks</td></tr>
<tr><td align=right><span class=honbun5>體力</span>：</td><td align=right>$ch_tairyoku</td></tr>
<tr><td align=right><span class=honbun5>健康</span>：</td><td align=right>$ch_kenkou</td></tr>
<tr><td align=right><span class=honbun5>速度</span>：</td><td align=right>$ch_speed</td></tr>
<tr><td align=right><span class=honbun5>力</span>：</td><td align=right>$ch_power</td></tr>
<tr><td align=right><span class=honbun5>腕力</span>：</td><td align=right>$ch_wanryoku</td></tr>
<tr><td align=right><span class=honbun5>腳力</span>：</td><td align=right>$ch_kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>其　他</span></td>
<tr><td align=right><span class=honbun5>LOVE</span>：</td><td align=right>$ch_love</td></tr>
<tr><td align=right><span class=honbun5>有趣</span>：</td><td align=right>$ch_unique</td></tr>
<tr><td align=right><span class=honbun5>淫蕩</span>：</td><td align=right>$ch_etti</td></tr>
</table>
	</td></tr>
	<tr><td colspan=3>
	<div align=center><input type=submit value=" O K "></div>
	</td></tr></table>
	</form>
	
	<div align=center><form method="POST" action="$this_script">
	<input type=hidden name=mode value="doukyo">
	<input type=hidden name=command value="com_henkou">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="評語變更形式輸出"></form></div>
	
EOM
	}
	
	if ($in{'command'} eq "com_henkou"){
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="doukyo">
	<input type=hidden name=command value="make_chara">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td>
	<div class=honbun2>●作戰的時候的評語</div>
	每各能力記上以那個能力取勝的時候說的評語。※40字以內（太多會令表現不安定）<br><br>
	<table border="0"><tr>
	<td>國語</td><td><input type=text name="ch_me_kokugo" size=80 value=$ch_me_kokugo></td></td></tr><tr>
	<td>數學</td><td><input type=text name="ch_me_suugaku" size=80 value=$ch_me_suugaku></td></tr><tr>
	<td>理科</td><td><input type=text name="ch_me_rika" size=80 value=$ch_me_rika></td></tr><tr>
	<td>社會</td><td><input type=text name="ch_me_syakai" size=80 value=$ch_me_syakai></td></tr><tr>
	<td>英語</td><td><input type=text name="ch_me_eigo" size=80 value=$ch_me_eigo></td></tr><tr>
	<td>音樂</td><td><input type=text name="ch_me_ongaku" size=80 value=$ch_me_ongaku></td></tr><tr>
	<td>美術</td><td><input type=text name="ch_me_bijutu" size=80 value=$ch_me_bijutu></td></tr><tr>
	<td>容貌</td><td><input type=text name="ch_me_looks" size=80 value=$ch_me_looks></td></tr><tr>
	<td>體力</td><td><input type=text name="ch_me_tairyoku" size=80 value=$ch_me_tairyoku></td></tr><tr>
	<td>健康</td><td><input type=text name="ch_me_kenkou" size=80 value=$ch_me_kenkou></td></tr><tr>
	<td>速度</td><td><input type=text name="ch_me_speed" size=80 value=$ch_me_speed></td></tr><tr>
	<td>力</td><td><input type=text name="ch_me_power" size=80 value=$ch_me_power></td></tr><tr>
	<td>腕力</td><td><input type=text name="ch_me_wanryoku" size=80 value=$ch_me_wanryoku></td></tr><tr>
	<td>腳力</td><td><input type=text name="ch_me_kyakuryoku" size=80 value=$ch_me_kyakuryoku></td></tr><tr>
	<td>LOVE</td><td><input type=text name="ch_me_love" size=80 value=$ch_me_love></td></tr><tr>
	<td>有趣</td><td><input type=text name="ch_me_unique" size=80 value=$ch_me_unique></td></tr><tr>
	<td>淫蕩</td><td><input type=text name="ch_me_etti" size=80 value=$ch_me_etti></td>
	</tr></table>
	<div align=center><input type=submit value=" 評語變更 "></div></form><br><br>
	<div align=center><a href="javascript:history.back()"> [返回前畫面] </a></div>
	</td></tr></table>
EOM
	}


		&hooter("login_view","返回");
		exit;
}

####Ｃ聯盟
sub c_league {
		if ($chara_x_size == "" && $chara_y_size == ""){
			$chara_gazou_size = "";
			$c_size_comment = "";
		}else{
			$chara_gazou_size = "width=$chara_x_size height=$chara_y_size";
			$c_size_comment = "畫像尺寸是橫$chara_x_size象素，縱$chara_y_size象素。";
		}
		open(IN,"$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
		$league_meisai = <IN>;
		@aite_erabi = <IN>;
		close(IN);
		$now_time= time;
#遊戲詳細初始化
		if ($league_meisai eq ""){
			&lock;
			$league_meisai = "$now_time<>1<>\n";
			open(OUT,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
			print OUT $league_meisai;
			close(OUT);
			&unlock;
		}
		($start_time,$nankai_taikai)= split(/<>/,$league_meisai);
		$nannitime = int(($now_time - $start_time) / (60*60*24)) + 1;
		if ($nannitime > $c_nissuu){&taikai_syokika;}
		
#比賽的情況
	if ($in{'command'}eq "game") {
		&lock;
#打開自己的造型數據放入到變量
	$chara_settei_file="./member/$k_id/chara_ini.cgi";
	open(CSF,"$chara_settei_file") || &error("未製作人物不能比賽");
	$chara_settei_data = <CSF>;
	@my_chara_para =  split(/<>/,$chara_settei_data);
	if ($chara_settei_data eq ""){&error("未製作人物不能比賽");}
	close(CSF);
#以被登記的造型ID排列作成。要是未登記登記
	$zibun_hazusi = 0;
	foreach (@aite_erabi){
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime)= split(/<>/);
#如果從比賽名單中找到了自己則去掉。
		if ($name eq $ch_oyaname){
			if ($now_time - $ch_lasttime < 60 * $c_siai_kankaku){&error("殘留上次比賽的疲勞。");}
			$my_genzaino_joukyou = "$_";		#把是自己的狀況預先算入變量之內
			$zibun_hazusi = 1;
			next;
		}
		push (@taisen_list,$ch_k_id);
		push (@all_taisen_list,$_);
	}
	if ($zibun_hazusi == 0){&c_league_touroku($chara_settei_data);}
	@nitteicheck = split(/<>/,$my_genzaino_joukyou);
	if ($nitteicheck[4] + $nitteicheck[5] + $nitteicheck[6] >= $c_siaisuu){&error("結束了全比賽日。");}
	$ch_randed=int(rand($#taisen_list));
	$aite_kettei =splice(@taisen_list,$ch_randed,1);
	if ($aite_kettei eq ""){&message("找不到對手。。","c_league");}
	if ($aite_kettei eq "$k_id"){&message("找不到對手。。","c_league");}
#打開對方的造型數據放入到變量
	$aite_settei_file="./member/$aite_kettei/chara_ini.cgi";
	open(ASF,"$aite_settei_file") || &error("根據對戰對方的情況比賽需要延期。");
	$aite_settei_data = <ASF>;
	@aite_chara_para =  split(/<>/,$aite_settei_data);
	if ($aite_settei_data eq ""){&error("根據對戰對方的情況比賽需要延期。");}
	close(ASF);
#如果有人物畫像變量代入
	if ($my_chara_para[3]){
		$my_chara_image = "<img src=$my_chara_para[3] $chara_gazou_size>";
	}else{$my_chara_image = "";}
	if ($aite_chara_para[3]){
		$aite_chara_image = "<img src=$aite_chara_para[3] $chara_gazou_size>";
	}else{$aite_chara_image = "";}
	
	&header(item_style);
#算出人物的力(體力)
	$my_chara_power = $my_chara_para[26] + $my_chara_para[25];
	$aite_chara_power = $aite_chara_para[26] + $aite_chara_para[25];
	print <<"EOM";
	<br><br><table width="600" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr align=center><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2>
$my_chara_para[2]的登場人物<br>
$my_chara_para[1]<br>
$my_chara_image
</td></tr>
<tr><td align=center><span class=honbun3>頭腦能量</span>：</td><td>$my_chara_para[26]</td></tr>
<tr><td align=center><span class=honbun3>身體能力</span>：</td><td>$my_chara_para[25]</td></tr>
</table>
	</td><td>
	<div class=tyuu>跟$aite_chara_para[1]的比賽開始了！</div><br><br>
	</td><td>
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px;"  width=150>
<tr><td align=center colspan=2>
$aite_chara_para[2]的登場人物<br>
$aite_chara_para[1]<br>
$aite_chara_image
</td></tr>
<tr><td align=center><span class=honbun3>頭腦能量</span>：</td><td>$aite_chara_para[26]</td></tr>
<tr><td align=center><span class=honbun3>身體能力</span>：</td><td>$aite_chara_para[25]</td></tr>
</table>
	</td></tr></table>
EOM

	if ($my_chara_para[16] > $aite_chara_para[16]){$turn =1;}
	$sentou_kaisuu =0;
	foreach (1..25){
			print "<br><br><table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"5\" align=center class=yosumi><tr><td colspan=2>";
			if ($turn == 1){&ch_kougeki (1,$my_chara_para[1]);			#自己的攻擊
			}else{&ch_kougeki (0,$aite_chara_para[1]);}			#對方的攻擊
			print <<"EOM";
			</td></tr>
			<tr><td align=left>
			<div class=tyuu>能源：$my_chara_power</div>
			</td>
			<td align=right>
			<div class=tyuu>能源：$aite_chara_power</div>
			</td></tr></table>
EOM
			$sentou_kaisuu ++;
			if ($aite_chara_power <= 0){$win_flag=1;last;}
			if ($my_chara_power <= 0){$win_flag=2;last;}
			if ($turn == 1){$turn = 0;} else {$turn = 1;}
	}
	print "<br><br>";
	
#split是預先放入了的自己的狀況
	($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/,$my_genzaino_joukyou);
#ch_yobi1=最後的對戰狀況 ch_yobi2=獲得點 ch_yobi3=上次勝 ch_yobi4=上次負 ch_yobi5=上次和

#如果勝了
	if ($win_flag == 1) {
		$ch_kati ++;
	#最後的戰鬥評語
		$ch_yobi1 = "<td align=center>$my_chara_para[1] vs $aite_chara_para[1]</td><td align=center>$my_chara_para[1]</td><td>$my_chara_para[$battle_naiyou_hanbetu]</td>";
		print "<div align=center style=\"color:#339933;font-size:14px;\">勝利！</div>";
#如果輸了
	}elsif($win_flag == 2){
	#最後的戰鬥評語
		$ch_yobi1 = "<td align=center>$my_chara_para[1] vs $aite_chara_para[1]</td><td align=center>$aite_chara_para[1]</td><td>$aite_chara_para[$battle_naiyou_hanbetu]</td>";
		$ch_make ++;
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">輸了。。</div>";
	}else{
		$ch_yobi1 = "<td align=center>$my_chara_para[1] vs $aite_chara_para[1]</td><td align=center>平局</td><td>ー</td>";
		$ch_hikiwake ++;
		print "<div align=center style=\"color:#ff3300;font-size:14px;\">未能分勝負。。是平局。</div>";
	}
	
	$ch_gazou ="$my_chara_para[3]";
	$ch_lasttime = $now_time;
	$c_sinki_temp = "$ch_k_id<>$ch_name<>$ch_oyaname<>$ch_gazou<>$ch_kati<>$ch_make<>$ch_hikiwake<>$ch_yuusyou<>$ch_lasttime<>$ch_yobi1<>$ch_yobi2<>$ch_yobi3<>$ch_yobi4<>$ch_yobi5<>$ch_yobi6<>\n"; 
	unshift (@all_taisen_list,$c_sinki_temp);
	unshift (@all_taisen_list,$league_meisai);
	open(TOO,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	print TOO @all_taisen_list;
	close(TOO);
	
	&unlock
#數據更新
#			&temp_routin;
#			&log_kousin($my_log_file,$k_temp);
	&hooter("c_league","返回","game.cgi");
	exit;
	}		#比賽的情況閉上

		&header(keiba_style);
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td bgcolor=#ffffff>是決定最強的登場人物的「Ｃ聯盟」。在$c_nissuu日間進行$c_siaisuu場比賽。勝利數最多的登場人物成為優勝者。比賽間隔是$c_siai_kankaku分。</td>
	<td  bgcolor=#333333 align=center width=200><img src="$img_dir/cleague_tytle.gif"></td>
	</tr></table><br>
		
		<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
		<tr><td>
EOM

	foreach (@aite_erabi){
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
			if ($name eq $ch_oyaname){
				$my_genzaino_joukyou = "$_";		#把自己的狀況預先算入變量之內
			}
			$key=(split(/<>/,$_))[4];		#選排序的要素
			$key2=(split(/<>/,$_))[11];		#選排序的要素
			$key3=(split(/<>/,$_))[10];		#選排序的要素
			push @alldata,$_;
			push @keys,$key;
			push @keys2,$key2;
			push @keys3,$key3;
	}
	
		sub bykeys{$keys[$b] <=> $keys[$a];}
		@junidata=@alldata[ sort bykeys 0..$#alldata]; 
		
		sub bykeys3{$keys3[$b] <=> $keys3[$a];}
		@sougoujunidata=@alldata[ sort bykeys3 0..$#alldata]; 
		
		sub bykeys2{$keys2[$b] <=> $keys2[$a];}
		@zenkaijunidata=@alldata[ sort bykeys2 0..$#alldata]; 
		
			($zibun_k_id,$zibun_name,$zibun_oyaname,$zibun_gazou,$zibun_kati,$zibun_make,$zibun_hikiwake) = split(/<>/,$my_genzaino_joukyou);
			if ($my_genzaino_joukyou ne ""){
				$syouhai_hyouzi = "『$zibun_name』現在、$zibun_kati勝$zibun_make敗$zibun_hikiwake和";
			}
	print <<"EOM";
	<div align=center class=dai>第$nankai_taikai回大會 - 第$nannitime日 -</div>
	<div align=center><form method="POST" action="$this_script">
	<input type=hidden name=mode value="c_league">
	<input type=hidden name=command value="game">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value=比賽></form>
	$syouhai_hyouzi
	</div>
	<hr size=1>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=3>
	●最近的比賽
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td>對　戰</td><td nowrap>勝　者</td><td nowrap>決勝的評語</td></tr>
EOM

	$i=1;
	foreach (@alldata) {
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		print "<tr class=sita2>$ch_yobi1</tr>";
				if($i >=5){last;}
			$i++;
	}

	print <<"EOM";
	</table><br><br>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=7>
	●到現在為止的名次（Top10）
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td></td><td nowrap>名字</td><td>作成者</td><td>勝　利</td><td nowrap>戰　敗</td><td>平　局</td><td>比賽消化數</td><td nowrap>優勝回數</td></tr>
EOM

	$i=1;
	foreach (@junidata) {
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		if ($i <= 3 && $ch_gazou ne ""){$ch_name_hyouzi = "<img src=$ch_gazou $chara_gazou_size><br>$ch_name";}else{$ch_name_hyouzi = "$ch_name";}
		$siaisyouka = $ch_kati + $ch_make + $ch_hikiwake;
		print <<"EOM";
		<tr class=sita2><td align=center>$i</td><td nowrap align=center>$ch_name_hyouzi</td><td align=center>$ch_oyaname</td><td align=right nowrap>$ch_kati勝</td><td align=right nowrap>$ch_make敗</td><td align=right>$ch_hikiwake和</td><td align=right nowrap>$siaisyouka</td><td align=right nowrap>$ch_yuusyou回</td></tr>
EOM
				if($i >=10){last;}
			$i++;
	}
	print "</table>";
	
	if ($nankai_taikai != 1){ 
	print <<"EOM";
	<br><br>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=7>
	●上次大會的名次（Top5）
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td></td><td nowrap>名字</td><td>作成者</td><td>勝　利</td><td nowrap>戰　敗</td><td>平　局</td><td nowrap>優勝回數</td></tr>
EOM

	$i=1;
	foreach (@zenkaijunidata) {
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		if ($i == 1 && $ch_gazou ne ""){$ch_name_hyouzi = "<img src=$ch_gazou $chara_gazou_size><br>$ch_name";}else{$ch_name_hyouzi = "$ch_name";}
		$siaisyouka = $ch_kati + $ch_make + $ch_hikiwake;
		print <<"EOM";
		<tr class=sita2><td align=center>$i</td><td nowrap align=center>$ch_name_hyouzi</td><td align=center>$ch_oyaname</td><td align=right nowrap>$ch_yobi3勝</td><td align=right nowrap>$ch_yobi4敗</td><td align=right>$ch_yobi5和</td><td align=right nowrap>$ch_yuusyou回</td></tr>
EOM
				if($i >= 5){last;}
			$i++;
	}
	print "</table>";
	print <<"EOM";
	<br><br>
	<table width="70%" border="0" cellspacing="0" cellpadding="5" align=center>
	<tr><td colspan=7>
	●綜合名次（點獲得Top10）<br>
	優勝=10點，２位=5點，３位=3點，４位=2點，５位=1點被加在一起算，以那個積累點數決定。
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td></td><td nowrap>名字</td><td>作成者</td><td>獲得點</td><td nowrap>優勝回數</td></tr>
EOM

	$i=1;
	foreach (@sougoujunidata) {
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		if ($ch_yobi2 eq ""){next;}
		if ($i <= 3 && $ch_gazou ne ""){$ch_name_hyouzi = "<img src=$ch_gazou $chara_gazou_size><br>$ch_name";}else{$ch_name_hyouzi = "$ch_name";}
		$siaisyouka = $ch_kati + $ch_make + $ch_hikiwake;
		print <<"EOM";
		<tr class=sita2><td align=center>$i</td><td nowrap align=center>$ch_name_hyouzi</td><td align=center>$ch_oyaname</td><td align=right nowrap>$ch_yobi2點</td><td align=right nowrap>$ch_yuusyou回</td></tr>
EOM
				if($i >= 10){last;}
			$i++;
	}
	print "</table>";
	
	}		#不是１次大會的情況閉上
		&hooter("login_view","返回");
		exit;
}

#####C聯盟的登記處理
sub c_league_touroku {
	open(TO,"$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	my @touroku_list = <TO>;
	close(TO);	
	my($ch2_k_id,$ch2_name,$ch2_oyaname,$ch2_gazou)= split(/<>/,@_[0]);
	$c_sinki_temp = "$ch2_k_id<>$ch2_name<>$ch2_oyaname<>$ch2_gazou<>0<>0<>0<>0<>$ch2_lasttime<>$ch2_yobi1<>$ch2_yobi2<>$ch2_yobi3<>$ch2_yobi4<>$ch2_yobi5<>$ch2_yobi6<>\n"; 
	push (@touroku_list,$c_sinki_temp);
	open(TOO,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
	print TOO @touroku_list;
	close(TOO);
	$my_genzaino_joukyou = "$c_sinki_temp";		#把是自己的狀況預先算入變量之內
}

sub ch_kougeki {
#隨機選擇攻擊內容
		$battle_rand = int(rand(17))+1;
		print "<table width=\"600\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" align=center><tr align=center><td>";
##自己的攻擊的情況
		if (@_[0] == 1){
			print "<div style=\"color:#339933;font-size:12px;\" align=left>@_[1]的攻擊！<br>";
#攻擊內容
			&ch_kougekinaiyou (1,$aite_chara_para[1]);
#結果表示
			if ($damage eq "no_d"){
					print "<div style=\"color:#ff3300;font-size:12px;\" align=right>$return_naiyou</div>\n";
			}else{
					print "<div style=\"color:#339933;font-size:12px;\" align=right>$return_naiyou</div>\n";
					$aite_chara_power -= $damage;
			}
			
##對方的攻擊的情況
		}else {
			print "<div style=\"color:#ff3300;font-size:12px;\" align=right>@_[1]的攻擊！<br>";
			&ch_kougekinaiyou (0,$my_chara_para[1]);
#結果表示
#不是自己的情況
			if ($damage eq "no_d"){
					print "<div style=\"color:#339933;font-size:12px;\" align=left>$return_naiyou</div>\n";
			}else{
#如果受到了損害
					print "<div style=\"color:#ff3300;font-size:12px;\" align=left>$return_naiyou</div>\n";
					$my_chara_power -= $damage;
			}
		}
	print "</td></tr></table>";
}

###攻擊內容的損害處理子程序
sub ch_kougekinaiyou {
# @_[0]=1是自己的攻擊，0是對方的攻擊
	if (@_[0] == 1){$align_settei = "align=left";}else{$align_settei = "align=right";}
	
			$battle_naiyou_hanbetu = $battle_rand + 26;	#使戰鬥random值的1為國語的評語
			if ($battle_rand <= 8 || $battle_rand == 15 || $battle_rand == 16){
				$seisinornikutai = "精神損害！";
			}else{$seisinornikutai = "肉體損害！";}
			if (@_[0] == 1){
				print "$my_chara_para[$battle_naiyou_hanbetu]</div><br>\n";
			}else{
				print "$aite_chara_para[$battle_naiyou_hanbetu]</div><br>\n";
			}
# iryoku_hantei (攻擊者,攻擊的內容)
			&ch_iryoku_hantei (@_[0],$battle_rand);
			if ($damage eq "no_d"){$return_naiyou = "@_[1]沒受到損傷。";}
			else{$return_naiyou = "@_[1]受<span style=\"font-size:18px\">$damage</span> 的$seisinornikutai";}
}

#威力判斷子程序
sub ch_iryoku_hantei {
#攻擊的內容的能力值
	$iryoku_hanteiti = @_[1] + 5;		#使戰鬥random值的1成為國語的能力
	if (@_[0] == 1){
		$hantei_kakkati = $my_chara_para[$iryoku_hanteiti]  - $aite_chara_para[$iryoku_hanteiti] ;
	}else{
		$hantei_kakkati = $aite_chara_para[$iryoku_hanteiti]  - $my_chara_para[$iryoku_hanteiti] ;
	}
	if ($hantei_kakkati <= 0){
			$damage = "no_d";
	}else{
			$damage = "$hantei_kakkati";
	}
}

###大會初始化處理
sub taikai_syokika {
			&lock;
	foreach (@aite_erabi){
		my ($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
			$key=(split(/<>/,$_))[4];		#選排序的要素
			push @alldata,$_;
			push @keys,$key;
	}
	
		sub bykeys{$keys[$b] <=> $keys[$a];}
		@junidata=@alldata[ sort bykeys 0..$#alldata]; 
	$i = 1;
	foreach (@junidata){
		($ch_k_id,$ch_name,$ch_oyaname,$ch_gazou,$ch_kati,$ch_make,$ch_hikiwake,$ch_yuusyou,$ch_lasttime,$ch_yobi1,$ch_yobi2,$ch_yobi3,$ch_yobi4,$ch_yobi5,$ch_yobi6)= split(/<>/);
		$ch_yobi3 = $ch_kati;
		$ch_yobi4 = $ch_make;
		$ch_yobi5 = $ch_hikiwake;
		$ch_kati = 0;
		$ch_make = 0;
		$ch_hikiwake = 0;
		if ($i == 1){$ch_yuusyou ++; $ch_yobi2 += 10;}
		if ($i == 2){$ch_yobi2 += 5;}
		if ($i == 3){$ch_yobi2 += 3;}
		if ($i == 4){$ch_yobi2 += 2;}
		if ($i == 5){$ch_yobi2 += 1;}
		$c_sinki_temp = "$ch_k_id<>$ch_name<>$ch_oyaname<>$ch_gazou<>$ch_kati<>$ch_make<>$ch_hikiwake<>$ch_yuusyou<>$ch_lasttime<>$ch_yobi1<>$ch_yobi2<>$ch_yobi3<>$ch_yobi4<>$ch_yobi5<>$ch_yobi6<>\n"; 
		push (@new_aite_erabi,$c_sinki_temp);
		$i ++;
	}
			$nankai_taikai ++;
			$league_meisai = "$now_time<>$nankai_taikai<>\n";
			@aite_erabi = @new_aite_erabi;
			@alldata = ();
			$nannitime = 1;
			unshift (@new_aite_erabi,$league_meisai);
			open(OUT,">$doukyo_logfile") || &error("Open Error : $doukyo_logfile");
			print OUT @new_aite_erabi;
			close(OUT);			
			&unlock;
	
}

#######新登記處理
sub new {
	if ($new_touroku_per == 1) {&error("現在，暫停新登記。");}		#ver.1.40
	&lock;
	&get_host;
	if($in{'name'} eq '' || $in{'pass'} eq '' || $in{'sex'} eq ''){&error("輸入有遺漏！");}
	if($in{'name'}  =~ / / || $in{'name'}  =~ /　/){&error("名字請勿使用空格");}
	if($in{'name'}  =~ /,/){&error("請別為名字使用「,」");}		#ver.1.3
#ver.1.40從這裡
	open(IN,"$logfile") || &error("Open Error : $logfile");
	@all_sankasya = <IN>;
	foreach (@all_sankasya) {
		&kozin_sprit;
		if($in{'name'} eq $name){ &error("那個名字已經被登記。請嘗試用另外的名字。");}
		if ($tajuukinsi_flag==1){
			if($return_host eq $host){ &error("禁止重複登記。");}
		}
	}
	close(IN);
#ver.1.40從這裡
#從密碼名單取得新ID
	open(PA,"$pass_logfile") || &error("Open Error : $pass_logfile");
	@all_pass_list = <PA>;
	close(PA);
	($saisin_id)= split(/<>/,$all_pass_list[0]);
	$saisin_id ++;

	$para1= 5 + (int(rand(15)));$para2= 5 + (int(rand(15)));$para3= 5 + (int(rand(15)));$para4= 5 + (int(rand(15)));$para5= 5 + (int(rand(15)));$para6= 5 + (int(rand(15)));$para7= 5 + (int(rand(15)));$para8= 5 + (int(rand(15)));$para9= 5 + (int(rand(15)));$para10= 5 + (int(rand(15)));$para11= 5 + (int(rand(15)));$para12= 5 + (int(rand(15)));$para13= 5 + (int(rand(15)));$para14= 5 + (int(rand(15)));$para15= 5 + (int(rand(15)));$para16= 5 + (int(rand(15)));$para17= 5 + (int(rand(15)));
	if($in{'sex'} eq "m"){
			$sintyou= 165 + (int(rand(20)));
	}else{
			$sintyou= 150 + (int(rand(25)));
	}
	if($in{'sex'} eq "m"){
			$taijuu= 50 + (int(rand(35)));
	}else{
			$taijuu= 48 + (int(rand(20)));
	}
	&time_get;
	$last_syokuzi = $date_sec - ($syokuzi_kankaku*60);		#ver.1.3
	
	$new_temp="$saisin_id<>$in{'name'}<>$in{'pass'}<>$new_money<>0<>學生<>$para1<>$para2<>$para3<>$para4<>$para5<>$para6<>$para7<>$para8<>$para9<>$para10<>$para11<>$para12<>$para13<>$para14<>$para15<>$para16<>$para17<>$date_sec<><>$in{'sex'}<>$date_sec<>$date<>$return_host<><><><><><>0<>100<><><>$last_syokuzi<>$sintyou<>$taijuu<>100<><>0<>0<><>50<><><><><>$k_yobi3<>$k_yobi4<>$k_yobi5<>\n";
	
	$pass_temp = "$saisin_id<>$in{'name'}<>$in{'pass'}<>\n";
	
#自己用目錄&log file作成
	$my_directry = "./member/$saisin_id";
	$my_log_file = "$my_directry/log.cgi";
	mkdir($my_directry, 0755) || &error("ID識別號$saisin_id的目錄已經存在著。");
if ($zidouseisei == 1){
	chmod 0777,"$my_directry";
}elsif ($zidouseisei == 2){
	chmod 0755,"$my_directry";
}else{
	chmod 0755,"$my_directry";
}
	open(MYF,">$my_log_file") || &error("Open Error : $my_log_file");
	print MYF $new_temp;
	chmod 0666,"$my_log_file";
	close(MYF);
#信息交換用文件作成
	$message_file="$my_directry/mail.cgi";
	open(MF,">$message_file") || &error("Write Error : $message_file");
	chmod 0666,"$message_file";
	close(MF);
	
#購買物記錄文件作成
	$monokiroku_file="$my_directry/mono.cgi";
	open(MK,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
	chmod 0666,"$monokiroku_file";
	close(MK);
	
#銀行詳細記錄文件作成
	$ginkoumeisai_file="$my_directry/ginkoumeisai.cgi";
	open(GM,">$ginkoumeisai_file") || &error("Write Error : $ginkoumeisai_file");
	chmod 0666,"$ginkoumeisai_file";
	close(GM);

#名單用log file作成
	push (@all_sankasya,$new_temp);
	if ($mem_lock_num == 0){
		$err = data_save($logfile, @all_sankasya);
		if ($err) {&error("$err");}
	}else{
		open(OUT,">>$logfile") || &error("Write Error : $logfile");
		print OUT $new_temp;
		close(OUT);
	}
#密碼記錄文件更新
	unshift (@all_pass_list,$pass_temp);
		open(PAO,">$pass_logfile") || &error("Write Error : $pass_logfile");
		print PAO @all_pass_list;
		close(PAO);
#ver.1.40到這裡

#ニュース記録
	&news_kiroku("遷入","$in{'name'}君成為了新的居民。");		#ver.1.3
	
	&unlock;
	&set_cookie;
	&header;
	&check_pass;
	print <<"EOM";
	<div align=center>
	<br><br>居民用以下的內容登記完成了。<br><br>
	
<table width="450" border="0" cellspacing="0" cellpadding="4" align=center style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px" bgcolor=$st_win_back>
<tr>
<td  width="25%"><span class=honbun2>名字</span>：$name</td>
<td><span class=honbun2>密碼</span>：$pass</td>
<td width="25%"><span class=honbun2>身長</span>：$sintyou</td>
<td width="25%"><span class=honbun2>體重</span>：$taijuu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  width="25%"><span class=tyuu>◆頭腦</span></td>
<td><span class=honbun2>國語</span>：$kokugo</td>
<td width="25%"><span class=honbun2>數學</span>：$suugaku</td>
<td width="25%"><span class=honbun2>理科</span>：$rika</td></tr>
<tr><td width="25%"><span class=honbun2>社會</span>：$syakai</td>
<td width="25%"><span class=honbun2>英語</span>：$eigo</td>
<td width="25%"><span class=honbun2>音樂</span>：$ongaku</td>
<td width="25%"><span class=honbun2>美術</span>：$bijutu</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px"><td  width="25%"><span class=tyuu>◆身体</span></td>
<td><span class=honbun2>容貌</span>：$looks</td>
<td><span class=honbun2>體力</span>：$tairyoku</td>
<td><span class=honbun2>健康</span>：$kenkou</td></tr>
<tr><td><span class=honbun2>速度</span>：$speed</td>
<td><span class=honbun2>力</span>：$power</td>
<td><span class=honbun2>腕力</span>：$wanryoku</td>
<td><span class=honbun2>腳力</span>：$kyakuryoku</td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px"><td  width="25%"><span class=tyuu>◆その他</span></td>
<td><span class=honbun2>LOVE</span>：$love</td>
<td><span class=honbun2>有趣</span>：$unique</td>
<td><span class=honbun2>淫蕩</span>：$etti</td></tr>
</table>
	
		<br><br><a href=$script>返回</a>
	</div>
	</body></html>
EOM
exit;
}

######數據保存
sub data_hozon {		#ver.1.40
	&lock;
	open(DH,"$logfile") || &error("Open Error : $logfile");
		@ranking_data = <DH>;
	close(DH);
	$sonzai_flag=0;
	$i = 0;
	foreach (@ranking_data){
		&list_sprit($_);
		if ($k_id eq "$list_k_id"){
			$ranking_data[$i] = $my_prof;
			$sonzai_flag = 1;
			last;
		}
		$i ++;
#		&list_temp;
#		push (@new_ranking_data,$list_temp);
	}
	if ($sonzai_flag==0){unshift (@ranking_data,$my_prof);}
#	unshift (@new_ranking_data,$my_prof);
	
#（ver.1.40從這裡）
	if ($mem_lock_num == 0){
		$err = data_save($logfile, @ranking_data);
		if ($err) {&error("$err");}
	}else{
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @ranking_data;
		close(OUT);
	}
#（ver.1.40到這裡）
#取得文件夾內的文件名作成備份記錄
					use DirHandle;
					$dir = new DirHandle ("./member/"."$k_id");
#ver.1.2從這裡
					$back_folder_name = "$k_id" . "backup";
					$back_folder_pass = "./member/$back_folder_name";
					if (! -e "./member/$back_folder_name"){
						mkdir($back_folder_pass, 0755) || &error("Error : can not Make Directry");
							if ($zidouseisei == 1){
								chmod 0777,"$back_folder_pass";
							}elsif ($zidouseisei == 2){
								chmod 0755,"$back_folder_pass";
							}else{
								chmod 0755,"$back_folder_pass";
							}
					}
#ver.1.2到這裡
					while($file_name = $dir->read){ #讀入1個$folder_name代入
							if($file_name eq '.' || $file_name eq '..' || $file_name =~ /^backup_/ || $file_name eq '.DS_Store'){next;}
							$backup_name = "backup_" ."$file_name";
							open (BK,"./member/$k_id/$file_name")  || &error("Open Error : ./member/$k_id/$file_name");
							@back_data = <BK>;
							close (BK);
							if (@back_data != ""){		#ver.1.22
								open (BKO,">./member/$back_folder_name/$backup_name");		#ver.1.2
								print BKO @back_data;
								close (BKO);
							}				#ver.1.22
					}
					$dir->close;  #閉上目錄
#ver.1.30從這裡
	open(GUEST,"$guestfile");
	@all_guest=<GUEST>;
	close(GUEST);
	@new_all_guest = ();
	foreach (@all_guest) {
		($sanka_timer,$sanka_name,$hyouzi_check) = split(/<>/);
		if ($name eq "$sanka_name"){next;}
		$sanka_tmp = "$sanka_timer<>$sanka_name<>$hyouzi_check<>\n";
		push (@new_all_guest,$sanka_tmp);
	}
#ver.1.40從這裡
	if ($mem_lock_num == 0){
		$err = data_save($guestfile, @new_all_guest);
		if ($err) {&error("$err");}
	}else{
		open(GUEST,">$guestfile");
		print GUEST @new_all_guest;
		close(GUEST);
	}
#ver.1.40到這裡
#ver.1.30到這裡
	&unlock;
	&set_cookie;
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
辛苦了。
</span>
</td></tr></table>
<br>
EOM
	&hooter("login_view","返回");
	print <<"EOM";
	<div align=center><form method=POST action="$script">
	<input type=submit value="TOP">
	</form></div>
EOM
	exit;
}
