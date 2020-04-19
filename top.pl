sub main_view {
if ($in{'command'} eq "mati_idou"){
	&header(syokudou_style);
	if ($matiidou_time2 <= 0){$kakaruzikan_com = "馬上到達。";}else{$kakaruzikan_com = "請等待$matiidou_time2秒。";}
	print <<"EOM";
	<br><br><br><br><table  border=0  cellspacing="5" cellpadding="0" width=200 align=center bgcolor=#ffffcc><tr><td>
	<div align=center style="font-size:11px">$idousyudan移動中...<br>$kakaruzikan_com</div>
	</td></tr></table>
	</body></html>
EOM
	exit;
}

#取得零件信息
&town_no_get;		#ver.1.40
&get_unit;			#ver.1.40
&kozin_house;			#ver.1.40
&simaitosi;			#ver.1.40
&admin_parts;		#ver.1.40

#####打開街的記錄畫面展開
	$town_data = "./log_dir/townlog".$this_town_no.".cgi";
	open(TW,"$town_data") || &error("Open Error : $town_data");
	$hyouzi_town_hairetu = <TW>;
	close(TW);
		&town_sprit($hyouzi_town_hairetu);
#家建築物建前審核畫面表示預定地
		if ($in{'mode'} eq "kentiku_do" && $in{'command'} eq "kakunin"){
				$sentaku_point = $in{'tateziku'} + $in{'yokoziku'} ;
				if ($town_sprit_matrix[$sentaku_point] ne "空地"){&error("選擇了的地方不是空地！");}
				$town_sprit_matrix[$sentaku_point] = "地";
		}
	&header("","sonomati");
	&get_cookie;
	&time_get;
#街中的背景顏色
	if($return_return_hour >= 22){
		$sotonoiro="#333366";
	}elsif ($return_hour >= 18){
		$sotonoiro="#666699";
	}elsif ($return_hour >= 16){
		$sotonoiro="#ff9966";
	}elsif ($return_hour >= 10){
		$sotonoiro="#ffff99";
	}elsif ($return_hour >= 7){
		$sotonoiro="#ffcc66";
	}elsif ($return_hour >= 0){
		$sotonoiro="#333366";
	}

#ver.1.30從這裡
	print "<table width=100% border=0 cellspacing=10 cellpadding=0>";
#參加者表示
	if ($sanka_hyouzi_kinou == 1){
open(GUEST,"$guestfile");
@all_guest=<GUEST>;
close(GUEST);
$genzai_zikoku = time;
$genzaino_ninzuu = @all_guest;

$sanka_flag=0;
@new_all_guest = ();
foreach (@all_guest) {
	($sanka_timer,$sanka_name,$hyouzi_check) = split(/<>/);
	if ($name eq "$sanka_name"){
		if ($in{'sanka_hyouzi_on'}){$hyouzi_check = "$in{'sanka_hyouzi_on'}";}
		$sanka_flag=1; $sanka_timer = $genzai_zikoku;
	}
	if( $genzai_zikoku - $logout_time > $sanka_timer){next;}
	$sanka_tmp = "$sanka_timer<>$sanka_name<>$hyouzi_check<>\n";
	push (@new_all_guest,$sanka_tmp);
	if ($hyouzi_check eq "on"){
		$sanka_hyouzi .= "$sanka_name<font size=1 color=#FF7F50>★</font>";
	}
}
if ($sanka_flag == 0 && $in{'mode'} ne ""){

if ($genzaino_ninzuu >= $douzi_login_ninzuu && $in{'iiyudane'} eq ""){&error("現在，同時超過著登入限制的$douzi_login_ninzuu人。真對不起，不過請暫且等侯再次登入。");}		#ver.1.30

		if ($in{'sanka_hyouzi_on'}){
			push(@new_all_guest,"$genzai_zikoku<>$name<>$in{'sanka_hyouzi_on'}<>\n");
			if ($in{'sanka_hyouzi_on'} eq "on"){$sanka_hyouzi .= "$name<font size=1 color=#FF7F50>★</font>";}
		}else{
			push(@new_all_guest,"$genzai_zikoku<>$name<>$mise_type<>\n");
			if ($mise_type eq "on"){$sanka_hyouzi .= "$name<font size=1 color=#FF7F50>★</font>";}
		}
}

#ver.1.40從這裡
	if ($mem_lock_num == 0){
		$err = data_save($guestfile, @new_all_guest);
		if ($err) {&error("$err");}
	}else{
		&lock;	
		open(GUEST,">$guestfile");
		print GUEST @new_all_guest;
		close(GUEST);
		&unlock;
	}
#ver.1.40到這裡
	$sankaninzuu = @new_all_guest;
		if ($sanka_hyouzi_iti == 1){
			print <<"EOM";
			<tr><td colspan=2>
			<font size=2 color=#333333>現在的總參加者(<B>$sankaninzuu人</B>)：</font>
			$sanka_hyouzi
			</td></tr>
EOM
		}
	}		#if （參加者的表示）閉上
	
	my @filesize_check = stat($logfile);
	if ($filesize_check[7] > 600000){&error("$logfile的容量有問題。請到管理者($master_ad)告知。");}

#幫助窗口
	print <<"EOM";
<!-- ver.1.30到這裡 -->
  <tr><td width="554" valign=top>
<div align=center><FORM NAME="foMes5">
<INPUT TYPE="text" SIZE="82" NAME="TeMes5" style="font-size:11px; color:#000000; background-color:#d6dbbf"></FORM></div>
      <table border="0" cellspacing="0" cellpadding="0" style="background-color:$sotonoiro;">
        <tr valign="center" style="$page_back[$this_town_no]"> 
          <td height="10" width="20"  align=center> </td>
EOM
#yoko的號碼部分輸出
		 foreach $yokoziku_koumoku (1..16) {
          	print "<td height=10 width=32 align=center class=migi>$yokoziku_koumoku</td>";
		}
		print "</tr>";
#只yoko的號碼(td)的數輸出tate的記號(tr)
		$i = 21;
		foreach $tateziku_kigou  (A..L) {
			print "<tr valign=center><td height=32 width=10 style=\"$page_back[$this_town_no]\" align=center class=sita>$tateziku_kigou</td>\n";
			foreach $yokoziku_bangou (1..16) {
				if ($town_sprit_matrix[$yokoziku_bangou + $i]){
					print "$unit{$town_sprit_matrix[$yokoziku_bangou + $i]}\n";
				}else{print "<td height=32 width=32></td>\n";}
			}
			print "</tr>\n";
			$i += 17;
		}
	print "</table>";
	
#ver.1.3從這裡
		open(IN,"$aisatu_logfile") || &error("Open Error : $aisatu_logfile");
		@aisatu_data = <IN>;
		close(IN);
			if ($top_aisatu_hyouzi == 1){
				if (@aisatu_data ne ""){$aisatu_table .= "<table border=0 width=95% align=center cellspacing=5 cellpadding=0><tr><td>";}
				$i=0;
				foreach (@aisatu_data){
					local($a_num,$a_name,$a_date,$a_com,$a_syurui,$a_yobi2)= split(/<>/);
					$aisatu_table .= "<span  style=\"color:$top_aisatu_hyouzi_iro1;\">$a_name：</span><span  style=\"color:$top_aisatu_hyouzi_iro2;\">$a_com</span><br>";
					$i ++;
					if ($i >= $top_aisatu_hyouzikensuu){last;}
				}
				if (@aisatu_data ne ""){$aisatu_table .= "</td></tr></table>";}
			}

	if ($in{'name'} eq ""){
		print "$top_information";
	}else{
		print "$aisatu_table";
	}

	print "</td><td valign=top>";
#ver.1.3到這裡

	if ($in{'mode'} eq ""){
		&top_gamen;
	}elsif ($in{'mode'} eq "kentiku_do" && $in{'command'} eq "kakunin"){
		&kentiku_kakunin;
	}else{
		&town_jouhou($this_town_no); &loged_gamen;
	}
	
#ver.1.30從這裡
		if ($sanka_hyouzi_kinou == 1 && $sanka_hyouzi_iti == 0){
			print <<"EOM";
			</td></tr>
			<tr><td colspan=2>
			<font size=2 color=#333333>現在的總參加者(<B>$sankaninzuu人</B>)：</font>
			$sanka_hyouzi
EOM
		}
#ver.1.30到這裡
	print "</td></tr></table>";
	&hooter("","");
}

####建築確認画面
sub kentiku_kakunin {
if ($in{'iegazou'} eq ""){&error("家的畫像沒被選擇");}
if ($in{'matirank'} eq ""){&error("家的排位沒被選擇");}
$ori_ie_image = "$img_dir/$in{'iegazou'}";
if ($in{'matirank'} eq "0"){$kauieno_rank = "A";}
elsif  ($in{'matirank'} eq "1"){$kauieno_rank = "B";}
elsif  ($in{'matirank'} eq "2"){$kauieno_rank = "C";}
elsif  ($in{'matirank'} eq "3"){$kauieno_rank = "D";}

#金額計算
	$kensetu_hiyou = $town_tika_hairetu[$in{'mati_sentaku'}] + $ie_hash{$in{'iegazou'}} + $housu_nedan[$in{'matirank'}];
print <<"EOM";
<table width="100%" border="0" cellspacing="0" cellpadding="7" class=yosumi><tr><td>
<div align=center class=dai>建 築 規 格 說 明 書</div><hr size=1><br>
<div class=tyuu>建築的街</div>
$town_hairetu[$in{'mati_sentaku'}]（地價：$town_tika_hairetu[$in{'mati_sentaku'}]萬元）<br><br>
<div class=tyuu>地方</div>
左面的<img src ="$img_dir/kentiku_yotei.gif" width=32 height=32 border=0 align=middle>位置建造。<br><br>
<div class=tyuu>家（外觀）</div>
<img src="$ori_ie_image" width=32 height=32> （$ie_hash{$in{'iegazou'}}萬元）<br><br>
<div class=tyuu>家（裝修）</div>
$kauieno_rank（價格：$housu_nedan[$in{'matirank'}]萬元）<br><br>
<div class=job_messe>建築費用<br>
<div class=dai>$kensetu_hiyou 萬元</div>
。</div>

<form method="POST"action="$script">
	<input type=hidden name=mode value="kentiku_do">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_k_id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=ori_ie_town value="$in{'mati_sentaku'}">
	<input type=hidden name=ori_ie_sentaku_point value="$sentaku_point">
	<input type=hidden name=ori_ie_tateziku value="$in{'tateziku'}">
	<input type=hidden name=ori_ie_yokoziku value="$in{'yokoziku'}">
	<input type=hidden name=ori_ie_image value="$ori_ie_image">
	<input type=hidden name=ori_ie_rank value="$in{'matirank'}">
	<input type=hidden name=kensetu_hiyou value="$kensetu_hiyou">
	<div align=center><input type="submit"value="用這個內容建造家"><br><br>
	<a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
</form>

</td></tr></table>
EOM
}


1;
