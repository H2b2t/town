#!/perl/bin/perl
# ↑使用合乎服務器的路徑。

$this_script = 'kekkon.cgi';
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
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("暫時未能行動。請等候$ato_nanbyou秒以後。")}
		
#條件分歧
	if($in{'mode'} eq "assenjo"){&assenjo;}
	elsif($in{'mode'} eq "kokuhaku"){&kokuhaku;}
	elsif($in{'mode'} eq "renai"){&renai;}
	elsif($in{'mode'} eq "kodomo_naming"){&kodomo_naming;}
	elsif($in{'mode'} eq "kosodate"){&kosodate;}
	else{&error("請用「返回」按鈕返回街");}
exit;
	
#############以下子程序
sub assenjo {
#性別的select
	@as_sex_array=('男','女');
#選擇式個人資料項目
		$as_prof_name1='婚姻狀況';
		@as_prof_array1=('','為了結婚而募集戀人','已婚戀人募集中','戀人募集中','已結婚','戀人已達到規定數','單身但現在不想談戀愛');
		
	open(IN,"$as_profile_file") || &error("Open Error : $as_profile_file");
	@alldata=<IN>;
	close(IN);
#情侶排名的情況
	if ($in{'command'} eq "couple_ranking"){
	open(COA,"$couple_file") || &error("$couple_file不能寫上");
		@all_couple = <COA>;
	close(COA);
	open(REN,"./dat_dir/love.dat") || &error("Open Error : ./dat_dir/love.dat");
		$top_koumoku = <REN>;
		my (@koumokumei_hairetu)= split(/<>/,$top_koumoku);
	close(REN);
			&lock;
	$wakareflag = 0;
	$now_time = time ;
	foreach (@all_couple){
		($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
		if ($cn_joutai eq "戀人"){$yobikata = "戀人";$wakare_time = $wakare_limit_koibito;}else{$yobikata = "夫婦";$wakare_time = $wakare_limit_haiguu;}
#分手處理
		if ($now_time - $cn_yobi1 > $wakare_time * 60 * 60 * 24){
			$wakareflag = 1;
			&news_kiroku("分手","$cn_name1君和$cn_name2君分手了。");
			if ($yobikata eq "夫婦"){
				&kekkon_id_sakujo($cn_name1);
				&kekkon_id_sakujo($cn_name2);
			}
			next;
		}
		push (@new_all_couple_sort,$_);
	}		#foreach閉上
#數據更新
	if ($wakareflag == 1){
			open(COP,">$couple_file") || &error("$couple_file不能寫上");
			print COP @new_all_couple_sort;
			close(COP);
	}
			&unlock;

#ver.1.40從這裡
	foreach (@new_all_couple_sort){
			$data=$_;
			$key=(split(/<>/,$data))[4];		#選排序的要素
			$key1=(split(/<>/,$data))[5];		#選排序的要素
			$key2=(split(/<>/,$data))[6];		#選排序的要素
			$key3=(split(/<>/,$data))[7];		#選排序的要素
			$key4=(split(/<>/,$data))[8];		#選排序的要素
			$key5=(split(/<>/,$data))[9];		#選排序的要素
			push @all_couple_sort,$data;
			push @keys,$key;
			push @keys1,$key1;
			push @keys2,$key2;
			push @keys3,$key3;
			push @keys4,$key4;
			push @keys5,$key5;
	}
		sub bykeys{$keys[$b] <=> $keys[$a];}
		sub bykeys1{$keys1[$b] <=> $keys1[$a];}
		sub bykeys2{$keys2[$b] <=> $keys2[$a];}
		sub bykeys3{$keys3[$b] <=> $keys3[$a];}
		sub bykeys4{$keys4[$b] <=> $keys4[$a];}
		sub bykeys5{$keys5[$b] <=> $keys5[$a];}
		@all_couple_sort0=@all_couple_sort[ sort bykeys 0..$#all_couple_sort];
		@all_couple_sort1=@all_couple_sort[ sort bykeys1 0..$#all_couple_sort];
		@all_couple_sort2=@all_couple_sort[ sort bykeys2 0..$#all_couple_sort];
		@all_couple_sort3=@all_couple_sort[ sort bykeys3 0..$#all_couple_sort];
		@all_couple_sort4=@all_couple_sort[ sort bykeys4 0..$#all_couple_sort];
		@all_couple_sort5=@all_couple_sort[ sort bykeys5 0..$#all_couple_sort];

		&header(assen_style);
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>現在成立的全部的情侶。<br>愛愛度高低順序排列。
	</td>
	<td  bgcolor=#ff6633 align=center width=35%><div style="font-size:13px; color:#ffffff">愛愛&#9829;情侶排行磅</div>
	</td></tr></table><br>
	<table width="90%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
EOM

		print "<tr  class=jouge bgcolor=#ffffcc><td style=\"color:#3366ff\">多的情侶</td>";
		foreach $juni (1..3){
			$sort_no=$koumoku_sentaku-1;
			$one_couple = (split(/<>/,$all_couple_sort1[$juni - 1]))[1];
			$two_couple = (split(/<>/,$all_couple_sort1[$juni - 1]))[2];
			$suuti =  (split(/<>/,$all_couple_sort1[$juni - 1]))[5];
			print "<td><span style=\"color:#3366ff\">NO.$juni</span>：$one_couple & $two_couple（$suuti）</td>";
		}
		print "</tr>";

		print "<tr  class=jouge bgcolor=#ffffff><td style=\"color:#3366ff\">「$koumokumei_hairetu[3]」多的情侶</td>";
		foreach $juni (1..3){
			$sort_no=$koumoku_sentaku-1;
			$one_couple = (split(/<>/,$all_couple_sort2[$juni - 1]))[1];
			$two_couple = (split(/<>/,$all_couple_sort2[$juni - 1]))[2];
			$suuti =  (split(/<>/,$all_couple_sort2[$juni - 1]))[6];
			print "<td><span style=\"color:#3366ff\">NO.$juni</span>：$one_couple & $two_couple（$suuti）</td>";
		}
		print "</tr>";
		
		print "<tr  class=jouge bgcolor=#ffffcc><td style=\"color:#3366ff\">「$koumokumei_hairetu[4]」多的情侶</td>";
		foreach $juni (1..3){
			$sort_no=$koumoku_sentaku-1;
			$one_couple = (split(/<>/,$all_couple_sort3[$juni - 1]))[1];
			$two_couple = (split(/<>/,$all_couple_sort3[$juni - 1]))[2];
			$suuti =  (split(/<>/,$all_couple_sort3[$juni - 1]))[7];
			print "<td><span style=\"color:#3366ff\">NO.$juni</span>：$one_couple & $two_couple（$suuti）</td>";
		}
		print "</tr>";
		
		print "<tr  class=jouge bgcolor=#ffffff><td style=\"color:#3366ff\">「$koumokumei_hairetu[5]」多的情侶</td>";
		foreach $juni (1..3){
			$sort_no=$koumoku_sentaku-1;
			$one_couple = (split(/<>/,$all_couple_sort4[$juni - 1]))[1];
			$two_couple = (split(/<>/,$all_couple_sort4[$juni - 1]))[2];
			$suuti =  (split(/<>/,$all_couple_sort4[$juni - 1]))[8];
			print "<td><span style=\"color:#3366ff\">NO.$juni</span>：$one_couple & $two_couple（$suuti）</td>";
		}
		print "</tr>";
		
		print "<tr  class=jouge bgcolor=#ffffcc><td style=\"color:#3366ff\">「$koumokumei_hairetu[6]」多的情侶</td>";
		foreach $juni (1..3){
			$sort_no=$koumoku_sentaku-1;
			$one_couple = (split(/<>/,$all_couple_sort5[$juni - 1]))[1];
			$two_couple = (split(/<>/,$all_couple_sort5[$juni - 1]))[2];
			$suuti =  (split(/<>/,$all_couple_sort5[$juni - 1]))[9];
			print "<td><span style=\"color:#3366ff\">NO.$juni</span>：$one_couple & $two_couple（$suuti）</td>";
		}
		print "</tr>";
		
	print <<"EOM";
	</table><br>
	<table width="90%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
	<tr  class=jouge bgcolor=#ffffaa align=center nowrap><td>名次</td><td>名字</td><td>關係</td><td>愛愛度</td><td>$koumokumei_hairetu[2]</td><td>$koumokumei_hairetu[3]</td><td>$koumokumei_hairetu[4]</td><td>$koumokumei_hairetu[5]</td><td>$koumokumei_hairetu[6]</td></tr>
EOM
	foreach (@all_couple_sort0){
		($cn_number,$cn_name1,$cn_name2,$cn_joutai)= split(/<>/);
		if ($cn_joutai eq "配偶"){
			$huuhu{"$cn_name1"} = "on";
			$huuhu{"$cn_name2"} = "on";
		}
	}
	
	$i = 1;
	foreach (@all_couple_sort0){
		($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
		if ($cn_joutai eq "戀人"){
			if ($huuhu{"$cn_name1"} eq "on" || $huuhu{"$cn_name2"} eq "on"){
				$yobikata = "情人";
				$c_color= "#6699cc";
			}else{
				$yobikata = "戀人";
				$c_color= "#ff6600";
			}
		}else{$yobikata = "夫婦";$c_color= "#ff0000";}
		print <<"EOM";
	<tr align=right><td align=center>$i</td><td  align=left style="color:$c_color;">$cn_name1 &#9829; $cn_name2</td><td align=center style="color:$c_color;">$yobikata</td><td class=mainasu>$cn_total_aijou</td><td>$cn_omoide1</td><td>$cn_omoide2</td><td>$cn_omoide3</td><td>$cn_omoide4</td><td>$cn_omoide5</td></tr>
EOM
		$i ++;
	}		#foreach閉上
#ver.1.40到這裡
	print "</table>";

	&hooter("assenjo","返回","kekkon.cgi");
	&hooter("login_view","返回街");
	exit;
	}		#情侶排列次序的情況閉上
	
#孩子排列次序的情況
	if ($in{'command'} eq "kodomo_ranking"){
	open(KOD,"$kodomo_file") || &error("Open Error : $kodomo_file");
	@all_kodomo=<KOD>;
	close(KOD);
		
	$now_time = time ;
	$kodomo_sakujo_flg = 0;
		foreach (@all_kodomo){
			($kod_num,$kod_name,$kod_oya1,$kod_oya2,$kod_job,$kod_kokugo,$kod_suugaku,$kod_rika,$kod_syakai,$kod_eigo,$kod_ongaku,$kod_bijutu,$kod_looks,$kod_tairyoku,$kod_kenkou,$kod_speed,$kod_power,$kod_wanryoku,$kod_kyakuryoku,$kod_love,$kod_unique,$kod_etti,$kod_yobi1,$kod_yobi2,$kod_yobi3,$kod_yobi4,$kod_yobi5,$kod_yobi6,$kod_yobi7,$kod_yobi8,$kod_yobi9,$kod_yobi10)=split(/<>/);
			$kono_nenrei = int (($now_time - $kod_yobi1)/(60*60*24));

#孩子刪掉處理
		if ($kono_nenrei > $kodomo_sibou_time2){
			$kodomo_sakujo_flg = 1;
			next;
		}
		
#孩子流產處理
		if ($kod_name eq "" && $now_time - $kod_yobi1 > $kodomo_sibou_time * 60 * 60 * 24 && $kod_yobi8 != 1){
			&lock;
			$kodomo_sakujo_flg = 1;
			&unlock;
			next;
		}
		
#孩子死亡處理
		if ($now_time - $kod_yobi7 > $kodomo_sibou_time * 60 * 60 * 24 && $kod_yobi8 != 1){
			&lock;
			$kodomo_sakujo_flg = 1;
			&unlock;
			next;
		}
#孩子自立處理
		if ($kono_nenrei >= 19 && $kod_yobi8 != 1){
			&kodomo_ziritu($_);
			$kod_job = $return_job;
			$kod_yobi8 = 1;
			$kodomo_sakujo_flg = 1;
		}
$new_kodomo_temp = "$kod_num<>$kod_name<>$kod_oya1<>$kod_oya2<>$kod_job<>$kod_kokugo<>$kod_suugaku<>$kod_rika<>$kod_syakai<>$kod_eigo<>$kod_ongaku<>$kod_bijutu<>$kod_looks<>$kod_tairyoku<>$kod_kenkou<>$kod_speed<>$kod_power<>$kod_wanryoku<>$kod_kyakuryoku<>$kod_love<>$kod_unique<>$kod_etti<>$kod_yobi1<>$kod_yobi2<>$kod_yobi3<>$kod_yobi4<>$kod_yobi5<>$kod_yobi6<>$kod_yobi7<>$kod_yobi8<>$kod_yobi9<>$kod_yobi10<>\n";
			push @new_all_kodomo,$new_kodomo_temp;
		}		#foreach閉上
		
#孩子數據更新
		if ($kodomo_sakujo_flg == 1){
			&lock;
			open(KODO,">$kodomo_file") || &error("$kodomo_file不能寫上");
			print KODO @new_all_kodomo;
			close(KODO);
			&unlock;
		}
	foreach (@new_all_kodomo){
			$data=$_;
			$key=(split(/<>/,$data))[25];		#選排序的要素
			push @all_kodomo_sort,$data;
			push @keys,$key;
	}
#分類處理
		sub bykeys{$keys[$b] <=> $keys[$a];}
		@all_kodomo_sort=@all_kodomo_sort[ sort bykeys 0..$#all_kodomo_sort];
		
	foreach (@all_kodomo_sort){
			($kod_num,$kod_name,$kod_oya1,$kod_oya2,$kod_job,$kod_kokugo,$kod_suugaku,$kod_rika,$kod_syakai,$kod_eigo,$kod_ongaku,$kod_bijutu,$kod_looks,$kod_tairyoku,$kod_kenkou,$kod_speed,$kod_power,$kod_wanryoku,$kod_kyakuryoku,$kod_love,$kod_unique,$kod_etti,$kod_yobi1,$kod_yobi2,$kod_yobi3,$kod_yobi4,$kod_yobi5,$kod_yobi6,$kod_yobi7,$kod_yobi8,$kod_yobi9,$kod_yobi10)=split(/<>/);
			$kono_nenrei = int (($now_time - $kod_yobi1)/(60*60*24));
			
			$kod_yobi5 = sprintf ("%.1f",$kod_yobi5);
			$kod_yobi6 = sprintf ("%.1f",$kod_yobi6);
			$ko_meisai_td = "<td>$kod_name</td><td>$kod_oya1&#9829;$kod_oya2</td><td align=right>$kono_nenrei歲</td><td align=right>$kod_yobi5 cm</td><td align=right>$kod_yobi6 kg</td><td align=right>$kod_yobi4</td>";
			if ($kod_name eq ""){next;}
			if ($kono_nenrei >=19){next;}
			if ($kono_nenrei >=16){push (@koukou_hairetu,$ko_meisai_td);}
			elsif ($kono_nenrei >=13){push (@tyuugaku_hairetu,$ko_meisai_td);}
			elsif ($kono_nenrei >=7){push (@syougaku_hairetu,$ko_meisai_td);}
			else{push (@youzi_hairetu,$ko_meisai_td);}
	}
		
		&header(assen_style);
		print <<"EOM";
	<table width="95%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>孩子的能力排名。根據年齡分成「幼兒部門」「小學生部門」「初中生部門」「高中生部門」。
	</td>
	<td  bgcolor=#ff6633 align=center width=35%><div style="font-size:13px; color:#ffffff">子供ランキングベスト20</div>
	</td></tr></table><br>
	<table width="95%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
	<tr><td valign=top width=50%>
	<div class=tyuu align=center>幼兒部門</div>
	<table width="100%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
	<tr  class=jouge bgcolor=#ffffaa align=center nowrap><td>名次</td><td>孩子的名字</td><td>父母的名字</td><td>年齡</td><td>身長</td><td>體重</td><td>能力值</td></tr>
EOM
	$i = 1;
	foreach (@youzi_hairetu){
			print "<tr><td align=center>$i</td>$_</tr>";
			$i ++;
			if ($i >= 20){last;}
	}
	print <<"EOM";
	</table></td><td valign=top width=50%>
	<div class=tyuu align=center>小學生部門</div>
	<table width="100%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
	<tr  class=jouge bgcolor=#ffffaa align=center nowrap><td>名次</td><td>孩子的名字</td><td>父母的名字</td><td>年齡</td><td>身長</td><td>體重</td><td>能力值</td></tr>
EOM
	$i = 1;
	foreach (@syougaku_hairetu){
			print "<tr><td align=center>$i</td>$_</tr>";
			$i ++;
			if ($i >= 20){last;}
	}
	print <<"EOM";
	</table></td></tr></table><br><br>
	<table width="95%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
	<tr><td valign=top width=50%>
	<div class=tyuu align=center>初中生部門</div>
	<table width="100%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
	<tr  class=jouge bgcolor=#ffffaa align=center nowrap><td>名次</td><td>孩子的名字</td><td>父母的名字</td><td>年齡</td><td>身長</td><td>體重</td><td>能力值</td></tr>
EOM
	$i = 1;
	foreach (@tyuugaku_hairetu){
			print "<tr><td align=center>$i</td>$_</tr>";
			$i ++;
			if ($i >= 20){last;}
	}
	print <<"EOM";
	</table></td><td valign=top width=50%>
	<div class=tyuu align=center>高中生部門</div>
	<table width="100%" border="0" cellspacing="0" cellpadding="5" align=center class=yosumi>
	<tr  class=jouge bgcolor=#ffffaa align=center nowrap><td>名次</td><td>孩子的名字</td><td>父母的名字</td><td>年齡</td><td>身長</td><td>體重</td><td>能力值</td></tr>
EOM
	$i = 1;
	foreach (@koukou_hairetu){
			print "<tr><td align=center>$i</td>$_</tr>";
			$i ++;
			if ($i >= 20){last;}
	}
	print "</table></td></tr></table>";

	print "<br><div align=center><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>";
	&hooter("login_view","返回街");
	exit;
	}		#孩子排名的情況閉上
	
#是個人資料刪掉的情況
	if ($in{'command'} eq "touroku_sakujo"){
	&lock;
#ver.1.40從這裡
	open(ASP,"$as_profile_file") || &error("Open Error : $as_profile_file");
	my @as_pro_alldata=<ASP>;
	close(ASP);
	@as_new_pro_alldata = ();
	foreach (@as_pro_alldata){
my ($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
			if ($in{'name'} eq "$pro_name"){next;} 
			push (@as_new_pro_alldata,$_);
	}
#記錄更新
	open(ASPO,">$as_profile_file") || &error("$as_profile_file不能寫上");
	print ASPO @as_new_pro_alldata;
	close(ASPO);
#		&as_prof_sakujo($in{'name'});
#ver.1.40到這裡
	&unlock;
	&message_only("刪掉了戀人介紹所的個人資料。");
	&hooter("assenjo","返回","kekkon.cgi");
	exit;
	}
	
#登記form的輸出
	if ($in{'command'} eq "touroku_form"){
		&as_prof_form;
		exit;
	}
	
#登記的情況
	if ($in{'command'} eq "touroku"){
		if ($love < $need_love){&error("登記必要的LOVE參數不夠");}
		$atta_flag=0;
		@new_alldata = ();
		foreach (@alldata){
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
#修正的情況
			if ($name eq "$pro_name"){next;} 
			push (@new_alldata,$_);
		}
		my($new_entry) = "$name<>$in{'pro_sex'}<>$in{'pro_age'}<>$in{'pro_addr'}<>$in{'pro_p1'}<>$in{'pro_p2'}<>$in{'pro_p3'}<>$in{'pro_p4'}<>$in{'pro_p5'}<>$in{'pro_p6'}<>$in{'pro_p7'}<>$k_sousisan<>$k_id<>$job<>$in{'pro_p11'}<>$in{'pro_p12'}<>$in{'pro_p13'}<>$in{'pro_p14'}<>$in{'pro_p15'}<>$in{'pro_p16'}<>$in{'pro_p17'}<>$in{'pro_p18'}<>$in{'pro_p19'}<>$in{'pro_p20'}<>\n";
#pro_p7個人資料 pro_p8=總資產　pro_p9=ID識別號(家表示用)pro_p10=職業
		unshift (@new_alldata,$new_entry);
		
#記錄更新
	&lock;
	open(OUT,">$as_profile_file") || &error("$profile_file不能寫上");
	print OUT @new_alldata;
	close(OUT);
	&unlock;
	&message("進行了戀人介紹所的個人資料登記。","assenjo","kekkon.cgi");
	exit;
	}
	if ($love < $need_love){$keikoku = "※因為LOVE參數不夠、$name君暫時不能登記。";}
	&header(assen_style);
		print <<"EOM";
	<table width="95%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>●這裡登記的是虛擬的戀愛和結婚。<br>
	●LOVE參數$need_love以上才可登記（參數窗口的上面會有新的心形圖標出現）。<br>
	●登記結束了，能夠表白(申請交往)，也能收領交往申請郵件。<br>
	●配偶加戀人合計，同時能和$koibito_seigen人交往。<br>
	●有戀人的話，能使用心記圖標的戀愛指令。<br>
	●為了結婚，需要根據戀愛指令加深戀人的愛愛度。<br>
	<font color=#336699>$keikoku</font>
	</td>
	<td  bgcolor=#ffff99 align=center width=35%><img src="$img_dir/assen_tytle.gif">
	</td></tr></table><br>

	<table width="95%" border="0" cellspacing="0" cellpadding="8" align=center bgcolor=#ffffff>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="easySerch">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<tr>
EOM

#檢索形式
# 名字
	print "<td>名　字 <input type=text name=serch_name size=20></td>\n";

# 年齡
	print "<td><select name=age>\n";
	print "<option value=\"\">年齡\n";
		for($i=1;$i<@as_age_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'age'} eq $as_age_array[$i]);
				print ($option,$as_age_array[$i]);
		}
	print "</select></td>\n";
	
# 住所
	print "<td><select name=address>\n";
	print "<option value=\"\">住所\n";
		for($i=1;$i<@as_address_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'address'} eq $as_address_array[$i]);
				print ($option,$as_address_array[$i]);
		}
	print "</select></td>\n";
	
# 個人資料1
	print "<td valign=top nowrap>\n";
	print "<select name=p1>\n";
	print "<option value=\"\">$as_prof_name1\n";
		for($i=1;$i<@as_prof_array1;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p1'} eq $as_prof_array1[$i]);
				print ($option,$as_prof_array1[$i]);
		}
	print "</select></td>\n";
	
# 個人資料2
	print "<td valign=top nowrap>\n";
	print "<select name=p2>\n";
	print "<option value=\"\">$as_prof_name2\n";
		for($i=1;$i<@as_prof_array2;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p2'} eq $as_prof_array2[$i]);
				print ($option,$as_prof_array2[$i]);
		}
	print "</select></td></tr><tr>\n";
	
# 個人資料3
	print "<td valign=top nowrap>\n";
	print "<select name=p3>\n";
	print "<option value=\"\" selected>$as_prof_name3\n";
		for($i=1;$i<@as_prof_array3;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p3'} eq $as_prof_array3[$i]);
				print ($option,$as_prof_array3[$i]);
		}
	print "</select></td>\n";
	
# 個人資料4
	print "<td valign=top nowrap>\n";
	print "<select name=p4>\n";
	print "<option value=\"\" selected>$as_prof_name4\n";
		for($i=1;$i<@as_prof_array4;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p4'} eq $as_prof_array4[$i]);
				print ($option,$as_prof_array4[$i]);
		}
	print "</select></td>\n";
	
# 個人資料5
	print "<td valign=top nowrap>\n";
	print "<select name=p5>\n";
	print "<option value=\"\" selected>$as_prof_name5\n";
		for($i=1;$i<@as_prof_array5;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p5'} eq $as_prof_array5[$i]);
				print ($option,$as_prof_array5[$i]);
		}
	print "</select></td>\n";
	
# 個人資料6
	print "<td valign=top nowrap>\n";
	print "<select name=p6>\n";
	print "<option value=\"\" selected>$as_prof_name6\n";
		for($i=1;$i<@as_prof_array6;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p6'} eq $as_prof_array6[$i]);
				print ($option,$as_prof_array6[$i]);
		}

	print <<"EOM";
	</select></td><td>
	<input type=submit value=" 檢索 ">
	</form>
	  </td>
    </tr>
  </table><br>
	<table border=0 align=center width=400>
	<tr><td align=left>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="couple_ranking">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="情侶排名">
	</form>
	</td><td align=right>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="kodomo_ranking">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="孩子排名">
	</form>
	</td></tr></table><br>
EOM
#	&hooter("login_view","返回街");
		
	$page=$in{'page'};	
	if ($page eq "") { $page = 0; }
	$i3=0;

##記錄表示處理
#unit hash代入個人的家信息
	open(OI,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
	@ori_ie_hairetu = <OI>;
	foreach (@ori_ie_hairetu) {
			&ori_ie_sprit($_);
			$unit{"$ori_k_id"} = "<input type=hidden name=mode value=houmon><input type=hidden name=ori_ie_id value=$ori_k_id><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$ori_ie_image\"></form>";
	}
	close(OI);
#表示自己的個人資料
			foreach (@alldata) {
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
			@my_prof_hairetu = split(/<>/);
			if ($name eq "$pro_name"){$prof_atta_flg = 1; last;}
			}

if ($in{'command'} ne "easySerch"){		#檢索的情況不表示自己的個人資料
			if($pro_sex eq "男"){
					$sex_style="border: #ffffff; border-style: solid; border-width: 2px; background-color:#ffffff";
			}elsif($pro_sex eq "女"){
					$sex_style="border: #ffffff; border-style: solid; border-width: 2px; background-color:#ffffff";
			}
			if ($unit{"$pro_p9"} ne ""){$ie_hyouzi="$unit{$pro_p9}"}else{$ie_hyouzi="：沒有</form>";}
			if ($prof_atta_flg == 0){$zibun_prof_com = "<tr><td align=center colspan=8>沒登記。</td></tr>";}else{
				$zibun_prof_com =<< "EOM";
				<tr><td width=120><span class=honbun2>名字</span>：$pro_name（$pro_p10）</td>
				<td width=120><span class=honbun2>性別</span>：$pro_sex</td>
				<td width=120><span class=honbun2>總資產</span>：$pro_p8元</td>
				<form method=POST action=\"original_house.cgi\"><td width=120><span class=honbun2>家</span>$ie_hyouzi</td></tr><!--ver.1.40-->
				<tr><td width=120><span class=honbun2>年齡</span>：$pro_age</td>
				<td width=120><span class=honbun2>住所</span>：$pro_addr</td>
				<td width=120><span class=honbun2>$as_prof_name1</span>：$pro_p1</td>
				<td width=120><span class=honbun2>$as_prof_name2</span>：$pro_p2</td></tr>
				<tr><td width=120><span class=honbun2>$as_prof_name3</span>：$pro_p3</td>
				<td width=120><span class=honbun2>$as_prof_name4</span>：$pro_p4</td>
				<td width=120><span class=honbun2>$as_prof_name5</span>：$pro_p5</td>
				<td width=120><span class=honbun2>$as_prof_name6</span>：$pro_p6</td></tr>
				<tr><td colspan=8 align="center"><span class=honbun2>一句評語</span>：$pro_p7<br><br>
				※職業、總資產、家等不在這更新不會變成最新的信息。<br>
				※結婚，已經達到規定的戀人數請隨意變更「婚姻狀況」的項目。</td></tr>
EOM
			}
			print <<"EOM";
			<table style=\"$sex_style\" align=center width=95%>
			<tr><td colspan=8 align=center><span class=honbun2><b>＜自己的個人資料＞</b></td></tr>
			$zibun_prof_com
	<tr><td colspan=8 align=center>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="touroku_form">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="個人資料登記&修正">
	</form>
	</td></tr>
			</table><br><br>
EOM
}

	
# 簡易檢索的情況
		if ($in{'command'} eq "easySerch"){
				$i=0;
				foreach (@alldata) {
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
					if ($in{'serch_name'} ne "" && $in{'serch_name'} ne $pro_name) { next; }		#條件不相符時到下面的人
					if ($in{'age'} ne "" && $in{'age'} ne $pro_age) { next; }		
					if ($in{'address'} ne "" && $in{'address'} ne $pro_addr) { next; }
					if ($in{'p1'} ne "" && $in{'p1'} ne $pro_p1) { next; }
					if ($in{'p2'} ne "" && $in{'p2'} ne $pro_p2) { next; }
					if ($in{'p3'} ne "" && $in{'p3'} ne $pro_p3) { next; }
					if ($in{'p4'} ne "" && $in{'p4'} ne $pro_p4) { next; }
					if ($in{'p5'} ne "" && $in{'p5'} ne $pro_p5) { next; }
					if ($in{'p6'} ne "" && $in{'p6'} ne $pro_p6) { next; }
			if ($name eq "$pro_name"){next;}
			if ($douseiai_per == 0){
				if ($sex eq "m" && $pro_sex eq "男"){next;}
				if ($sex eq "f" && $pro_sex eq "女"){next;}
			}
					$i++;
					push(@newrank,$_);
				}
				@alldata=@newrank;
				print "<div align=center class=sub2>$i個條件符合。<br>
				<a href=\"javascript:history.back()\"> [返回前畫面] </a>
				</div><br>";
				&hooter("assenjo","全部表示","kekkon.cgi");
		}
#表示全體的個人資料
			if ($douseiai_per == 0){
				if ($sex eq "m"){$tourokusya_hyouki = "＜現在的女性登記者＞";}
				elsif ($sex eq "f"){$tourokusya_hyouki = "＜現在的男性登記者＞";}
			}else{$tourokusya_hyouki = "＜現在的登記者＞";}
	print <<"EOM";
	<div align=center class="honbun4">$tourokusya_hyouki</div><br>
EOM
		foreach (@alldata) {
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
			@my_prof_hairetu = split(/<>/);
			if ($name eq "$pro_name"){next;}
			if ($douseiai_per == 0){
				if ($sex eq "m" && $pro_sex eq "男"){next;}
				if ($sex eq "f" && $pro_sex eq "女"){next;}
			}
		$i3++;
		if ($i3 < $page + 1) { next; }
		if ($i3 > $page + $hyouzi_max_grobal) { last; }
		
			if($pro_sex eq "男"){
					$sex_style="border: #ffff99; border-style: double; border-width: 7px; background-color:#ffff99";
			}elsif($pro_sex eq "女"){
					$sex_style="border: #ffff99; border-style: double; border-width: 7px; background-color:#ffff99";
			}
			if ($unit{"$pro_p9"} ne ""){$ie_hyouzi="$unit{$pro_p9}"}else{$ie_hyouzi="：沒有</form>";}
#總資產的豆點處理
			if ($pro_p8 =~ /^[-+]?\d\d\d\d+/g) {
			  for ($i = pos($pro_p8) - 3, $j = $pro_p8 =~ /^[-+]/; $i > $j; $i -= 3) {
			    substr($pro_p8, $i, 0) = ',';
			  }
			}
			print <<"EOM";
			<table style=\"$sex_style\" align=center width=450>
			<tr><td align=right width=120><div class=honbun2>名字</div></td><td>：$pro_name（$pro_p10）</td></tr>
			<tr><td align=right width=120><div class=honbun2>性別</div></td><td>：$pro_sex</td></tr>
			<tr><td align=right width=120><div class=honbun2>總資產</div></td><td>：$pro_p8元</td></tr>
			<tr><td align=right width=120><div class=honbun2>家</div></td><form method=POST action=\"original_house.cgi\"><td>$ie_hyouzi<!--ver.1.40-->
EOM
			$i=0;
			foreach (@my_prof_hairetu){
					$_ =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
					$i ++; 
					if ($i <= 2){next;}
					if ($i >= 12){last;}
					elsif ($i == 3){$pr_koumokumei ="年齡";}
					elsif ($i == 4){$pr_koumokumei ="住所";}
					elsif ($i == 5){$pr_koumokumei ="$as_prof_name1";}
					elsif ($i == 6){$pr_koumokumei ="$as_prof_name2";}
					elsif ($i == 7){$pr_koumokumei ="$as_prof_name3";}
					elsif ($i == 8){$pr_koumokumei ="$as_prof_name4";}
					elsif ($i == 9){$pr_koumokumei ="$as_prof_name5";}
					elsif ($i == 10){$pr_koumokumei ="$as_prof_name6";}
					elsif ($i == 11) {$pr_koumokumei = "一句評語";}
				if ($_ ne "" && $_ ne "\n"){
					print <<"EOM";
					<tr><td align=right width=120><div class=honbun2>$pr_koumokumei</div></td>
					<td>：$_</td></tr>
EOM
				}
		}	#foreach閉上
#如果LOVE參數超過登記結束形式輸出
		if ($love >= $need_love && $prof_atta_flg == 1){
			print <<"EOM";
     <tr><td colspan=2 align=center>
	 <form method="POST" action="$this_script">
	<input type=hidden name=mode value="kokuhaku">
	<input type=hidden name=kokuhaku_syubetu value="mousikomi">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name="sousinsaki_name" value="$pro_name">
	表白的言詞 <input type=text name=m_com size=30>
	<input type=submit value="要求交往"></form>
EOM
		}
		print <<"EOM";
	</td></tr>
	</table><br>
EOM

		}	#foreach閉上（記錄表示處理到這裡）

		$next = $page + $hyouzi_max_grobal;
		$back = $page - $hyouzi_max_grobal;
		print "<div align=center><table border=0><tr>";
		if ($back >= 0) {
#檢索的情況的按鈕
				if($in{'command'} eq "easySerch"){
					print <<"EOM";
			<form method=POST action=\"$this_script\">
			<input type=hidden name=mode value=assenjo>
			<input type=hidden name=command value=easySerch>
			<input type=hidden name=name value=$in{'name'}>
			<input type=hidden name=pass value=$in{'pass'}>
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=sex value=$in{'sex'}>
			<input type=hidden name=age value=$in{'age'}>
			<input type=hidden name=address value=$in{'address'}>
			<input type=hidden name=p1 value=$in{'p1'}>
			<input type=hidden name=p2 value=$in{'p2'}>
			<input type=hidden name=p3 value=$in{'p3'}>
			<input type=hidden name=p4 value=$in{'p4'}>
			<input type=hidden name=p5 value=$in{'p5'}>
			<input type=hidden name=p5 value=$in{'p6'}>
			<input type=hidden name=page value="$back">
			<input type=submit value="BACK">
			</form>
EOM
				}else{
#通常的情況
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="assenjo">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=page value="$back">
			<input type=submit value="BACK"></form></td>
EOM
				}
		}
		if ($next < $i3) {
				if($in{'command'} eq "easySerch"){
					print <<"EOM";
			<form method=POST action=\"$this_script\">
			<input type=hidden name=mode value=assenjo>
			<input type=hidden name=command value=easySerch>
			<input type=hidden name=name value=$in{'name'}>
			<input type=hidden name=pass value=$in{'pass'}>
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=sex value=$in{'sex'}>
			<input type=hidden name=age value=$in{'age'}>
			<input type=hidden name=address value=$in{'address'}>
			<input type=hidden name=p1 value=$in{'p1'}>
			<input type=hidden name=p2 value=$in{'p2'}>
			<input type=hidden name=p3 value=$in{'p3'}>
			<input type=hidden name=p4 value=$in{'p4'}>
			<input type=hidden name=p5 value=$in{'p5'}>
			<input type=hidden name=p6 value=$in{'p6'}>
			<input type=hidden name=page value="$next">
			<input type=submit value="NEXT">
</form>
EOM
				}else{
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="assenjo">
			<input type=hidden name=name value="$in{'name'}">
			<input type=hidden name=pass value="$in{'pass'}">
			<input type=hidden name=town_no value=$in{'town_no'}>
			<input type=hidden name=page value="$next">
			<input type=submit value="NEXT"></form></td>
EOM
				}
		}
		print "</tr></table>";

	&hooter("login_view","返回街");
	exit;
}

##登記form
sub as_prof_form {
		if ($love < $need_love){&error("登記必要的LOVE參數不夠");}
		$atta_flag = 0;
		foreach (@alldata){
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
			@my_prof_hairetu = split(/<>/);
			if ($pro_name eq "$name"){$atta_flag = 1; last;}
		}
	if ($atta_flag == 0){
	$pro_name = ""; $pro_sex = ""; $pro_age = ""; $pro_addr = ""; $pro_p1 = ""; $pro_p2 = ""; $pro_p3 = ""; $pro_p4 = ""; $pro_p5 = ""; $pro_p6 = ""; $pro_p7 = ""; $pro_p8 = ""; $pro_p9 = ""; $pro_p10 = ""; $pro_p11 = ""; $pro_p12 = ""; $pro_p13 = ""; $pro_p14 = ""; $pro_p15 = ""; $pro_p16 = ""; $pro_p17 = ""; $pro_p18 = ""; $pro_p19 = ""; $pro_p20 = "";
	@my_prof_hairetu = ();
	}
	
	&header(assen_style);
	if ($sex eq "m"){$sex_sentaku = "男"}else{$sex_sentaku = "女"}
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="touroku">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=pro_sex value="$sex_sentaku">
	<input type=hidden name=town_no value=$in{'town_no'}>
<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>●選擇及記述只想公開的項目，其他可以留空。<br>
	●「婚姻狀況」的項目請選擇在遊戲內的狀態。隨意變更已婚、已經達到規定的戀人數。<br>
	●無論什麼時候都能修正・更新。
	</td>
	<td  bgcolor=#ff6633 align=center width=35%><div style="font-size:13px; color:#ffffff">戀人介紹所個人資料登記</div>
	</td></tr></table><br>
	
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td>
EOM
		print ' 年齡<br><select name="pro_age">';
		for($i=0;$i<@as_age_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($pro_age eq $as_age_array[$i]);
				print ($option,$as_age_array[$i]);
		}
		print '</select></td><td>';


		print ' 住所<br><select name="pro_addr">';
		for($i=0;$i<@as_address_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($pro_addr eq $as_address_array[$i]);
				print ($option,$as_address_array[$i]);
		}
		print '</select></td><td>';

 		print "$as_prof_name1<br><select name=\"pro_p1\">";
		for($i=0;$i<@as_prof_array1;$i++){
				$option='<option>';
				$option='<option selected>' if($pro_p1 eq $as_prof_array1[$i]);
				print ($option,$as_prof_array1[$i]);
		}
		print '</select></td><td>';

		print "$as_prof_name2<br><select name=\"pro_p2\">";
		for($i=0;$i<@as_prof_array2;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p2 eq $as_prof_array2[$i]);
				print ($option,$as_prof_array2[$i]);
		}
		print '</select></td></tr><tr><td>';
 
 		print "$as_prof_name3<br><select name=\"pro_p3\">";
		for($i=0;$i<@as_prof_array3;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p3 eq $as_prof_array3[$i]);
				print ($option,$as_prof_array3[$i]);
		}
		print '</select></td><td>';
 
 		print "$as_prof_name4<br><select name=\"pro_p4\">";
		for($i=0;$i<@as_prof_array4;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p4 eq $as_prof_array4[$i]);
				print ($option,$as_prof_array4[$i]);
		}
		print '</select></td><td>';
 
 		print "$as_prof_name5<br><select name=\"pro_p5\">";
		for($i=0;$i<@as_prof_array5;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p5 eq $as_prof_array5[$i]);
				print ($option,$as_prof_array5[$i]);
		}
		print '</select></td><td>';
		
 		print "$as_prof_name6<br><select name=\"pro_p6\">";
		for($i=0;$i<@as_prof_array6;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p6 eq $as_prof_array6[$i]);
				print ($option,$as_prof_array6[$i]);
		}
		print '</select></td></tr>';
		
		print "<tr><td align=right>一句評語</td><td colspan=3><input type=text name=pro_p7 size=80 value=$my_prof_hairetu[10]></td></tr>\n";

		print <<"EOM";
	<tr><td colspan=4 align=center>
	<input type=submit value=" 以這些內容登記 "><br>
	</td></tr></table>
	</form><br>
	<div align=center><form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="touroku_sakujo">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value=" 刪掉登記了的個人資料 ">
	</form></div>
EOM
	&hooter("assenjo","返回","kekkon.cgi");
}

###########表白郵件
sub kokuhaku {
		if ($love < $need_love){&error("因為LOVE參數不夠而不能發送郵件。");}
		if ($in{'sousinsaki_name'} eq ""){&error("未輸入對方的名字");}
		if ($in{'m_com'} eq ""){&error("未輸入信息");}
		$aite_name = "$in{'sousinsaki_name'}";

		&lock;
#錯誤檢查處理
			open(COA,"$couple_file") || &error("$couple_file不能寫上");
				@all_couple = <COA>;
			close(COA);
			$zibun_count = 0;
			$aite_count = 0;
			foreach (@all_couple){
				($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
#cn_yobi1=下次能約會的日期和時間 cn_yobi2=最後的邀請了約會(日期和時間) cn_yobi3=前一個的約會(日期和時間)cn_yobi4=最近的約會的人 cn_kodomo=未使用
				if ($name eq "$cn_name1"){
#結婚OK的情況
					if ($in{'command'} eq "propose_ok"){
						if ($cn_name2 eq "$aite_name"){
							if ($cn_joutai eq "配偶"){&error("這位已經是你的配偶。");}
							$sinkon_number = "$cn_number";
						}
#求婚的情況，迴避作為戀人的錯誤
					}elsif($in{'kokuhaku_syubetu'} eq "propose"){
					
#交往申請，是交往OK的情況
					}else{
						$zibun_count ++;
						if ($cn_name2 eq "$aite_name"){&error("這位已經是你的$cn_joutai。");}
					}
				}
				if ($name eq "$cn_name2"){
#結婚OK的情況
					if ($in{'command'} eq "propose_ok"){
						if ($cn_name1 eq "$aite_name"){
							if ($cn_joutai eq "配偶"){&error("這位已經是你的配偶。");}
							$sinkon_number = "$cn_number";
						}
#求婚的情況，迴避作為戀人的錯誤
					}elsif($in{'kokuhaku_syubetu'} eq "propose"){
#交往OK的情況
					}else{
						$zibun_count ++;
						if ($cn_name1 eq "$aite_name"){&error("這位已經是你的$cn_joutai。");}
					}
				}
#如果未輸入對方的名字
				if ($aite_name eq "$cn_name1" || $aite_name eq "$cn_name2"){
#於結婚OK對方結婚錯誤表示
					if ($in{'command'} eq "propose_ok" && $cn_joutai eq "配偶"){
						&error("這位已經結了婚。");
					}
#求婚的情況，如果對方結婚錯誤表示
					if($in{'kokuhaku_syubetu'} eq "propose" && $cn_joutai eq "配偶"){
						&error("這位已經結了婚。");
					}
					$aite_count ++;
				}
			}		#foreach閉上
			
#結婚OK的情況，是否戀人的檢查
		if ($in{'command'} eq "propose_ok"){
			if ($sinkon_number eq ""){&error("二人不是戀人。");}
#求婚的情況，迴避作為戀人的錯誤		#ver.1.30
		}elsif($in{'kokuhaku_syubetu'} eq "propose"){		#ver.1.30
#交往申請，是交往OK的情況的戀人人數檢查
		}else{
			if($zibun_count >= $koibito_seigen){&error("$name君因為已經與$koibito_seigen人交往而不能再有新的戀人。");}
			if($aite_count >= $koibito_seigen){&error("$aite_name君因為已經與$koibito_seigen人交往而不能再有新的戀人。");}
		}

		open(PR,"$as_profile_file") || &error("Open Error : $as_profile_file");
		@alldata=<PR>;
		close(PR);
		$zibunatta_flg = 0;
		$aiteatta_flg = 0;
		foreach (@alldata){
			($pro_name,$pro_sex)= split(/<>/);
			if ($name eq "$pro_name"){$zibunatta_flg = 1;}
			if ($aite_name eq "$pro_name"){$aiteatta_flg = 1;}
		}
		if ($zibunatta_flg == 0){&error("$name君沒有在戀人介紹所登記。");}
		if ($aiteatta_flg == 0){&error("$aite_name君沒有在戀人介紹所登記。");}

#表白郵件發寄送
		&id_check ($aite_name);
			if ($aite_name eq $name){&error("不能向自己表白");}
			$message_file="./member/$return_id/mail.cgi";
			open(AIT,"$message_file") || &error("對方的郵件記錄文件($message_file)不能打開。");
			$last_mail_check_time = <AIT>;
			@mail_cont = <AIT>;
			close(AIT);
#<>禁止處理
		$in{'m_com'} =~ s/<>/&lt;&gt;/g;
# 評語的換行處理
		$in{'m_com'} =~ s/\r\n/<br>/g;
		$in{'m_com'} =~ s/\r/<br>/g;
		$in{'m_com'} =~ s/\n/<br>/g;
		$m_comment = $in{'m_com'};
		&time_get;
		if ($in{'command'} eq "kousai_ok"){
			$new_mail = "同意交往接收<>$in{'name'}<>$m_comment<>$date2<>$date_sec<><><><><><>\n";
		}elsif ($in{'command'} eq "propose_ok"){
			$new_mail = "答應求婚接收<>$in{'name'}<>$m_comment<>$date2<>$date_sec<><><><><><>\n";
		}elsif ($in{'kokuhaku_syubetu'} eq "propose"){
			$new_mail = "求婚接收<>$in{'name'}<>$m_comment<>$date2<>$date_sec<><><><><><>\n";
		}else{
			$new_mail = "表白接收<>$in{'name'}<>$m_comment<>$date2<>$date_sec<><><><><><>\n";
		}
			unshift (@mail_cont,$new_mail);
#檢查郵件如果沒有最後時間放入1
			if ($last_mail_check_time eq ""){$last_mail_check_time = "1\n";}
			unshift (@mail_cont,$last_mail_check_time);
			
#自己的郵件發送完畢的信息記錄（不是管理者郵件）
		if ($in{'command'} ne "from_system"){
			$my_sousin_file="./member/$k_id/mail.cgi";
			open(ZIB,"$my_sousin_file") || &error("$my_sousin_file不能打開。");
			$my_last_mail_check_time = <ZIB>;
			@my_mail_cont = <ZIB>;
			close(ZIB);
		$my_m_comment = $in{'m_com'};
		if ($in{'command'} eq "kousai_ok"){
			$sousin_mail = "同意交住發送<>$aite_name<>$my_m_comment<>$date2<><><><><><><>\n";
		}elsif ($in{'command'} eq "propose_ok"){
			$sousin_mail = "答應求婚發送<>$aite_name<>$my_m_comment<>$date2<><><><><><><>\n";
		}elsif ($in{'kokuhaku_syubetu'} eq "propose"){
			$sousin_mail = "求婚發送<>$aite_name<>$my_m_comment<>$date2<><><><><><><>\n";
		}else{
			$sousin_mail = "表白發送<>$aite_name<>$my_m_comment<>$date2<><><><><><><>\n";
		}
			unshift (@my_mail_cont,$sousin_mail);
#檢查郵件如果沒有最後時間放入現在的時間
			if ($my_last_mail_check_time eq ""){$my_last_mail_check_time = "$date_sec\n";}
			unshift (@my_mail_cont,$my_last_mail_check_time);
		
#對對方的郵件記錄的寫入處理
			open(OUT,">$message_file") || &error("$message_file不能寫上");
			print OUT @mail_cont;
			close(OUT);
#寫入到自己的郵件記錄處理
			open(ZIBO,">$my_sousin_file") || &error("$my_sousin_file不能寫上");
			print ZIBO @my_mail_cont;
			close(ZIBO);

#是交往回答的情況的戀愛記錄更新
			if ($in{'command'} eq "kousai_ok"){
				&couple_kiroku($name,$aite_name,"戀人","");
#名字１,名字２,狀態,情侶號碼
#街的新聞記錄
				&news_kiroku("戀人","$name君和$aite_name君成為了戀人。");
#結婚回答的情況的戀愛記錄更新
			}elsif ($in{'command'} eq "propose_ok"){
				&couple_kiroku($name,$aite_name,"結婚","$sinkon_number");
				&news_kiroku("結婚","$name君和$aite_name君結婚了。");
#記錄對方的個人記錄的配偶ID為自己的ID
					&id_check($aite_name);
					&openAitelog ($return_id);
					$aite_house_type = "$k_id";
					&aite_temp_routin;
				open(OUT,">$aite_log_file") || &error("$aite_log_file不能打開");
				print OUT $aite_k_temp;
				close(OUT);
			}
		}
		&unlock;
#結婚的情況自己的個人記錄，記錄配偶ID
		if ($in{'command'} eq "propose_ok"){
			$house_type = "$return_id";
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
		}
		if ($in{'command'} eq "kousai_ok"){
			&message_only("與$aite_name君成為了戀人。");
			&hooter("mail_sousin","郵件畫面");
			&hooter("login_view","返回");
		}elsif ($in{'command'} eq "propose_ok"){
			&message_only("與$aite_name君結婚了。");
			&hooter("mail_sousin","郵件畫面");
			&hooter("login_view","返回");
		}elsif ($in{'kokuhaku_syubetu'} eq "propose"){
			&message_only("$aite_name君向您求婚了。");
			&hooter("renai","返回","kekkon.cgi");
		}else{
			&message_only("向$aite_name君表白了。");
			&hooter("assenjo","返回","kekkon.cgi");
		}
	exit;
}

#戀愛記錄的記錄
sub couple_kiroku {
#結婚成立的情況
				if (@_[2] eq "結婚"){
					open(COA,"$couple_file") || &error("$couple_file不能寫上");
						@all_couple = <COA>;
					close(COA);
					foreach (@all_couple){
						($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
						if (@_[3] eq "$cn_number"){
							$cn_joutai = "配偶";
						}
						$couple_tmp = "$cn_number<>$cn_name1<>$cn_name2<>$cn_joutai<>$cn_total_aijou<>$cn_omoide1<>$cn_omoide2<>$cn_omoide3<>$cn_omoide4<>$cn_omoide5<>$cn_kodomo<>$cn_yobi1<>$cn_yobi2<>$cn_yobi3<>$cn_yobi4<>$cn_yobi5<>\n";
						push (@new_all_couple,$couple_tmp);
					}
						open(COP,">$couple_file") || &error("$couple_file不能寫上");
						print COP @new_all_couple;
						close(COP);
#戀人成立的情況
				}elsif (@_[2] eq "戀人"){
					open(CO,"$couple_file") || &error("$couple_file不能寫上");
					$last_couple = <CO>;
					@couple_news = <CO>;
						($new_cn_number,$cn_name1,$cn_name2,$cn_joutai)= split(/<>/,$last_couple);
						$new_cn_number ++;
					close(CO);
					$now_time = time;
					$new_couple_tmp = "$new_cn_number<>@_[0]<>@_[1]<>戀人<>0<>0<>0<>0<>0<>0<>0<>$now_time<><><><><>\n";
					unshift (@couple_news,$last_couple);
					unshift (@couple_news,$new_couple_tmp);
					
					open(COP,">$couple_file") || &error("$couple_file不能寫上");
					print COP @couple_news;
					close(COP);
				}
}

#戀愛指令
sub renai {
	open(COA,"$couple_file") || &error("$couple_file不能寫上");
		@all_couple = <COA>;
	close(COA);
		
	open(REN,"./dat_dir/love.dat") || &error("Open Error : ./dat_dir/love.dat");
	$top_koumoku = <REN>;
	@date_hairetu = <REN>;
	close(REN);
	my (@koumokumei_hairetu)= split(/<>/,$top_koumoku);
#約會的情況
	if ($in{'command'} eq "do_date"){
		$dekityatta = 0;
		$date_aite_iru_flg=0;
		foreach (@all_couple){
			($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
			if ($cn_number eq "$in{'date_aite'}"){
				$date_aite_iru_flg=1;
				if ($name eq "$cn_yobi4"){&error("下次輪到由對方邀請約會。");}
				&time_get;
				if ($cn_yobi1 > $date_sec){&error("暫時不能約會。");}
				if ($name eq "$cn_name1"){$aitenonamae = "$cn_name2";}
				else{$aitenonamae = "$cn_name1";}
				foreach  (@date_hairetu) {
					my ($date_name,$date_dousi,$date_tanosii,$date_h,$date_omosiroi,$date_kandou,$date_oisii,$date_hiyou,$date_kankaku,$kodomo_kakuritu)= split(/<>/);
					if ($date_name eq "$in{'date_koumoku'}"){
							$date_comment .= "$aitenonamae君和$date_dousi<br>";
							if ($date_tanosii){$cn_omoide1 += $date_tanosii; $date_comment .= "$koumokumei_hairetu[2]$date_tanosii。<br>";}
							if ($date_h){$cn_omoide2 += $date_h; $date_comment .= "$koumokumei_hairetu[3]增加了$date_h。<br>";}
							if ($date_omosiroi){$cn_omoide3 += $date_omosiroi; $date_comment .= "$koumokumei_hairetu[4]增加了$date_omosiroi。<br>";}
							if ($date_kandou){$cn_omoide4 += $date_kandou; $date_comment .= "$koumokumei_hairetu[5]增加了$date_kandou。<br>";}
							if ($date_oisii){$cn_omoide5 += $date_oisii; $date_comment .= "$koumokumei_hairetu[6]增加了$date_oisii。<br>";}
					if ($in{'siharaihouhou'} ne "現金"){
						$bank -= $date_hiyou;
						&kityou_syori("信用支付(約會費用)","$date_hiyou","",$bank,"普");
					}else{
						if ($money < $date_hiyou){&error("錢不夠");}
						$money -= $date_hiyou;
					}
							$cn_yobi1= $date_sec + (60*60*$date_kankaku);		#下次能約會的時間
							$cn_yobi3 = "$cn_yobi2";		#前一個的約會
							$cn_yobi2 = "$date_dousi（$date2）";		#最近的約會
#生孩子的事件
							if ($kodomo_kakuritu == 1){
								if ($cn_joutai eq "配偶"){
									$ko_randed=int(rand($kodomo_kakuritu1)+1);
								}elsif ($cn_joutai eq "戀人"){
									$ko_randed=int(rand($kodomo_kakuritu2)+1);
								}
								if ($ko_randed == 1){		#如果孩子出生了
									$dekityatta = 1;
									$cn_yobi2 = "$date_dousi<span class=mainasu>有了孩子！</span>（$date2）";
									$date_comment .= "<div class=mainasu>恭喜恭喜！<br>能有二人之間的孩子了！<br>請看發送了的郵件決定了孩子的名字。</div>";
								}
							}
							$cn_yobi4 = "$name";				#邀請了的人
							$cn_total_aijou = $cn_omoide1 + $cn_omoide2 + $cn_omoide3 + $cn_omoide4 + $cn_omoide5;
							last;
					}		#約會內容一致的情況閉上
				}		#約會內容foreach閉上
			}		#情侶號碼一致之閉上
			$date_tmp = "$cn_number<>$cn_name1<>$cn_name2<>$cn_joutai<>$cn_total_aijou<>$cn_omoide1<>$cn_omoide2<>$cn_omoide3<>$cn_omoide4<>$cn_omoide5<>$cn_kodomo<>$cn_yobi1<>$cn_yobi2<>$cn_yobi3<>$cn_yobi4<>$cn_yobi5<>\n";
			push (@new_all_couple,$date_tmp);
		}		#情侶號碼foreach閉上
		if ($date_aite_iru_flg==0){&error("約會對方沒找到。");}

#記錄更新
		&lock;
#如果有了孩子
		if ($dekityatta == 1){
			&time_get;
			open(KOD,"$kodomo_file") || &error("Open Error : $kodomo_file");
			$last_kodomo = <KOD>;
			@all_kodomo=<KOD>;
			close(KOD);
			($kod_num,$kod_name)= split(/<>/,$last_kodomo);
			$kod_num ++;
			$date_sec_tmp = $date_sec - (60*60*$kosodate_kankaku);
			$new_kodomo_temp = "$kod_num<><>$name<>$aitenonamae<><>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$date_sec_tmp<>$date_sec_tmp<><><>50<>3<>$date_sec_tmp<><><><>\n";
			unshift (@all_kodomo,$last_kodomo);
			unshift (@all_kodomo,$new_kodomo_temp);
#決定孩子的名字的郵件發送
			$my_sousin_file="./member/$k_id/mail.cgi";
			open(ZIB,"$my_sousin_file") || &error("$my_sousin_file不能打開。");
			$my_last_mail_check_time = <ZIB>;
			@my_mail_cont = <ZIB>;
			close(ZIB);
			$sousin_mail = "生孩子<>$aitenonamae<>$kod_num<>$date2<>$date_sec<><><><><><>\n";
			unshift (@my_mail_cont,$sousin_mail);
			unshift (@my_mail_cont,$my_last_mail_check_time);
			
#郵件記錄更新
			open(ZIBO,">$my_sousin_file") || &error("$my_sousin_file不能寫上");
			print ZIBO @my_mail_cont;
			close(ZIBO);
#孩子記錄更新
		open(KODO,">$kodomo_file") || &error("$kodomo_file不能寫上");
		print KODO @all_kodomo;
		close(KODO);
		}		#如果有了孩子閉上
#情侶記錄更新
		open(COP,">$couple_file") || &error("$couple_file不能寫上");
		print COP @new_all_couple;
		close(COP);
		&unlock;
#個人記錄更新
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);
		
	&header("","sonomati");
		print <<"EOM";
		<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
	<span class="job_messe">
	$date_comment
	</span>
	</td></tr></table>
	<br>
EOM
			&hooter("renai","戀愛畫面","kekkon.cgi");
			&hooter("login_view","返回");
	exit;
	}		#約會的情況閉上
#按順序愛愛度分類
	foreach (@all_couple){
			$data=$_;
			$key=(split(/<>/,$data))[4];		#選排序的要素
			push @all_couple_sort,$data;
			push @keys,$key;
	}
		sub bykeys{$keys[$b] <=> $keys[$a];}
		@all_couple_sort=@all_couple_sort[ sort bykeys 0..$#all_couple_sort]; 
	&header(assen_style);
		print <<"EOM";
<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>●能與戀人或配偶約會。但約會需要二人交替邀請。<br>
	●根據約會增加二人的回憶，愛愛度(回憶數值的共計)超過$aijou_kijun，並且全部的回憶數值超過最低基準的$omoide_kijun就能申請結婚。<br>
	●自己或對方有配偶不能結婚。<br>
	●結婚後，能共同擁有配偶住的家的各種設定和店的進貨等（如果二人也有家，不需要賣掉家）。<br>
	●戀人的情況$wakare_limit_koibito日間、配偶的情況$wakare_limit_haiguu星期日間不做約會二人就會分手了。
	</td>
	<td  bgcolor=#ff6633 align=center width=35%><div style="font-size:13px; color:#ffffff">戀　愛</div>
	<div align=center><form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="couple_ranking">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="情侶排名">
	</form></div>
	</td></tr></table><br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="renai">
	<input type=hidden name=command value="do_date">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr bgcolor=#ffcc66>
	<td colspan=3 class=honbun3>請選擇與對方的約會內容。選擇欄裡面是「所需的費用」與「到下次能約會為止的時間」。<br>
	根據約會的內容有不同的概率會有孩子(對方要是配偶$kodomo_kakuritu1分之一，要是戀人$kodomo_kakuritu2分之一的概率)。</td></tr>
	<tr bgcolor=#ffcc66><td align=right>
	對象 <select name="date_aite">
EOM
	my (@my_koibito_hairetu,$my_haiguusya_hairetu);
	$koibito_iru = 0;
	foreach (@all_couple_sort){
		($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
		if ($name eq "$cn_name1"){
				if ($cn_joutai eq "戀人"){
					push (@my_koibito_hairetu,$_);
					print "<option value=\"$cn_number\">$cn_name2</option>";
				}elsif ($cn_joutai eq "配偶"){
					$my_haiguusya_hairetu = "$_";
					print "<option value=\"$cn_number\">$cn_name2</option>";
				}
				$koibito_iru ++; 
		}
		if ($name eq "$cn_name2"){
				if ($cn_joutai eq "戀人"){
					push (@my_koibito_hairetu,$_);
					print "<option value=\"$cn_number\">$cn_name1</option>";
				}elsif ($cn_joutai eq "配偶"){
					$my_haiguusya_hairetu = "$_";
					print "<option value=\"$cn_number\">$cn_name1</option>";
				}
				$koibito_iru ++; 
		}
	}
	if ($koibito_iru == 0){
		print "<option value=\"\">現在沒有交往對象</option>";
	}
	print <<"EOM";
	</selct></td><td align=center>
	約會內容 <select name="date_koumoku">
EOM
	foreach  (@date_hairetu) {
		my ($date_name,$date_dousi,$date_tanosii,$date_h,$date_omosiroi,$date_kandou,$date_oisii,$date_hiyou,$date_kankaku)= split(/<>/);
		print <<"EOM";
	<option value="$date_name">$date_name（$date_hiyou元、$date_kankaku小時）</option>
EOM
	}
	print "</select></td><td>";
	
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
	支払い <select name="siharaihouhou"><option value="現金">現金</option>$siharai_houhou</select>
	<input type=submit value=" O K ">
	</td></tr>
	</table></form>
EOM

#配偶的表示
	if ($my_haiguusya_hairetu ne ""){
		($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/,$my_haiguusya_hairetu);
		if ($cn_name1 eq $name){$haiguusya_name = $cn_name2;}else{$haiguusya_name = $cn_name1;}
		if ($cn_yobi1 < time){$next_d = "<span class=purasu> O K </span>";}else{&byou_hiduke($cn_yobi1);$next_d = "<span class=mainasu>$bh_full_date</span>";}
	print <<"EOM";
	<div class=honbun4 align=center>＜$name君的配偶＞</div>
	<table width="90%" border="0" cellspacing="0" cellpadding="6" align=center class=yosumi>
	<tr bgcolor=#ffffaa>
	<td style="font-size:12px;color:ff3300" width=90 nowrap>$haiguusya_name</td>
	<td><span class=honbun2>愛愛度：$cn_total_aijou</span></td>
	<td><span class=honbun2>$koumokumei_hairetu[2]：</span>$cn_omoide1</td>
	<td><span class=honbun2>$koumokumei_hairetu[3]：</span>$cn_omoide2</td>
	<td><span class=honbun2>$koumokumei_hairetu[4]：</span>$cn_omoide3</td>
	<td><span class=honbun2>$koumokumei_hairetu[5]：</span>$cn_omoide4</td>
	<td><span class=honbun2>$koumokumei_hairetu[6]：</span>$cn_omoide5</td></tr>
	<tr bgcolor=#ffffaa><td colspan=7><hr size=1><span class=honbun2>下次能約會的時間：</span>$next_d<br>
	<span class=honbun2>最近的約會：</span>$cn_yobi2<span class=purasu>$cn_yobi4君。</span><br>
	<span class=honbun2>前一個的約會：</span>$cn_yobi3<br>
	<form method="POST" action="$script">
	<input type=hidden name=mode value="mail_do">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=sousinsaki_name value="$haiguusya_name">
	信息 <input type=text size=64 name=m_com>
	<input type="submit" value=" 發送郵件 ">
	</form>
	</td></tr></table><br><br>
EOM
	}		#配偶的情況在閉上
#戀人的表示
	if (@my_koibito_hairetu != ""){print "<div class=honbun4 align=center>＜$name君的戀人＞</div>";}
	foreach  (@my_koibito_hairetu) {
		($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
		if ($cn_name1 eq $name){$koibito_name = $cn_name2;}else{$koibito_name = $cn_name1;}
		if ($cn_yobi1 < time){$next_d = "<span class=purasu> O K </span>";}else{&byou_hiduke($cn_yobi1);$next_d = "<span class=mainasu>$bh_full_date</span>";}
		if ($cn_yobi4 ne ""){$sasoi_aite_folo = "君邀請。";}else{$sasoi_aite_folo = "";}
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="6" align=center class=yosumi>
	<tr bgcolor=#ffffff>
	<td style="font-size:12px;color:ff3300" width=90 nowrap>$koibito_name</td>
	<td><span class=honbun2>愛愛度：$cn_total_aijou</span></td>
	<td><span class=honbun2>$koumokumei_hairetu[2]：</span>$cn_omoide1</td>
	<td><span class=honbun2>$koumokumei_hairetu[3]：</span>$cn_omoide2</td>
	<td><span class=honbun2>$koumokumei_hairetu[4]：</span>$cn_omoide3</td>
	<td><span class=honbun2>$koumokumei_hairetu[5]：</span>$cn_omoide4</td>
	<td><span class=honbun2>$koumokumei_hairetu[6]：</span>$cn_omoide5</td></tr>
	<tr><td colspan=7><hr size=1><span class=honbun2>下次能約會的時間：</span>$next_d<br>
	<span class=honbun2>最近的約會：</span>$cn_yobi2<span class=purasu>$cn_yobi4$sasoi_aite_folo</span><br>
	<span class=honbun2>前一個的約會：</span>$cn_yobi3<br>
	<form method="POST" action="$script">
	<input type=hidden name=mode value="mail_do">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=sousinsaki_name value="$koibito_name">
	信息 <input type=text size=64 name=m_com>
	<input type="submit" value=" 發送郵件 ">
	</form>
	</td></tr>
EOM
#如果愛愛度和回憶數值超過基準求婚形式輸出
	if ($cn_total_aijou >= $aijou_kijun && $cn_omoide1 >= $omoide_kijun && $cn_omoide2 >= $omoide_kijun && $cn_omoide3 >= $omoide_kijun && $cn_omoide4 >= $omoide_kijun && $cn_omoide5 >= $omoide_kijun && $my_haiguusya_hairetu eq ""){
	print <<"EOM";
	 <tr bgcolor=#ffcccc><td colspan=7><form method="POST" action="$this_script">
	<input type=hidden name=mode value="kokuhaku">
	<input type=hidden name=kokuhaku_syubetu value="propose">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name="sousinsaki_name" value="$koibito_name">
	<span class=mainasu>求婚的言詞</span> <input type=text name=m_com size=70>
	<input type=submit value="求婚"></form>
	</td></tr>
EOM
	}
	print "</table><br><br>";
	}
	&hooter("login_view","返回街");
exit;
}

#決定孩子的名字
sub kodomo_naming {
			open(KOD,"$kodomo_file") || &error("Open Error : $kodomo_file");
			@all_kodomo=<KOD>;
			close(KOD);
			@new_all_kodomo = ();
			$kodomoatta_flg = 0;
			$umu_news = "0";
			foreach (@all_kodomo){
				($kod_num,$kod_name,$kod_oya1,$kod_oya2,$kod_job,$kod_kokugo,$kod_suugaku,$kod_rika,$kod_syakai,$kod_eigo,$kod_ongaku,$kod_bijutu,$kod_looks,$kod_tairyoku,$kod_kenkou,$kod_speed,$kod_power,$kod_wanryoku,$kod_kyakuryoku,$kod_love,$kod_unique,$kod_etti,$kod_yobi1,$kod_yobi2,$kod_yobi3,$kod_yobi4,$kod_yobi5,$kod_yobi6,$kod_yobi7,$kod_yobi8,$kod_yobi9,$kod_yobi10)=split(/<>/);
					if ($kod_num eq "$in{'kod_num'}"){
						$kodomoatta_flg = 1;
#生產的情況
						if ($in{'umu_umanai'} eq "umu"){
							if (length($in{'kodomo_name'}) > 20) {&error("孩子的名字以全角10個字以內。");}
							if ($kod_name ne ""){&error("這個孩子已經附有名字。");}
							$kod_name = "$in{'kodomo_name'}";
							$message_in = "「$kod_name」出生了！";
							$kod_yobi1 = time;
							$umu_news = "1";
							$news_messe = "$kod_oya1君和$kod_oya2君生了孩子。以「$kod_name」命名了。";
#不生的情況刪掉
						}elsif($in{'umu_umanai'} eq "umanai"){
							$message_in = "打下了孩子。";
							$umu_news = "2";
							$news_messe = "$kod_oya1君和$kod_oya2君的孩子打下了。";
							next;
						}
					}
				$kodomo_temp = "$kod_num<>$kod_name<>$kod_oya1<>$kod_oya2<>$kod_job<>$kod_kokugo<>$kod_suugaku<>$kod_rika<>$kod_syakai<>$kod_eigo<>$kod_ongaku<>$kod_bijutu<>$kod_looks<>$kod_tairyoku<>$kod_kenkou<>$kod_speed<>$kod_power<>$kod_wanryoku<>$kod_kyakuryoku<>$kod_love<>$kod_unique<>$kod_etti<>$kod_yobi1<>$kod_yobi2<>$kod_yobi3<>$kod_yobi4<>$kod_yobi5<>$kod_yobi6<>$kod_yobi7<>$kod_yobi8<>$kod_yobi9<>$kod_yobi10<>\n";
				push (@new_all_kodomo,$kodomo_temp);
			}		#foreach閉上
		&lock;
		if ($kodomoatta_flg == 0){&error("這個孩子已經出生或流產。");}
#孩子記錄更新
		open(KODO,">$kodomo_file") || &error("$kodomo_file不能寫上");
		print KODO @new_all_kodomo;
		close(KODO);
#街新聞記錄
		if ($umu_news == 1){
			&news_kiroku("生孩子","$news_messe");
		} elsif ($umu_news == 2){
#			&news_kiroku("死亡","$news_messe");
		}
		&unlock;
		
		&message_only("$message_in");
		&hooter("mail_sousin","郵件畫面");
		&hooter("login_view","返回");
	exit;
}

#育兒
sub kosodate {
	open(KOD,"$kodomo_file") || &error("Open Error : $kodomo_file");
	@all_kodomo=<KOD>;
	close(KOD);

	$monokiroku_file="./member/$k_id/mono.cgi";
	open(MK,"$monokiroku_file") || &error("自己的購買物文件不能打開");
	@my_kounyuu_list =<MK>;
	close(MK);
#參數提高的情況
	if ($in{'command'} eq "do_kosodate"){
		$sodate_taisyou_flg=0;
		foreach (@all_kodomo){
			($kod_num,$kod_name,$kod_oya1,$kod_oya2,$kod_job,$kod_kokugo,$kod_suugaku,$kod_rika,$kod_syakai,$kod_eigo,$kod_ongaku,$kod_bijutu,$kod_looks,$kod_tairyoku,$kod_kenkou,$kod_speed,$kod_power,$kod_wanryoku,$kod_kyakuryoku,$kod_love,$kod_unique,$kod_etti,$kod_yobi1,$kod_yobi2,$kod_yobi3,$kod_yobi4,$kod_yobi5,$kod_yobi6,$kod_yobi7,$kod_yobi8,$kod_yobi9,$kod_yobi10)=split(/<>/);
#$kod_num<>$kod_name<>$kod_oya1<>$kod_oya2<>$kod_job<>$kod_kokugo<>$kod_suugaku<>$kod_rika<>$kod_syakai<>$kod_eigo<>$kod_ongaku<>$kod_bijutu<>$kod_looks<>$kod_tairyoku<>$kod_kenkou<>$kod_speed<>$kod_power<>$kod_wanryoku<>$kod_kyakuryoku<>$kod_love<>$kod_unique<>$kod_etti<>$kod_yobi1<>$kod_yobi2<>$kod_yobi3<>$kod_yobi4<>$kod_yobi5<>$kod_yobi6<>$kod_yobi7<>$kod_yobi8<>$kod_yobi9<>$kod_yobi10
#kod_yobi1=生孩子時間(秒)kod_yobi2=最後育兒了的時間 kod_yobi3=最後的育兒評語 kod_yobi4=總能力值　kod_yobi5=身長 kod_yobi6=體重 kod_yobi7=最後的吃飯時間 kod_yobi8=自立旗標 kod_yobi9=最後育兒了的人
		if ($in{'kod_num'} eq "$kod_num"){
			$sodate_taisyou_flg=1;
			&time_get;
			if (($date_sec - $kod_yobi2) < (60*60*$kosodate_kankaku)){&error("暫時不能育兒。");}
			if ($kod_yobi9  eq "$name"){&error("下次輪到配偶育兒。");}
			$konoagatta_suuti = $in{'par_suuti'}/10;
			if ($in{'nouryoku'} eq "國語") { $kod_kokugo += $konoagatta_suuti; $kokugo -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "數學") { $kod_suugaku += $konoagatta_suuti; $suugaku -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "理科") { $kod_rika += $konoagatta_suuti; $rika -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "社會") { $kod_syakai += $konoagatta_suuti; $syakai -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "英語") { $kod_eigo += $konoagatta_suuti; $eigo -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "音樂") { $kod_ongaku += $konoagatta_suuti; $ongaku -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "美術") { $kod_bijutu += $konoagatta_suuti; $bijutu -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "體力") { $kod_tairyoku += $konoagatta_suuti; $tairyoku -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "健康") { $kod_kenkou += $konoagatta_suuti; $kenkou -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "速度") { $kod_speed += $konoagatta_suuti; $speed -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "力") { $kod_power += $konoagatta_suuti; $power -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "腕力") { $kod_wanryoku += $konoagatta_suuti; $wanryoku -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "腳力") { $kod_kyakuryoku += $konoagatta_suuti; $kyakuryoku -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "容貌") { $kod_looks += $konoagatta_suuti; $looks -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "LOVE") { $kod_love += $konoagatta_suuti; $love -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "有趣") { $kod_unique += $konoagatta_suuti; $unique -=$in{'par_suuti'}; }
			elsif ($in{'nouryoku'} eq "淫蕩") { $kod_etti += $konoagatta_suuti; $etti -=$in{'par_suuti'}; }
			elsif ($in{'syokuryou'}) {
				$syouhinattaflg = 0;
				foreach (@my_kounyuu_list){
					&syouhin_sprit($_);
					if ($in{'syokuryou'} eq "$syo_hinmoku"){
#算出年齡區別概率
						$kono_nenrei = int (($now_time - $kod_yobi1)/(60*60*24));
						if ($kono_nenrei >= 16){$nenreibetu_kakeritu =0.8;}
						elsif  ($kono_nenrei >= 14){$nenreibetu_kakeritu =1;}
						elsif  ($kono_nenrei >= 10){$nenreibetu_kakeritu =1.2;}
						elsif  ($kono_nenrei >= 5){$nenreibetu_kakeritu =1.5;}
						elsif  ($kono_nenrei >= 3){$nenreibetu_kakeritu =2.5;}
						else {$nenreibetu_kakeritu =3.5;}
						$syouhinattaflg = 1;
						$kod_taijuu_hue = $nenreibetu_kakeritu * ($syo_cal / 1000);
						$kod_yobi6 += $kod_taijuu_hue;
						$randed = (int (rand(10)+10))/10;
						$sintyouup = $randed * (($syo_tairyoku + $syo_kenkou + $syo_speed + $syo_power + $syo_wanryoku + $syo_kyakuryoku)/10);
						$kod_yobi5 += $nenreibetu_kakeritu * $sintyouup ;
						if ($syo_taikyuu_tani eq "回"){$syo_taikyuu -- ;}
						$kod_yobi7 = $date_sec;
					}		#商品找到了
				if ($syo_taikyuu <= 0){next;}
				&syouhin_temp;
				push (@new_myitem_hairetu,$syo_temp);
				}		#foreach閉上
				if ($syouhinattaflg == 0){&error("沒有商品。");}
			}else{&error("指示不明確。");}		#吃飯的情況閉上
				if ($kokugo < 0 || $suugaku < 0 || $rika < 0 || $syakai < 0 || $eigo < 0 || $ongaku < 0 || $bijutu < 0 || $looks < 0 || $tairyoku < 0 || $kenkou < 0 || $speed < 0 || $power < 0 || $wanryoku < 0 || $kyakuryoku < 0 || $love < 0 || $unique < 0 || $etti < 0){&error("參數不夠。父母在全部的參數中必須是正數。");}
#更新最後的育兒時間
			$kod_yobi2 = $date_sec;
#記錄最後育兒了的人
			$kod_yobi9 = "$name";
#吃飯的情況
			if ($in{'syokuryou'}){
				$kod_yobi3 = "$name君讓孩子吃了$in{'syokuryou'}($date2)";
				$message_in ="讓$kod_name吃了$in{'syokuryou'}。";
#參數提高的情況
			}else{
				$youikuhi = $konoagatta_suuti * $youikuhiyou;
				$kod_yobi3 = "$name君提昇了孩子的$in{'nouryoku'}參數$konoagatta_suuti($date2)";
				$message_in ="$kod_name的$in{'nouryoku'}參數增加了$konoagatta_suuti。花了$youikuhi元作為養育費。";
				$money -= $youikuhi;
			}
#綜合能力值計算
				$sogo_sisuu = ($kod_yobi5 + $kod_yobi6)/50;
				$kod_yobi4 = int (($kod_kokugo + $kod_suugaku + $kod_rika + $kod_syakai + $kod_eigo + $kod_ongaku + $kod_bijutu + $kod_looks + $kod_tairyoku + $kod_kenkou + $kod_speed + $kod_power + $kod_wanryoku + $kod_kyakuryoku + $kod_love + $kod_unique + $kod_etti)*$sogo_sisuu);
				
			}		#孩子號碼一致的情況閉上
			$new_kodomo_temp = "$kod_num<>$kod_name<>$kod_oya1<>$kod_oya2<>$kod_job<>$kod_kokugo<>$kod_suugaku<>$kod_rika<>$kod_syakai<>$kod_eigo<>$kod_ongaku<>$kod_bijutu<>$kod_looks<>$kod_tairyoku<>$kod_kenkou<>$kod_speed<>$kod_power<>$kod_wanryoku<>$kod_kyakuryoku<>$kod_love<>$kod_unique<>$kod_etti<>$kod_yobi1<>$kod_yobi2<>$kod_yobi3<>$kod_yobi4<>$kod_yobi5<>$kod_yobi6<>$kod_yobi7<>$kod_yobi8<>$kod_yobi9<>$kod_yobi10<>\n";
			push (@new_all_kodomo,$new_kodomo_temp);
		}	#foreach閉上
		if ($sodate_taisyou_flg==0){&error("對象的孩子沒找到。");}
#子供記錄更新
		&lock;
		open(KODO,">$kodomo_file") || &error("$kodomo_file不能寫上");
		print KODO @new_all_kodomo;
		close(KODO);
#更新自己的所有物文件
		if ($in{'syokuryou'}){
					open(OUT,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
					print OUT @new_myitem_hairetu;
					close(OUT);	
		}
		&unlock;
#個人記錄更新
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);

			&message_only("$message_in");
			&hooter("kosodate","育兒畫面","kekkon.cgi");
			&hooter("login_view","返回");
	exit;
	}		#參數提高的情況閉上

	&header(assen_style);
		print <<"EOM";
<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>●把自己的參數培育孩子，能給予食品育兒。但必須與對方交替育兒。<br>
	●吃飯對身長和體重帶來影響，不過與參數沒有關係。<br>
	●給予孩子的參數不能超過自己的10分之一。<br>
	●孩子的參數1需要$youikuhiyou元的養育費。<br>
	●育兒的間隔是$kosodate_kankaku小時。<br>
	●孩子是1日1歲成長，19歲變成自立，變得不再在父母的家。自立後掙錢一定期間有生活補貼。<br>
	●$kodomo_sibou_time日間，不給予孩子進餐孩子會死。
	</td>
	<td  bgcolor=#ff6633 align=center width=35%><div style="font-size:13px; color:#ffffff">育兒</div>
	<div align=center><form method="POST" action="$this_script">
	<input type=hidden name=mode value="assenjo">
	<input type=hidden name=command value="kodomo_ranking">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="孩子排名">
	</form></div>
	</td></tr></table><br>
EOM
#攜帶品形式作成
	$syokuryouattane_flag=0;
	foreach (@my_kounyuu_list){
		&syouhin_sprit ($_);
			if ($syo_taikyuu <=0){next;}
			if ($syo_syubetu ne "食品" && $syo_syubetu ne "快餐食品"){next;}
			$syokuryou_form .= "<option value=\"$syo_hinmoku\">$syo_hinmokuを</option>";
			$syokuryouattane_flag=1;
	}
	if ($syokuryouattane_flag==0){$syokuryou_form .="<option value=\"\">沒有食品</option>";}

#hash代入每職業的工資
	open(SP,"./dat_dir/job.dat") || &error("Open Error : ./dat_dir/job.dat");
	$top_koumoku = <SP>;
	@job_hairetu = <SP>;
	close(SP);
	foreach  (@job_hairetu) {
		&job_sprit($_);
		$job_kihonkyuu {$job_name} = $job_kyuuyo;
	}
	
#孩子的表示
	$now_time= time;
	$kodomoiruka_flag=0;
	foreach  (@all_kodomo) {
				($kod_num,$kod_name,$kod_oya1,$kod_oya2,$kod_job,$kod_kokugo,$kod_suugaku,$kod_rika,$kod_syakai,$kod_eigo,$kod_ongaku,$kod_bijutu,$kod_looks,$kod_tairyoku,$kod_kenkou,$kod_speed,$kod_power,$kod_wanryoku,$kod_kyakuryoku,$kod_love,$kod_unique,$kod_etti,$kod_yobi1,$kod_yobi2,$kod_yobi3,$kod_yobi4,$kod_yobi5,$kod_yobi6,$kod_yobi7,$kod_yobi8,$kod_yobi9,$kod_yobi10)=split(/<>/);
		if ($kod_oya1 eq $name){$konokonooya = $kod_oya2;}elsif($kod_oya2 eq $name){$konokonooya = $kod_oya1;}else{next;}
#孩子沒有名字的情況
	if ($kod_name eq ""){
		print <<"EOM";
		<table width="90%" border="0" cellspacing="0" cellpadding="6" align=center class=yosumi>
		<tr bgcolor=#ffffff><td style="font-size:12px;color:ff3300" width=90 nowrap>跟$konokonooya君的孩子還未出生。</td></tr>
		</table><br><br>
EOM
		$kodomoiruka_flag=1;
		next;
	}
#自立的情況
	if ($kod_yobi8 == 1){
		$kono_nenrei = int (($now_time - $kod_yobi1)/(60*60*24));
		$ima_kasegi = ($job_kihonkyuu {$kod_job} * $kono_nenrei) + ($kod_yobi4 * 10);
		print <<"EOM";
		<table width="90%" border="0" cellspacing="0" cellpadding="6" align=center class=yosumi>
		<tr bgcolor=#ffffff><td style="font-size:12px;color:339933" width=90 nowrap>跟$konokonooya君的孩子「$kod_name」君自立了，成了為「$kod_job」。現在、$kono_nenrei歲，工資:$ima_kasegi元</td></tr>
		</table><br><br>
EOM
		$kodomoiruka_flag=1;
		next;
	}
#孩子有名字的情況
	$kono_nenrei = int (($now_time - $kod_yobi1)/(60*60*24));
	$kod_yobi5 = sprintf ("%.1f",$kod_yobi5);
	$kod_yobi6 = sprintf ("%.1f",$kod_yobi6);
	&check_BMI($kod_yobi5,$kod_yobi6);
	&byou_hiduke($kod_yobi7);
	print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="6" align=center class=yosumi>
	<tr bgcolor=#ffffaa><td colspan=7><span  style="font-size:12px;color:ff3300">$kod_name</span>
	（$kono_nenrei歲）跟$konokonooya君的孩子　<span class="honbun2">最後的育兒：$kod_yobi3</span></td></tr>
	<tr bgcolor=#dddddd><td colspan=7>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="kosodate">
	<input type=hidden name=command value="do_kosodate">
	<input type=hidden name=kod_num value="$kod_num">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<select name=nouryoku>
	<option value="國語">國語參數</option>
	<option value="數學">數學參數</option>
	<option value="理科">理科參數</option>
	<option value="社會">社會參數</option>
	<option value="英語">英語參數</option>
	<option value="音樂">音樂參數</option>
	<option value="美術">美術參數</option>
	<option value="體育">體育參數</option>
	<option value="健康">健康參數</option>
	<option value="速度">速度參數</option>
	<option value="力">力參數</option>
	<option value="腕力">腕力參數</option>
	<option value="腳力">腳力參數</option>
	<option value="容貌">容貌參數</option>
	<option value="LOVE">LOVE參數</option>
	<option value="有趣">有趣參數</option>
	<option value="淫蕩">淫蕩參數</option>
	</select>
	 <select name=par_suuti>
	<option value="10">10</option>
	<option value="50">50</option>
	<option value="100">100</option>
	<option value="200">200</option>
	<option value="300">300</option>
	<option value="500">500</option>
	<option value="800">800</option>
	<option value="1000">1000</option>
	</select>
	　<input type=submit value=" 提昇 ">
	</form>

	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="kosodate">
	<input type=hidden name=command value="do_kosodate">
	<input type=hidden name=kod_num value="$kod_num">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<select name=syokuryou>
	$syokuryou_form
	</select>
	<input type=submit value=" 給予 ">
	</form>
	
	</td></tr>
	<tr><td><span class="honbun2">綜合能力值：</span>$kod_yobi4</td>
	<td>身長：$kod_yobi5 cm</td>
	<td>體重：$kod_yobi6 kg</td>
	<td>身體質量指數：$BMI（$taikei）</td>
	<td>最後的吃飯：$bh_tukihi</td>
	</tr>
	<tr>
	<td>國語：$kod_kokugo</td>
	<td>數學：$kod_suugaku</td>
	<td>理科：$kod_rika</td>
	<td>社會：$kod_syakai</td>
	<td>英語：$kod_eigo</td>
	<td>音樂：$kod_ongaku</td>
	<td>美術：$kod_bijutu</td></tr><tr>
	<td>容貌：$kod_looks</td>
	<td>體力：$kod_tairyoku</td>
	<td>健康：$kod_kenkou</td>
	<td>速度：$kod_speed</td>
	<td>力：$kod_power</td>
	<td>腕力：$kod_wanryoku</td>
	<td>腳力：$kod_kyakuryoku</td></tr><tr>
	<td>LOVE：$kod_love</td>
	<td>有趣：$kod_unique</td>
	<td>淫蕩：$kod_etti</td>
	</tr></table>
	<br><br>
EOM
			$kodomoiruka_flag=1;
	}		#foreach閉上
	if ($kodomoiruka_flag==0){print "<div align=center class=honbun4>現在，沒有孩子。</div>";}
	&hooter("login_view","返回街");
exit;
}

#孩子自立子程序
sub kodomo_ziritu {
			my ($kodziritu_num,$kodziritu_name,$kodziritu_oya1,$kodziritu_oya2,$kodziritu_job,$kodziritu_kokugo,$kodziritu_suugaku,$kodziritu_rika,$kodziritu_syakai,$kodziritu_eigo,$kodziritu_ongaku,$kodziritu_bijutu,$kodziritu_looks,$kodziritu_tairyoku,$kodziritu_kenkou,$kodziritu_speed,$kodziritu_power,$kodziritu_wanryoku,$kodziritu_kyakuryoku,$kodziritu_love,$kodziritu_unique,$kodziritu_etti,$kodziritu_yobi1,$kodziritu_yobi2,$kodziritu_yobi3,$kodziritu_yobi4,$kodziritu_yobi5,$kodziritu_yobi6,$kodziritu_yobi7,$kodziritu_yobi8,$kodziritu_yobi9,$kodziritu_yobi10)=split(/<>/,@_[0]);
	open(SP,"./dat_dir/job.dat") || &error("Open Error : ./dat_dir/job.dat");
	my $top_koumoku = <SP>;
	my @job_hairetu = <SP>;
	close(SP);
#檢查BMI
	&check_BMI($kod_yobi5,$kod_yobi6);
#工資多的按順序分類
	foreach (@job_hairetu){
			$data=$_;
			$key=(split(/<>/,$data))[18];		#選排序的要素
			push @job_hairetu_sort,$data;
			push @ko_keys,$key;
	}
		sub bykeys_up{$ko_keys[$b] <=> $ko_keys[$a];}
		@job_hairetu_sort=@job_hairetu_sort[ sort bykeys_up 0..$#job_hairetu_sort];
#檢索滿足條件的職業
	foreach (@job_hairetu_sort){
		&job_sprit($_);
		if($kodziritu_kokugo < $job_kokugo){next;}
		if($kodziritu_suugaku < $job_suugaku){next;}
		if($kodziritu_rika < $job_rika){next;}
		if($kodziritu_syakai < $job_syakai){next;}
		if($kodziritu_eigo < $job_eigo){next;}
		if($kodziritu_ongaku < $job_ongaku){next;}
		if($kodziritu_bijutu < $job_bijutu){next;}
		if($BMI < $job_BMI_min){next;}
		if ($job_BMI_max) { if($BMI > $job_BMI_max){next;}}
		if($kodziritu_looks < $job_looks){next;}
		if($kodziritu_tairyoku < $job_tairyoku){next;}
		if($kodziritu_kenkou < $job_kenkou){next;}
		if($kodziritu_speed < $job_speed){next;}
		if($kodziritu_power < $job_power){next;}
		if($kodziritu_wanryoku < $job_wanryoku){next;}
		if($kodziritu_kyakuryoku < $job_kyakuryoku){next;}
		if($kodziritu_love < $job_love){next;}
		if($kodziritu_unique < $job_unique){next;}
		if($kodziritu_etti < $job_etti){next;}
		if($kodziritu_yobi5 < $job_sintyou){next;}
		last;
	}	#foreach閉上
		if ($job_name eq ""){$job_name = "流浪者";}
		$return_job = $job_name;
	&lock;
		&news_kiroku("就業","$kodziritu_oya1君和$kodziritu_oya2君的孩子「$kod_name」君自立了，成為$job_name。");
	&unlock;
}

#離婚時配偶的ID刪掉處理
sub kekkon_id_sakujo {
		&id_check(@_[0]);
		&openAitelog ($return_id);
		$aite_house_type = "";
		&aite_temp_routin;
				open(OUT,">$aite_log_file") || &error("$aite_log_file不能打開");
				print OUT $aite_k_temp;
				close(OUT);
}
