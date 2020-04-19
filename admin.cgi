#!/perl/bin/perl
#↑使用合乎服務器的路徑。

$this_script = 'admin.cgi';
#require './jcode.pl';
require './cgi-lib.pl';
require './town_ini.cgi';
require './town_lib.pl';
require './unit.pl';
&decode;
#維護檢查
	if($mente_flag == 1 && $in{'admin_pass'} eq "" && $in{'mode'} ne ""){&error("$mente_message")}
$seigenyou_now_time = time;
#限制時間檢查
		$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $access_byou);
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("還不能行動。請等候$ato_nanbyou秒。")}
		
#條件分歧
	if($in{'mode'} eq "admin"){&admin;}
	elsif($in{'mode'} eq "admin_bbs"){&admin_bbs;}
	elsif($in{'mode'} eq "bbs1_settei_do"){&bbs1_settei_do;}
	elsif($in{'mode'} eq "yakuba"){&yakuba;}
	elsif($in{'mode'} eq "ad_orosi_kousin"){&ad_orosi_kousin;}
	elsif($in{'mode'} eq "parts_taiou_hyou"){&parts_taiou_hyou;}
	elsif($in{'mode'} eq "itiran"){&itiran;}
	elsif($in{'mode'} eq "kensaku"){&kensaku;}
	elsif($in{'mode'} eq "kozindata_henkou"){&kozindata_henkou;}
	elsif($in{'mode'} eq "hukkatu"){&hukkatu;}
	elsif($in{'mode'} eq "deletUsr"){&deletUsr;}
	elsif($in{'mode'} eq "make_town"){&make_town;}
	else{&error("請用「返回」按鈕返回街");}
exit;
	
#############以下是子程序
sub admin {
#密碼輸入畫面
	if ($in{'admin_pass'} eq ""){
	&header;
	print <<"EOM";
	<form method="POST" action="$this_script">
	<br><div align=center>
	請輸入密碼。<br><br>
	<input type=text name="admin_pass" size=10><input type=submit value="OK"></div>
	</form>
EOM
exit;
	}
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
	
		$refe = $ENV{'HTTP_REFERER'};
	if ($refe !~ /$setti1/ && $refe !~ /$setti2/ && $refe !~ /$setti3/){
	&error("請從首頁進入。<br>$refe");}
	
#畫面輸出
	&header;
	print <<"EOM";
	<div align=center class=midasi>管理者選單</div><br>
	<table width="500" border="0" cellspacing="0" cellpadding="10" align=center>
  <tr><td>
  <div class=tyuu>●街的佈置作成</div>
EOM
 	$i=0;
 	foreach (@town_hairetu) {
			 print <<"EOM";
			<form method="POST" action="$this_script">
			<input type=hidden name=mode value="make_town">
			<input type=hidden name=command value="m_form">
			<input type=hidden name=admin_pass value="$in{'admin_pass'}">
			<input type=hidden name=town_no value="$i">
			<input type=hidden name=town_n value="$_">
			<input type=submit value="『$_』的佈置作成">
			</form>
EOM
 			$i ++;
  	}
	 print "<hr size=1>";
	 print "<div class=tyuu>●管理者作成BBS的設定</div>";
 	$i=0;
 	foreach (@admin_bbs_syurui) {
			 print <<"EOM";
			<form method="POST" action="$this_script">
			<input type=hidden name=mode value="admin_bbs">
			<input type=hidden name=bbs_num value="$i">
			<input type=hidden name=admin_pass value="$in{'admin_pass'}">
			<input type=submit value="$_的設定">
			</form>
EOM
 			$i ++;
  	}
	 
  print <<"EOM";
  		<hr size=1>
		  	<div class=tyuu>●成員管理</div>
  			<form method="POST" action="$this_script">
			<input type=hidden name=mode value="itiran">
			<input type=hidden name=sort_id value="0">
			<input type=hidden name=admin_pass value="$in{'admin_pass'}">
			<input type=submit value="登記人一覽(排列次序)">
			</form>
  	<hr size=1>
	 ※自ver.1.2個人數據的備份數據被member目錄內的「ID識別號+backup」目錄保存。使再這個目錄因為刪掉期限過去那個人的數據成為被刪掉了之後也留有的方法，請刪掉偶然成為了只backup的目錄。<br>
	 ※個人數據以外的各種記錄(log_dir文件夾內的文件)1日1次備份處理被進行。全部的log file，被「log_dir」文件夾內的「backup_dir」文件夾以「backup_」的文件名保存。現狀，有關復活的指令因為沒準備，如果萬有一記錄消失了請從這個備份文件複製，使用符合的文件。

  	<hr size=1>
		  	<div class=tyuu>●批發商品的更新</div>
			  ※按這個按鈕管理者能任意的時間更新批發商品。
  			<form method="POST" action="$this_script">
			<input type=hidden name=mode value="ad_orosi_kousin">
			<input type=hidden name=admin_pass value="$in{'admin_pass'}">
			<input type=submit value="更新">
			</form>
  	<hr size=1>
	</td></tr></table>
	<div align=center><a href=$script>[返回]</a></div>
	</body></html>
EOM
exit;
}

###########以下是子程序

sub town_temp{
$town_temp = "$town_name<>$zinkou<>$keizai<>$hanei<>$t_x0<>$t_x1<>$t_x2<>$t_x3<>$t_x4<>$t_x5<>$t_x6<>$t_x7<>$t_x8<>$t_x9<>$t_x10<>$t_x11<>$t_x12<>$t_x13<>$t_x14<>$t_x15<>$t_x16<>$t_a0<>$t_a1<>$t_a2<>$t_a3<>$t_a4<>$t_a5<>$t_a6<>$t_a7<>$t_a8<>$t_a9<>$t_a10<>$t_a11<>$t_a12<>$t_a13<>$t_a14<>$t_a15<>$t_a16<>$t_b0<>$t_b1<>$t_b2<>$t_b3<>$t_b4<>$t_b5<>$t_b6<>$t_b7<>$t_b8<>$t_b9<>$t_b10<>$t_b11<>$t_b12<>$t_b13<>$t_b14<>$t_b15<>$t_b16<>$t_c0<>$t_c1<>$t_c2<>$t_c3<>$t_c4<>$t_c5<>$t_c6<>$t_c7<>$t_c8<>$t_c9<>$t_c10<>$t_c11<>$t_c12<>$t_c13<>$t_c14<>$t_c15<>$t_c16<>$t_d0<>$t_d1<>$t_d2<>$t_d3<>$t_d4<>$t_d5<>$t_d6<>$t_d7<>$t_d8<>$t_d9<>$t_d10<>$t_d11<>$t_d12<>$t_d13<>$t_d14<>$t_d15<>$t_d16<>$t_e0<>$t_e1<>$t_e2<>$t_e3<>$t_e4<>$t_e5<>$t_e6<>$t_e7<>$t_e8<>$t_e9<>$t_e10<>$t_e11<>$t_e12<>$t_e13<>$t_e14<>$t_e15<>$t_e16<>$t_f0<>$t_f1<>$t_f2<>$t_f3<>$t_f4<>$t_f5<>$t_f6<>$t_f7<>$t_f8<>$t_f9<>$t_f10<>$t_f11<>$t_f12<>$t_f13<>$t_f14<>$t_f15<>$t_f16<>$t_g0<>$t_g1<>$t_g2<>$t_g3<>$t_g4<>$t_g5<>$t_g6<>$t_g7<>$t_g8<>$t_g9<>$t_g10<>$t_g11<>$t_g12<>$t_g13<>$t_g14<>$t_g15<>$t_g16<>$t_h0<>$t_h1<>$t_h2<>$t_h3<>$t_h4<>$t_h5<>$t_h6<>$t_h7<>$t_h8<>$t_h9<>$t_h10<>$t_h11<>$t_h12<>$t_h13<>$t_h14<>$t_h15<>$t_h16<>$t_i0<>$t_i1<>$t_i2<>$t_i3<>$t_i4<>$t_i5<>$t_i6<>$t_i7<>$t_i8<>$t_i9<>$t_i10<>$t_i11<>$t_i12<>$t_i13<>$t_i14<>$t_i15<>$t_i16<>$t_j0<>$t_j1<>$t_j2<>$t_j3<>$t_j4<>$t_j5<>$t_j6<>$t_j7<>$t_j8<>$t_j9<>$t_j10<>$t_j11<>$t_j12<>$t_j13<>$t_j14<>$t_j15<>$t_j16<>$t_k0<>$t_k1<>$t_k2<>$t_k3<>$t_k4<>$t_k5<>$t_k6<>$t_k7<>$t_k8<>$t_k9<>$t_k10<>$t_k11<>$t_k12<>$t_k13<>$t_k14<>$t_k15<>$t_k16<>$t_l0<>$t_l1<>$t_l2<>$t_l3<>$t_l4<>$t_l5<>$t_l6<>$t_l7<>$t_l8<>$t_l9<>$t_l10<>$t_l11<>$t_l12<>$t_l13<>$t_l14<>$t_l15<>$t_l16<>$t_m0<>$t_m1<>$t_m2<>$t_m3<>$t_m4<>$t_m5<>$t_m6<>$t_m7<>$t_m8<>$t_m9<>$t_m10<>$t_m11<>$t_m12<>$t_m13<>$t_m14<>$t_m15<>$t_m16<>$t_n0<>$t_n1<>$t_n2<>$t_n3<>$t_n4<>$t_n5<>$t_n6<>$t_n7<>$t_n8<>$t_n9<>$t_n10<>$t_n11<>$t_n12<>$t_n13<>$t_n14<>$t_n15<>$t_n16<>$tika<>$t_yobi2<>$t_yobi3<>$t_yobi4<>$t_yobi5<>$t_yobi6<>$t_yobi7<>\n";
}

######街的佈置
sub make_town {
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
		&header(2);
	if($in{'command'} eq "m_form"){
		&town_form;
		exit;
	}
	if($in{'command'} eq "regi"){
$town_temp = "$in{'town_n'}<>$in{'zinkou'}<>$in{'keizai'}<>$in{'hanei'}<>$in{'t_x0'}<>$in{'t_x1'}<>$in{'t_x2'}<>$in{'t_x3'}<>$in{'t_x4'}<>$in{'t_x5'}<>$in{'t_x6'}<>$in{'t_x7'}<>$in{'t_x8'}<>$in{'t_x9'}<>$in{'t_x10'}<>$in{'t_x11'}<>$in{'t_x12'}<>$in{'t_x13'}<>$in{'t_x14'}<>$in{'t_x15'}<>$in{'t_x16'}<>$in{'t_a0'}<>$in{'t_a1'}<>$in{'t_a2'}<>$in{'t_a3'}<>$in{'t_a4'}<>$in{'t_a5'}<>$in{'t_a6'}<>$in{'t_a7'}<>$in{'t_a8'}<>$in{'t_a9'}<>$in{'t_a10'}<>$in{'t_a11'}<>$in{'t_a12'}<>$in{'t_a13'}<>$in{'t_a14'}<>$in{'t_a15'}<>$in{'t_a16'}<>$in{'t_b0'}<>$in{'t_b1'}<>$in{'t_b2'}<>$in{'t_b3'}<>$in{'t_b4'}<>$in{'t_b5'}<>$in{'t_b6'}<>$in{'t_b7'}<>$in{'t_b8'}<>$in{'t_b9'}<>$in{'t_b10'}<>$in{'t_b11'}<>$in{'t_b12'}<>$in{'t_b13'}<>$in{'t_b14'}<>$in{'t_b15'}<>$in{'t_b16'}<>$in{'t_c0'}<>$in{'t_c1'}<>$in{'t_c2'}<>$in{'t_c3'}<>$in{'t_c4'}<>$in{'t_c5'}<>$in{'t_c6'}<>$in{'t_c7'}<>$in{'t_c8'}<>$in{'t_c9'}<>$in{'t_c10'}<>$in{'t_c11'}<>$in{'t_c12'}<>$in{'t_c13'}<>$in{'t_c14'}<>$in{'t_c15'}<>$in{'t_c16'}<>$in{'t_d0'}<>$in{'t_d1'}<>$in{'t_d2'}<>$in{'t_d3'}<>$in{'t_d4'}<>$in{'t_d5'}<>$in{'t_d6'}<>$in{'t_d7'}<>$in{'t_d8'}<>$in{'t_d9'}<>$in{'t_d10'}<>$in{'t_d11'}<>$in{'t_d12'}<>$in{'t_d13'}<>$in{'t_d14'}<>$in{'t_d15'}<>$in{'t_d16'}<>$in{'t_e0'}<>$in{'t_e1'}<>$in{'t_e2'}<>$in{'t_e3'}<>$in{'t_e4'}<>$in{'t_e5'}<>$in{'t_e6'}<>$in{'t_e7'}<>$in{'t_e8'}<>$in{'t_e9'}<>$in{'t_e10'}<>$in{'t_e11'}<>$in{'t_e12'}<>$in{'t_e13'}<>$in{'t_e14'}<>$in{'t_e15'}<>$in{'t_e16'}<>$in{'t_f0'}<>$in{'t_f1'}<>$in{'t_f2'}<>$in{'t_f3'}<>$in{'t_f4'}<>$in{'t_f5'}<>$in{'t_f6'}<>$in{'t_f7'}<>$in{'t_f8'}<>$in{'t_f9'}<>$in{'t_f10'}<>$in{'t_f11'}<>$in{'t_f12'}<>$in{'t_f13'}<>$in{'t_f14'}<>$in{'t_f15'}<>$in{'t_f16'}<>$in{'t_g0'}<>$in{'t_g1'}<>$in{'t_g2'}<>$in{'t_g3'}<>$in{'t_g4'}<>$in{'t_g5'}<>$in{'t_g6'}<>$in{'t_g7'}<>$in{'t_g8'}<>$in{'t_g9'}<>$in{'t_g10'}<>$in{'t_g11'}<>$in{'t_g12'}<>$in{'t_g13'}<>$in{'t_g14'}<>$in{'t_g15'}<>$in{'t_g16'}<>$in{'t_h0'}<>$in{'t_h1'}<>$in{'t_h2'}<>$in{'t_h3'}<>$in{'t_h4'}<>$in{'t_h5'}<>$in{'t_h6'}<>$in{'t_h7'}<>$in{'t_h8'}<>$in{'t_h9'}<>$in{'t_h10'}<>$in{'t_h11'}<>$in{'t_h12'}<>$in{'t_h13'}<>$in{'t_h14'}<>$in{'t_h15'}<>$in{'t_h16'}<>$in{'t_i0'}<>$in{'t_i1'}<>$in{'t_i2'}<>$in{'t_i3'}<>$in{'t_i4'}<>$in{'t_i5'}<>$in{'t_i6'}<>$in{'t_i7'}<>$in{'t_i8'}<>$in{'t_i9'}<>$in{'t_i10'}<>$in{'t_i11'}<>$in{'t_i12'}<>$in{'t_i13'}<>$in{'t_i14'}<>$in{'t_i15'}<>$in{'t_i16'}<>$in{'t_j0'}<>$in{'t_j1'}<>$in{'t_j2'}<>$in{'t_j3'}<>$in{'t_j4'}<>$in{'t_j5'}<>$in{'t_j6'}<>$in{'t_j7'}<>$in{'t_j8'}<>$in{'t_j9'}<>$in{'t_j10'}<>$in{'t_j11'}<>$in{'t_j12'}<>$in{'t_j13'}<>$in{'t_j14'}<>$in{'t_j15'}<>$in{'t_j16'}<>$in{'t_k0'}<>$in{'t_k1'}<>$in{'t_k2'}<>$in{'t_k3'}<>$in{'t_k4'}<>$in{'t_k5'}<>$in{'t_k6'}<>$in{'t_k7'}<>$in{'t_k8'}<>$in{'t_k9'}<>$in{'t_k10'}<>$in{'t_k11'}<>$in{'t_k12'}<>$in{'t_k13'}<>$in{'t_k14'}<>$in{'t_k15'}<>$in{'t_k16'}<>$in{'t_l0'}<>$in{'t_l1'}<>$in{'t_l2'}<>$in{'t_l3'}<>$in{'t_l4'}<>$in{'t_l5'}<>$in{'t_l6'}<>$in{'t_l7'}<>$in{'t_l8'}<>$in{'t_l9'}<>$in{'t_l10'}<>$in{'t_l11'}<>$in{'t_l12'}<>$in{'t_l13'}<>$in{'t_l14'}<>$in{'t_l15'}<>$in{'t_l16'}<>$in{'t_m0'}<>$in{'t_m1'}<>$in{'t_m2'}<>$in{'t_m3'}<>$in{'t_m4'}<>$in{'t_m5'}<>$in{'t_m6'}<>$in{'t_m7'}<>$in{'t_m8'}<>$in{'t_m9'}<>$in{'t_m10'}<>$in{'t_m11'}<>$in{'t_m12'}<>$in{'t_m13'}<>$in{'t_m14'}<>$in{'t_m15'}<>$in{'t_m16'}<>$in{'t_n0'}<>$in{'t_n1'}<>$in{'t_n2'}<>$in{'t_n3'}<>$in{'t_n4'}<>$in{'t_n5'}<>$in{'t_n6'}<>$in{'t_n7'}<>$in{'t_n8'}<>$in{'t_n9'}<>$in{'t_n10'}<>$in{'t_n11'}<>$in{'t_n12'}<>$in{'t_n13'}<>$in{'t_n14'}<>$in{'t_n15'}<>$in{'t_n16'}<>$in{'tika'}<>$in{'t_yobi2'}<>$in{'t_yobi3'}<>$in{'t_yobi4'}<>$in{'t_yobi5'}<>$in{'t_yobi6'}<>$in{'t_yobi7'}<>\n";
# 更新記錄
						&lock;
						$town_data = "./log_dir/townlog".$in{'town_no'}.".cgi";
						open(KOUT,">$town_data") || &error("Write Error : $town_data");
						print KOUT $town_temp;
						close(KOUT);
						&unlock;
	print <<"EOM";
	<div align=center>製作了$in{'town_n'}。<br><br>
	<a href=$script?town_no=$in{'town_no'} target=_blank>[街的確認]</a><br><br>
	<a href=\"javascript:history.back()\"> [返回前畫面] </a><br><br>
EOM
	&hooter("admin","返回","admin.cgi");
	exit;
	}
}


sub town_form {
	&get_unit;
	&simaitosi;
	&admin_parts;
	
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
	$town_data = "./log_dir/townlog".$in{'town_no'}.".cgi";
	if(! -e $town_data){
		open(INI,">$town_data") || &error("Write Error : $town_data");
		close(INI);
	}
	open(IN,"$town_data") || &error("Open Error : $town_data");
	$maketown_data=<IN>;
	close(IN);
			&town_sprit($maketown_data);
	print <<"EOM";
	<table border="0" cellspacing="0" cellpadding="10">
	<tr><td valign=top width=50%>
	<div class="tyuu">$in{'town_n'}的佈置作成畫面</div>
	這個輸入欄的位置與街的佈置對應著。<br>
	把右面有的表\做為參考輸入欄記述「記號」，按OK按鈕，在那個地方與記號對應了的圖片被建設的。<br>
	<font color=#ff6600>※如果在設置後，只數字被輸入，那個參加者建築了的家(數字是那一位的ID)。因為變更了這個數字的話家丟失了，請注意會令街全體皆產生問題。</font><br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="make_town">
	<input type=hidden name=command value="regi">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=hidden name=town_no value="$in{'town_no'}">
	<input type=hidden name=town_n value="$in{'town_n'}">
	<input type=hidden name=zinkou value="$zinkou">
	<input type=hidden name=keizai value="$keizai">
	<input type=hidden name=hanei value="$hanei">
	<input type=hidden name=t_yobi1 value="$t_yobi1">
	<input type=hidden name=t_yobi2 value="$t_yobi2">
	<input type=hidden name=t_yobi3 value="$t_yobi3">
	<input type=hidden name=t_yobi4 value="$t_yobi4">
	<input type=hidden name=t_yobi5 value="$t_yobi5">
	<input type=hidden name=t_yobi6 value="$t_yobi6">
	<input type=hidden name=t_yobi7 value="$t_yobi7">
		<table border="0" cellspacing="0" cellpadding="0" width=400><!--形式用的街開始-->
        <tr valign="bottom"> <!--橫軸的數字輸出部分-->
         <td height="10" width="20"  align=center class=sumi> </td>
EOM
#橫的號碼部分輸出
		 foreach $yokoziku_koumoku (1..16) {
          	print "<td height=10 width=32 align=center class=migi>$yokoziku_koumoku</td>\n";
		}
		print "</tr>";
#橫的號碼(td)的數輸出縱的記號(tr)
		$i = 21;
		foreach $tateziku_kigou  (a..l) {
			print "<tr valign=center><td height=32 width=10 align=center class=sita>$tateziku_kigou</td>\n";
			foreach $yokoziku_bangou (1..16) {
				$name_seikei= "t_" . $tateziku_kigou . $yokoziku_bangou;
				print "<td height=32 width=32><input type=text size=4 value=\"$town_sprit_matrix[$yokoziku_bangou + $i]\" name=$name_seikei style=font-size:10px></td>\n";
			}
			print "</tr>\n";
			$i += 17;
		}
	print <<"EOM";
      </table>
	<br><div align=center><input type=submit value=" O K ">
	<a href=\"javascript:history.back()\"> [返回前畫面] </a>
	</div>
	</form>
	</td><td valign=top><!--table右部分-->
	■圖片&記號對應表\<br>
	<FORM NAME="foMes5">
<INPUT TYPE="text" SIZE="82" NAME="TeMes5" style="font-size:11px; color:#000000; background-color:#d6dbbf"></FORM>
EOM
	&parts_taiou_hyou;
	print <<"EOM";
	</td></tr></table>
	</body></html>
EOM
}

#####圖片&關鍵字對應表
sub parts_taiou_hyou {
	print <<"EOM";
	<table border="0" cellspacing="0" cellpadding="5" width=90% bgcolor=#ffffcc>
	<tr class=jouge bgcolor=#ffff99 align=center><td>記號</td><td>圖片</td><td>記號</td><td>圖片</td><td>記號</td><td>圖片</td><td>記號</td><td>圖片</td><td>記號</td><td>圖片</td></tr><tr>
EOM

	@parts_keys = keys %unit;
	sub byPartskeys {$a cmp $b};
	@parts_keys = sort byPartskeys @parts_keys;
	
	$i = 1;
	foreach (@parts_keys){
		if ($_ ne "地"){
			print "<td align=right nowrap>$_</td>$unit{$_}";
			if ($i % 5 == 0){print "</tr><tr>";}
			$i ++;
		}
	}

	print <<"EOM";
	</tr>
	<tr><td colspan=8>
	</td></tr></table>
EOM
exit;
}
#####管理者作成BBS
sub admin_bbs {
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
	&header;
	&bbs1_settei;
	&hooter("admin","返回","admin.cgi");
	exit;
}

#####参加者一覧
sub itiran {
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
	&header;
	open(IN,"$logfile") || &error("Open Error : $logfile");
	@rankingMember = <IN>;
		foreach (@rankingMember) {
			$data=$_;
			$key=(split(/<>/,$data))[$in{'sort_id'}];		#選排序的要素
			push @alldata,$data;
			push @keys,$key;
		}
	close(IN);
	if($in{'sort_id'} eq ""){
		sub gyakujun{$keys[$a] <=> $keys[$b];}
		@alldata=@alldata[ sort gyakujun 0..$#alldata]; 
	}elsif($in{'sort_id'} eq "1" || $in{'sort_id'} eq "28"){
		sub byString{$keys[$a] cmp $keys[$b];}
		@alldata=@alldata[ sort byString 0..$#alldata]; 
	}else{
		sub seijun{$keys[$b] <=> $keys[$a];}
		@alldata=@alldata[ sort seijun 0..$#alldata]; 
	}
#作成同樣host的排列
	if($in{'sort_id'} eq "28"){
			foreach (@alldata) {
				&list_sprit($_);
				if($list_host eq "$maeno_host"){
						push @tajuutouroku , $_;
						$check_flag=0;
						foreach $two(@tajuutouroku){
							(@check_list_host)= split(/<>/,$two);
									if($list_host eq "$check_list_host[28]"){$check_flag ++;}
						}
						if($check_flag <= 1 && $maeno_data ne ""){push @tajuutouroku , $maeno_data;}
				}
				$maeno_host = $list_host;
				$maeno_data = $_;
			}
	}
	print <<"EOM";
	<center>
	<div align=center class=tyuu>登記人一覽(排列次序數據)</div><br>
<a href=$this_script?mode=itiran&sort_id=0&admin_pass=$in{'admin_pass'}><span class=sub3>[新參加順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&admin_pass=$in{'admin_pass'}><span class=sub3>[ID順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=49&admin_pass=$in{'admin_pass'}><span class=sub3>[資產順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=1&admin_pass=$in{'admin_pass'}><span class=sub3>[名字順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=38&admin_pass=$in{'admin_pass'}><span class=sub3>[最近的吃飯順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=28&admin_pass=$in{'admin_pass'}><span class=sub3>[HOST順]</span></a><img src=$img_dir/space.gif width=5 height=1>
</center>
	
	<table border=0 width=95% align=center cellspacing="1" cellpadding="5">
	<tr><td colspan=10>●單擊名字能訪問那人的個人數據。再在那個畫面能進行「用戶刪掉」「各種數據的修正」「錢的匯款(減少錢)」「郵件發送」等。<br>※黑名單為雙重登記人被記錄了的用戶。<br>※這個名單的數字全部用於數據保存時的東西，與現在的數據不同。
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="kensaku">
	<input type=hidden name=command value="kozin_file">
	<input type=hidden name=name value="$list_name">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	ID號 <input type=text name=k_id size="6">也能在這邊輸入ID打開個人數據。
	</form>
	
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="kensaku">
	<input type=hidden name=command value="kozin_file">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	名字 <input type=text name=name size="20">也能在這邊輸入名字打開個人數據。
	</form>
	
	</td></tr>
	<tr  class=jouge bgcolor=#ffff66><td align=center >ID</td><td align=center  width=120>名字</td><td align=center >性別</td><td align=center >資產</td><td align=center >職業</td><td align=center >最近的吃飯</td><td align=center >HOST</td><td align=center >黑名單</td></tr>
EOM
#多重登録者表示
	if($in{'sort_id'} eq "28"){
		print "<tr  class=jouge bgcolor=#bbbbbb><td colspan=8>在多重登記人(同樣IP or HOST的登記人)</td></tr>";
		foreach (@tajuutouroku) {
			&list_sprit($_);
#整形性別表示
	if ($list_sex eq "f") {$seibetu = "女";}else{$seibetu = "男";}
	
#整形最後吃飯表示
	$ENV{'TZ'} = "CST-8";
	($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime($list_last_syokuzi);
	my $mon  = $mon+1;
	my $year = $year + 1900;
	my $a_date = "$year年$mon月$mday日  $hour時$min分";

#按順序表示名單
						print <<"EOM";
<tr class=sita2><td align=center>$list_k_id</td><td nowrap><a href=$this_script?mode=kensaku&command=kozin_file&k_id=$list_k_id&admin_pass=$in{'admin_pass'}>$list_name</a></td><td align=center>$seibetu</td><td align=right nowrap>$list_sousisan元</td><td>$list_job</td><td align=left nowrap>$a_date</td><td align=left nowrap>$list_host</td><td align=left nowrap>$list_k_yobi3</td></tr>
EOM
		}	#foreach閉上
		print "<tr  class=sita2 bgcolor=#ffffcc><td colspan=8>以下全參加者的名單</td></tr>";
	}
	
	
	foreach (@alldata) {
		&list_sprit($_);
		if ($list_sex eq "f") {$seibetu = "女";$f_count ++ ;}else{$seibetu = "男";$m_count ++ ;}
	
#整形最後吃飯表示
	$ENV{'TZ'} = "CST-8";
	($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime($list_last_syokuzi);
	my $mon  = $mon+1;
	my $year = $year + 1900;
	my $a_date = "$year年$mon月$mday日  $hour時$min分";
	
						print <<"EOM";
<tr class=sita2><td align=center>$list_k_id</td><td nowrap><a href=$this_script?mode=kensaku&command=kozin_file&k_id=$list_k_id&admin_pass=$in{'admin_pass'}>$list_name</a></td><td align=center>$seibetu</td><td align=right nowrap>$list_sousisan元</td><td>$list_job</td><td align=left nowrap>$a_date</td><td align=left nowrap>$list_host</td><td align=left nowrap>$list_k_yobi3</td></tr>
EOM
		}
	close(IN);
	$total_count=$m_count+$f_count;
	print <<"EOM";
</table>
	<center><br>
<a href=$this_script?mode=itiran&sort_id=0&admin_pass=$in{'admin_pass'}><span class=sub3>[新參加順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&admin_pass=$in{'admin_pass'}><span class=sub3>[ID順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=49&admin_pass=$in{'admin_pass'}><span class=sub3>[資產順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=1&admin_pass=$in{'admin_pass'}><span class=sub3>[名字順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=38&admin_pass=$in{'admin_pass'}><span class=sub3>[最近的吃飯順]</span></a><img src=$img_dir/space.gif width=5 height=1>
<a href=$this_script?mode=itiran&sort_id=28&admin_pass=$in{'admin_pass'}><span class=sub3>[HOST順]</span></a><img src=$img_dir/space.gif width=5 height=1>
</center>
<br><div align=center>總登記人數：$total_count人　男性：$m_count人　女性：$f_count人<br><br>
</div>
	</body></html>
EOM
	&hooter("admin","返回","admin.cgi");
	exit;
}
sub kensaku {
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
#名字單擊又是ID檢索的情況
	if ($in{'k_id'}){
		$kensaku_ID = "$in{'k_id'}";
#是名字檢索的情況
	}elsif($in{'name'}){
			open(HUK,"$logfile") || &error("Open Error : $logfile");
			$hukkatu_flag=0;
			while (<HUK>) {
					&kozin_sprit;
					if($in{'name'} eq $name){$hukkatu_flag=1; $kensaku_ID = "$k_id"; last;}
			}
			close(HUK);
			if($hukkatu_flag == 0){&error("$in{'name'}這名字沒有被登記");}
	}else{&error("不明白檢索對象");}
#是個人文件檢索的情況
	if($in{'command'} eq "kozin_file"){
			$my_log_file = "./member/"."$kensaku_ID"."/log.cgi";
#ver.1.2從這裡
			$my_backlog_file = "./member/"."$kensaku_ID"."backup/backup_log.cgi";
#			if (! -e $my_log_file){&error("ID番号$kensaku_IDのログファイルは存在しません");}
			if (! -e $my_log_file){
				$backup_comment = "<br>因為log file不存在打開著備份數據。能推數據復活按鈕使之復活數據。";
				$my_log_file = $my_backlog_file;
				if (! -e $my_backlog_file){&error("ID識別號$kensaku_ID的log file不存在");}
			}
#ver.1.2到這裡
			open(MYL,"$my_log_file") || &error("log file($my_log_file)不能打開");
			$my_prof = <MYL>;
			&kozin_sprit2($my_prof);
			close(MYL);
			$hukkatu_botan= <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="deletUsr">
	<input type=hidden name=command value="del_kakunin">
	<input type=hidden name=name value="$name">
	<input type=hidden name="k_id" value="$kensaku_ID">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=submit value="刪掉這個用戶">
	</form>
EOM
			$page_comment = "$name君的個人file data。$backup_comment";		#ver.1.2
			$data_syuusei_title =<<"EOM";
			<div class=honbun2>■數據修正</div>
	※能變更有輸入欄的項目在這邊數據。如果做被黑名單文字創造不能進入的一方的進入許可，請消去黑名單的文字。
EOM
#是數據復活的情況
	}elsif($in{'command'} eq "hukkatu"){
			$my_log_file = "./member/"."$kensaku_ID"."backup/backup_log.cgi";		#ver.1.2
			if (! -e $my_log_file){&error("ID識別號$kensaku_ID的log file不存在");}
			open(MYL,"$my_log_file") || &error("log file($my_log_file)不能打開");
			$my_prof = <MYL>;
			&kozin_sprit2($my_prof);
			close(MYL);
	
			$hukkatu_botan= <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="hukkatu">
	<input type=hidden name="k_id" value="$kensaku_ID">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=submit value="這個數據使之復活">
	</form>
EOM
			$page_comment = "$name君的被備份的數據。";
			$data_syuusei_title = "<div class=honbun2>■被保存的數據</div>";
	}
		&header;
	
#整形性別表示
	if ($sex eq "f") {$seibetu = "女";}else{$seibetu = "男";}
	
#整形最後吃飯表示
	$ENV{'TZ'} = "CST-8";
	($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime($last_syokuzi);
	$mon  = $mon+1;
	$year = $year + 1900;
	$s_date = "$year/$mon/$mday  $hour : $min";
	
#整形訪問日期和時間
	$ENV{'TZ'} = "CST-8";
	($a_sec,$a_min,$a_hour,$a_mday,$a_mon,$a_year,$a_wday) = localtime($access_byou);
	$a_mon  = $a_mon+1;
	$a_year = $a_year + 1900;
	$access_date = "$a_year/$a_mon/$a_mday  $a_hour : $a_min";
	
					print <<"EOM";
	<div align=center class=tyuu>$page_comment</div><br><br>
	<table width="95%" border="0" cellspacing="0" cellpadding="5" align=center style="font-size:11px" class=yosumi><tr><td>
			<form method="POST" action="$this_script">
			<input type=hidden name=mode value="kozindata_henkou">
			<input type=hidden name=admin_pass value="$in{'admin_pass'}">
			<input type=hidden name="k_id" value="$k_id">
			<input type=hidden name="name" value="$name">
	<table width="95%" border="0" cellspacing="0" cellpadding="3" align=center style="font-size:11px">
	<tr><td colspan=6>
	$data_syuusei_title
	</td></tr>
	<tr>
	<td>●名字<br>$name</td>
	<td>●性別<br><input type=text size=5 value="$seibetu" name=seibetu>※男 or 女</td>
	<td>●密碼<br><input type=text size=16 value="$pass" name=pass></td>
	<td>●身長<br><input type=text size=5 value="$sintyou" name=sintyou>cm</td>
	<td>●体重<br><input type=text size=10 value="$taijuu" name=taijuu>kg</td>
	<td>●最後訪問<br>$access_date</td></tr><tr>
	
	<td>●總資產<br>$k_sousisan元</td>
	<td>●所持金<br><input type=text size=16 value="$money" name=money>元</td>
	<td>●銀行<br><input type=text size=16 value="$bank" name=bank>元</td>
	<td>●超級定期<br><input type=text size=16 value="$super_teiki" name=super_teiki>元</td>
	<td nowrap>●貸款日額<br><input type=text size=16 value="$loan_nitigaku" name=loan_nitigaku>元</td>
	<td>●貸款剩餘回數<br><input type=text size=5 value="$loan_kaisuu" name=loan_kaisuu>回</td></tr><tr>
	
	<td>●最後的吃飯<br>$s_date</td>
	<td>●身體能源<br><input type=text size=10 value="$energy" name=energy></td>
	<td>●頭腦能源<br><input type=text size=10 value="$nou_energy" name=nou_energy></td>
	<td colspan=2>●HOST<br>$host</td>
	<td>●黑名單<br><input type=text size=20 value="$k_yobi3" name=k_yobi3></td></tr><tr>
	
	<td>●病<br><input type=text size=20 value="$byoumei" name=byoumei></td>
	<td>●病指數<br><input type=text size=20 value="$byouki_sisuu" name=byouki_sisuu></td>
	<td>●職業<br><input type=text size=24 value="$job" name=job></td>
	<td>●主職業<br><input type=text size=24 value="$jobsyu" name=jobsyu></td>
	<td>●工作經驗值<br><input type=text size=10 value="$job_keiken" name=job_keiken></td>
	<td>●工作回數<br><input type=text size=10 value="$job_kaisuu" name=job_kaisuu>回</td></tr><tr>
	</table><br>
	
	<table width="95%" border="0" cellspacing="0" cellpadding="3" align=center><tr>
	<td>●國  語 <input type=text size=6 value="$kokugo" name=kokugo></td>
	<td>●數  學 <input type=text size=6 value="$suugaku" name=suugaku></td>
	<td>●理  科 <input type=text size=6 value="$rika" name=rika></td>
	<td>●社  會 <input type=text size=6 value="$syakai" name=syakai></td>
	<td>●英  語 <input type=text size=6 value="$eigo" name=eigo></td>
	<td>●音  樂 <input type=text size=6 value="$ongaku" name=ongaku></td>
	<td>●美  術 <input type=text size=6 value="$bijutu" name=bijutu></td></tr><tr>
	<td>●容  貌 <input type=text size=6 value="$looks" name=looks></td>
	<td>●體  力 <input type=text size=6 value="$tairyoku" name=tairyoku></td>
	<td>●健  康 <input type=text size=6 value="$kenkou" name=kenkou></td>
	<td>●速  度 <input type=text size=6 value="$speed" name=speed></td>
	<td>●力 <input type=text size=6 value="$power" name=power></td>
	<td>●腕  力 <input type=text size=6 value="$wanryoku" name=wanryoku></td>
	<td>●腳  力 <input type=text size=6 value="$kyakuryoku" name=kyakuryoku></td></tr><tr>
	<td>●ＬＯＶＥ <input type=text size=6 value="$love" name=love></td>
	<td>●興  趣 <input type=text size=6 value="$unique" name=unique></td>
	<td>●淫  蕩 <input type=text size=6 value="$etti" name=etti></td>
	</tr></table>
EOM
	if($in{'command'} eq "kozin_file"){
		print "<div align=center><input type=submit value=\"數據修正\"></div>";
	}
	print <<"EOM";
	</td></tr></table></form>
	<br><br>
EOM
	if($in{'command'} eq "kozin_file"){
	print <<"EOM";
	<table width="95%" border="0" cellspacing="0" cellpadding="5" align=center style="font-size:11px" class=yosumi><tr><td colspan=2>
	<div class=honbun2>■匯入</div>
	※能匯入任意的錢。匯款者的名字初始設置為「管理者名」。能輸入減的金額的使之減少錢。
	</td></tr><tr><td width=220>
	給$name君匯入錢</td><td>
	<form method="POST" action="basic.cgi">
	<input type=hidden name=mode value="ginkoufurikomi">
	<input type=hidden name=command value="from_system">
	<input type=hidden name=name value="$admin_name">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=hidden name=k_id value="$kensaku_ID">
	<input type=hidden name=aitenonamae value="$name">
	匯款金額 <input type=text name=hurikomigaku size=12>元
	<input type=submit value="匯入">
	</form>
	</td></tr></table>
	<br><br>
	<table width="95%" border="0" cellspacing="0" cellpadding="5" align=center style="font-size:11px" class=yosumi><tr><td width=300>
	<div class=honbun2>■消息發送</div>
	※能對$name君發送消息。發送者名初始設置為「管理者名」。
	</td><td>
	<form method="POST" action="$script">
	<input type=hidden name=mode value="mail_do">
	<input type=hidden name=command value="from_system">
	<input type=hidden name=name value="$admin_name">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=hidden name="sousinsaki_name" value="$name">
	<textarea cols=50 rows=4 name=m_com wrap="soft"></textarea>
	<input type="submit" value="消息發送">
	</form></td></tr></table>
	<br><br>
	
<table width="95%" border="0" cellspacing="0" cellpadding="5" align=center style="font-size:11px" class=yosumi><tr><td width=300>
	<div class=honbun2>■備份數據的復活</div>
	※$name君的現行數據與最後被保存了的數據轉換。
	</td><td>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="kensaku">
	<input type=hidden name=command value="hukkatu">
	<input type=hidden name=k_id value="$kensaku_ID">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=hidden name="hukkatu_name" value="$name">
	<input type="submit" value="數據復活">
	</form></td></tr></table>
	<br><br>
EOM
	}
	print <<"EOM"; 
	<div align=center>$hukkatu_botan
	<br><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
	</body></html>
EOM
exit;
}

###個人數據變更
sub kozindata_henkou {
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
#名單數據修正
	open(IN,"$logfile") || &error("Open Error : $logfile");
	@rankingMember = <IN>;
	close(IN);
		$sonzai_flag=0;
		if ($in{'seibetu'} eq "男"){$henkou_seibetu = "m";}elsif($in{'seibetu'} eq "女"){$henkou_seibetu = "f";}
		else{&error("請決定性別是「男人」或者「女人」");}
		foreach (@rankingMember) {
			&list_sprit($_);
			if ($list_name eq "$in{'name'}"){
				$sonzai_flag=1;
				$list_name = $in{'name'}; $list_sex = $henkou_seibetu; $list_pass = $in{'pass'};
				$list_sintyou = $in{'sintyou'}; $list_taijuu = $in{'taijuu'}; #$list_sousisan = $in{'k_sousisan'};		ver.1.3
				$list_money = $in{'money'}; $list_bank = $in{'bank'}; $list_super_teiki = $in{'super_teiki'};
				$list_loan_nitigaku = $in{'loan_nitigaku'}; $list_loan_kaisuu = $in{'loan_kaisuu'}; $list_energy = $in{'energy'};
				$list_nou_energy = $in{'nou_energy'}; $list_k_yobi3 = $in{'k_yobi3'}; $list_byoumei = $in{'byoumei'};
				$list_byouki_sisuu = $in{'byouki_sisuu'}; $list_job = $in{'job'}; $list_jobsyu = $in{'jobsyu'};
				$list_job_keiken = $in{'job_keiken'}; $list_job_kaisuu = $in{'job_kaisuu'}; $list_kokugo = $in{'kokugo'};
				$list_suugaku = $in{'suugaku'}; $list_rika = $in{'rika'}; $list_syakai = $in{'syakai'};
				$list_eigo = $in{'eigo'}; $list_ongaku = $in{'ongaku'}; $list_bijutu = $in{'bijutu'};
				$list_looks = $in{'looks'}; $list_tairyoku = $in{'tairyoku'}; $list_kenkou = $in{'kenkou'};
				$list_speed = $in{'speed'}; $list_power = $in{'power'}; $list_wanryoku = $in{'wanryoku'}; $list_kyakuryoku = $in{'kyakuryoku'};
				$list_love = $in{'love'}; $list_unique = $in{'unique'}; $list_etti = $in{'etti'};
			}
			&list_temp;
			push (@new_ranking_data,$list_temp);
		}
		if ($sonzai_flag==0){&error("在名單上沒找到那個名字的參加者");}
#個人數據修正
		$my_log_file = "./member/$in{'k_id'}/log.cgi";
		open(MYL,"$my_log_file")|| &error("Open Error : $my_log_file");
		$my_prof = <MYL>;
		&kozin_sprit2($my_prof);
		close(MYL);
				$name = $in{'name'}; $sex = $henkou_seibetu; $pass = $in{'pass'};
				$sintyou = $in{'sintyou'}; $taijuu = $in{'taijuu'}; $sousisan = $in{'k_sousisan'};
				$money = $in{'money'}; $bank = $in{'bank'}; $super_teiki = $in{'super_teiki'};
				$loan_nitigaku = $in{'loan_nitigaku'}; $loan_kaisuu = $in{'loan_kaisuu'}; $energy = $in{'energy'};
				$nou_energy = $in{'nou_energy'}; $k_yobi3 = $in{'k_yobi3'}; $byoumei = $in{'byoumei'};
				$byouki_sisuu = $in{'byouki_sisuu'}; $job = $in{'job'}; $jobsyu = $in{'jobsyu'};
				$job_keiken = $in{'job_keiken'}; $job_kaisuu = $in{'job_kaisuu'}; $kokugo = $in{'kokugo'};
				$suugaku = $in{'suugaku'}; $rika = $in{'rika'}; $syakai = $in{'syakai'};
				$eigo = $in{'eigo'}; $ongaku = $in{'ongaku'}; $bijutu = $in{'bijutu'};
				$looks = $in{'looks'}; $tairyoku = $in{'tairyoku'}; $kenkou = $in{'kenkou'};
				$speed = $in{'speed'}; $power = $in{'power'}; $wanryoku = $in{'wanryoku'}; $kyakuryoku = $in{'kyakuryoku'};
				$love = $in{'love'}; $unique = $in{'unique'}; $etti = $in{'etti'};
		
#記錄更新
	&temp_routin;
	&log_kousin($my_log_file,$k_temp);
	
	&lock;
	
#（ver.1.21從這裡）
	if ($mem_lock_num == 0){
		$err = data_save($logfile, @new_ranking_data);
		if ($err) {&error("$err");}
	}else{
		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new_ranking_data;
		close(OUT);
	}
#（ver.1.21到這裡）

	&unlock;
	&message("做了數據修正。","itiran","admin.cgi");
	&kensaku;
}

sub deletUsr {
	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}
	if($in{'command'} eq "del_kakunin"){
			&header;
			print <<"EOM";
			<br><br><div align=center>刪掉$in{'name'}君。好嗎？
			<form method="POST" action="$this_script">
			<input type=hidden name=mode value="deletUsr">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name="k_id" value="$in{'k_id'}">
			<input type=hidden name=admin_pass value="$in{'admin_pass'}">
			<input type=submit value="O K">
			</form>
			<a href=\"javascript:history.back()\"> [返回前畫面] </a>
			</div>
			</body></html>
EOM
			exit;
	}	#確認畫面的情況閉上
	
	&lock;			#ver.1.3鎖位置變更
#家刪掉處理
					&ie_sakujo_syori ($in{'name'});
#取得文件夾內的文件名刪掉。個人文件夾的刪掉
					use DirHandle;
					$dir = new DirHandle ("./member/"."$in{'k_id'}");
					while($file_name = $dir->read){ #讀入1個$folder_name代入
							unlink ("./member/$in{'k_id'}/$file_name");
					}
					$dir->close;  #閉上目錄
					rmdir("./member/$in{'k_id'}") || &error("member目錄內、$in{'k_id'}目錄的數據不能刪掉");
#從成員名單刪掉
	open(IN,"$logfile") || &error("Open Error : $logfile");
	@rankingMember = <IN>;
		foreach (@rankingMember) {
			&list_sprit($_);
			if ($in{'k_id'} eq "$list_k_id"){next;}
			push @alldata,$_;
		}
		
#個人資料&結婚幫助所刪掉處理		ver.1.3
	&prof_sakujo($in{'name'});		#ver.1.3
	&as_prof_sakujo($in{'name'});		#ver.1.3
	
#（ver.1.21從這裡）
	if ($mem_lock_num == 0){
		$err = data_save($logfile, @alldata);
		if ($err) {&error("$err");}
	}else{
		open(OUT,">$logfile") || &error("$logfile不能打開");
		print OUT @alldata;
		close(OUT);
	}
#（ver.1.21到這裡）
	open(PROO,">$profile_file") || &error("$profile_file不能寫上");
	print PROO @new_pro_alldata;
	close(PROO);
	
	open(ASPO,">$as_profile_file") || &error("$as_profile_file不能寫上");
	print ASPO @as_new_pro_alldata;
	close(ASPO);
	&unlock;

	&message("$in{'name'}君被刪掉了。","itiran","admin.cgi");
}

#數據復活
sub hukkatu {
					&lock;
#ver.1.2從這裡
#沒有使之復活的ID的文件夾的情況作成
					$hukkatu_folder = "./member/$in{'k_id'}";
					if (! -e "$hukkatu_folder"){
						mkdir($hukkatu_folder, 0755) || &error("Error : can not Make Directry");
							if ($zidouseisei == 1){
								chmod 0777,"$hukkatu_folder";
							}elsif ($zidouseisei == 2){
								chmod 0755,"$hukkatu_folder";
							}else{
								chmod 0755,"$hukkatu_folder";
							}
					}
#ver.1.2到這裡
#取得附有了文件夾內的backup_的文件名復活備份數據
					use DirHandle;
					$back_folder_pass = "./member/"."$in{'k_id'}"."backup";		#ver.1.2
					$dir = new DirHandle ("$back_folder_pass");		#ver.1.2
					while($file_name = $dir->read){ #讀入1個$folder_name代入
							if($file_name =~ /^backup_/){
								open (BK,"$back_folder_pass/$file_name")  || &error("Open Error : ./member/$in{'k_id'}/$file_name");		#ver.1.2
								@back_data = <BK>;
								if ($file_name eq "backup_log.cgi"){@back_logdata = @back_data;}
								close (BK);
								$orig_file_name = substr ($file_name,7);
								open (BKO,">./member/$in{'k_id'}/$orig_file_name");
								print BKO @back_data;
								close (BKO);
							}
					}
					$dir->close;  #閉上目錄
					@check_log = data_read($logfile);
					$list_aru_flag = 0;
					foreach (@check_log){
						&list_sprit($_);
						if($list_k_id eq "$in{'k_id'}"){$list_aru_flag = 1;last;}
					}
#（ver.1.40從這裡）
					if ($list_aru_flag == 0){
						push (@check_log,@back_logdata);
						if ($mem_lock_num == 0){
							$err = data_save($logfile, @check_log);
							if ($err) {&error("$err");}
						}else{
							open(CKO,">$logfile") || &error("Write Error : $logfile");
							print CKO @check_log;
							close(CKO);
						}
					}
#（ver.1.40到這裡）
					&unlock;
					&message("轉換了為最後保存了的數據。","itiran","admin.cgi");
}

#管理者權限的批發商品更新			#ver.1.2
sub ad_orosi_kousin {
	&lock;
#打開商品數據記錄
			open(OL,"./dat_dir/syouhin.dat") || &error("Open Error : ./dat_dir/syouhin.dat");
			$top_koumoku = <OL>;
#商品排列更新記錄
	@new_syouhin_hairetu = ();
	srand ($$ | time);

	while (<OL>){
			my $r = rand @new_syouhin_hairetu+1;
			push (@new_syouhin_hairetu,$new_syouhin_hairetu[$r]);
			$new_syouhin_hairetu[$r] = $_;
	}
		close(OL);
	$i=0;
				foreach (@new_syouhin_hairetu){
					&syouhin_sprit($_);
					if ($syo_syubetu eq "食"){next;}
					$syo_zaiko = int ($syo_zaiko * $ton_zaiko_tyousei); 
					&syouhin_temp;
					push (@new_syouhin_hairetu2,$syo_temp);
					$i ++;
					if ($i >= $orosi_sinakazu){last;}
				}
	
#類別分類
				foreach (@new_syouhin_hairetu2){
						$data=$_;
						$key=(split(/<>/,$data))[0];
						push @alldata,$data;
						push @keys,$key;
				}
				sub by_syu_keys{$keys[$a] cmp $keys[$b];}
				@alldata=@alldata[ sort by_syu_keys 0..$#alldata]; 
	
	open(OLOUT,">$orosi_logfile") || &error("$orosi_logfile不能寫入");
	print OLOUT @alldata;
	close(OLOUT);
	
#更新日變更時
open(IN,"$maintown_logfile") || &error("Open Error : $maintown_logfile");
	$maintown_para = <IN>;
	&main_town_sprit($maintown_para);
close(IN);
			&time_get;
#把批發標誌做為1更新主要town記錄
			$mt_orosiflag = 1;
			$mt_yobi9 = $date2;		#記錄批發更新日的時候
			&main_town_temp;
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			print OUT $mt_temp;
			close(OUT);	

	&unlock;
	&message("更新了批發商品。","admin","admin.cgi");
}

#個人資料刪掉子程序		ver.1.3
sub prof_sakujo {
	open(PRO,"$profile_file") || &error("Open Error : $profile_file");
	my @pro_alldata=<PRO>;
	close(PRO);
	@new_pro_alldata = ();
	foreach (@pro_alldata){
my ($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
			if (@_[0] eq "$pro_name"){next;} 
			push (@new_pro_alldata,$_);
	}
#記錄更新
	open(PROO,">$profile_file") || &error("$profile_file不能寫上");
	print PROO @new_pro_alldata;
	close(PROO);
}

sub  as_prof_sakujo {		#ver.1.3
	open(ASP,"$as_profile_file") || &error("Open Error : $as_profile_file");
	my @as_pro_alldata=<ASP>;
	close(ASP);
	@as_new_pro_alldata = ();
	foreach (@as_pro_alldata){
my ($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
			if (@_[0] eq "$pro_name"){next;} 
			push (@as_new_pro_alldata,$_);
	}
#記錄更新
	open(ASPO,">$as_profile_file") || &error("$as_profile_file不能寫上");
	print ASPO @as_new_pro_alldata;
	close(ASPO);
}

####BBS1設定
sub bbs1_settei {
#管理者作成BBS的情況
	if ($in{'mode'} eq "admin_bbs"){
			$my_directry = "./member/admin";
			if (! -d $my_directry){
						mkdir($my_directry, 0755) || &error("Error : can not Make Directry");
					if ($zidouseisei == 1){
						chmod 0777,"$my_directry";
					}elsif ($zidouseisei == 2){
						chmod 0755,"$my_directry";
					}else{
						chmod 0755,"$my_directry";
					}
			}
			$bbs1_settei_file="$my_directry/bbs".$in{'bbs_num'}."_ini.cgi";
			if (! -e $bbs1_settei_file){
				open(OIB,">$bbs1_settei_file") || &error("Write Error : $bbs1_settei_file");
				chmod 0666,"$bbs1_settei_file";
				close(OIB);
			}
			$bbs1_log_file="$my_directry/bbs".$in{'bbs_num'}."_log.cgi";
			if (! -e $bbs1_log_file){
				open(OIL,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
				chmod 0666,"$bbs1_log_file";
				close(OIL);
			}
	}else{
			$my_directry = "./member/$in{'iesettei_id'}";
			$bbs1_settei_file="$my_directry/bbs1_ini.cgi";
			if (! -e $bbs1_settei_file){
				open(OIB,">$bbs1_settei_file") || &error("Write Error : $bbs1_settei_file");
				chmod 0666,"$bbs1_settei_file";
				close(OIB);
			}
			$bbs1_log_file="$my_directry/bbs1_log.cgi";
			if (! -e $bbs1_log_file){
				open(OIL,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
				chmod 0666,"$bbs1_log_file";
				close(OIL);
			}
	}
		open(OIB,"$bbs1_settei_file") || &error("Open Error : $bbs1_settei_file");
			$bbs1_settei_data = <OIB>;
			($bbs1_title,$bbs1_come,$bbs1_body_style,$bbs1_toukousya_style,$bbs1_table2_style,$bbs1_toukouwidth,$bbs1_a_hover_style,$bbs1_tablewidth,$bbs1_title_style,$bbs1_leed_style,$bbs1_siasenbako,$bbs1_yobi5,$bbs1_yobi6,$bbs1_yobi7,$bbs1_yobi8,$bbs1_yobi9,$bbs1_yobi10)= split(/<>/,$bbs1_settei_data);
#bbs1_yobi5 = 記事號碼的風格　bbs1_yobi6＝同樣的街的居民專用留言板　bbs1_yobi7＝input的風格
		close(OIB);
		
#風格的初始化
	if ($bbs1_body_style eq ""){$bbs1_body_style = "background-color:#ffcc66;";}
	if ($bbs1_title_style eq ""){$bbs1_title_style = "font-size: 16px; color: #666666;line-height:180%; text-align:center;";}
	if ($bbs1_leed_style eq ""){$bbs1_leed_style = "font-size: 11px; line-height: 16px; color: #336699";}
	if ($bbs1_yobi5 eq ""){$bbs1_yobi5 = "font-size: 15px; color: #336699";}
	if ($bbs1_toukousya_style eq ""){$bbs1_toukousya_style = "font-size: 11px; color: #ff6600";}
	if ($bbs1_table2_style eq ""){$bbs1_table2_style = "font-size: 11px; line-height: 16px; color: #666666; background-color:#ffffcc; border: #336699; border-style: dotted; border-width:4px";}
	if ($bbs1_toukouwidth eq ""){$bbs1_toukouwidth = "50";}
	if ($bbs1_a_hover_style eq ""){$bbs1_a_hover_style = " color:#333333;text-decoration: none";}
	if ($bbs1_tablewidth eq ""){$bbs1_tablewidth = "500";}
	if ($bbs1_siasenbako eq ""){$bbs1_siasenbako = "font-size:11px;color:#000000";}
	if ($bbs1_yobi7 eq ""){$bbs1_yobi7 = "font-size:11px;color:#000000";}
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="bbs1_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=admin_pass value="$in{'admin_pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
EOM
	if ($in{'mode'} eq "admin_bbs"){
	print "<input type=hidden name=bbs_num value=\"$in{'bbs_num'}\">\n";
	print "<input type=hidden name=command value=\"admin_bbs\">\n";
	}
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
EOM
	if ($in{'mode'} eq "admin_bbs"){
		print "<div class=tyuu>■$admin_bbs_syurui[$in{'bbs_num'}]的留言板設定</div>";
	}else{
		print "<div class=tyuu>■通常的留言板設定</div>";
	}
	print <<"EOM";
	●留言板的標題(可指定HTML標記。也可指定絕對URL的畫像)<br>
	<textarea  cols=80 rows=4 name="標題" wrap="soft">$bbs1_title</textarea><br>
	●標題下的評語<br>
	<input type=text name="評語" size=120  value=$bbs1_come><br>
	●背景的風格設定<br>
	<input type=text name="bbs1_body_style" size=120 value="$bbs1_body_style"><br>
	●標題的風格設定<br>
	<input type=text name="bbs1_title_style" size=120 value="$bbs1_title_style"><br>
	●標題下的評語的風格設定<br>
	<input type=text name="bbs1_leed_style" size=120 value="$bbs1_leed_style"><br>
	●記事號碼的風格設定<br>
	<input type=text name="bbs1_yobi5" size=120 value="$bbs1_yobi5"><br>
	●留言者名的風格設定<br>
	<input type=text name="bbs1_toukousya_style" size=120 value="$bbs1_toukousya_style"><br>
	●留言板內的基本風格設定<br>
	<input type=text name="bbs1_table2_style" size=120 value="$bbs1_table2_style"><br>
	●留言欄的尺寸(半角字符數指定)<br>
	<input type=text name="bbs1_toukouwidth" size=120 value="$bbs1_toukouwidth"><br>
	●鏈接(a HTML標記)的風格設定<br>
	<input type=text name="bbs1_a_hover_style" size=120 value="$bbs1_a_hover_style"><br>
	●表的寬度<br>
	<input type=text name="bbs1_tablewidth" size=120 value="$bbs1_tablewidth"><br>
	●input和select的風格設定<br>
	<input type=text name="bbs1_siasenbako" size=120 value="$bbs1_siasenbako"><br>
	●回帖部分的風格設定<br>
	<input type=text name="bbs1_yobi7" size=120 value="$bbs1_yobi7"><br>
EOM
	if ($in{'mode'} eq "admin_bbs"){
		print <<"EOM";
	●同樣的街的居民專用留言板(只住在設置了這個留言板的街的人能閱覽·寫入)<br>
	<select name="bbs1_yobi6">
	<option value="">通常</option>
EOM
	if ($bbs1_yobi6 eq "on"){
		print "<option value=\"on\" selected>同樣的街的居民專用</option>";
	}else{
		print "<option value=\"on\">同樣的街的居民專用</option>"
	}
	print "</select><br><br>";
	}
	
	print "<input type=submit value=設定變更>";

		if ($in{'mode'} eq "admin_bbs"){
		print <<"EOM";
	<a href="original_house.cgi?mode=normal_bbs&ori_ie_id=admin&bbs_num=$in{'bbs_num'}&name=$in{'name'}&admin_pass=$in{'admin_pass'}&con_sele=0" target=_blank>[現在的設定內容的確認]</a>
	</td></tr></table>
	</form>
EOM
		}else{
		print <<"EOM";
	<a href="original_house.cgi?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=0" target=_blank>[現在的設定內容的確認]</a>
	</td></tr></table>
	</form>
EOM
		}
}

sub bbs1_settei_do {
#管理者作成BBS的情況
	if ($in{'command'} eq "admin_bbs"){
		$bbs1_settei_file="./member/admin/bbs".$in{'bbs_num'}."_ini.cgi";
	}else{
		$bbs1_settei_file="./member/$in{'iesettei_id'}/bbs1_ini.cgi";
	}
		open(OIB,"$bbs1_settei_file") || &error("Open Error : $bbs1_settei_file");
			$bbs1_settei_data = <OIB>;
			($bbs1_title,$bbs1_come,$bbs1_body_style,$bbs1_toukousya_style,$bbs1_table2_style,$bbs1_toukouwidth,$bbs1_a_hover_style,$bbs1_tablewidth,$bbs1_title_style,$bbs1_leed_style,$bbs1_siasenbako,$bbs1_yobi5,$bbs1_yobi6,$bbs1_yobi7,$bbs1_yobi8,$bbs1_yobi9,$bbs1_yobi10)= split(/<>/,$bbs1_settei_data);
		close(OIB);
		
		&lock;
			$bbs1_title = $in{'標題'};
			$bbs1_come = $in{'評語'};
			$bbs1_body_style = $in{'bbs1_body_style'};
			$bbs1_toukousya_style = $in{'bbs1_toukousya_style'};
			$bbs1_table2_style = $in{'bbs1_table2_style'};
			$bbs1_toukouwidth = $in{'bbs1_toukouwidth'};
			$bbs1_a_hover_style = $in{'bbs1_a_hover_style'};
			$bbs1_tablewidth = $in{'bbs1_tablewidth'};
			$bbs1_title_style = $in{'bbs1_title_style'};
			$bbs1_leed_style = $in{'bbs1_leed_style'};
			$bbs1_siasenbako = $in{'bbs1_siasenbako'};
			$bbs1_yobi5 = $in{'bbs1_yobi5'};
			$bbs1_yobi6 = $in{'bbs1_yobi6'};
			$bbs1_yobi7 = $in{'bbs1_yobi7'};
			$bbs1_yobi8 = $in{'bbs1_yobi8'};
			$bbs1_yobi9 = $in{'bbs1_yobi9'};
			$bbs1_yobi10 = $in{'bbs1_yobi10'};
		$bbs_settei_temp = "$bbs1_title<>$bbs1_come<>$bbs1_body_style<>$bbs1_toukousya_style<>$bbs1_table2_style<>$bbs1_toukouwidth<>$bbs1_a_hover_style<>$bbs1_tablewidth<>$bbs1_title_style<>$bbs1_leed_style<>$bbs1_siasenbako<>$bbs1_yobi5<>$bbs1_yobi6<>$bbs1_yobi7<>$bbs1_yobi8<>$bbs1_yobi9<>$bbs1_yobi10<>\n";
	open(OLOUT,">$bbs1_settei_file") || &error("$bbs1_settei_file不能寫入");
	print OLOUT $bbs_settei_temp;
	close(OLOUT);
		&unlock;
		if ($in{'command'} eq "admin_bbs"){
			&header;
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>變更了設定。</td></tr></table><br>
	
	<form method=POST action="$this_script">
	<input type=hidden name=mode value="admin_bbs">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=admin_pass value=$in{'admin_pass'}>
	<input type=hidden name=bbs_num value=$in{'bbs_num'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form></div>
EOM
	exit;
		}else{
			&my_house_settei;
		}
}

#######排列次序表示
sub yakuba {
	&lock;			#ver.1.3鎖位置變更
	$now_time= time;		#ver.1.40
	if($in{'sortid'}){$sortid = $in{'sortid'};}else{$sortid = 5;}
	open(IN,"$logfile") || &error("Open Error : $logfile");
	@rankingMember = <IN>;
		foreach (@rankingMember) {
			&list_sprit($_);
#放置用戶刪掉處理
			if($list_last_syokuzi < $now_time - (60*60*24*$deleteUser)){ 		#ver.1.40
#家刪掉處理
					&ie_sakujo_syori ($list_name);
#ver.1.3從這裡
#個人資料&婚姻介紹所刪掉處理
					&prof_sakujo ($list_name);
					&as_prof_sakujo($list_name);
#取得文件夾內的文件名刪掉。個人文件夾的刪掉
					$sakujo_folder_id = "./member/$list_k_id";
					if (-e "$sakujo_folder_id") {
						use DirHandle;
						$dir = new DirHandle ("./member/"."$list_k_id");
						while($file_name = $dir->read){ #讀入1個$folder_name代入
								unlink ("./member/$list_k_id/$file_name");
						}
						$dir->close;  #閉上目錄
						rmdir("./member/$list_k_id") || &error("ID識別號$list_k_id的$list_name君的數據不能刪掉");
					}
					&news_kiroku("遷居","$list_name君離開了街。");
#ver.1.3到這裡
					next;
			}
			$data=$_;
			$key=(split(/<>/,$data))[$in{'sortid'}];		#選排序的要素
			push @alldata,$data;
			push @keys,$key;
		}
	close(IN);
#（ver.1.21從這裡）
	if ($mem_lock_num == 0){
		$err = data_save($logfile, @alldata);
		if ($err) {&error("$err");}
	}else{
		open(OUT,">$logfile") || &error("$logfile不能打開");
		print OUT @alldata;
		close(OUT);
	}
#（ver.1.21到這裡）
	&unlock;
	
		sub bykeys{$keys[$b] <=> $keys[$a];}
		@alldata=@alldata[ sort bykeys 0..$#alldata]; 

	&header(yakuba_style);		#ver.1.30
	print <<"EOM";
	<table width="98%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>能看社區新遷入者和各種排列次序。<br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="yakuba">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<select name="sortid">
<!--ver.1.3-->
	<option value="">最近的街的新聞$news_kensuu件</option>
EOM
	print "<option value=23";
	if ($sortid == 23){print " selected";}
	print ">最近的遷入者$rankMax人</option>";
	
		print "<option value=49";
	if ($sortid == 49){print " selected";}
	print ">富翁順序前$rankMax名</option>";
@global_nouryokuti = ("國語","數學","理科","社會","英語","音樂","美術","容貌","體力","健康","速度","力","腕力","脚力","LOVE","有趣","淫蕩");
	$i=6;
	foreach (@global_nouryokuti) {
		print "<option value=$i";
		if ($sortid == $i){print " selected";}
		print ">$_順序前$rankMax名</option>";
		$i ++;	
	}
	print <<"EOM";
	</select> <input type=submit value="OK"></form></td>
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/yakuba_tytle.gif"></td>
	</tr></table><br>
<!--ver.1.3從這裡-->
EOM
	if($in{'sortid'} eq ""){
#街新聞表示
				open(NS,"$news_file") || &error("$news_file不能打開。");
				@town_news = <NS>;
				close(NS);
					print <<"EOM";
					<table width="98%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
					<tr bgcolor=#eeeecc><td>
					<div class=honbun4>◎最近的街的新聞$news_kensuu件</div>
EOM
				foreach (@town_news){
					my ($hiduke,$nw_syubetu,$nw_kizi)= split(/<>/);
					if ($nw_syubetu eq "戀人"){$news_style = "color:#ff3366;"; $news_kigou = "&#9829;";}
					elsif ($nw_syubetu eq "結婚"){$news_style = "color:#ff3300;"; $news_kigou = "&#9829;";}
					elsif ($nw_syubetu eq "遷入"){$news_style = "color:#3366cc;"; $news_kigou = "◆";}
					elsif ($nw_syubetu eq "生孩子"){$news_style = "color:#009900;"; $news_kigou = "●";}
					elsif ($nw_syubetu eq "就業"){$news_style = "color:#009900;"; $news_kigou = "◎";}
					elsif ($nw_syubetu eq "分手"){$news_style = "color:#666666;"; $news_kigou = "&#9829;";}
					elsif ($nw_syubetu eq "死亡"){$news_style = "color:#666666;"; $news_kigou = "■";}
					elsif ($nw_syubetu eq "遷居"){$news_style = "color:#666666;"; $news_kigou = "▲";}
					elsif ($nw_syubetu eq "家"){$news_style = "color:#990000;"; $news_kigou = "●";}
					print <<"EOM";
					<div style="color:#666666; line-height:180%;">$hiduke<span style="$news_style"> $news_kigou$nw_kizi</span></div>
EOM
				}
				print "</td></tr></table><br><br>";
	}else{
	print <<"EOM";
<!--ver.1.3到這裡-->
	<table width="98%" border="0" cellspacing="1" cellpadding="3" align=center class=yosumi>
	<tr><td colspan=23>
	※「保存數據」不更新數據這個排列次序不被反映。<br>
	※富翁順序表，以所持金 + 活期存款寄存額 + 超級定期寄存額 - 貸款額決定。</td></tr>
	<tr  class=jouge bgcolor=#ffff66 align=center><td>順位</td><td>名　字</td><td>性別</td><td>職　業</td><td>資　産</td><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td>家</td></tr>
EOM

#unithash代入個人的家信息
	open(OI,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
	@ori_ie_hairetu = <OI>;
	foreach (@ori_ie_hairetu) {
			&ori_ie_sprit($_);
			$unit{"$ori_k_id"} = "<form method=POST action=\"original_house.cgi\"><input type=hidden name=mode value=houmon><input type=hidden name=ori_ie_id value=$ori_k_id><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$ori_ie_image\"></form>";		#ver.1.40
	}
	close(OI);
$i=1;
	foreach (@alldata) {
		&list_sprit($_);
		if ($list_sex eq "f") {$seibetu = "女";}else{$seibetu = "男";}
		print <<"EOM";
		<tr class=sita><td align=center>$i</td><td nowrap>$list_name</td><td align=center>$seibetu</td><td>$list_job</td><td align=right nowrap>$list_sousisan元</td><td align=right>$list_kokugo</td><td align=right nowrap>$list_suugaku</td><td align=right nowrap>$list_rika</td><td align=right nowrap>$list_syakai</td><td align=right nowrap>$list_eigo</td><td align=right nowrap>$list_ongaku</td><td align=right nowrap>$list_bijutu</td><td align=right nowrap>$list_looks</td><td align=right nowrap>$list_tairyoku</td><td align=right nowrap>$list_kenkou</td><td align=right nowrap>$list_speed</td><td align=right nowrap>$list_power</td><td align=right nowrap>$list_wanryoku</td><td align=right nowrap>$list_kyakuryoku</td><td align=right nowrap>$list_love</td><td align=right nowrap>$list_unique</td><td align=right nowrap>$list_etti</td><td align=center valign=center>$unit{"$list_k_id"}</td></tr>
EOM
				if($i >=$rankMax){last;}
			$i++;
	}
	print "</table>";
	}		#ver.1.3
	&hooter("login_view","返回");
	exit;
}	#子程序閉上
