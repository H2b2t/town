#!/perl/bin/perl
# ↑使用合乎服務器的路徑。

$this_script = 'original_house.cgi';
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
	if($in{'mode'} eq "my_house_settei"){&my_house_settei;}
	elsif($in{'mode'} eq "my_house_settei_do"){&my_house_settei_do;}
	elsif($in{'mode'} eq "houmon"){&houmon;}
	elsif($in{'mode'} eq "bbs1_settei_do"){&bbs1_settei_do;}
	elsif($in{'mode'} eq "omise_settei_do"){&omise_settei_do;}
	elsif($in{'mode'} eq "dokuzi_settei_do"){&dokuzi_settei_do;}
	elsif($in{'mode'} eq "gentei_settei_do"){&gentei_settei_do;}
	elsif($in{'mode'} eq "bbs_regist"){&bbs_regist;}
	elsif($in{'mode'} eq "gentei_delete"){&gentei_delete;}
	elsif($in{'mode'} eq "bbs_delete"){&bbs_delete;}
	elsif($in{'mode'} eq "gentei_regist"){&gentei_regist;}
	elsif($in{'mode'} eq "saisensuru"){&saisensuru;}
	elsif($in{'mode'} eq "comment_change"){&comment_change;}
	elsif($in{'mode'} eq "normal_bbs"){&normal_bbs;}
	elsif($in{'mode'} eq "house_change"){&house_change;}
	elsif($in{'mode'} eq "my_syouhin"){&my_syouhin;}
	else{&error("請用「返回」按鈕返回街");}
exit;
	
#############以下子程序

####自己的家的設定
sub my_house_settei {		#ver.1.3
	open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		@ori_ie_para = <IN>;
	close(IN);
		$oriie_atta=0;
		foreach (@ori_ie_para){
				&ori_ie_sprit($_);
				if ($in{'iesettei_id'} eq "$ori_k_id"){
					$oriie_atta=1;
					last;
				}
		}
	if ($oriie_atta == 0){&error("家沒找到。");}
	$my_directry = "./member/$in{'iesettei_id'}";
	$oriie_settei_file="$my_directry/oriie_settei.cgi";
#如果沒有家設定文件則作成
	if (! -e $oriie_settei_file){
		open(OIS,">$oriie_settei_file") || &error("Write Error : $oriie_settei_file");
		chmod 0666,"$oriie_settei_file";
		close(OIS);
	}
		open(OIS,"$oriie_settei_file") || &error("Open Error : $oriie_settei_file");
			$kihon_oriie_settei = <OIS>;
			&oriie_settei_sprit ($kihon_oriie_settei);
		close(OIS);
	
	&header(kentiku_style);
	if ($in{'iesettei_id'} eq "$k_id"){$settei_title = "自己的家設定"; $settei_t_color = "#336699";}
	else{$settei_title = "配偶的家設定"; $settei_t_color = "#ff6666";}
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr bgcolor=$settei_t_color><td align=center style="color:#ffffff;font-size:13px;">$settei_title</td></tr></table><br>
EOM
	if ($my_con1 eq "0"){&bbs1_settei;}elsif ($my_con1 eq "1"){&omise_settei;}elsif ($my_con1 eq "2"){&dokuzi_settei;}elsif ($my_con1 eq "3"){&gentei_settei;}
	if ($my_con2 eq "0"){&bbs1_settei;}elsif ($my_con2 eq "1"){&omise_settei;}elsif ($my_con2 eq "2"){&dokuzi_settei;}elsif ($my_con2 eq "3"){&gentei_settei;}	
	if ($my_con3 eq "0"){&bbs1_settei;}elsif ($my_con3 eq "1"){&omise_settei;}elsif ($my_con3 eq "2"){&dokuzi_settei;}elsif ($my_con3 eq "3"){&gentei_settei;}	
	if ($my_con4 eq "0"){&bbs1_settei;}elsif ($my_con4 eq "1"){&omise_settei;}elsif ($my_con4 eq "2"){&dokuzi_settei;}elsif ($my_con4 eq "3"){&gentei_settei;}
	
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="comment_change">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<div class=tyuu>■基本設定</div>
	●在街上鼠標指著了家的時候被表示的評語(40字以內)<br>
	<input type=text name="ori_ie_setumei" size=80 value=$ori_ie_setumei><input type=submit value="OK"></form><hr size=1>
	
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="my_house_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	●請選擇內容（※設置內容。選擇之後能變更內容。相關的標題在頁內表示）<br>
EOM
	if ($ori_ie_rank != 3){print "這裡最頂的是進入家的時候最初被表示的內容。<br>";}

		if ($ori_ie_rank == 0){$i=4;}elsif($ori_ie_rank == 1){$i=3;}elsif($ori_ie_rank == 2){$i=2;}elsif($ori_ie_rank == 3){$i=1;}
		
		$selectcount = 0;
		$titlecount = 4;
		foreach (1..$i){
		if ($ori_ie_rank != 3){print "<div class=honbun2>○$_空間的內容</div>";}
		print <<"EOM";
		<select name="內容$_">
		<option value="">不公開</option>
EOM
		print "<option value=0";
		if ($oriie_settei_sprit[$selectcount] eq "0"){print " selected";}
		print ">通常的留言板</option>\n";
		print "<option value=1";
		if ($oriie_settei_sprit[$selectcount] eq "1"){print " selected";}
		print ">店</option>\n";
		print "<option value=2";
		if ($oriie_settei_sprit[$selectcount] eq "2"){print " selected";}
		print ">獨自URL</option>\n";
		print "<option value=3";
		if ($oriie_settei_sprit[$selectcount] eq "3"){print " selected";}
		print ">只戶主能寫的留言板</option>\n";
		print "</select>\n";

		if ($ori_ie_rank != 3) {print "標題 <input type=text name=\"標題$_\" value=\"$oriie_settei_sprit[$titlecount]\">";}
		$selectcount ++;
		$titlecount ++;
		}
		print <<"EOM";
		<input type=submit value=OK>
	</form>
	<hr size=1>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	●家的外觀，內部裝修(空間內容)的變更<br>
	能改變家的外觀，升級內部裝修。<br>
	<input type=submit value=" 選擇畫面 "></form>
	<hr size=1>
EOM
	if ($in{'iesettei_id'} eq "$k_id"){
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change">
	<input type=hidden name=command value="baikyaku">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	●家的出售<br>
	想變更家的地方的情況，賣掉一次家之後再次購買。出售只能得到土地的價格。現在的空間內容被保持到重新購買的家。<br>
	<input type=submit value=" 家的出售 "></form>
		
		<div align=center><a href="javascript:history.back()"> [返回前畫面] </a></div>
		</td></tr></table>
EOM
	}else{
		print "※不能出售配偶的家。";
	}
		&hooter("login_view","返回");
	exit;
}

###評語變更
sub comment_change {
	if (length($in{'ori_ie_setumei'}) > 80) {&error("評語是40字以內");}
	if ($in{'ori_ie_setumei'} =~ /'/) {&error("半角的「'」不能使用。");}		#ver.1.3
	&lock;
	open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		@ori_ie_para = <IN>;
	close(IN);
		foreach (@ori_ie_para){
			&ori_ie_sprit($_);
			if ($in{'iesettei_id'} eq $ori_k_id){
				$ori_ie_setumei = $in{'ori_ie_setumei'};
			}
			&ori_ie_temp;
			push (@new_ori_ie_para,$ori_ie_temp);
		}
		
	open(OLOUT,">$ori_ie_list") || &error("$ori_ie_list不能寫入");
	print OLOUT @new_ori_ie_para;
	close(OLOUT);
	&unlock;
	&message("變更了家的評語。","my_house_settei","original_house.cgi");
}


###自己的家的設定處理
sub my_house_settei_do {
	$my_directry = "./member/$in{'iesettei_id'}";
	$oriie_settei_file="$my_directry/oriie_settei.cgi";
		open(OIS,"$oriie_settei_file") || &error("Open Error : $oriie_settei_file");
			$kihon_oriie_settei = <OIS>;
			&oriie_settei_sprit ($kihon_oriie_settei);
		close(OIS);
		
		$my_con1 = $in{'內容1'};
		$my_con2 = $in{'內容2'};
		$my_con3 = $in{'內容3'};
		$my_con4 = $in{'內容4'};
		$my_con1_title = $in{'標題1'};
		$my_con2_title = $in{'標題2'};
		$my_con3_title = $in{'標題3'};
		$my_con4_title = $in{'標題4'};
		$my_yobi5 = $in{'my_yobi5'};
		$my_yobi6 = $in{'my_yobi6'};
		$my_yobi7 = $in{'my_yobi7'};
		&oriie_settei_temp;
	&lock;
	open(OLOUT,">$oriie_settei_file") || &error("$oriie_settei_file不能寫入");
	print OLOUT $ori_ie_settei_temp;
	close(OLOUT);
	&unlock;
	&my_house_settei;
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
#bbs1_yobi5 = 記錄號碼的風格 bbs1_yobi6=同樣的街的居民專用留言板 bbs1_yobi7=input的風格
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
	●留言板的標題（可指定HTML標記。可指定絕對URL畫像）<br>
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
	●留言者名稱的風格設定<br>
	<input type=text name="bbs1_toukousya_style" size=120 value="$bbs1_toukousya_style"><br>
	●留言板內的基本風格設定<br>
	<input type=text name="bbs1_table2_style" size=120 value="$bbs1_table2_style"><br>
	●留言欄的以尺寸（半角字符數指定）<br>
	<input type=text name="bbs1_toukouwidth" size=120 value="$bbs1_toukouwidth"><br>
	●連結(a HTML標記)的風格設定<br>
	<input type=text name="bbs1_a_hover_style" size=120 value="$bbs1_a_hover_style"><br>
	●TABLE 的寬度<br>
	<input type=text name="bbs1_tablewidth" size=120 value="$bbs1_tablewidth"><br>
	●input和select的風格設定<br>
	<input type=text name="bbs1_siasenbako" size=120 value="$bbs1_siasenbako"><br>
	●回帖部分的風格設定<br>
	<input type=text name="bbs1_yobi7" size=120 value="$bbs1_yobi7"><br>
EOM
	if ($in{'mode'} eq "admin_bbs"){
		print <<"EOM";
	●同樣的街的居民專用的留言板（只住在設置了這個公告牌的街的人能閱覽・寫入）<br>
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
	<a href="$this_script?mode=normal_bbs&ori_ie_id=admin&bbs_num=$in{'bbs_num'}&name=$in{'name'}&admin_pass=$in{'admin_pass'}&con_sele=0" target=_blank>[現在的設定內容的確認]</a>
	</td></tr></table>
	</form>
EOM
		}else{
		print <<"EOM";
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=0" target=_blank>[現在的設定內容的確認]</a>
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
	
	<form method=POST action="$script">
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

####戶主留言板的設定
sub gentei_settei {
	$my_directry = "./member/$in{'iesettei_id'}";
	$gentei_settei_file="$my_directry/gentei_ini.cgi";
	if (! -e $gentei_settei_file){
		open(OIB,">$gentei_settei_file") || &error("Write Error : $gentei_settei_file");
		chmod 0666,"$gentei_settei_file";
		close(OIB);
	}
	$gentei_log_file="$my_directry/gentei_log.cgi";
	if (! -e $gentei_log_file){
		open(OIL,">$gentei_log_file") || &error("Write Error : $gentei_log_file");
		chmod 0666,"$gentei_log_file";
		close(OIL);
	}
		open(OIB,"$gentei_settei_file") || &error("Open Error : $gentei_settei_file");
			$gentei_settei_data = <OIB>;
			($gentei_title,$gentei_come,$gentei_body_style,$gentei_daimei_style,$gentei_table2_style,$gentei_kensuu,$gentei_tablewidth,$gentei_title_style,$gentei_leed_style,$gentei_siasenbako,$gentei_yobi5,$gentei_yobi6,$gentei_yobi7,$gentei_yobi8,$gentei_yobi9,$gentei_yobi10)= split(/<>/,$gentei_settei_data);
		close(OIB);
		
#風格的初始化
	if ($gentei_body_style eq ""){$gentei_body_style = "background-color:#99cc99;";}
	if ($gentei_title_style eq ""){$gentei_title_style = "font-size: 20px; color: #339966;line-height:150%; text-align:center;";}
	if ($gentei_leed_style eq ""){$gentei_leed_style = "font-size: 11px; color: #ff6600;line-height:160%;";}
	if ($gentei_daimei_style eq ""){$gentei_daimei_style = "font-size: 14px; color: #445555;line-height:200%;";}
	if ($gentei_table2_style eq ""){$gentei_table2_style = "font-size: 11px; line-height: 16px; color: #666666; background-color:#ffffcc; border: #339966; border-style: dotted; border-width:4px;";}
	if ($gentei_kensuu eq ""){$gentei_kensuu = "5";}
	if ($gentei_tablewidth eq ""){$gentei_tablewidth = "520";}
	if ($gentei_siasenbako eq ""){$gentei_siasenbako = "font-size:11px;color:#000000";}
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="gentei_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<div class=tyuu>■戶主留言板的設定</div>
	●留言板的標題（可指定 HTML標記。也可指定絕對URL的畫像）<br>
	<textarea  cols=80 rows=4 name="標題" wrap="soft">$gentei_title</textarea><br>
	●標題下的評語<br>
	<input type=text name="評語" size=120  value=$gentei_come><br>
	●背景的風格設定<br>
	<input type=text name="gentei_body_style" size=120 value="$gentei_body_style"><br>
	●留言板標題的風格設定<br>
	<input type=text name="gentei_title_style" size=120 value="$gentei_title_style"><br>
	●標題下的評語的風格設定<br>
	<input type=text name="gentei_leed_style" size=120 value="$gentei_leed_style"><br>
	●記事的題名的風格設定<br>
	<input type=text name="gentei_daimei_style" size=120 value="$gentei_daimei_style"><br>
	●留言板內的基本風格設定<br>
	<input type=text name="gentei_table2_style" size=120 value="$gentei_table2_style"><br>
	●在１頁裡表面示做的以記事件數（半角字符數指定）<br>
	<input type=text name="gentei_kensuu" size=120 value="$gentei_kensuu"><br>
	●TABLE的寬度<br>
	<input type=text name="gentei_tablewidth" size=120 value="$gentei_tablewidth"><br>
	●input和select的風格設定<br>
	<input type=text name="gentei_siasenbako" size=120 value="$gentei_siasenbako"><br>
	<input type=submit value=設定變更>
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=3" target=_blank>[現在的設定內容的確認]</a>
	</form>
	
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="gentei_regist">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}><br><br>
	<div class=tyuu>■留言（HTML標記可）</div>
	標題<br>
	<input type=text name="b_title" size=80><br>
	内容<br>
	<textarea  cols=90 rows=7 name="b_com" wrap="soft"></textarea><br>
	<input type=submit value="留言">
	</form>
	</td></tr></table>
	
EOM
}

sub gentei_settei_do {
	$gentei_settei_file="./member/$in{'iesettei_id'}/gentei_ini.cgi";
		open(OIB,"$gentei_settei_file") || &error("Open Error : $gentei_settei_file");
			$gentei_settei_data = <OIB>;
			($gentei_title,$gentei_come,$gentei_body_style,$gentei_daimei_style,$gentei_table2_style,$gentei_kensuu,$gentei_tablewidth,$gentei_title_style,$gentei_leed_style,$gentei_siasenbako,$gentei_yobi5,$gentei_yobi6,$gentei_yobi7,$gentei_yobi8,$gentei_yobi9,$gentei_yobi10)= split(/<>/,$gentei_settei_data);
		close(OIB);
		
		&lock;
			$gentei_title = $in{'標題'};
			$gentei_come = $in{'評語'};
			$gentei_body_style = $in{'gentei_body_style'};
			$gentei_daimei_style = $in{'gentei_daimei_style'};
			$gentei_table2_style = $in{'gentei_table2_style'};
			$gentei_kensuu = $in{'gentei_kensuu'};
			$gentei_tablewidth = $in{'gentei_tablewidth'};
			$gentei_title_style = $in{'gentei_title_style'};
			$gentei_leed_style = $in{'gentei_leed_style'};
			$gentei_siasenbako = $in{'gentei_siasenbako'};
			$gentei_yobi5 = $in{'gentei_yobi5'};
			$gentei_yobi6 = $in{'gentei_yobi6'};
			$gentei_yobi7 = $in{'gentei_yobi7'};
			$gentei_yobi8 = $in{'gentei_yobi8'};
			$gentei_yobi9 = $in{'gentei_yobi9'};
			$gentei_yobi10 = $in{'gentei_yobi10'};
		$gentei_settei_temp = "$gentei_title<>$gentei_come<>$gentei_body_style<>$gentei_daimei_style<>$gentei_table2_style<>$gentei_kensuu<>$gentei_tablewidth<>$gentei_title_style<>$gentei_leed_style<>$gentei_siasenbako<>$gentei_yobi5<>$gentei_yobi6<>$gentei_yobi7<>$gentei_yobi8<>$gentei_yobi9<>$gentei_yobi10<>\n";
	open(OLOUT,">$gentei_settei_file") || &error("$gentei_settei_file不能寫入");
	print OLOUT $gentei_settei_temp;
	close(OLOUT);
		&unlock;
		&my_house_settei;
}


####店的設定
sub omise_settei {
	$my_directry = "./member/$in{'iesettei_id'}";
	$omise_settei_file="$my_directry/omise_ini.cgi";
	if (! -e $omise_settei_file){
		open(OIB,">$omise_settei_file") || &error("Write Error : $omise_settei_file");
		chmod 0666,"$omise_settei_file";
		close(OIB);
	}
	$omise_log_file="$my_directry/omise_log.cgi";
	if (! -e $omise_log_file){
		open(OIL,">$omise_log_file") || &error("Write Error : $omise_log_file");
		chmod 0666,"$omise_log_file";
		close(OIL);
	}
		open(OIB,"$omise_settei_file") || &error("Open Error : $omise_settei_file");
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
#omise_yobi5=基本售價 omise_yobi6=商品類別的風格設定 omise_yobi7=連結的風格
		close(OIB);
		
#風格的初始化
	if ($omise_yobi5 eq ""){$omise_yobi5 = "2";}
	if ($omise_body_style eq ""){$omise_body_style = "background-color:#ffcc33;";}
	if ($omise_title_style eq ""){$omise_title_style = "font-size: 18px; color: #ff6600; line-height:160%;";}
	if ($omise_leed_style eq ""){$omise_leed_style = "font-size: 11px; line-height: 16px; color: #000000";}
	if ($omise_table1_style eq ""){$omise_table1_style = "font-size: 11px; line-height: 18px; color: #666666; background-color:#ffffff; border: #666666; border-style: solid; border-width:1px";}
	if ($omise_table2_style eq ""){$omise_table2_style = "font-size: 10px; color: #336699; background-color:#ffffff; border: #666666; border-style: solid; border-width:1px";}
	if ($omise_syouhin_table eq ""){$omise_syouhin_table = "font-size: 11px; color: #333333; background-color:#ffffaa; ";}
	if ($omise_koumokumei eq ""){$omise_koumokumei = "font-size: 11px; color: #000000; background-color:#ffcc66; ";}
	if ($omise_yobi6 eq ""){$omise_yobi6 = "background-color:#ffff88;";}
	if ($omise_yobi7 eq ""){$omise_yobi7 = "font-size: 11px; color:#333333;text-decoration: none";}
	if ($omise_siasenbako eq ""){$omise_siasenbako = "font-size:11px;color:#000000";}
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="omise_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<div class=tyuu>■店的設定</div>
	●店的標題（可指定HTML標記。也可指定絕對URL的畫像）<br>
	<textarea  cols=80 rows=4 name="標題" wrap="soft">$omise_title</textarea><br>
	●店的種類（超市能處理全部的商品，不過進貨額為表示價格的1.5倍。同時，請注意如果過一會改變了店的種類，現在購入了的商品會全部丟失。）<br>
	<select name="omise_syubetu">
EOM
	foreach (@global_syouhin_syubetu){
		print "<option value=$_";
		if ($omise_syubetu eq "$_"){print " selected";}
		print ">$_</option>\n";
	}
	print <<"EOM";
	</select>
	<br>
	●店的評語<br>
	<textarea  cols=80 rows=3 name="評語" wrap="soft">$omise_come</textarea><br>
	●基本賣價倍率（在百貨商店購入的是以價值的3倍的金額賣。不能比這個價格貴地設定。也能用商品名單個別設定）<br>
	<input type=text name="omise_yobi5" size=120  value=$omise_yobi5><br>
	●背景的風格設定<br>
	<input type=text name="omise_body_style" size=120 value="$omise_body_style"><br>
	●標題的風格設定br>
	<input type=text name="omise_title_style" size=120 value="$omise_title_style"><br>
	●評語的風格設定<br>
	<input type=text name="omise_leed_style" size=120 value="$omise_leed_style"><br>
	●標題部 TABLE 的風格設定<br>
	<input type=text name="omise_table1_style" size=120 value="$omise_table1_style"><br>
	●商品名單TABLE的框框及凡例的風格設定<br>
	<input type=text name="omise_table2_style" size=120 value="$omise_table2_style"><br>
	●商品名單 TABLE 內風格設定<br>
	<input type=text name="omise_syouhin_table" size=120 value="$omise_syouhin_table"><br>
	●商品名單的項目名部分的風格設定<br>
	<input type=text name="omise_koumokumei" size=120 value="$omise_koumokumei"><br>
	●商品類別部分的風格設定<br>
	<input type=text name="omise_yobi6" size=120 value="$omise_yobi6"><br>
	●input和select的風格設定<br>
	<input type=text name="omise_siasenbako" size=120 value="$omise_siasenbako"><br>
	●a標記的風格設定<br>
	<input type=text name="omise_yobi7" size=120 value="$omise_yobi7"><br>
	<input type=submit value=設定變更>
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=1" target=_blank>[現在的設定內容的確認]</a><br><br>
	</form>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="my_syouhin">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="購入了的商品的名單">
	</form>
	<form method=POST action=\"$script\">
	<input type=hidden name=mode value=orosi>
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="出去進貨">（去街的批發商）</form></td></tr></table>
EOM
}

sub omise_settei_do {
	$omise_settei_file="./member/$in{'iesettei_id'}/omise_ini.cgi";
		open(OIB,"$omise_settei_file") || &error("Open Error : $omise_settei_file");
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
		close(OIB);
		
		&lock;
			$change_syubetu_flag = "";
			$omise_title = $in{'標題'};
			$omise_come = $in{'評語'};
			if ($omise_syubetu ne $in{'omise_syubetu'}){$change_syubetu_flag = "on";}
			$omise_syubetu = $in{'omise_syubetu'};
			$omise_body_style = $in{'omise_body_style'};
			$omise_table1_style = $in{'omise_table1_style'};
			$omise_table2_style = $in{'omise_table2_style'};
			$omise_koumokumei = $in{'omise_koumokumei'};
			$omise_syouhin_table = $in{'omise_syouhin_table'};
			$omise_title_style = $in{'omise_title_style'};
			$omise_leed_style = $in{'omise_leed_style'};
			$omise_siasenbako = $in{'omise_siasenbako'};
			if ($in{'omise_yobi5'} > 3){&error("賣價要在3倍以下");}
			if ($in{'omise_yobi5'} <= 0){&error("賣價不妥。");}			#ver.1.3
			$omise_yobi5 = $in{'omise_yobi5'};
			$omise_yobi6 = $in{'omise_yobi6'};
			$omise_yobi7 = $in{'omise_yobi7'};
			$omise_yobi8 = $in{'omise_yobi8'};
			$omise_yobi9 = $in{'omise_yobi9'};
			$omise_yobi10 = $in{'omise_yobi10'};
		$omise_settei_temp = "$omise_title<>$omise_come<>$omise_body_style<>$omise_syubetu<>$omise_table1_style<>$omise_table2_style<>$omise_koumokumei<>$omise_syouhin_table<>$omise_title_style<>$omise_leed_style<>$omise_siasenbako<>$omise_yobi5<>$omise_yobi6<>$omise_yobi7<>$omise_yobi8<>$omise_yobi9<>$omise_yobi10<>\n";
	open(OLOUT,">$omise_settei_file") || &error("$omise_settei_file不能寫入");
	print OLOUT $omise_settei_temp;
	close(OLOUT);
#要是店的種類變更初始化商品名單
		if ($change_syubetu_flag eq "on"){
			$i = ""; 
			$omise_log_file="./member/$in{'iesettei_id'}/omise_log.cgi";
			open(SP,">$omise_log_file") || &error("Open Error : $omise_log_file");
			print SP $i;
			close(SP);
		}
		&unlock;
		&my_house_settei;
}


####獨自URL的設定
sub dokuzi_settei {
	$my_directry = "./member/$in{'iesettei_id'}";
	$dokuzi_settei_file="$my_directry/dokuzi_ini.cgi";
	if (! -e $dokuzi_settei_file){
		open(OIB,">$dokuzi_settei_file") || &error("Write Error : $dokuzi_settei_file");
		chmod 0666,"$dokuzi_settei_file";
		close(OIB);
	}
		open(OIB,"$dokuzi_settei_file") || &error("Open Error : $dokuzi_settei_file");
			$dokuzi_settei_data = <OIB>;
			($dokuzi_url,$dokuzi_width,$dokuzi_height,$dokuzi_haikei_style,$dokuzi_title,$dokuzi_come,$dokuzi_title_style,$dokuzi_leed_style,$dokuzi_siasenbako,$dokuzi_yobi10)= split(/<>/,$dokuzi_settei_data);
		close(OIB);
		
#風格的初始化
	if ($dokuzi_haikei_style eq ""){$dokuzi_haikei_style = "background-color:#ffffff;";}
	if ($dokuzi_title_style eq ""){$dokuzi_title_style = "font-size: 16px; color: #666666;line-height:160%;";}
	if ($dokuzi_leed_style eq ""){$dokuzi_leed_style = "font-size: 11px; line-height: 16px; color: #336699";}
	if ($dokuzi_width eq ""){$dokuzi_width = "800";}
	if ($dokuzi_height eq ""){$dokuzi_height = "400";}
	if ($dokuzi_siasenbako eq ""){$dokuzi_siasenbako = "font-size:11px;color:#000000";}
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="dokuzi_settei_do">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td>
	<div class=tyuu>■獨自URL的設定</div>
	●角標題（可指定HTML標記指定。可指定絕對URL畫像。即使不指定也可。）<br>
	<textarea  cols=80 rows=4 name="標題" wrap="soft">$dokuzi_title</textarea><br>
	●URL指定<br>
	<input type=text name="dokuzi_url" size=120 value="$dokuzi_url"><br>
	●標題下的評語<br>
	<input type=text name="評語" size=120  value=$dokuzi_come><br>
	●背景的風格設定<br>
	<input type=text name="dokuzi_haikei_style" size=120 value="$dokuzi_haikei_style"><br>
	●標題的風格設定br>
	<input type=text name="dokuzi_title_style" size=120 value="$dokuzi_title_style"><br>
	●標題下的評語的風格設定<br>
	<input type=text name="dokuzi_leed_style" size=120 value="$dokuzi_leed_style"><br>
	●IFRAME的橫尺寸<br>
	<input type=text name="dokuzi_width" size=120 value="$dokuzi_width"><br>
	●IFRAME的縱尺寸<br>
	<input type=text name="dokuzi_height" size=120 value="$dokuzi_height"><br>
	●錢箱的風格設定<br>
	<input type=text name="dokuzi_siasenbako" size=120 value="$dokuzi_siasenbako"><br>
	
	<input type=submit value=設定變更>
	<a href="$this_script?mode=houmon&ori_ie_id=$in{'iesettei_id'}&name=$in{'name'}&pass=$in{'pass'}&con_sele=2" target=_blank>[現在的設定內容的確認]</a>
	</td></tr></table>
	</form>
EOM
}

sub dokuzi_settei_do {
	$dokuzi_settei_file="./member/$in{'iesettei_id'}/dokuzi_ini.cgi";
		open(OIB,"$dokuzi_settei_file") || &error("Open Error : $dokuzi_settei_file");
			$dokuzi_settei_data = <OIB>;
			($dokuzi_url,$dokuzi_width,$dokuzi_height,$dokuzi_haikei_style,$dokuzi_title,$dokuzi_come,$dokuzi_title_style,$dokuzi_leed_style,$dokuzi_siasenbako,$dokuzi_yobi10)= split(/<>/,$dokuzi_settei_data);
		close(OIB);
		
		&lock;
			$dokuzi_title = $in{'標題'};
			$dokuzi_come = $in{'評語'};
			$dokuzi_url = $in{'dokuzi_url'};
			$dokuzi_haikei_style = $in{'dokuzi_haikei_style'};
			$dokuzi_title_style = $in{'dokuzi_title_style'};
			$dokuzi_leed_style = $in{'dokuzi_leed_style'};
			$dokuzi_width = $in{'dokuzi_width'};
			$dokuzi_height = $in{'dokuzi_height'};
			$dokuzi_siasenbako = $in{'dokuzi_siasenbako'};
			$dokuzi_yobi10 = $in{'dokuzi_yobi10'};
		$dokuzi_settei_temp = "$dokuzi_url<>$dokuzi_width<>$dokuzi_height<>$dokuzi_haikei_style<>$dokuzi_title<>$dokuzi_come<>$dokuzi_title_style<>$dokuzi_leed_style<>$dokuzi_siasenbako<>$dokuzi_yobi10<>\n";
	open(OLOUT,">$dokuzi_settei_file") || &error("$dokuzi_settei_file不能寫入");
	print OLOUT $dokuzi_settei_temp;
	close(OLOUT);
		&unlock;
		&my_house_settei;
}

#######家的變更
sub house_change{
#出售的情況
	if ($in{'command'} eq "baikyaku"){
	&lock;
#家名單的寫入
	open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		@ori_ie_para = <IN>;
	close(IN);
		foreach (@ori_ie_para){
				&ori_ie_sprit($_);
				if ($name eq "$ori_ie_name"){
#town信息另寫用取得信息
						$my_town_is = $ori_ie_town;
						$my_point_is = $ori_ie_sentaku_point;
						next;
				}
				&ori_ie_temp;
				push (@new_ori_ie_list,$ori_ie_temp);
		}

#在town信息裡寫入
	$write_town_data = "./log_dir/townlog". $my_town_is .".cgi";
	open(TWI,"$write_town_data") || &error("Open Error : $write_town_data");
	$hyouzi_town_hairetu = <TWI>;
	close(TWI);
		@town_sprit_matrix =  split(/<>/,$hyouzi_town_hairetu);
		$town_sprit_matrix[$my_point_is] = "空地";
		$town_temp=join("<>",@town_sprit_matrix);
#town信息更新
	open(TWO,">$write_town_data") || &error("$write_town_data不能寫上");
	print TWO $town_temp;
	close(TWO);

#家名單更新
	open(OIO,">$ori_ie_list") || &error("$ori_ie_list不能寫上");
	print OIO @new_ori_ie_list;
	close(OIO);

#新聞記錄
	&news_kiroku("家","$name君於「$town_hairetu[$my_town_is]」的家賣掉了。");		#ver.1.3
	
	&unlock;
#記錄更新
	if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
		$money += $town_tika_hairetu[$my_town_is] * 10000;
	}
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			
&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
賣掉了家。
</span>
</td></tr></table>
<br>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form></div>

	</body></html>
EOM
exit;
	}
#變更處理
	if ($in{'command'} eq "do_change"){
		if ($in{'matirank'} eq ""){&error("沒有選擇家的排位");}
		$kensetu_hiyou = ($ie_hash{$in{'iegazou'}} + $housu_nedan[$in{'matirank'}])*10000;
		if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
			if ($kensetu_hiyou > $money){&error("錢不夠。");}
		}
	&lock;
#家名單的寫入
	open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		@ori_ie_para = <IN>;
	close(IN);
		foreach (@ori_ie_para){
				&ori_ie_sprit($_);
				if ($in{'iesettei_id'} eq $ori_k_id){		#ver.1.3
					if ($in{'iegazou'} ne ""){
						$ori_ie_image = "$img_dir/$in{'iegazou'}";
					}
					if ($in{'matirank'} ne "99"){
						$ori_ie_rank = $in{'matirank'};
					}
				}
				&ori_ie_temp;
				push (@new_ori_ie_list,$ori_ie_temp);
		}
#家名單更新
	open(OIO,">$ori_ie_list") || &error("$ori_ie_list不能寫上");
	print OIO @new_ori_ie_list;
	close(OIO);

	&unlock;
#記錄更新
	if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
		$money -= $kensetu_hiyou;
	}
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			
&header;
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
做了家的變更。
</span>
</td></tr></table>
<br>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form></div>

	</body></html>
EOM
exit;
	}		#變更處理的情況閉上
	
#從hash展開家畫像
	&header(kentiku_style);
	while(($ie_key,$ie_val) = each %ie_hash){
			push @ie_keys,$ie_key;
			push @ie_values,$ie_val;
	}
		sub by_iekey{$ie_values[$a] <=> $ie_values[$b];}
		@ie_rank=@ie_keys[ sort by_iekey 0..$#ie_keys]; 
	$i=1;
	foreach(@ie_rank){
		$iegazou .= "<td align=center><input type=radio name=iegazou value=$_><br><img src=\"$img_dir/$_\" width=32 height=32><br>$ie_hash{$_}萬元\n";
		if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
		$i ++;
	}
		$iegazou .= "<td align=center><input type=radio name=iegazou value=\"\"><br>維持現狀\n";
		if ($i % 12 == 0){$iegazou .= "</tr><tr>";}
			print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>外觀，內部裝修的變更，和建築時是同等的金額花費。</td>
	</tr></table><br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="house_change">
	<input type=hidden name=command value="do_change">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td valign=top>
	<div class=honbun2>●家的選擇</div>
	<table boader=0 cellspacing="0" cellpadding="5" width=100%><tr>
	$iegazou
	</tr></table><br>
	
	<table boader=0 cellspacing="0" cellpadding="5" width=100%><tr>
	<td><div class=honbun2>●家的排位(內部裝修費)</div><br>
	<input type=radio name=matirank value="0">Ａ排位：$housu_nedan[0]萬元（可以同時擁有４個空間）<br>
	<input type=radio name=matirank value="1">Ｂ排位：$housu_nedan[1]萬元（可以同時擁有３個空間）<br>
	<input type=radio name=matirank value="2">Ｃ排位：$housu_nedan[2]萬元（可以同時擁有２個空間）<br>
	<input type=radio name=matirank value="3">Ｄ排位：$housu_nedan[3]萬元（可以同時擁有１個空間）<br>
	<input type=radio name=matirank value="99">維持現狀
	</td></tr></table>
EOM

	print <<"EOM";
	<br><br><div align=center><input type=submit value=" OK  "></div>
	</td></tr></table>
	<div align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
	</body></html>
EOM
	exit;
}

#####訪問處理
sub houmon {
	$houmonsaki_settei_file = "./member/$in{'ori_ie_id'}/oriie_settei.cgi";
	open(HS,"$houmonsaki_settei_file") || &error("工程中");
	$kihon_oriie_settei = <HS>;
	&oriie_settei_sprit ($kihon_oriie_settei);
	close(HS);
	if ($my_con1 eq ""){&error("沒有人出現的家。");}		#ver.1.30
	
#錢箱子算入變量之內
$saisenbako_data =<<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="saisensuru">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<select name=saisengaku>
	<option value=10>10元</option>
	<option value=50>50元</option>
	<option value=100>100元</option>
	<option value=200>200元</option>
	<option value=500>500元</option>
	<option value=1000>1000元</option>
	</select>
	<input type=submit value="捐錢">
	</form>
EOM

	if ($my_con1_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=houmon><input type=hidden name=ori_ie_id value=$in{'ori_ie_id'}><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=con_sele value=$my_con1><input type=hidden name=town_no value=$in{'town_no'}><input type=submit value=$my_con1_title></form></td>";
	}
	
	if ($my_con2_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=houmon><input type=hidden name=ori_ie_id value=$in{'ori_ie_id'}><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=con_sele value=$my_con2><input type=hidden name=town_no value=$in{'town_no'}><input type=submit value=$my_con2_title></form></td>";
	}
	
	if ($my_con3_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=houmon><input type=hidden name=ori_ie_id value=$in{'ori_ie_id'}><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=con_sele value=$my_con3><input type=hidden name=town_no value=$in{'town_no'}><input type=submit value=$my_con3_title></form></td>";
	}
	
	if ($my_con4_title){
		$centents_botan .="<td><form method=POST action=\"$this_script\"><input type=hidden name=mode value=houmon><input type=hidden name=ori_ie_id value=$in{'ori_ie_id'}><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=con_sele value=$my_con4><input type=hidden name=town_no value=$in{'town_no'}><input type=submit value=$my_con4_title></form></td>";
	}
	
	if ($in{'con_sele'} eq ""){
		if ($my_con1 eq "0"){&normal_bbs;}
		elsif  ($my_con1 eq "1"){&omise;}
		elsif  ($my_con1 eq "2"){&dokuzi_url;}
		elsif  ($my_con1 eq "3"){&gentei;}
	}elsif  ($in{'con_sele'} eq "0"){&normal_bbs;}
	elsif  ($in{'con_sele'} eq "1"){&omise;}
	elsif  ($in{'con_sele'} eq "2"){&dokuzi_url;}
	elsif  ($in{'con_sele'} eq "3"){&gentei;}
}

#####通常的BBS
sub normal_bbs {
	if ($tajuukinsi_flag==1){
		if($k_yobi3 ne ""){
			&error("多重登記被禁止。<br>$k_yobi3");
		}
	}
	if ($tajuukinsi_flag==1){&tajuucheck;}
#ver.1.30從這裡
	$genzai_zikoku = time;
	open(GUEST,"$guestfile");
	@all_guest=<GUEST>;
	close(GUEST);
	@new_all_guest = ();
	foreach (@all_guest) {
		($sanka_timer,$sanka_name,$hyouzi_check) = split(/<>/);
		if ($name eq "$sanka_name"){
			$sanka_timer = $genzai_zikoku;
		}
		$sanka_tmp = "$sanka_timer<>$sanka_name<>$hyouzi_check<>\n";
		push (@new_all_guest,$sanka_tmp);
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
#ver.1.30到這裡
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_settei_file = "./member/admin/bbs".$in{'bbs_num'}."_ini.cgi";
	}else{
		$bbs1_settei_file = "./member/$in{'ori_ie_id'}/bbs1_ini.cgi";
	}
		open(OIB,"$bbs1_settei_file") || &error("Open Error : $bbs1_settei_file");
			$bbs1_settei_data = <OIB>;
			($bbs1_title,$bbs1_come,$bbs1_body_style,$bbs1_toukousya_style,$bbs1_table2_style,$bbs1_toukouwidth,$bbs1_a_hover_style,$bbs1_tablewidth,$bbs1_title_style,$bbs1_leed_style,$bbs1_siasenbako,$bbs1_yobi5,$bbs1_yobi6,$bbs1_yobi7,$bbs1_yobi8,$bbs1_yobi9,$bbs1_yobi10)= split(/<>/,$bbs1_settei_data);
		close(OIB);
#居民專用留言板的情況檢查
	if ($bbs1_yobi6 eq "on"){
		if ($in{'admin_pass'} ne $admin_pass){
			&my_town_check($name);
			if ($return_my_town eq "no_town"){&error("住這街以外的人不能看");}
			if ($return_my_town ne "$in{'town_no'}"){&error("住這街以外的人不能看");}
		}
	}
	&ori_header("$bbs1_body_style","$bbs1_siasenbako","$bbs1_a_hover_style");

	print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM

	print <<"EOM";
	<br><table width="$bbs1_tablewidth" border="0" cellspacing="0" cellpadding="14" align=center style="$bbs1_table2_style">
	<tr><td>
	<div style = "$bbs1_title_style">$bbs1_title</div>
	<div style = "$bbs1_leed_style">$bbs1_come</div>
	</td></tr>
	<td>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="bbs_regist">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=job value="$job">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<textarea cols="$bbs1_toukouwidth" rows="4" name="b_com" wrap="soft"></textarea>
	<input type=submit value="新留言">
	</form>
EOM
	$page=$in{'page'};	
	if ($page eq "") { $page = 0; }
	$i=0;
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_log_file = "./member/admin/bbs".$in{'bbs_num'}."_log.cgi";
	}else{
		$bbs1_log_file = "./member/$in{'ori_ie_id'}/bbs1_log.cgi";
	}
	open(IN,"$bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	@bbs_alldata=<IN>;
	close(IN);
	foreach (@bbs_alldata){
		($b_num,$b_name,$b_date,$b_res,$b_mail,$b_com)= split(/<>/);
		if ($b_num){$i++;}
		if ($i == 1){next;}
		if ($i < $page + 1) { next; }
		if ($i > $page + 10) { last; }
		if ($b_res){
	print "<div><span style=\"$bbs1_toukousya_style\">$b_name</span>：$b_com（$b_date）<span style=\"font-size:9px\">記事no.$b_mail</span></div>\n";		#ver.1.40
		}else{
				print <<"EOM";
	<br><hr size=1><br>
	<div><span style=\"$bbs1_yobi5\">NO.$b_num</span><br> <span style=\"$bbs1_toukousya_style\">$b_name</span>：$b_com（$b_date）<span style=\"font-size:9px\">記事no.$b_mail</span><!--ver.1.40-->
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="bbs_regist">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=job value="$job">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=b_res value="$b_num">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=text size="$bbs1_toukouwidth" name=b_com style="$bbs1_yobi7"> <input type=submit value="回帖">
	</form></div>
EOM
		}
	}		#foreach閉上
	
		$next = $page + 10;
		$back = $page - 10;
		print "<div align=center><table border=0><tr>";
		if ($back >= 0) {
#管理者BBS的情況
				if($in{'ori_ie_id'} eq "admin"){
					print <<"EOM";
			<form method=POST action=\"$this_script\">
			<input type=hidden name=mode value=normal_bbs>
			<input type=hidden name=ori_ie_id value=admin>
			<input type=hidden name=bbs_num value=$in{'bbs_num'}>
			<input type=hidden name=name value=$in{'name'}>
			<input type=hidden name=pass value=$in{'pass'}>
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=page value="$back">
			<input type=submit value="BACK">
			</form>
EOM
				}else{
#是個人的家的BBS的情況
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="houmon">
			<input type=hidden name=con_sele value="0">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
			<input type=hidden name=page value="$back">
			<input type=submit value="BACK"></form></td>
EOM
				}
		}
		if ($next < $i) {
				if($in{'ori_ie_id'} eq "admin"){
					print <<"EOM";
			<form method=POST action=\"$this_script\">
			<input type=hidden name=mode value=normal_bbs>
			<input type=hidden name=ori_ie_id value=admin>
			<input type=hidden name=bbs_num value=$in{'bbs_num'}>
			<input type=hidden name=name value=$in{'name'}>
			<input type=hidden name=pass value=$in{'pass'}>
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=page value="$next">
			<input type=submit value="NEXT">
</form>
EOM
				}else{
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="houmon">
			<input type=hidden name=con_sele value="0">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
			<input type=hidden name=page value="$next">
			<input type=submit value="NEXT"></form></td>
EOM
				}
		}
		print "</tr></table></div>";
	print <<"EOM";
	</td></tr></table>
	<table width="$bbs1_tablewidth" border="0" cellspacing="0" cellpadding="0" align=center>
	<tr><td>
	<form method="POST" action="$this_script">
	<div style=" font-size: 10px; color: #444444"><br>
	<center>
	<input type=hidden name=mode value="bbs_delete">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	記事no. <input type=text name=b_count size=8>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="刪掉">
	</center>
	<br>※遊戲管理者能指定「記事no.」刪掉記事。<br>
	※留言能得到錢，不過無意義的發言，灌水行為等不合適的留言，會被減少金，HOST公開，訪問拒絕等處理。</div>
	</form></td></tr><tr><td>
	<br><div style=" font-size: 11px;" align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
	</td></tr>
	</table>
EOM
	if ($in{'ori_ie_id'} eq "admin"){
		&hooter("login_view","返回");
	}else{
		&hooter("login_view","從家離開");
	}
exit;
}


#BBS留言處理
sub bbs_regist {
	&lock;
#log file更新
	# 讀入記錄
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_log_file = "./member/admin/bbs".$in{'bbs_num'}."_log.cgi";
	}else{
		$bbs1_log_file = "./member/$in{'ori_ie_id'}/bbs1_log.cgi";
	}
	open(IN,"$bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	# 取得頭行
	$total_counter = <IN>;
	($total_counter,$all_total_counter)= split(/<>/, $total_counter);		#ver.1.40
	$top = <IN>;
	local($b_num,$b_name,$b_date,$b_res,$b_count,$b_com)= split(/<>/, $top);		#ver.1.40
	close(IN);
	
	$in{'b_com'} =~ s/<>/&lt;&gt;/g;

#HTML標記禁止處理
#		$in{'b_com'} =~ s/</&lt;/g;
#		$in{'b_com'} =~ s/>/&gt;/g;
# 評語的換行處理
	$in{'b_com'} =~ s/\r\n/<br>/g;
	$in{'b_com'} =~ s/\r/<br>/g;
	$in{'b_com'} =~ s/\n/<br>/g;
		$in{'b_com'} =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
#ver.1.30從這裡
	$name_seikei = $in{'name'} . "<span style=\"font-size:9px\">（$in{'job'}）</span>";
	if ($name_seikei eq "$b_name" && $in{'b_com'} eq "$b_com") {
		&error("是重複留言");
	}
#ver.1.30到這裡
	if ($in{'b_com'} eq "") {
		&error("未輸入評語");
	}

	open(IN,"$bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	@all_data = <IN>;
	shift @all_data;
	$total_kizisuu = @all_data;
	close(IN);
	
	&time_get;
	$all_total_counter ++;		#計算總數記事數ver.1.40
#要是新留言取得新記事No
	if ($in{'b_res'} eq ""){
		$total_counter++;
#定義更新陣列
	$new_toukou = "$total_counter<>$in{'name'}<span style=\"font-size:9px\">（$in{'job'}）</span><>$date2<>$in{'b_res'}<>$all_total_counter<>$in{'b_com'}<>\n";		#ver.1.40

	unshift (@all_data,$new_toukou);
	$total_counter = "$total_counter<>$all_total_counter<>\n";		#ver.1.40
	unshift (@all_data,$total_counter);
	
#回帖的情況
	}else{
#定義更新陣列
			$new_toukou = "<>$in{'name'}<span style=\"font-size:9px\">（$in{'job'}）</span><>$date2<>$in{'b_res'}<>$all_total_counter<>$in{'b_com'}<>\n";		#ver.1.40
		foreach (@all_data){
			($b_num,$b_name,$b_date,$b_res,$b_mail,$b_com)= split(/<>/, $_);
			if ($b_num eq "$in{'b_res'}" || $b_res eq "$in{'b_res'}"){push (@top_idou ,$_);	next;}
			push (@new_all_data,$_);
		}
		push (@top_idou ,$new_toukou);	
		unshift (@new_all_data,@top_idou);
		$total_counter = "$total_counter<>$all_total_counter<>\n";		#ver.1.40
		unshift (@new_all_data,$total_counter);
		@all_data = ();
		@all_data = @new_all_data;
	}		#回帖的情況閉上
	
	if ($total_kizisuu >= $bbs_kizi_max){pop @all_data;}
# 更新記錄
	open(OUT,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
	print OUT @all_data;
	close(OUT);
	
#街的繁榮度提高
	&town_haneiup($in{'town_no'});

# 鎖解除
	&unlock;
	
#取得錢
	$randed += int(rand(10))+1;
	if ($randed == 7){
		$randed += int(rand(1000))+500;
		$money += $randed;
		$message_in = "●是獎金！取得$randed元。";
	}else{
		$randed += int(rand(200))+100;
		$money += $randed;
		$message_in = "●得到了$randed元。";
	}
	&temp_routin;
	&log_kousin($my_log_file,$k_temp);
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
$message_in
</span>
</td></tr></table>
<br>
	<form method=POST action="$this_script">
EOM
	if ($in{'ori_ie_id'} eq "admin"){
		print "<input type=hidden name=mode value=\"normal_bbs\">";
	}else{
		print "<input type=hidden name=mode value=\"houmon\">";
	}

	print <<"EOM";
	<input type=hidden name=con_sele value="0">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form></div>
EOM
	exit;
}

#####戶主留言板
sub gentei {
	$gentei_settei_file = "./member/$in{'ori_ie_id'}/gentei_ini.cgi";
		open(OIB,"$gentei_settei_file") || &error("Open Error : $gentei_settei_file");
			$gentei_settei_data = <OIB>;
			($gentei_title,$gentei_come,$gentei_body_style,$gentei_daimei_style,$gentei_table2_style,$gentei_kensuu,$gentei_tablewidth,$gentei_title_style,$gentei_leed_style,$gentei_siasenbako,$gentei_yobi5,$gentei_yobi6,$gentei_yobi7,$gentei_yobi8,$gentei_yobi9,$gentei_yobi10)= split(/<>/,$gentei_settei_data);
		close(OIB);
	&ori_header("$gentei_body_style","$gentei_siasenbako");

	print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM

	print <<"EOM";
	<table width="$gentei_tablewidth" border="0" cellspacing="0" cellpadding="8" align=center style="$gentei_table2_style">
	<tr><td>
	<div style = "$gentei_title_style">$gentei_title</div>
	<div style = "$gentei_leed_style">$gentei_come</div>
	</td></tr>
	<td>
EOM
	$page=$in{'page'};	
	if ($page eq "") { $page = 0; }
	$i=0;
	$gentei_log_file = "./member/$in{'ori_ie_id'}/gentei_log.cgi";
	open(IN,"$gentei_log_file") || &error("Open Error : $gentei_log_file");
	@bbs_alldata=<IN>;
	foreach (@bbs_alldata){
		($b_num,$b_name,$b_date,$b_title,$b_mail,$b_com)= split(/<>/);
		$i++;
		if ($i < $page + 1) { next; }
		if ($i > $page + $gentei_kensuu) { last; }
				print "<div style=\"$gentei_daimei_style\">$b_title</div><div>$b_com（$b_date）<span style=\"font-size:9px\">記事no.$b_num</span></div><br>\n";		#ver.1.40
	}		#foreach閉上
	close(IN);
	
		$next = $page + $gentei_kensuu;
		$back = $page - $gentei_kensuu;
		print "<div align=center><table border=0><tr>";
		if ($back >= 0) {
			print <<"EOM";
	<td><form method="POST" action="$this_script">
	<input type=hidden name=mode value="houmon">
	<input type=hidden name=con_sele value="3">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=page value="$back">
	<input type=submit value="BACK"></form></td>
EOM
		}
		if ($next < $i) {
			print <<"EOM";
	<td><form method="POST" action="$this_script">
	<input type=hidden name=mode value="houmon">
	<input type=hidden name=con_sele value="3">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=page value="$next">
	<input type=submit value="NEXT"></form></td>
EOM
		}

	print <<"EOM";
	</tr></table></div>
	</td></tr>
	</table>
	<div align=center>
	<form method="POST" action="$this_script">
	<div style=" font-size: 10px; color: #444444"><br>
	<input type=hidden name=mode value="gentei_delete">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	記事no. <input type=text name=b_num size=8>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="削除">
	</form>
	※只有寫了記事的本人和遊戲管理者能指定「記事no.」刪掉記事。<br>
	</div>
EOM
	&hooter("login_view","從家離開");
exit;
}


#戶主留言板留言處理
sub gentei_regist {
	&lock;
#log file更新
	# 讀入記錄
	$gentei_log_file = "./member/$in{'iesettei_id'}/gentei_log.cgi";		#ver.1.3
	open(IN,"$gentei_log_file") || &error("Open Error : $gentei_log_file");
	# 取得頭行
	$top = <IN>;
	local($b_num,$b_name,$b_date,$b_title,$b_mail,$b_com)= split(/<>/, $top);
#HTML標記禁止處理
#		$in{'b_com'} =~ s/</&lt;/g;
#		$in{'b_com'} =~ s/>/&gt;/g;
	if ($in{'name'} eq $b_name && $in{'b_com'} eq $b_com) {
		&error("是重複留言");
	}
	if ($in{'b_com'} eq "") {
		&error("未輸入內容");
	}
	# 取得新記事No
	$b_num++;
	# 定義更新陣列
	&time_get;
	$new[0] = "$b_num<>$in{'name'}<>$date2<>$in{'b_title'}<>$in{'b_mail'}<>$in{'b_com'}<>\n";
	$new[1] = $top;

	while (<IN>) {
		$i++;
		push(@new,$_);
		if ($i >= 50){last;}
	}
	close(IN);

# 更新記錄
	open(OUT,">$gentei_log_file") || &error("Write Error : $gentei_log_file");
	print OUT @new;
	close(OUT);
# 鎖解除
	&unlock;
	&message("留了言。","my_house_settei","original_house.cgi");
}

#####店
sub omise {	
	$omise_log_file = "./member/$in{'ori_ie_id'}/omise_log.cgi";
	open(IN,"$omise_log_file") || &error("Open Error : $omise_log_file");
	@omise_alldata=<IN>;
	close(IN);
#類別分類
				foreach (@omise_alldata){
						$data=$_;
						$key=(split(/<>/,$data))[0];
						push @tinretu_alldata,$data;
						push @keys,$key;
				}
				sub by_syu_keys{$keys[$a] cmp $keys[$b];}
				@tinretu_alldata=@tinretu_alldata[ sort by_syu_keys 0..$#tinretu_alldata]; 
	
	$omise_settei_file = "./member/$in{'ori_ie_id'}/omise_ini.cgi";
		open(OIB,"$omise_settei_file") || &error("Open Error : $omise_settei_file");
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
#omise_yobi5=基本售價 omise_yobi6=商品類別的風格設定 omise_yobi7=連結的風格
		close(OIB);
	&ori_header("$omise_body_style","$omise_siasenbako","$omise_yobi7");
		print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM
	print <<"EOM";
	<form method="POST" action="$script">
	<input type=hidden name=mode value="buy_syouhin">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center style="$omise_table1_style">
	<tr>
	<td  style="$omise_title_style" nowrap>$omise_title</td>
	<td style="$omise_leed_style" width=65%>$omise_come</td>
	</tr></table><br>
	<table width="100%" border="0" cellspacing="1" cellpadding="5" align=center style="$omise_table2_style">
	<tr><td colspan=26>凡例：(國)＝國語up值、(數)＝數學up值、(理)＝理科up值、(社)＝社會up值、(英)＝英語up值、(音)＝音樂up值、(美)＝美術up值、（容）=容貌up值、（體）=體力up值、（健）=健康up值、（速）=速度up值、（力）=力up值、（腕）=腕力up值、（腳）=腳力up值、（愛）=LOVEup值、（趣）=有趣up值、（淫）=淫蕩up值<br>
	※禮物是禮物專用的商品。不能自己使用。
EOM
	if ($kaenai_seigen == 1){		#ver.1.40
		if ($k_id eq "$in{'ori_ie_id'}" || $house_type eq "$in{'ori_ie_id'}"){		#ver.1.3
			print "<br><font color=#ff6600>※不能在自己和配偶的店買商品。</font>";
		}
	}

	print <<"EOM";
	</td></tr>
		<tr style="$omise_koumokumei"><td align=center nowrap>商品</td><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>L</td><td>趣</td><td>淫</td><td align=center nowrap>卡路里</td><td align=center nowrap>耐久</td><td align=center>使用<br>間隔</td><td align=center>身體<br>能量<br>消費</td><td align=center>頭腦<br>能量<br>消費</td><td align=center>價格</td><td align=center nowrap>　備　考　</td><td align=center nowrap>庫存</td></tr>
EOM

	foreach (@tinretu_alldata) {
			&syouhin_sprit($_);
			if($syo_zaiko <= 0){next;}
#如果有獨自價格的設定那個價格
			if ($tokubai){
					$syo_nedan = "$tokubai";
			}else{
				if ($omise_syubetu eq "超市"){
					$syo_nedan = int($syo_nedan *1.5 * $omise_yobi5);
				}else{
					$syo_nedan = int ($syo_nedan * $omise_yobi5);
				}
			}
			if($syo_zaiko <= 0){
					$kounyuubotan ="";
					$syo_zaiko = "賣光";
			}else{
					$kounyuubotan ="<input type=radio value=\"$syo_hinmoku,&,$syo_taikyuu,&,$syo_nedan\" name=\"syo_hinmoku\">";
			}
			if($syo_cal > 0){$calory_hyouzi = "$syo_cal kcal";}else{$calory_hyouzi = "ー";}
			if ($maeno_syo_syubetu ne "$syo_syubetu"){
				print "<tr style=\"$omise_yobi6\"><td colspan=26>▼$syo_syubetu</td></tr>";
			}
			$taikyuu_hyouzi_seikei = "$syo_taikyuu"."$syo_taikyuu_tani";
#ver.1.3從這裡
if ($syo_nedan =~ /^[-+]?\d\d\d\d+/g) {
  for ($i = pos($syo_nedan) - 3, $j = $syo_nedan =~ /^[-+]/; $i > $j; $i -= 3) {
    substr($syo_nedan, $i, 0) = ',';
  }
}
#ver.1.3到這裡
		print <<"EOM";
		<tr style="$omise_syouhin_table" align=center><td nowrap align=left>$kounyuubotan $syo_hinmoku</td><td>$syo_kokugo</td><td>$syo_suugaku</td><td>$syo_rika</td><td>$syo_syakai</td><td>$syo_eigo</td><td>$syo_ongaku</td><td>$syo_bijutu</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td align=right>$calory_hyouzi</td><td nowrap>$taikyuu_hyouzi_seikei</td><td nowrap>$syo_kankaku分</td><td>$syo_sintai_syouhi</td><td>$syo_zunou_syouhi</td><td align=right nowrap>$syo_nedan元</td><td align=left>$syo_comment</td><td align=right>$syo_zaiko</td></tr>
EOM
		$maeno_syo_syubetu = "$syo_syubetu";
	}		#foreach閉上
#ver.1.30從這裡
#所有物檢查
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(MK,"$monokiroku_file") || &error("自己的購買物文件不能打開");
	@my_kounyuu_list =<MK>;
	close(MK);
	foreach (@my_kounyuu_list){
		&syouhin_sprit ($_);
		if ($syo_kouka eq "信用"){
			if ($syo_taikyuu - (int ((time - $syo_kounyuubi) / (60*60*24)))){
				$siharai_houhou .= "<option value=\"$syo_hinmoku\">$syo_hinmoku</option>";
			}
		}
	}
	print <<"EOM";
	<tr><td colspan=26><div align=center>
	支付方法 <select name="siharaihouhou"><option value="現金">現金</option>$siharai_houhou</select>
	<input type=submit value=" O K "></div></td></tr>
	</table></form>
	<div align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
EOM
#ver1.30到這裡
	&hooter("login_view","從家離開");
	exit;
}


#####獨自URL
sub dokuzi_url {
	$dokuzi_settei_file = "./member/$in{'ori_ie_id'}/dokuzi_ini.cgi";
		open(OIB,"$dokuzi_settei_file") || &error("Open Error : $dokuzi_settei_file");
			$dokuzi_settei_data = <OIB>;
			($dokuzi_url,$dokuzi_width,$dokuzi_height,$dokuzi_haikei_style,$dokuzi_title,$dokuzi_come,$dokuzi_title_style,$dokuzi_leed_style,$dokuzi_siasenbako,$dokuzi_yobi10) = split(/<>/,$dokuzi_settei_data);
		close(OIB);
	&ori_header("$dokuzi_haikei_style","$dokuzi_siasenbako");
	print <<"EOM";
	<table  border="0" cellspacing="0" cellpadding="5" align=center >
	<tr>$centents_botan<td align=right>$saisenbako_data</td></tr>
	</table>
EOM
	print <<"EOM";
	<table width="$dokuzi_tablewidth" border="0" cellspacing="0" cellpadding="8" align=center style="$dokuzi_table2_style">
	<tr><td>
	<div style = "$dokuzi_title_style">$dokuzi_title</div>
	<div style = "$dokuzi_leed_style">$dokuzi_come</div>
	</td></tr>
	<tr><td align=center>
	<IFRAME src="$dokuzi_url"  width="$dokuzi_width" height="$dokuzi_height" scrolling=auto marginheight=0 FRAMEBORDER=0></IFRAME>
	</td></tr>
	</table></body></html>
EOM
	&hooter("login_view","從家離開");
exit;
}

###錢箱裡金處理
sub saisensuru {		#ver.1.3
	if ($money < $in{'saisengaku'}){&error("錢不夠。");}
	$money -= $in{'saisengaku'};
#記錄更新
	&lock;	
			&temp_routin;
			open(OUT,">$my_log_file") || &error("$my_log_file不能寫上");
			print OUT $k_temp;
			close(OUT);

	&openAitelog ($in{'ori_ie_id'});
	$aite_bank += $in{'saisengaku'};
	
			&aite_temp_routin;
				open(OUT,">$aite_log_file") || &error("$aite_log_file不能打開");
				print OUT $aite_k_temp;
				close(OUT);
#ver.1.40到這裡
	&aite_kityou_syori("捐錢←$name","",$in{'saisengaku'},$aite_bank,"普",$in{'ori_ie_id'},"lock_off");
	&unlock;
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
	對$aite_name君贈了$in{'saisengaku'}元。
	</td></tr></table>
	<br><br><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
	</body></html>
EOM
exit;
}

##########自己的店的商品名單
sub my_syouhin {
	$omise_log_file="./member/$in{'iesettei_id'}/omise_log.cgi";
	open(SP,"$omise_log_file") || &error("Open Error : $omise_log_file");
	@myitem_hairetu = <SP>;
	close(SP);
#價格變更的情況
	if ($in{'command'} eq "價格設定"){
		if ($in{'syo_nedan'} * 3 < $in{'hanbaikakaku'}){&error("銷售價格要在購入價格的3倍以內。");}
#		if ($in{'syo_nedan'} / 10 > $in{'hanbaikakaku'}){&error("銷售價格要在購入價格的10分之一以上。");}
		if($in{'hanbaikakaku'} =~ /[^0-9]/){&error("銷售價格不妥。");}			#ver.1.3
		foreach  (@myitem_hairetu) {
			&syouhin_sprit($_);
			if ($in{'syo_hinmoku'} eq "$syo_hinmoku"){
					$tokubai = $in{'hanbaikakaku'};
			}
		&syouhin_temp;
		push (@new_myitem_hairetu,$syo_temp);
		}
			&lock;
			open(OUT,">$omise_log_file") || &error("Write Error : $omise_log_file");
			print OUT @new_myitem_hairetu;
			close(OUT);	
			&unlock;
			&message("設定了$in{'syo_hinmoku'}的價格為$in{'hanbaikakaku'}元。","my_syouhin","original_house.cgi");
	}
	
#類別分類
				foreach (@myitem_hairetu){
						$data=$_;
						$key=(split(/<>/,$data))[0];
						push @alldata,$data;
						push @keys,$key;
				}
				sub by_syu_keys{$keys[$a] cmp $keys[$b];}
				@alldata=@alldata[ sort by_syu_keys 0..$#alldata]; 
#從店設定文件取得銷售價格
	$omise_settei_file = "./member/$in{'iesettei_id'}/omise_ini.cgi";
		open(OIB,"$omise_settei_file") || &error("Open Error : $omise_settei_file");
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu,$omise_table1_style,$omise_table2_style,$omise_koumokumei,$omise_syouhin_table,$omise_title_style,$omise_leed_style,$omise_siasenbako,$omise_yobi5,$omise_yobi6,$omise_yobi7,$omise_yobi8,$omise_yobi9,$omise_yobi10)= split(/<>/,$omise_settei_data);
		close(OIB);
		
	&header(omise_list_style);
	print <<"EOM";
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>各商品的銷售價格能個別設定。但不能以進貨價格的３倍以上設定。<br>
	現在的店的種類 = $omise_syubetu</td>
	</tr></table><br>
	
	<table width="100%" border="0" cellspacing="1" cellpadding="5" align=center class=yosumi>
	<tr><td colspan=28><font color=#330033>凡例：(國)＝國語up值、(數)＝數學up值、(理)＝理科up值、(社)＝社會up值、(英)＝英語up值、(音)＝音樂up值、(美)＝美術up值、（容）=容貌up值、（體）=體力up值、（健）=健康up值、（速）=速度up值、（力）=力up值、（腕）=腕力up值、（腳）=腳力up值、（愛）=LOVEup值、（趣）=有趣up值、（淫）=淫蕩up值<br>
	※耐久，○回代表能使用的回數，要是○日代表能使用的日數。<br>
	※卡路里是能攝取的數值。</font></td></tr>
		<tr bgcolor=#996699><td align=center nowrap>商品</td><td align=center nowrap>銷售價格</td><td align=center nowrap>進貨價格</td><td align=center nowrap>庫存</td><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>L</td><td>趣</td><td>淫</td><td align=center nowrap>卡路里</td><td align=center>使用<br>間隔</td><td align=center>身體<br>能量<br>消費</td><td align=center>頭腦<br>能量<br>消費</td><td align=center nowrap>耐久</td><td align=center nowrap>　備　考　</td><td align=center nowrap>購入日</td></tr>
EOM

	foreach (@alldata) {
			&syouhin_sprit($_);
			if ($omise_syubetu ne "超市"){
				if ($omise_syubetu ne "$syo_syubetu"){next;}
			}
			if($syo_cal > 0){$calory_hyouzi = "$syo_cal kcal";}else{$calory_hyouzi = "<div align=center>ー</div>";}
			if ($maeno_syo_syubetu ne "$syo_syubetu"){
				print "<tr bgcolor=#cc9999><td colspan=28>▼$syo_syubetu</td></tr>";
			}
			$taikyuu_hyouzi_seikei = "$syo_taikyuu"."$syo_taikyuu_tani";
			&byou_hiduke($syo_kounyuubi);
			if ($omise_syubetu eq "超市"){
				$syo_nedan *= 1.5;
			}
#如果做獨自的價格設定不那個價格，如果是那樣設定的價格率
			if ($tokubai){$hannbaityuu = "$tokubai";}else{$hannbaityuu = $syo_nedan * $omise_yobi5;}
		print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="my_syouhin">
	<input type=hidden name=command value="価格設定">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=syo_hinmoku value="$syo_hinmoku">
	<input type=hidden name=syo_nedan value="$syo_nedan">
		<tr bgcolor=#ffcccc align=center><td nowrap align=left>$syo_hinmoku</td><td nowrap><input type="text" name="hanbaikakaku" size=8 value=$hannbaityuu><input type=submit value="OK"></form><td nowrap align=right>$syo_nedan</td></td><td nowrap>$syo_zaiko</td><td>$syo_kokugo</td><td>$syo_suugaku</td><td>$syo_rika</td><td>$syo_syakai</td><td>$syo_eigo</td><td>$syo_ongaku</td><td>$syo_bijutu</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td align=right>$calory_hyouzi</td><td nowrap>$syo_kankaku分</td><td>$syo_sintai_syouhi</td><td>$syo_zunou_syouhi</td><td nowrap>$taikyuu_hyouzi_seikei</td><td align=left>$syo_comment</td><td nowrap>$bh_tukihi</td></tr>
EOM
		$maeno_syo_syubetu = "$syo_syubetu";
	}		#foreach閉上
	if (! @alldata){print "<tr><td colspan=26>現在沒有物品。</td></tr>";}
	print <<"EOM";
	</table>
EOM
	&hooter("my_house_settei","返回","original_house.cgi");
	exit;
}

###BBS記事刪掉
sub bbs_delete {
	if ($in{'b_count'} eq ""){&error("沒指定記事no.");}
	&lock;
#log file更新
	# 讀入記錄
	if ($in{'ori_ie_id'} eq "admin"){
		$bbs1_log_file = "./member/admin/bbs".$in{'bbs_num'}."_log.cgi";
	}else{
		$bbs1_log_file = "./member/$in{'ori_ie_id'}/bbs1_log.cgi";
	}
	open(IN,"$bbs1_log_file") || &error("Open Error : $bbs1_log_file");
	$count_gyou = <IN>;
	@all_data = <IN>;
	close(IN);
		$kizi_atta_flag = 0;
		$sakujo_b_num = "";
		@new_all_data = ();
		foreach (@all_data){
			($b_num,$b_name,$b_date,$b_res,$b_mail,$b_com)= split(/<>/, $_);
			if ($in{'b_count'} eq "$b_mail"){
				$kizi_atta_flag = 1;
				if ($b_num){$sakujo_b_num = "$b_num";}else{$sakujo_b_num = "res";}
				$b_name =~ s/<span style="font-size:9px">（.*//;
				if ($in{'name'} ne $admin_name){&error("管理者以外不能刪掉記事。");
				}else{next;}
			}
			if ($b_res){if ($b_res eq "$sakujo_b_num"){&error("附有了子記事的父記事不能刪掉。");}}
			$bbs_temp = "$b_num<>$b_name<>$b_date<>$b_res<>$b_mail<>$b_com<>\n";
			push (@new_all_data,$bbs_temp);
		}
		if ($kizi_atta_flag == 0){&error("沒找到符合的記事no.。");}
		unshift (@new_all_data,$count_gyou);
		open (OUT,">$bbs1_log_file") || &error("Write Error : $bbs1_log_file");
		print OUT @new_all_data;
		close(OUT);
	&unlock;
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">刪掉了記事。</span>
</td></tr></table>
<br>
	<form method=POST action="$this_script">
EOM
	if ($in{'ori_ie_id'} eq "admin"){
		print "<input type=hidden name=mode value=\"normal_bbs\">";
	}else{
		print "<input type=hidden name=mode value=\"houmon\">";
	}
	print <<"EOM";
	<input type=hidden name=con_sele value="0">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form></div>
EOM
	exit;
}

###戶主限制留言板記事刪掉
sub gentei_delete {
	if ($in{'ori_ie_id'} != $k_id and $in{'ori_ie_id'} != $house_type and $in{'name'} ne $admin_name){&error("家主（配偶者）、ゲーム管理者以外は記事削除できません。");}
	if ($in{'b_num'} eq ""){&error("沒指定記事no.");}
	&lock;
#log file更新
	# 讀入記錄
	$gentei_log_file = "./member/$in{'ori_ie_id'}/gentei_log.cgi";
	open(IN,"$gentei_log_file") || &error("Open Error : $gentei_log_file");
	@all_data=<IN>;
	close(IN);
		$kizi_atta_flag = 0;
		@new_all_data = ();
		foreach (@all_data){
			($b_num,$b_name,$b_date,$b_title,$b_mail,$b_com)= split(/<>/);
			if ($in{'b_num'} eq "$b_num"){
				$kizi_atta_flag = 1;
				if ($name ne $b_name &&  $in{'name'} ne $admin_name){&error("寫了的本人以外不能刪掉記事。");
				}else{next;}
			}
			$bbs_temp = "$b_num<>$b_name<>$b_date<>$b_title<>$b_mail<>$b_com<>\n";
			push (@new_all_data,$bbs_temp);
		}
		if ($kizi_atta_flag == 0){&error("沒找到符合的記事no.。");}
		open (OUT,">$gentei_log_file") || &error("Write Error : $gentei_log_file");
		print OUT @new_all_data;
		close(OUT);
	&unlock;
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">刪掉了記事。</span>
</td></tr></table>
<br>
	<form method=POST action="$this_script">
	<input type=hidden name=mode value=\"houmon\">
	<input type=hidden name=con_sele value="3">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=ori_ie_id value="$in{'ori_ie_id'}">
	<input type=hidden name=bbs_num value="$in{'bbs_num'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form></div>
EOM
	exit;
}
