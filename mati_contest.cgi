#!/perl/bin/perl
# ↑使用合乎服務器的路徑。

$this_script = 'mati_contest.cgi';
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
	if($in{'mode'} eq "matikon"){&matikon;}
	elsif($in{'mode'} eq "mati_kouken"){&mati_kouken;}
	else{&error("請用「返回」按鈕返回街");}
exit;
	
#############以下子程序
sub matikon {
	open(MA,"$maticon_logfile") || &error("$maticon_logfile不能打開");
	$matikon_settei = <MA>;
	@mati_alldata = <MA>;
	close(MA);
		&time_get;
#開始時記錄初始化
		if ($matikon_settei eq ""){
			&lock;
			$i = 0;
			@new_matikon_data = ();
			foreach (@town_hairetu){
				$mati_kon_temp = "$i<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>\n";
				push (@new_matikon_data,$mati_kon_temp);
				$i ++;
			}
			@mati_alldata = @new_matikon_data;
			$matikon_settei = "$date_sec<>1<>1<>\n";
			unshift (@new_matikon_data,$matikon_settei);
			open(OUT,">$maticon_logfile") || &error("Open Error : $maticon_logfile");
			print OUT @new_matikon_data;
			close(OUT);
			&unlock;
		}
#如果新追加了街，街數據追加
		$i = 0;
		$tuika_flag=0;
		foreach (@town_hairetu){
			my $new_mati_hueta = 0;
			foreach $kizon_mati (@mati_alldata){
				($mat_num) = split(/<>/,$kizon_mati);
				if ($mat_num eq $i){$new_mati_hueta = 1;}
			}
			if ($new_mati_hueta == 0){		#街數據沒有街號碼（街排列找到了的情況）
				my $mati_kon_temp = "$i<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>\n";
				push (@mati_alldata,$mati_kon_temp);
				$tuika_flag=1;
			}
			$i ++;
		}
		if ($tuika_flag ==1){
			&lock;
			unshift (@mati_alldata,$matikon_settei);
			open(OUT,">$maticon_logfile") || &error("Open Error : $maticon_logfile");
			print OUT @mati_alldata;
			close(OUT);
			&unlock;
			shift  @mati_alldata;
		}

#讀取設定，第幾大會第幾日設定
		$saisyuu_flag=0;
		($start_con_time,$nannitime_hozon,$dainankai_con,$rank_hiduke)= split(/<>/,$matikon_settei);
		$nannitime_con = int(($date_sec - $start_con_time) / (60*60*24)) + 1;
		if ($nannitime_con ne "$nannitime_hozon" && $nannitime_con <= $mati_con_nissuu){&matikon_changeDay;}
		if ($nannitime_con > $mati_con_nissuu){&matikon_saisyuu;}
		if ($nannitime_con == $mati_con_nissuu){
				$nanniti_hyouki = "最後一日";
		}else{
				$nanniti_hyouki = "第$nannitime_con日";
		}
#排名分類
	foreach (@mati_alldata){
#		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$mat_yobi2,$mat_yobi3,$mat_yobi4,$mat_yobi5)= split(/<>/);
			$data=$_;
			$bunka_key=(split(/<>/,$data))[5];
			$sports_key=(split(/<>/,$data))[6];
			$ninjou_key=(split(/<>/,$data))[7];
			$yuuhuku_key=(split(/<>/,$data))[8];
			$bunka_z_key=(split(/<>/,$data))[9];
			$sports_z_key=(split(/<>/,$data))[10];
			$ninjou_z_key=(split(/<>/,$data))[11];
			$yuuhuku_z_key=(split(/<>/,$data))[12];
			push @matirank_alldata,$data;
			push @bunkaKeys,$bunka_key;
			push @sportsKeys,$sports_key;
			push @ninjouKeys,$ninjou_key;
			push @yuuhukuKeys,$yuuhuku_key;
			push @bunka_zKeys,$bunka_z_key;
			push @sports_zKeys,$sports_z_key;
			push @ninjou_zKeys,$ninjou_z_key;
			push @yuuhuku_zKeys,$yuuhuku_z_key;
	}
		sub bybunkaKeys{$bunkaKeys[$b] <=> $bunkaKeys[$a];}
		@bunka_rank=@matirank_alldata[ sort bybunkaKeys 0..$#matirank_alldata]; 
		
		sub bysportsKeys{$sportsKeys[$b] <=> $sportsKeys[$a];}
		@sports_rank=@matirank_alldata[ sort bysportsKeys 0..$#matirank_alldata]; 
		
		sub byninjouKeys{$ninjouKeys[$b] <=> $ninjouKeys[$a];}
		@ninjou_rank=@matirank_alldata[ sort byninjouKeys 0..$#matirank_alldata]; 
		
		sub byyuuhukuKeys{$yuuhukuKeys[$b] <=> $yuuhukuKeys[$a];}
		@yuuhuku_rank=@matirank_alldata[ sort byyuuhukuKeys 0..$#matirank_alldata]; 
		
		sub bybunka_zKeys{$bunka_zKeys[$b] <=> $bunka_zKeys[$a];}
		@bunka_z_rank=@matirank_alldata[ sort bybunka_zKeys 0..$#matirank_alldata]; 
		
		sub bysports_zKeys{$sports_zKeys[$b] <=> $sports_zKeys[$a];}
		@sports_z_rank=@matirank_alldata[ sort bysports_zKeys 0..$#matirank_alldata]; 
		
		sub byninjou_zKeys{$ninjou_zKeys[$b] <=> $ninjou_zKeys[$a];}
		@ninjou_z_rank=@matirank_alldata[ sort byninjou_zKeys 0..$#matirank_alldata]; 
		
		sub byyuuhuku_zKeys{$yuuhuku_zKeys[$b] <=> $yuuhuku_zKeys[$a];}
		@yuuhuku_z_rank=@matirank_alldata[ sort byyuuhuku_zKeys 0..$#matirank_alldata]; 
	
	&header(gym_style);
			print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>$title 之「街競賽」營運。以參數及金錢為自己住的街貢獻，「文化度」「體育振興度」「人氣度」「富裕度」的各街參數上升。<br>根據到前一天為止的街參數的多，確定之後一日的名次。<br>
	$mati_con_nissuu日過了的時候最終的名次決定，每各自的排名優勝賞金被街給予(4個排名如果全部獲得冠軍為下列賞金×4)。居民平分那些賞金額匯入一般往戶頭。<br>為街的名譽努力吧。<br>
	※各排名的優勝賞金:$mati_con_syoukin萬元<br>
	※沒有自己的家的玩者不能參加這個競賽。能提高參數的間隔是1小時。</td>
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/matikon_tytle.gif"><br>
	<div style="color:ffffff; font-size:14px;">第$dainankai_con回大會</div>
	<div style="color:ffff66; font-size:13px;">$nanniti_hyouki</div>
	</td>
	</tr></table><br>
	
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td colspan=4>
	<div class=tyuu>現在的排名（$rank_hiduke 總計）</div>
	</td></tr>
	<tr align=center><td>
	<table border="0" cellspacing="1" cellpadding="3" ><tr><td colspan=3>■文化度</td></tr>
	<tr class=jouge bgcolor=#ffff66 align=center><td></td><td>街　名</td><td>點</td></tr>
EOM
	$i = 1;
	foreach (@bunka_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		print "<tr><td>$i</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_bunka_y</td></tr>";
		$i ++;
	}
	print <<"EOM";
	</table>
	</td><td>
	<table border="0" cellspacing="1" cellpadding="3" ><tr><td colspan=3>■體育振興度</td></tr>
	<tr class=jouge  bgcolor=#ffff66 align=center><td></td><td>街　名</td><td>點</td></tr>
EOM
	$i = 1;
	foreach (@sports_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		print "<tr><td>$i</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_sports_y</td></tr>";
		$i ++;
	}
	print <<"EOM";
	</table>
	</td><td>
	<table border="0" cellspacing="1" cellpadding="3" ><tr><td colspan=3>■人氣度</td></tr>
	<tr class=jouge bgcolor=#ffff66 align=center><td></td><td>街　名</td><td>點</td></tr>
EOM
	$i = 1;
	foreach (@ninjou_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		print "<tr><td>$i</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_ninjou_y</td></tr>";
		$i ++;
	}
	print <<"EOM";
	</table>
	</td><td>
	<table border="0" cellspacing="1" cellpadding="3" ><tr><td colspan=3>■富裕度</td></tr>
	<tr class=jouge bgcolor=#ffff66 align=center><td></td><td>街　名</td><td>捐款額</td></tr>
EOM

	$i = 1;
	foreach (@yuuhuku_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		print "<tr><td>$i</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_yuuhuku_y元</td></tr>";
		$i ++;
	}
	
	print <<"EOM";
	</table>
	</td></tr></table><br><br>
EOM
#功勞者排名的輸出
	print <<"EOM";
	<table width="90%" border="0" cellspacing="1" cellpadding="3" align=center class=yosumi>
	<tr><td colspan=5>
	<div class=tyuu>現在的功勞者排名Top5</div>
	※「貢獻度」是各貢獻點的合計。捐款以1萬1點計算。
	</td></tr>
	<tr class=jouge bgcolor=#ffcc99 align=center><td></td><td>名字</td><td>貢獻度</td><td>文化貢獻</td><td>體育貢獻</td><td>人氣貢獻</td><td>捐款</td></tr>
EOM
	open(KOR,"$kourousya_logfile") || &error("$kourousya_logfile不能打開");
	@kourou_alldata = <KOR>;
	close(KOR);
	foreach (@kourou_alldata){
			$data=$_;
			$kourou_key=(split(/<>/,$data))[2];
			$kourou_z_key=(split(/<>/,$data))[12];
			push @korourank_alldata,$data;
			push @kourouKeys,$kourou_key;
			push @kourou_zKeys,$kourou_z_key;
	}
		sub bykourouKeys{$kourouKeys[$b] <=> $kourouKeys[$a];}
		@kourou_rank=@korourank_alldata[ sort bykourouKeys 0..$#korourank_alldata]; 
		
		sub bykourou_zKeys{$kourou_zKeys[$b] <=> $kourou_zKeys[$a];}
		@kourou_z_rank=@korourank_alldata[ sort bykourou_zKeys 0..$#korourank_alldata]; 
	$i = 1;
	foreach (@kourou_rank){
		($kourou_num,$kourou_name,$kourou_total,$kourou_bunka,$kourou_sports,$kourou_ninjou,$kourou_yuuhuku,$kourou_bunka_z,$kourou_sports_z,$kourou_ninjou_z,$kourou_yuuhuku_z,$kourou_yobi1,$kourou_yobi2,$kourou_yobi3,$kourou_yobi4,$kourou_yobi5)= split(/<>/);
#kourou_yobi1=最後貢獻時間 kourou_yobi2=kourou_total_z(上次的功勞點總數)kourou_yobi3=積累功勞總數
		print "<tr align=right><td>$i位</td><td align=left>$kourou_name</td><td>$kourou_total點</td><td>$kourou_bunka</td><td>$kourou_sports</td><td>$kourou_ninjou</td><td>$kourou_yuuhuku元</td></tr>";
		if($i >= 5){last;}
		$i ++;
	}
	print "</table><br><br>";

	&my_town_check($name);
#有家的人用的輸出
	if ($return_my_town ne "no_town"){
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td colspan=2>
	<div class=tyuu>貢獻自己的街（$town_hairetu[$return_my_town]）</div>
	※１回的貢獻，參數，或是錢，兩邊還是只揀一個。間隔都是1小時。
	</td></tr>
	<tr><td width=50%>
	<form method=POST action="$this_script">
	<input type=hidden name=mode value="mati_kouken">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=sunderu_mati value=$return_my_town>
	●參數提高<br>
	<select name=nouryoku>
	<option value="">----文化----</option>
	<option value="kokugo">國語</option>
	<option value="suugaku">數學</option>
	<option value="rika">理科</option>
	<option value="syakai">社會</option>
	<option value="eigo">英語</option>
	<option value="ongaku">音樂</option>
	<option value="bijutu">美術</option>
	<option value="">----體育振興----</option>
	<option value="tairyoku">體力</option>
	<option value="kenkou">健康</option>
	<option value="speed">速度</option>
	<option value="power">力</option>
	<option value="wanryoku">腕力</option>
	<option value="kyakuryoku">腳力</option>
	<option value="">----人氣----</option>
	<option value="looks">容貌</option>
	<option value="love">LOVE</option>
	<option value="unique">有趣</option>
	<option value="etti">淫蕩</option>
	</select>
	<select name=suuti>
	<option value="5">5點</option>
	<option value="10">10點</option>
	<option value="15">15點</option>
	<option value="20">20點</option>
	<option value="25">25點</option>
	<option value="30">30點</option>
	<option value="40">40點</option>
	<option value="50">50點</option>
	</select>
	<input type=submit value=" O K ">
	</form>
	</td><td>
	<form method=POST action="$this_script">
	<input type=hidden name=mode value="mati_kouken">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=sunderu_mati value=$return_my_town>
	●富裕度提高<br>
	<select name=okane>
	<option value="">金額的選擇</option>
	<option value="1000">1000元</option>
	<option value="5000">5000元</option>
	<option value="10000">1万元</option>
	<option value="30000">3万元</option>
	<option value="50000">5万元</option>
	<option value="100000">10万元</option>
	<option value="200000">20万元</option>
	<option value="300000">30万元</option>
	<option value="400000">40万元</option>
	<option value="500000">50万元</option>
	</select>
	<input type=submit value=" O K ">
	</form>
	</td></tr></table>
EOM
#沒有家的人用的輸出
	}else{
		print "<div class=honbun2 align=center>因為$name君沒有家而不能對街貢獻。</div>";
	}
#上次最後排名
	$zenkai_taikai = $dainankai_con-1;
	if ($zenkai_taikai != 0){
	print <<"EOM";
	<br><br><table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td colspan=4>
	<div class=tyuu>第$zenkai_taikai回大會最後名次</div>
	</td></tr>
	<tr align=center><td>
	<table border="0" cellspacing="1" cellpadding="3">
	
EOM
	$i = 1;
	foreach (@bunka_z_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		if ($i == 1){
			print "<tr align=center bgcolor=#ffff66 class=jouge><td colspan=3>文化度<div class=tyuu>優勝</div><div class=dai>$town_hairetu[$mat_num]</div>（$mat_bunka_z點）</td></tr>";
			if($saisyuu_flag ==1){&syoukin_haihu($mat_num,"（文化度）");}
		}else{
			print "<tr><td>$i</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_bunka_z</td></tr>";
		}
		$i ++;
	}
	print <<"EOM";
	</table>
	</td><td>
	<table border="0" cellspacing="1" cellpadding="3" >
EOM
	$i = 1;
	foreach (@sports_z_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		if ($i == 1){
			print "<tr align=center bgcolor=#ffff66 class=jouge><td colspan=3>體育振興度<div class=tyuu>優勝</div><div class=dai>$town_hairetu[$mat_num]</div>（$mat_sports_z點）</td></tr>";
			if($saisyuu_flag ==1){&syoukin_haihu($mat_num,"（體育振興度）");}
		}else{
			print "<tr><td>$i位</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_sports_z</td></tr>";
		}
		$i ++;
	}
	print <<"EOM";
	</table>
	</td><td>
	<table border="0" cellspacing="1" cellpadding="3" >
EOM
	$i = 1;
	foreach (@ninjou_z_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		if ($i == 1){
			print "<tr align=center bgcolor=#ffff66 class=jouge><td colspan=3>人氣度<div class=tyuu>優勝</div><div class=dai>$town_hairetu[$mat_num]</div>（$mat_ninjou_z點）</td></tr>";
			if($saisyuu_flag ==1){&syoukin_haihu($mat_num,"（人氣度）");}
		}else{
			print "<tr><td>$i</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_ninjou_z</td></tr>";
		}
		$i ++;
	}
	print <<"EOM";
	</table>
	</td><td>
	<table border="0" cellspacing="1" cellpadding="3" >
EOM

	$i = 1;
	foreach (@yuuhuku_z_rank){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$k_yobi2,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
		if ($i == 1){
			print "<tr align=center bgcolor=#ffff66 class=jouge><td colspan=3>富裕度<div class=tyuu>優勝</div><div class=dai>$town_hairetu[$mat_num]</div>（$mat_yuuhuku_z元）</td></tr>";
			if($saisyuu_flag ==1){&syoukin_haihu($mat_num,"（富裕度）");}
		}else{
			print "<tr><td>$i</td><td>$town_hairetu[$mat_num]</td><td align=right>$mat_yuuhuku_z元</td></tr>";
		}
		$i ++;
	}
	
	print <<"EOM";
	</table>
	</td></tr></table><br><br>
EOM

#上回功勞者排名的輸出
	print <<"EOM";
	<table width="90%" border="0" cellspacing="1" cellpadding="3" align=center  class=yosumi>
	<tr><td colspan=5>
	<div class=tyuu>第$zenkai_taikai回大會功勞者排名Top10</div>
	</td></tr>
	<tr class=jouge bgcolor=#ffcc99 align=center><td></td><td>名字</td><td>貢獻度</td><td>文化貢獻</td><td>體育貢獻</td><td>人氣貢獻</td><td>捐款</td></tr>
EOM
	$i = 1;
	foreach (@kourou_z_rank){
		($kourou_num,$kourou_name,$kourou_total,$kourou_bunka,$kourou_sports,$kourou_ninjou,$kourou_yuuhuku,$kourou_bunka_z,$kourou_sports_z,$kourou_ninjou_z,$kourou_yuuhuku_z,$kourou_yobi1,$kourou_yobi2,$kourou_yobi3,$kourou_yobi4,$kourou_yobi5)= split(/<>/);
#kourou_yobi1=最後貢獻時間 kourou_yobi2=kourou_total_z(上次的功勞點總數)kourou_yobi3=積累功勞總數
		print "<tr align=right><td>$i位</td><td align=left>$kourou_name</td><td>$kourou_yobi2點</td><td>$kourou_bunka_z</td><td>$kourou_sports_z</td><td>$kourou_ninjou_z</td><td>$kourou_yuuhuku_z元</td></tr>";
		if($i >= 10){last;}
		$i ++;
	}
	print "</table><br><br>";
	}		#上回大會不是0的閉上
	&hooter("login_view","返回");
	exit;
}

###街的貢獻處理
sub mati_kouken {
	if ($in{'nouryoku'} eq "" && $in{'okane'} eq ""){&error("貢獻的內容沒被選");}
#給功勞者文件的寫入
	open(KOR,"$kourousya_logfile") || &error("$kourousya_logfile不能打開");
	@kourou_alldata = <KOR>;
	close(KOR);
	$kourou_member_flag = 0;
	my $now_time = time;
	foreach (@kourou_alldata){
		($kourou_num,$kourou_name,$kourou_total,$kourou_bunka,$kourou_sports,$kourou_ninjou,$kourou_yuuhuku,$kourou_bunka_z,$kourou_sports_z,$kourou_ninjou_z,$kourou_yuuhuku_z,$kourou_yobi1,$kourou_yobi2,$kourou_yobi3,$kourou_yobi4,$kourou_yobi5)= split(/<>/);
		if ($name eq "$kourou_name"){
			if($now_time - $kourou_yobi1 < 60*60){&error("能貢獻的間隔的1小時還未過去");}
			$kourou_member_flag = 1;
			$kourou_yobi1 = $now_time;	#記錄最後貢獻時間
			if ($in{'nouryoku'}){		#參數提高的情況
				$kourou_total += $in{'suuti'};
				if ($in{'nouryoku'} eq "kokugo" || $in{'nouryoku'} eq "suugaku" || $in{'nouryoku'} eq "rika" || $in{'nouryoku'} eq "syakai" || $in{'nouryoku'} eq "eigo" || $in{'nouryoku'} eq "ongaku" || $in{'nouryoku'} eq "bijutu"){		#文化貢獻
					$kourou_bunka += $in{'suuti'};
					
				}elsif($in{'nouryoku'} eq "tairyoku" || $in{'nouryoku'} eq "kenkou" || $in{'nouryoku'} eq "speed" || $in{'nouryoku'} eq "power" || $in{'nouryoku'} eq "wanryoku" || $in{'nouryoku'} eq "kyakuryoku"){		#體育貢獻
					$kourou_sports += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "looks" || $in{'nouryoku'} eq "love" || $in{'nouryoku'} eq "unique" || $in{'nouryoku'} eq "etti"){		#人氣貢獻
					$kourou_ninjou += $in{'suuti'};
				}
			}elsif($in{'okane'}){		#捐款的情況
					if ($money <= $in{'okane'}){&error("錢不夠");}
					$okane_kanzan = $in{'okane'}/10000;
					$kourou_total += $okane_kanzan;
					$kourou_yuuhuku += $in{'okane'};
			}
		}		#名字一致的情況閉上
		$kourou_temp = "$kourou_num<>$kourou_name<>$kourou_total<>$kourou_bunka<>$kourou_sports<>$kourou_ninjou<>$kourou_yuuhuku<>$kourou_bunka_z<>$kourou_sports_z<>$kourou_ninjou_z<>$kourou_yuuhuku_z<>$kourou_yobi1<>$kourou_yobi2<>$kourou_yobi3<>$kourou_yobi4<>$kourou_yobi5<>\n";
		push (@new_kourou_alldata,$kourou_temp);
	}		#foreach閉上
#新功勞者的情況
	if ($kourou_member_flag == 0){
		$kourou_num ++;
		if ($in{'okane'}){
			$n_kourou_total += $in{'okane'}/10000;
			$n_kourou_yuuhuku += $in{'okane'};
			$n_kourou_bunka = 0; $n_kourou_sports = 0; $n_kourou_ninjou = 0;
		}else{
			$n_kourou_total += $in{'suuti'};
				if ($in{'nouryoku'} eq "kokugo" || $in{'nouryoku'} eq "suugaku" || $in{'nouryoku'} eq "rika" || $in{'nouryoku'} eq "syakai" || $in{'nouryoku'} eq "eigo" || $in{'nouryoku'} eq "ongaku" || $in{'nouryoku'} eq "bijutu"){		#文化貢獻
					$n_kourou_bunka = $in{'suuti'};$n_kourou_sports = 0;$n_kourou_ninjou = 0;$n_kourou_yuuhuku = 0;
				}elsif($in{'nouryoku'} eq "tairyoku" || $in{'nouryoku'} eq "kenkou" || $in{'nouryoku'} eq "speed" || $in{'nouryoku'} eq "power" || $in{'nouryoku'} eq "wanryoku" || $in{'nouryoku'} eq "kyakuryoku"){		#體育貢獻
					$n_kourou_sports = $in{'suuti'};$n_kourou_bunka = 0;$n_kourou_ninjou = 0;$n_kourou_yuuhuku = 0;
				}elsif($in{'nouryoku'} eq "looks" || $in{'nouryoku'} eq "love" || $in{'nouryoku'} eq "unique" || $in{'nouryoku'} eq "etti"){		#人氣貢獻
					$n_kourou_ninjou = $in{'suuti'};$n_kourou_sports = 0;$n_kourou_bunka = 0;$n_kourou_yuuhuku = 0;
				}
		}
		
		$sinki_kourou_temp = "$kourou_num<>$name<>$n_kourou_total<>$n_kourou_bunka<>$n_kourou_sports<>$n_kourou_ninjou<>$n_kourou_yuuhuku<>0<>0<>0<>0<>$now_time<>0<>0<>0<>0<>\n";
		push (@new_kourou_alldata,$sinki_kourou_temp);
	}
	
#對街文件的寫入&抽個人參數
	open(MA,"$maticon_logfile") || &error("$maticon_logfile不能打開");
	$matikon_settei = <MA>;
	@mati_alldata = <MA>;
	close(MA);
	foreach (@mati_alldata){
		($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$mat_yobi2,$mat_yobi3,$mat_yobi4,$mat_yobi5)= split(/<>/);
#自己的街的情況
		if ($in{'sunderu_mati'} eq "$mat_num"){
#參數提高的情況
			if ($in{'nouryoku'}){
				if ($in{'nouryoku'} eq "kokugo"){
					$kokugo -= $in{'suuti'};
					$mat_bunka += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "suugaku"){
					$suugaku -= $in{'suuti'};
					$mat_bunka += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "rika"){
					$rika -= $in{'suuti'};
					$mat_bunka += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "syakai"){
					$syakai -= $in{'suuti'};
					$mat_bunka += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "eigo"){
					$eigo -= $in{'suuti'};
					$mat_bunka += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "ongaku"){
					$ongaku -= $in{'suuti'};
					$mat_bunka += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "bijutu"){
					$bijutu -= $in{'suuti'};
					$mat_bunka += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "tairyoku"){
					$tairyoku -= $in{'suuti'};
					$mat_sports += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "kenkou"){
					$kenkou -= $in{'suuti'};
					$mat_sports += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "speed"){
					$speed -= $in{'suuti'};
					$mat_sports += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "power"){
					$power -= $in{'suuti'};
					$mat_sports += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "wanryoku"){
					$wanryoku -= $in{'suuti'};
					$mat_sports += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "kyakuryoku"){
					$kyakuryoku -= $in{'suuti'};
					$mat_sports += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "looks"){
					$looks -= $in{'suuti'};
					$mat_ninjou += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "love"){
					$love -= $in{'suuti'};
					$mat_ninjou += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "unique"){
					$unique -= $in{'suuti'};
					$mat_ninjou += $in{'suuti'};
				}elsif($in{'nouryoku'} eq "etti"){
					$etti -= $in{'suuti'};
					$mat_ninjou += $in{'suuti'};
				}
#捐款的情況
			}elsif ($in{'okane'}){
					$money -= $in{'okane'};
					$mat_yuuhuku += $in{'okane'};
			}			#富裕度提高的情況閉上
		}		#自己的街的情況閉上
		my $kouken_temp = "$mat_num<>$mat_bunka<>$mat_sports<>$mat_ninjou<>$mat_yuuhuku<>$mat_bunka_y<>$mat_sports_y<>$mat_ninjou_y<>$mat_yuuhuku_y<>$mat_bunka_z<>$mat_sports_z<>$mat_ninjou_z<>$mat_yuuhuku_z<>$mat_yobi1<>$mat_yobi2<>$mat_yobi3<>$mat_yobi4<>$mat_yobi5<>\n";
		push (@new_mati_alldata,$kouken_temp);
	}			#foreach閉上
	unshift (@new_mati_alldata,$matikon_settei);

#記錄更新
			&lock;
	open(KOO,">$kourousya_logfile") || &error("$kourousya_logfile不能寫上");
	print KOO @new_kourou_alldata;
	close(KOO);
			
	open(MK,">$maticon_logfile") || &error("$maticon_logfile不能寫上");
	print MK @new_mati_alldata;
	close(MK);
			&unlock;
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);

	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>做了對街的貢獻。這個點被下次的排名總計的時反映。</td></tr></table><br>

	<form method=POST action="$this_script">
	<input type=hidden name=mode value="matikon">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=admin_pass value=$in{'admin_pass'}>
	<input type=submit value="返回">
	</form></div>

	</body></html>
EOM
exit;
}

#日期變更處理（昨天時刻的數值移動）
sub matikon_changeDay {
			&lock;
			foreach (@mati_alldata){
				my ($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$mat_yobi2,$mat_yobi3,$mat_yobi4,$mat_yobi5)= split(/<>/);
				$mat_bunka_y = $mat_bunka;
				$mat_sports_y = $mat_sports;
				$mat_ninjou_y = $mat_ninjou;
				$mat_yuuhuku_y = $mat_yuuhuku;
				$changeDay_temp = "$mat_num<>$mat_bunka<>$mat_sports<>$mat_ninjou<>$mat_yuuhuku<>$mat_bunka_y<>$mat_sports_y<>$mat_ninjou_y<>$mat_yuuhuku_y<>$mat_bunka_z<>$mat_sports_z<>$mat_ninjou_z<>$mat_yuuhuku_z<>$mat_yobi1<>$mat_yobi2<>$mat_yobi3<>$mat_yobi4<>$mat_yobi5<>\n";
				push (@change_mati_alldata,$changeDay_temp);
			}
			@mati_alldata = ();
			@mati_alldata = @change_mati_alldata;
			$nannitime_hozon = $nannitime_con ;
			$rank_hiduke = "$date2";
			$change_matikon_settei = "$start_con_time<>$nannitime_hozon<>$dainankai_con<>$rank_hiduke<>\n";
			unshift (@change_mati_alldata,$change_matikon_settei);
			open(OUT,">$maticon_logfile") || &error("Open Error : $maticon_logfile");
			print OUT @change_mati_alldata;
			close(OUT);
			&unlock;
}


#住的街的檢查子程序
sub my_town_check {
		open(MTC,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		my @ori_ie_para = <MTC>;
		close(MTC);
		$my_town_ari = 0;
		foreach (@ori_ie_para){
			my ($ori_k_id,$ori_ie_name,$ori_ie_setumei,$ori_ie_image,$ori_ie_syubetu,$ori_ie_kentikubi,$ori_ie_town)= split(/<>/);
			if (@_[0] eq "$ori_ie_name"){
				$return_my_town = "$ori_ie_town";
				$my_town_ari = 1;
				last;
			}
		}
		if ($my_town_ari == 0){$return_my_town = "no_town";}
}

#最後排名處理
sub matikon_saisyuu {
			&lock;
			@change_mati_alldata = ();
			foreach (@mati_alldata){
				my ($mat_num,$mat_bunka,$mat_sports,$mat_ninjou,$mat_yuuhuku,$mat_bunka_y,$mat_sports_y,$mat_ninjou_y,$mat_yuuhuku_y,$mat_bunka_z,$mat_sports_z,$mat_ninjou_z,$mat_yuuhuku_z,$mat_yobi1,$mat_yobi2,$mat_yobi3,$mat_yobi4,$mat_yobi5)= split(/<>/);
				$mat_bunka_z = $mat_bunka;
				$mat_sports_z = $mat_sports;
				$mat_ninjou_z = $mat_ninjou;
				$mat_yuuhuku_z = $mat_yuuhuku;
				$mat_bunka_y = 0; $mat_sports_y = 0; $mat_ninjou_y = 0; $mat_yuuhuku_y = 0;
				$mat_bunka = 0; $mat_sports = 0; $mat_ninjou = 0; $mat_yuuhuku = 0;
				$saisyuu_temp = "$mat_num<>$mat_bunka<>$mat_sports<>$mat_ninjou<>$mat_yuuhuku<>$mat_bunka_y<>$mat_sports_y<>$mat_ninjou_y<>$mat_yuuhuku_y<>$mat_bunka_z<>$mat_sports_z<>$mat_ninjou_z<>$mat_yuuhuku_z<>$mat_yobi1<>$mat_yobi2<>$mat_yobi3<>$mat_yobi4<>$mat_yobi5<>\n";
				push (@change_mati_alldata,$saisyuu_temp);
			}
			@mati_alldata = ();
			@mati_alldata = @change_mati_alldata;
			$nannitime_hozon =1;
			$rank_hiduke = "$date2";
			$dainankai_con ++;
			$start_con_time = $date_sec;
			$nannitime_con = 1;		#把１作為最初的表示用
			$saisyuu_matikon_settei = "$start_con_time<>$nannitime_hozon<>$dainankai_con<>$rank_hiduke<>\n";
			unshift (@change_mati_alldata,$saisyuu_matikon_settei);
			
#功勞者數據更新
	open(KOR,"$kourousya_logfile") || &error("$kourousya_logfile不能打開");
	my @kourou_alldata = <KOR>;
	close(KOR);
	my @new_kourou_alldata = ();
	foreach (@kourou_alldata){
		my ($kourou_num,$kourou_name,$kourou_total,$kourou_bunka,$kourou_sports,$kourou_ninjou,$kourou_yuuhuku,$kourou_bunka_z,$kourou_sports_z,$kourou_ninjou_z,$kourou_yuuhuku_z,$kourou_yobi1,$kourou_yobi2,$kourou_yobi3,$kourou_yobi4,$kourou_yobi5)= split(/<>/);
		$kourou_yobi2 = $kourou_total;
		$kourou_bunka_z = $kourou_bunka;
		$kourou_sports_z = $kourou_sports;
		$kourou_ninjou_z = $kourou_ninjou;
		$kourou_yuuhuku_z = $kourou_yuuhuku;
		$kourou_yobi3 += $kourou_total;
		$kourou_total = 0; $kourou_bunka = 0; $kourou_sports = 0; $kourou_ninjou = 0; $kourou_yuuhuku = 0; 
		my $kourou_temp = "$kourou_num<>$kourou_name<>$kourou_total<>$kourou_bunka<>$kourou_sports<>$kourou_ninjou<>$kourou_yuuhuku<>$kourou_bunka_z<>$kourou_sports_z<>$kourou_ninjou_z<>$kourou_yuuhuku_z<>$kourou_yobi1<>$kourou_yobi2<>$kourou_yobi3<>$kourou_yobi4<>$kourou_yobi5<>\n";
		push (@new_kourou_alldata,$kourou_temp);
	}		#foreach閉上
			
#數據更新
			open(OUT,">$maticon_logfile") || &error("Open Error : $maticon_logfile");
			print OUT @change_mati_alldata;
			close(OUT);
			$saisyuu_flag=1;

			open(KOO,">$kourousya_logfile") || &error("$kourousya_logfile不能寫上");
			print KOO @new_kourou_alldata;
			close(KOO);
			&unlock;
}

#對優勝的居民的賞金散發
sub syoukin_haihu {
	&lock;	
	$yuusyou_taun = @_[0];
	open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		my @ori_ie_para = <IN>;
	close(IN);
#計算居民的數
		$syoukin_taisyousya = 0;
		foreach (@ori_ie_para){
my ($ori_k_id,$ori_ie_name,$ori_ie_setumei,$ori_ie_image,$ori_ie_syubetu,$ori_ie_kentikubi,$ori_ie_town,$ori_ie_tateziku,$ori_ie_yokoziku,$ori_ie_sentaku_point,$ori_ie_rank,$ori_ie_yobi7,$ori_ie_yobi8,$ori_ie_yobi9,$ori_ie_yobi10)= split(/<>/);
	if ($ori_ie_town eq "$yuusyou_taun"){$syoukin_taisyousya ++;}
		}
		$syoukingaku = int($mati_con_syoukin*10000/$syoukin_taisyousya);
	
		foreach (@ori_ie_para){
 ($ori_k_id,$ori_ie_name,$ori_ie_setumei,$ori_ie_image,$ori_ie_syubetu,$ori_ie_kentikubi,$ori_ie_town,$ori_ie_tateziku,$ori_ie_yokoziku,$ori_ie_sentaku_point,$ori_ie_rank,$ori_ie_yobi7,$ori_ie_yobi8,$ori_ie_yobi9,$ori_ie_yobi10)= split(/<>/);
				if ($ori_ie_town eq "$yuusyou_taun"){
					$haihusaki_dir = "./member/$ori_k_id/log.cgi";			#ver.1.40
					if (-e "$haihusaki_dir"){			#ver.1.40
						&openAitelog ($ori_k_id);
						$aite_bank += $syoukingaku;
							&aite_temp_routin;
										open(OUT,">$aite_log_file") || &error("$aite_log_file不能寫上");
										print OUT $aite_k_temp;
										close(OUT);
						$kityou_naiyou = "街競賽賞金"."@_[1]";
						&aite_kityou_syori("$kityou_naiyou","",$syoukingaku,$aite_bank,"普",$ori_k_id,"lock_off");
					}			#ver.1.40
				}
		}
	&unlock;
}

