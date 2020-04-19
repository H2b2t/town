sub town_no_get {
#街信息變量代入
	if (@_[0] eq ""){
#沒有指定街的名字的情況(登入時)自己的家的街檢查
		if ($in{'name'}){
			open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
			@ori_ie_para = <IN>;
			close(IN);
			$iearuflag = 0;
			foreach (@ori_ie_para){
					&ori_ie_sprit($_);
					if ($ori_ie_name eq "$in{'name'}"){$this_town_no = $ori_ie_town; $iearuflag=1; last;}
			}
			if ($iearuflag == 0){$this_town_no = 0;}
#沒有指定街的名字的情況(首頁的訪問)
		}else{$this_town_no = 0;}
#有指定那個街就打開的記錄
	}else{
		$this_town_no = @_[0];
	}
	
	if (! $in{'town_no'}){$in{'town_no'} = "$this_town_no";}
}

##########批發店的輸出
#####建築
sub kentiku {
	&header(kentiku_style);
	$i = 0;
	foreach (@town_hairetu){
		$mati_sentaku .= "街的名字<option value=$i>$_</option>\n";
		$mati_kakunin_open .= "<a href=$script?town_no=$i target=_blank>☆$_　</a>";
		$i ++;
	}
	$i = 21;
	foreach (A..M){
		$tateziku .= "縱軸<option value=$i>$_</option>\n";
		$i += 17;
	}
	foreach (1..16){
		$yokoziku .= "横軸<option value=$_>$_</option>\n";
	}
	
#從hash展開家的畫像
	while(($ie_key,$ie_val) = each %ie_hash){
			push @ie_keys,$ie_key;
			push @ie_values,$ie_val;
	}
		sub by_iekey{$ie_values[$a] <=> $ie_values[$b];}
		@ie_rank=@ie_keys[ sort by_iekey 0..$#ie_keys]; 
	$i=1;
	foreach(@ie_rank){
		$iegazou .= "<td align=center><input type=radio name=iegazou value=$_><br><img src=\"$img_dir/$_\" width=32 height=32><br>$ie_hash{$_}萬元\n";
		if ($i % 8 == 0){$iegazou .= "</tr><tr>";}
		$i ++;
	}
			print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>能在喜歡的街喜歡的地方的空地空間建造自己的家。<br>
	建築費用是「那個街的地價」+「家的價格(外裝費)+」「內裝費(排位A～D)」。有家的話，以後登入時最初去到的是那個街。</td>
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/kentiku_tytle.gif"></td>
	</tr></table><br>
	<form method="POST" action="$script">
	<input type=hidden name=mode value="kentiku_do">
	<input type=hidden name=command value="kakunin">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="80%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr><td valign=top>
	<div class=honbun2>●指定建的地方。家是只能在<img src=$img_dir/akiti.gif width=32 height=32>的地方建造。</div><br>
	街的名字 <select name="mati_sentaku">$mati_sentaku</select>
	縱軸 <select name="tateziku">$tateziku</select>
	橫軸 <select name="yokoziku">$yokoziku</select><br>
	▼不清楚SALE的地方，打開下面各街的連結確認。<br>
	$mati_kakunin_open<br><br>
	<div class=honbun2>●家的選擇</div>
	<table boader=0 cellspacing="0" cellpadding="5" width=100%><tr>
	$iegazou
	</tr></table>
	</td></tr><tr><td>
	<br><div class=honbun2>●指定家的排位(內裝費)。</div><br>
	<input type=radio name=matirank value="0">Ａ排位：$housu_nedan[0]萬元（可以同時擁有４個空間）<br>
	<input type=radio name=matirank value="1">Ｂ排位：$housu_nedan[1]萬元（可以同時擁有３個空間）<br>
	<input type=radio name=matirank value="2">Ｃ排位：$housu_nedan[2]萬元（可以同時擁有２個空間）<br>
	<input type=radio name=matirank value="3">Ｄ排位：$housu_nedan[3]萬元（可以同時擁有１個空間）<br><br>
	※建造自己的家，能在家中設置以下的內容。<br><br>
	<font color=#ff6600>○簡易留言板</font>：不用說就知是是訪問了戶主家的人都能寫入的留言板。<br>
	<font color=#ff6600>○商賣空間</font>：從批發商購入自己喜歡的商品，能自由設定價格銷售(預想將來可能會開設學校和體育管等其他的買賣功能)。<br>
	<font color=#ff6600>○獨自URL空間</font>：指定自己喜歡的URL，能表示IFRAME窗口。根據想法自己的家要怎樣的內容也可以，推薦作為自己的個人網頁。<br>
	<font color=#ff6600>○戶主留言板</font>：只供管理者寫入能的留言板。發表日記和小品文等自己的文章<br><br>
	D級自上述內容只能選一個設置，而A級能設置全部的內容。<br>同時，全部的家都放置了「錢箱」供訪問者自由投放金錢。
EOM


	print <<"EOM";
	<br><br><div align="center"><input type=submit value=" 確認畫面  "></div>
	</td></tr></table>
	<div align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
	</body></html>
EOM
	exit;
}

#######施工作業
sub kentiku_do {
#確認畫面輸出
	if ($in{'command'} eq "kakunin"){
		&main_view($in{'mati_sentaku'});
		exit;
	}
	if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
		if ($in{'kensetu_hiyou'} * 10000 > $money){&error("錢不夠。");}
	}
	&lock;
#給家名單的寫入
	open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		@ori_ie_para = <IN>;
	close(IN);
		foreach (@ori_ie_para){
				&ori_ie_sprit($_);
				if ($in{'ori_k_id'} eq "$ori_k_id"){&error("家是一人只能建造1所。搬家的情況，請從家管理畫面賣掉了家的以後重新購買。");}
		}
	&time_get;
	$ori_ie_temp = "$in{'ori_k_id'}<>$in{'name'}<>『$in{'name'}』的家<>$in{'ori_ie_image'}<><>$date_sec<>$in{'ori_ie_town'}<>$in{'ori_ie_tateziku'}<>$in{'ori_ie_yokoziku'}<>$in{'ori_ie_sentaku_point'}<>$in{'ori_ie_rank'}<><><><><>\n";
	unshift (@ori_ie_para,$ori_ie_temp);

#在town信息裡寫入
	$write_town_data = "./log_dir/townlog".$in{'ori_ie_town'}.".cgi";
	open(TWI,"$write_town_data") || &error("Open Error : $write_town_data");
	$hyouzi_town_hairetu = <TWI>;
	close(TWI);
		@town_sprit_matrix =  split(/<>/,$hyouzi_town_hairetu);
		if ($town_sprit_matrix[$in{'ori_ie_sentaku_point'}] ne "空地"){&error("選擇了的地方不是空地。其他可能是已被購買了。");}
		$town_sprit_matrix[$in{'ori_ie_sentaku_point'}] = "$in{'ori_k_id'}";
		$town_temp=join("<>",@town_sprit_matrix);
#town信息更新
	open(TWO,">$write_town_data") || &error("$write_town_data不能寫上");
	print TWO $town_temp;
	close(TWO);

#家名單更新
	open(OIO,">$ori_ie_list") || &error("$ori_ie_list不能寫上");
	print OIO @ori_ie_para;
	close(OIO);
#新聞記錄
	&news_kiroku("家","$in{'name'}君於「$town_hairetu[$in{'ori_ie_town'}]」建築了家。");		#ver.1.3

	&unlock;
#記錄更新
	if ($in{'pass'} ne "$admin_pass" || $in{'name'} ne "$admin_name"){
		$money -= $in{'kensetu_hiyou'} * 10000;
	}
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			
&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
恭喜恭喜！<br>
於 $town_hairetu[$in{'ori_ie_town'}] 建築了家。<br>
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


######批發商
sub orosi {
open(IN,"$maintown_logfile") || &error("Open Error : $maintown_logfile");
	$maintown_para = <IN>;
	&main_town_sprit($maintown_para);
close(IN);
		if($mt_orosiflag == 0){
				&time_get;
##批發旗標以０過掉著規定時間
				if($return_hour >= "$mt_t_time"){
	&lock;
#批發旗標為１更新主要town記錄
			$mt_orosiflag = 1;
			$mt_yobi9 = $date2;		#記錄批發更新日的時候
			&main_town_temp;
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			print OUT $mt_temp;
			close(OUT);	
#打開商品數據記錄
			open(OL,"./dat_dir/syouhin.dat") || &error("Open Error : ./dat_dir/syouhin.dat");
			$top_koumoku = <OL>;
#商品排列到random換更新記錄
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
	
	&unlock;
				}		#if（商品換入新品時間過去時的情況）的閉上
		}		#if（批發旗標是0的情況）的閉上

#批發商品的表示
	open(IN,"$orosi_logfile") || &error("Open Error : $orosi_logfile");
		@kyouno_hairetu = <IN>;
	close(IN);
	&header(orosi_style);
#ver.1.3從這裡
#unit hash 代入個人的家信息
	open(OI,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
	@ori_ie_hairetu = <OI>;
	foreach (@ori_ie_hairetu) {
			&ori_ie_sprit($_);
			$unit{"$ori_k_id"} = "1";
	}
	close(OI);
	if ($in{'iesettei_id'} eq $k_id){
		&my_omise_orosi_rou;
	}elsif ($in{'iesettei_id'} eq $house_type && $house_type != ""){
		&haiguusya_omise_orosi_rou;
	}else{
		if ($unit{"$k_id"} != ""){
			&my_omise_orosi_rou;
			$in{'iesettei_id'} = $k_id;
		}elsif($unit{"$house_type"} != ""){
			&haiguusya_omise_orosi_rou;
			$in{'iesettei_id'} = $house_type;
		}else{
			$orosisakinomise = "因為沒有店所以不能進貨。";
			$settei_t_color = "#888888";
			$misearuyoflag = "nasi";
		}
	}
	
sub my_omise_orosi_rou {
		$orosisakinomise = "自己的店的進貨。";
		$settei_t_color = "#336699";
		if ($unit{"$house_type"} != ""){
			$change_form = "<form method=POST action=\"$script\"><input type=hidden name=mode value=orosi><input type=hidden name=iesettei_id value=\"$house_type\"><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=submit value=\"配偶的店的進貨\"></form>";
		}
}

sub haiguusya_omise_orosi_rou {
		$orosisakinomise = "配偶的店的進貨。";
		$settei_t_color = "#ff6666";
		if ($unit{"$k_id"} != ""){
			$change_form = "<form method=POST action=\"$script\"><input type=hidden name=mode value=orosi><input type=hidden name=iesettei_id value=\"$k_id\"><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=submit value=\"自己的店的進貨\"></form>";
		}
}

#自己的商品庫存檢查
	$omise_log_file="./member/$in{'iesettei_id'}/omise_log.cgi";
	open(MKF,"$omise_log_file");
	@my_item_list = <MKF>;
	close(MKF);
	foreach (@my_item_list){
			&syouhin_sprit($_);
			$my_omise_zaiko_itiran .= "○$syo_hinmoku $syo_zaiko個　";
	}
#ver.1.3到這裡
#ver.1.30從這裡
	print <<"EOM";
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>自己的店能通過這裡購入商品(沒有店的話購買也沒有意義)。想購買的商品核取之後，在頁最底指定數量後按「OK」按鈕。商品供應是每天1次，不過時間是random。同時，錢在一般自戶口扣下。
	<div class=honbun2>最後批發商品更新日時：$mt_yobi9</div>
	<font color=#ff6600>※在店的種類以外的商品不能購買。選擇超市，為這裡表示的價格的1.5倍。<br>
	※店能放的商品項目數是$mise_zaiko_gendo。<br>
	※一種商品的存貨上限的庫存數是$mise_zaiko_limit。</font></td>
	<td  bgcolor=#333333 align=center><img src="$img_dir/orosi_tytle.gif"></td>
	</tr></table><br>
	<!--ver.1.3從這裡-->
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi>
	<tr bgcolor=$settei_t_color><td>
	<div  align=center style="color:#ffffff;font-size:13px;">$orosisakinomise</div>
	<div  align=left style="color:#ffffff;font-size:10px;">現在的庫存狀況：$my_omise_zaiko_itiran</div>
	</td>
	<td>$change_form</td>
	</tr></table><br>
	<!--ver.1.3到這裡-->
	<table width="100%" border="0" cellspacing="1" cellpadding="5" align=center class=yosumi>
	<tr><td colspan=27><font color=#336699>凡例：(國)＝國語up值、(數)＝數學up值、(理)＝理科up值、(社)＝社會up值、(英)＝英語up值、(音)＝音樂up值、(美)＝美術up值、（容）=容貌up值、（體）=體力up值、（健）=健康up值、（速）=速度up值、（力）=力up值、（腕）=腕力up值、（腳）=腳力up值、（愛）=LOVEup值、（趣）=有趣up值、（淫）=淫蕩up值<br>
	※耐久，○○回是能使用的回數，而○○日是能使用的日數。</font></td></tr>
EOM

		print <<"EOM";
	<form method="POST" action="$script">
	<input type=hidden name=mode value="buy_orosi">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
EOM
	foreach (@kyouno_hairetu){
		&syouhin_sprit($_);
			if($syo_zaiko <= 0){
					$syo_zaiko = "賣光";
					$kounyuubotan = "";
			}else{
					if ($misearuyoflag eq "nasi"){
						$syo_zaiko = "不可購買";
						$kounyuubotan = "";
					}else{
						$kounyuubotan = "<input type=radio name=syo_hinmoku value=\"$syo_hinmoku,&,$syo_nedan,&,$syo_zaiko,&,$syo_syubetu\">";
					}
			}
			if($syo_cal > 0){$calory_hyouzi = "$syo_cal kcal";}else{$calory_hyouzi = "ー";}
			if ($maeno_syo_syubetu ne "$syo_syubetu"){
				print <<"EOM";
				<tr bgcolor=#ffff66><td colspan=27>▼$syo_syubetu</td></tr>
		<tr bgcolor=#cc9966><td align=center  width=170>商品</td><td align=center nowrap>庫存</td><td align=center>價格</td><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td align=center nowrap>卡路里</td><td align=center nowrap>耐久</td><td align=center>使用<br>間隔</td><td align=center>身體<br>能量<br>消費</td><td align=center>頭腦<br>能量<br>消費</td><td align=center nowrap>　備　考　</td></tr>
EOM
			}
			$taikyuu_hyouzi_seikei = "$syo_taikyuu"."$syo_taikyuu_tani";
		print <<"EOM";
	<tr bgcolor=#cccc99><td align=left>$kounyuubotan$syo_hinmoku</td><td align=right nowrap>$syo_zaiko</td><td align=right nowrap>$syo_nedan元</td><td>$syo_kokugo</td><td>$syo_suugaku</td><td>$syo_rika</td><td>$syo_syakai</td><td>$syo_eigo</td><td>$syo_ongaku</td><td>$syo_bijutu</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td align=right>$calory_hyouzi</td><td nowrap>$taikyuu_hyouzi_seikei</td><td nowrap>$syo_kankaku分</td><td>$syo_sintai_syouhi</td><td>$syo_zunou_syouhi</td><td align=left>$syo_comment</td></tr>
EOM
		$maeno_syo_syubetu = "$syo_syubetu";
	}		#foreach閉上
	if ($misearuyoflag ne "nasi"){
		print <<"EOM";
	<tr><td align=center colspan=27>購入數 <input type=\"text\" name=\"kounyuusuu\" size=10>　<input type=submit value="OK"></td></tr>
	</table></form>
EOM
	}else{print "</table></form>";}		#ver.1.40
#ver.1.30到這裡
	&hooter("login_view","返回");
	exit;
}

#####批發商品購買處理
sub buy_orosi {
	if ($in{'kounyuusuu'} < 1){&error("購入數不妥");}
	if($in{'kounyuusuu'} =~ /[^0-9]/){&error("購入數請用半角數字輸入");}
	($katta_syouhin,$katta_nedan,$imano_zaiko,$orosi_syubetu) = split(/,&,/,$in{'syo_hinmoku'});
	if ($in{'kounyuusuu'} > $imano_zaiko){&error("沒那麼多庫存");}
	if ($in{'kounyuusuu'} > $mise_zaiko_limit){&error("店能放的庫存的上限是$mise_zaiko_limit。");}
	open(IN,"$orosi_logfile") || &error("Open Error : $orosi_logfile");
		@kyouno_hairetu = <IN>;
	close(IN);
	foreach (@kyouno_hairetu){
		&syouhin_sprit($_);
			if($katta_syouhin eq "$syo_hinmoku"){
				if($syo_zaiko <= 0){&error("沒有庫存");}
			}
	}
	$katta_total_gaku = $katta_nedan * $in{'kounyuusuu'};
	if ($katta_total_gaku > $bank){&error("一般戶口的錢不夠");}
#檢查自己的店的類別
	$omise_settei_file="./member/$in{'iesettei_id'}/omise_ini.cgi";
		open(OIB,"$omise_settei_file") || &error("店設定文件不能打開。請確認是否已在家開設了店");
			$omise_settei_data = <OIB>;
			($omise_title,$omise_come,$omise_body_style,$omise_syubetu)= split(/<>/,$omise_settei_data);
		close(OIB);
		if ($omise_syubetu ne "超市"){
			if ($omise_syubetu ne "$orosi_syubetu"){&error("不能在你的店處理這個商品");}
		}
		if ($omise_syubetu eq "超市"){
			$katta_nedan *= 1.5;
			$katta_total_gaku *= 1.5;
		}
		
#檢查自己的商品庫存文件是否有那個商品
	$omise_log_file="./member/$in{'iesettei_id'}/omise_log.cgi";
	open(MKF,"$omise_log_file") || &error("自己的商品庫存文件不能打開");
	@my_item_list = <MKF>;
	close(MKF);
	$motteru_flag =0;
	$my_mise_zaiko = 0;
#持有辨別(持有庫存平衡)商品項目數的點數
	foreach (@my_item_list){
		&syouhin_sprit($_);
#如果持有
		if ($katta_syouhin eq "$syo_hinmoku"){
			if($omise_syubetu eq "超市" && $syo_comment =~ /専門店限定商品/){&error("這個商品在$orosi_syubetu專門店以外不能購買。");}		#ver.1.30
						$syo_zaiko += $in{'kounyuusuu'};
						if ($syo_zaiko > $mise_zaiko_limit){&error("店能放的庫存的上限是$mise_zaiko_limit。");}	#ver.1.3
						$bank -= $katta_total_gaku;
						$motteru_flag =1;
		}
		if ($syo_zaiko <= 0) {next;}
		&syouhin_temp;
		$my_mise_zaiko ++;
		push (@new_myitem_list,$syo_temp);
	}		#foreach閉上
#物品種類要是限度以上同樣的物品也不可以買的處理
	if($douitem_ok == 1){
		if ($my_mise_zaiko >= $mise_zaiko_gendo){&error("因為超越店能放的商品項目數($mise_zaiko_gendo)暫時不能進貨。");}
	}
#沒有的情況(批發log file每參數拷貝)
	if ($motteru_flag ==0){
		if ($my_mise_zaiko >= $mise_zaiko_gendo){&error("店能放的商品項目數是$mise_zaiko_gendo。");}
		open(SP,"$orosi_logfile") || &error("Open Error : $orosi_logfile");
		@kounyuu_hairetu = <SP>;
		close(SP);
		$kounyuu_ok = 0;
		foreach (@kounyuu_hairetu){
			&syouhin_sprit($_);
			if ($katta_syouhin eq "$syo_hinmoku"){
			if($omise_syubetu eq "超市" && $syo_comment =~ /専門店限定商品/){&error("這個商品在$orosi_syubetu專業店以外不能購買。");}		#ver.1.30
#記錄購買日
					$syo_kounyuubi = time;
					$syo_zaiko = $in{'kounyuusuu'};
					&syouhin_temp;
					push (@new_myitem_list,$syo_temp);
					$bank -= $katta_total_gaku;
					$kounyuu_ok = 1;
					last;
			}
		}
		if ($kounyuu_ok == 0){&error("不能購買。");}
		
	}		#沒有的情況閉上
	
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
#記帳
			&kityou_syori("進貨($katta_syouhin×$in{'kounyuusuu'})","$katta_total_gaku","",$bank,"普");
			
#自己的購買物文件的備份記錄更新
	&lock;
	open(MK,">$omise_log_file") || &error("自己的商品庫存文件不能寫上");
	print MK @new_myitem_list;
	close(MK);
	
			
#設置批發商的殘餘數
	open(SYO,"$orosi_logfile") || &error("Open Error : $orosi_logfile");
		@depa_zan = <SYO>;
	close(SYO);
	@new_depa_zan=();
	foreach (@depa_zan){
		&syouhin_sprit($_);
		if($katta_syouhin eq "$syo_hinmoku"){
			$syo_zaiko -= $in{'kounyuusuu'} ;
		}
		&syouhin_temp;
		push (@new_depa_zan,$syo_temp);
	}

	open(OLOUT,">$orosi_logfile") || &error("$orosi_logfile不能寫入");
	print OLOUT @new_depa_zan;
	close(OLOUT);

	&unlock;

&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
●購入了$katta_syouhin（$katta_nedan元×$in{'kounyuusuu'})（進貨總額：$katta_total_gaku元）。
</span>
</td></tr></table>
<br>
	<form method=POST action="$script">
	<input type=hidden name=mode value="orosi">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">		<!--ver.1.3-->
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="繼續進貨">
	</form>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form>
	</div>

	</body></html>
EOM
exit;
}

#######體育俱樂部
sub gym {
	open(SP,"./dat_dir/gym.dat") || &error("Open Error : ./dat_dir/gym.dat");
	$top_koumoku = <SP>;
	@gym_hairetu = <SP>;
	close(SP);
	&header(gym_style);
	&gym_sprit($top_koumoku);
	$toremadeatonanbyou = $next_tra - time;
	if($toremadeatonanbyou > 0){$tore_messe = "$name君到可以練習是$toremadeatonanbyou秒以後。";}else{$tore_messe = "今天鍛鍊身體吧。";}
	print <<"EOM";
	<table width="100%" border="0" cellspacing="0" cellpadding="10"><tr><td width="554" >
	<form method="POST" action="$script" NAME="foMes5">		<!--ver.1.2-->
	<INPUT TYPE="hidden" NAME="TeMes5">		<!--ver.1.2-->
	<input type=hidden name=mode value="training">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td colspan=8 bgcolor=#ffffff>$tore_messe<br></td>
	<td colspan=4 bgcolor=#333333 align=center><img src="$img_dir/gim_tytle.gif"></td>
	</tr>
	<tr><td colspan=13><font color=#336699>凡例：(容)＝容貌up值、(體)＝體力up值、(健)＝健康up值、(速)＝速度up值、(力)＝力up值、(腕)＝腕力up值、(腳)＝腳力up值、(淫)＝淫蕩up值、(間)＝下次能練習的間隔、(消)＝消費的身體力</font></td></tr>
	<tr bgcolor=#ffff66><td align=center>$gym_name</td><td>$gym_looks</td><td>$gym_tairyoku</td><td>$gym_kenkou</td><td>$gym_speed</td><td>$gym_power</td><td>$gym_wanryoku</td><td>$gym_kyakuryoku</td><td>$gym_etti</td><td align=center>$gym_nedan</td><td>$gym_kankaku</td><td>$gym_syouhi</td></tr>
EOM
	foreach $gym_hyouzi (@gym_hairetu) {
			&gym_sprit($gym_hyouzi);
		print <<"EOM";
	<tr><td nowrap><input type=radio value="$gym_name" name="tra_menu">$gym_name</td><td>$gym_looks</td><td>$gym_tairyoku</td><td>$gym_kenkou</td><td>$gym_speed</td><td>$gym_power</td><td>$gym_wanryoku</td><td>$gym_kyakuryoku</td><td>$gym_etti</td><td align=right>$gym_nedan元</td><td>$gym_kankaku分</td><td align=right>$gym_syouhi</td></tr>
EOM
	}
	print <<"EOM";
	<tr><td colspan=12><div align=center><input type=submit value=" O K "></div></td>
	</table></form></td><td valign=top>
EOM
	&loged_gamen;
	print "</td></tr></table>";
	&hooter("login_view","返回");
	exit;
}

####練習
sub training {
	open(SP,"./dat_dir/gym.dat") || &error("Open Error : ./dat_dir/gym.dat");
	$top_koumoku = <SP>;
	@gym_hairetu = <SP>;
	close(SP);
	foreach $gym_hyouzi (@gym_hairetu) {
			&gym_sprit($gym_hyouzi);
			if($in{'tra_menu'} eq "$gym_name"){
				$now_time = time;
				if($energy < $gym_syouhi){&error("身體力不夠。");}
				if($next_tra > $now_time){&error("暫時不能練習。");}
				if($money < $gym_nedan){&error("錢不夠。");}
				
				if($gym_looks){$looks += $gym_looks; $print_messe .= "・容貌值$gym_looks提高。<br>";}
				if($gym_tairyoku){$tairyoku += $gym_tairyoku; $print_messe .= "・體力$gym_tairyoku提高。<br>";}
				if($gym_kenkou){$kenkou += $gym_kenkou; $print_messe .= "・健康值$gym_kenkou提高。<br>";}
				if($gym_speed){$speed += $gym_speed; $print_messe .= "・速度$gym_speed提高。<br>";}
				if($gym_power){$power += $gym_power; $print_messe .= "・力$gym_power提高。<br>";}
				if($gym_wanryoku){$wanryoku += $gym_wanryoku; $print_messe .= "・腕力$gym_wanryoku提高。<br>";}
				if($gym_kyakuryoku){$kyakuryoku += $gym_kyakuryoku; $print_messe .= "・腳力$gym_kyakuryoku提高。<br>";}
				if($gym_etti){$etti += $gym_etti; $print_messe .= "・淫蕩度$gym_etti提高。<br>";}

				$next_tra = $now_time + ($gym_kankaku*60);
				$energy -= $gym_syouhi;$print_messe .= "・使用了$gym_syouhi的身體能源。<br>";
				$taijuu_heri = $gym_syouhi / 100;
				$taijuu -= $taijuu_heri; $print_messe .= "・$taijuu_heri kg體重減少了。<br>";
				$money -= $gym_nedan;
				last;
			}
	}
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
●以$in{'tra_menu'}鍛鍊了身體。<br>
$print_messe
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


#######學校
sub school {
	open(SP,"./dat_dir/school.dat") || &error("Open Error : ./dat_dir/school.dat");
	$top_koumoku = <SP>;
	@school_hairetu = <SP>;
	close(SP);
	&header(school_style);
	&school_sprit($top_koumoku);
	&time_get;
	if ($date eq "$last_school"){$tore_messe = "能聽講義是１日１次。今天聽的講義結束了。"; $sc_check = "out";}else{$tore_messe = "今日も頑張って勉強しましょう。";$sc_check = "ok";}
	print <<"EOM";
	<table width="100%" border="0" cellspacing="0" cellpadding="10"><tr><td width="554" >
	<form method="POST" action="$script" NAME="foMes5">		<!--ver.1.2-->
	<INPUT TYPE="hidden" NAME="TeMes5">		<!--ver.1.2-->
	<input type=hidden name=mode value="do_school">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=sc_check value="$sc_check">
	<table width="100%" border="0" cellspacing="0" cellpadding="10" class=yosumi>
	<tr>
	<td colspan=7 bgcolor=#ffffff>$tore_messe<br></td>
	<td colspan=3 bgcolor=#333333 align=center><img src="$img_dir/school_tytle.gif"></td>
	</tr>
	<tr bgcolor=#ffff66 align=center><td align=center>$sc_name</td><td nowrap>$sc_kokugo</td><td nowrap>$sc_suugaku</td><td nowrap>$sc_rika</td><td nowrap>$sc_syakai</td><td nowrap>$sc_eigo</td><td nowrap>$sc_ongaku</td><td nowrap>$sc_bijutu</td><td>$sc_nedan</td><td>$sc_syouhi</td></tr>
EOM
	foreach  (@school_hairetu) {
			&school_sprit($_);
		print <<"EOM";
	<tr align=center><td nowrap align=left><input type=radio value="$sc_name" name="sc_name">$sc_name</td><td>$sc_kokugo</td><td>$sc_suugaku</td><td>$sc_rika</td><td>$sc_syakai</td><td>$sc_eigo</td><td>$sc_ongaku</td><td>$sc_bijutu</td><td align=right nowrap>$sc_nedan元</td><td>$sc_syouhi</td></tr>
EOM
	}
	print <<"EOM";
	<tr><td colspan=10><div align=center><input type=submit value=" O K "></div></td>
	</table></form></td><td valign=top>
EOM
	&loged_gamen;
	print "</td></tr></table>";
	&hooter("login_view","返回");
	exit;
}

####接受講習
sub do_school {
	if($in{'sc_check'} eq "out"){&error("今天的聽講結束了。");}
	&time_get;		#ver.1.2
	if ($date eq "$last_school"){&error("今天的聽講結束了。");}		#ver.1.2
	open(SP,"./dat_dir/school.dat") || &error("Open Error : ./dat_dir/school.dat");
	$top_koumoku = <SP>;
	@school_hairetu = <SP>;
	close(SP);
	foreach  (@school_hairetu) {
			&school_sprit($_);
			if($in{'sc_name'} eq "$sc_name"){
				if($nou_energy < $sc_syouhi){&error("頭腦力不夠。");}
				if($money < $sc_nedan){&error("錢不夠。");}
				if($sc_kokugo){$kokugo += $sc_kokugo; $print_messe .= "・國語$sc_kokugo提高。<br>";}
				if($sc_suugaku){$suugaku += $sc_suugaku; $print_messe .= "・數學$sc_suugaku提高。<br>";}
				if($sc_rika){$rika += $sc_rika; $print_messe .= "・理科$sc_rika提高。<br>";}
				if($sc_syakai){$syakai += $sc_syakai; $print_messe .= "・社會$sc_syakai提高。<br>";}
				if($sc_eigo){$eigo += $sc_eigo; $print_messe .= "・英語$sc_eigo提高。<br>";}
				if($sc_ongaku){$ongaku += $sc_ongaku; $print_messe .= "・音樂$sc_ongaku提高。<br>";}
				if($sc_bijutu){$bijutu += $sc_bijutu; $print_messe .= "・美術$sc_bijutu提高。<br>";}
				&time_get;
				$last_school = $date;
				$nou_energy -= $sc_syouhi;$print_messe .= "・使用了$sc_syouhi的頭腦能源。<br>";
				$money -= $sc_nedan;
				last;
			}
	}
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
&header;
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
●聽講了$in{'sc_name'}<br>
$print_messe
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

#######食堂
sub syokudou {
#食堂旗標0把選單更新，旗標1就
open(IN,"$maintown_logfile") || &error("Open Error : $maintown_logfile");
	$maintown_para = <IN>;
			&main_town_sprit($maintown_para);
close(IN);
		if($mt_syokudouflag == 0){
	&lock;
			$mt_syokudouflag = 1;
			&main_town_temp;
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			print OUT $mt_temp;
			close(OUT);	
#打開商品數據記錄
						open(OL,"./dat_dir/syouhin.dat") || &error("Open Error : ./dat_dir/syouhin.dat");
						$top_koumoku = <OL>;
#商品排列到random換更新記錄
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
		if ($syo_syubetu ne "食"){next;}
		$syo_zaiko = int($syo_zaiko/$zaiko_tyousetuti);
		if($syo_zaiko <= 0) {$syo_zaiko = 1;}
		&syouhin_temp;
		push (@new_syouhin_hairetu2,$syo_temp);
		$i ++;
		if ($i >= $syokudou_sinakazu){last;}
	}
	open(OLOUT,">$syokudou_logfile") || &error("$syokudou_logfile不能寫入");
	print OLOUT @new_syouhin_hairetu2;
	close(OLOUT);
	&unlock;
		}		#if（日期變更）閉上
		
	open(SP,"$syokudou_logfile") || &error("Open Error : $syokudou_logfile");
	@syokudou_hairetu = <SP>;
	close(SP);
	&header(syokudou_style);
	print <<"EOM";
	<table width="100%" border="0" cellspacing="0" cellpadding="10"><tr><td width="554" >
	<form method="POST" action="$script" NAME="foMes5">		<!--ver.1.2-->
	<INPUT TYPE="hidden" NAME="TeMes5">		<!--ver.1.2-->
	<input type=hidden name=mode value="syokuzisuru">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="100%" border="0" cellspacing="0" cellpadding="6" align=center class=yosumi>
	<tr>
	<td colspan=11 bgcolor=#ffffff>中央食堂。菜單每天變化。吃飯一次的話$syokuzi_kankaku分經過之前是不能吃下一次飯。再者、$deleteUser日間不進餐就會死（用戶被刪掉）<br></td>
	<td colspan=3 bgcolor=#333333 align=center><img src="$img_dir/syokudou_tytle.gif"></td>
	</tr>
	<tr><td colspan=14><font color=#336699>凡例：（容）容貌up值、（體）體力up值、（健）健康up值、（速）速度up值、（力）力up值、（腕）腕力up值、（腳）腳力up值、（愛）LOVEup值、（趣）有趣up值、（淫）淫蕩up值</font></td></tr>
		<tr bgcolor=#ffff66><td align=center nowrap>菜單</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td align=center>卡路里</td><td align=center>價格</td><td align=center>餘下</td></tr>
EOM
	$i =1;
	foreach (@syokudou_hairetu) {
			if ($i % 10 ==0){print <<"EOM";
		<tr bgcolor=#ffff66><td align=center nowrap>菜單</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td align=center>卡路里</td><td align=center>價格</td><td align=center>餘下</td></tr>
EOM
			}
			&syouhin_sprit($_);
			$syo_nedan *= 3;
			if($syo_zaiko <= 0){
					$kounyuubotan ="";
					$syo_zaiko = "賣光";
			}else{
					$kounyuubotan ="<input type=radio value=\"$syo_hinmoku\" name=\"syo_hinmoku\">";
			}
		print <<"EOM";
		<tr><td nowrap>$kounyuubotan $syo_hinmoku</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td>$syo_cal kcal</td><td align=right nowrap>$syo_nedan元</td><td align=right>$syo_zaiko</td></tr>
EOM
	$i ++;
	}
	print <<"EOM";
	<tr><td colspan=14><div align=center><input type=submit value=" O K "></div></td>
	</table></form></td><td valign=top>
EOM
	&loged_gamen;
	print "</td></tr></table>";
	&hooter("login_view","返回");
	exit;
}

####吃飯處理
sub syokuzisuru {		#ver.1.3
	if($in{'syo_hinmoku'} eq ""){&error("未選菜色");}		#ver.1.40
	open(SP,"./dat_dir/syouhin.dat") || &error("Open Error : ./dat_dir/syouhin.dat");
	$top_koumoku = <SP>;
	@syokuzi_hairetu = <SP>;
	close(SP);
	foreach $syokuzi_hyouzi (@syokuzi_hairetu) {
			&syouhin_sprit($syokuzi_hyouzi);
			if($in{'syo_hinmoku'} eq "$syo_hinmoku"){
				$now_time = time;
				if($now_time < $last_syokuzi + ($syokuzi_kankaku*60)){&error("暫時不能吃飯。");}
				if($money < $syo_nedan*3){&error("錢不夠。");}
				
				$looks += $syo_looks;
				$tairyoku += $syo_tairyoku;
				$kenkou += $syo_kenkou;
				$speed += $syo_speed;
				$power += $syo_power;
				$wanryoku += $syo_wanryoku;
				$kyakuryoku += $syo_kyakuryoku;
				$love += $syo_love;		#ver.1.2
				$unique += $syo_unique;		#ver.1.2
				$etti += $syo_etti;
				$taijuu += $syo_cal / 1000;
				$last_syokuzi = $now_time;
				$money -= ($syo_nedan*3);
				last;
			}
	}


#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			
#設置食堂的殘餘數
	open(SYO,"$syokudou_logfile") || &error("Open Error : $syokudou_logfile");
		@syoku_zan = <SYO>;
	close(SYO);
	@new_syoku_zan=();
	foreach (@syoku_zan){
		&syouhin_sprit($_);
		if($in{'syo_hinmoku'} eq "$syo_hinmoku"){
			$syo_zaiko = $syo_zaiko-1 ;
		}
		&syouhin_temp;
		push (@new_syoku_zan,$syo_temp);
	}
			
	&lock;	
	open(OLOUT,">$syokudou_logfile") || &error("$syokudou_logfile不能寫入");
	print OLOUT @new_syoku_zan;
	close(OLOUT);
	&unlock;
	
			&message("吃了$in{'syo_hinmoku'}。","login_view");
}

#######百貨商店
sub depart_gamen {
#百貨商店旗標0是更新，旗標1菜單就
open(IN,"$maintown_logfile") || &error("Open Error : $maintown_logfile");
	$maintown_para = <IN>;
			&main_town_sprit($maintown_para);
close(IN);
		if($mt_departflag == 0){
				&lock;
						$mt_departflag = 1;
						&main_town_temp;
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			print OUT $mt_temp;
			close(OUT);	
			#打開商品數據記錄
									open(OL,"./dat_dir/syouhin.dat") || &error("Open Error : ./dat_dir/syouhin.dat");
									$top_koumoku = <OL>;
			#商品排列到random換更新記錄
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
					$syo_zaiko = int($syo_zaiko/$zaiko_tyousetuti);
					if($syo_zaiko <= 0) {$syo_zaiko = 1;}
					&syouhin_temp;
					push (@new_syouhin_hairetu2,$syo_temp);
					$i ++;
					if ($i >= $depart_sinakazu){last;}
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
				
				open(OLOUT,">$depart_logfile") || &error("$depart_logfile不能寫入");
				print OLOUT @alldata;
				close(OLOUT);
		&unlock;
	}		#if（日期變更）閉上
		
	open(SP,"$depart_logfile") || &error("Open Error : $depart_logfile");
	@syokudou_hairetu = <SP>;
	close(SP);
	&header(syokudou_style);
	print <<"EOM";
	<form method="POST" action="$script">
	<input type=hidden name=mode value="buy_syouhin">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>百貨商店。商品供應每天改變。種類豐富價格是提高。同時能拿的所有物的限度是$syoyuu_gendosuu品目。<div class="honbun2">●$name君的所持金：$money元</div></td>
	<td  bgcolor=#333333 align=center><img src="$img_dir/depart_tytle.gif"></td>
	</tr></table><br>
	<table width="100%" border="0" cellspacing="1" cellpadding="5" align=center class=yosumi>
	<tr><td colspan=26><font color=#336699>凡例：(國)＝國語up值、(數)＝數學up值、(理)＝理科up值、(社)＝社會up值、(英)＝英語up值、(音)＝音樂up值、(美)＝美術up值、（容）=容貌up值、（體）=體力up值、（健）=健康up值、（速）=速度up值、（力）=力up值、（腕）=腕力up值、（腳）=腳力up值、（愛）=LOVEup值、（趣）=有趣up值、（淫）=淫蕩up值<br></font>
	<font color=#ff6600>※禮物是送禮專用的商品。不能自己使用。</font></td></tr>
EOM

	foreach (@syokudou_hairetu) {
			&syouhin_sprit($_);
			$syo_nedan *= 3;
			if($syo_zaiko <= 0){
					$kounyuubotan ="";
					$syo_zaiko = "賣光";
			}else{
					$kounyuubotan ="<input type=radio value=\"$syo_hinmoku,&,$syo_taikyuu,&,$syo_nedan\" name=\"syo_hinmoku\">";
			}
			if($syo_cal > 0){$calory_hyouzi = "$syo_cal kcal";}else{$calory_hyouzi = "ー";}
			if ($maeno_syo_syubetu ne "$syo_syubetu"){
				print <<"EOM";
		<tr bgcolor=#ff9933><td align=center nowrap>商品</td><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td align=center nowrap>卡路里</td><td align=center nowrap>耐久</td><td align=center>使用<br>間隔</td><td align=center>身體<br>能量<br>消費</td><td align=center>頭腦<br>能量<br>消費</td><td align=center>價格</td><td align=center nowrap>　備　考　</td><td align=center nowrap>庫存</td></tr>
				<tr bgcolor=#ffff66><td colspan=26>▼$syo_syubetu</td></tr>
EOM
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
		<tr bgcolor=#ffcc66 align=center><td width=150 align=left>$kounyuubotan $syo_hinmoku</td><td>$syo_kokugo</td><td>$syo_suugaku</td><td>$syo_rika</td><td>$syo_syakai</td><td>$syo_eigo</td><td>$syo_ongaku</td><td>$syo_bijutu</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td align=right>$calory_hyouzi</td><td nowrap>$taikyuu_hyouzi_seikei</td><td nowrap>$syo_kankaku分</td><td>$syo_sintai_syouhi</td><td>$syo_zunou_syouhi</td><td align=right nowrap>$syo_nedan元</td><td align=left>$syo_comment</td><td align=right>$syo_zaiko</td></tr>
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
EOM
#ver1.30到這裡
	&hooter("login_view","返回");
	exit;
}

####購買處理
sub buy_syouhin {
#ver.1.30從這裡
	if ($kaenai_seigen == 1){		#ver.1.40
		if ($k_id eq "$in{'ori_ie_id'}" || $house_type eq "$in{'ori_ie_id'}" && $in{'ori_ie_id'} ne ""){&error("不能買在自己和配偶的店商品。");}
	}
	($katta_syouhin,$katta_taikyuu,$katta_nedan) = split(/,&,/,$in{'syo_hinmoku'});
			if ($in{'siharaihouhou'} eq "現金"){
					if ($katta_nedan > $money){&error("錢不夠");}
			}

#檢查自己購買物的文件是否有那個商品
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(MKF,"$monokiroku_file") || &error("自己的購買物文件不能打開");
	@my_item_list = <MKF>;
	close(MKF);
	foreach (@my_item_list){
		&syouhin_sprit($_);
		if ($syo_taikyuu <= 0){next;}
		if ($syo_syubetu eq "禮物"){$gift_item_suu ++ ;next;}
		if ($syo_syubetu eq "禮物商品"){next;}
		$my_item_suu ++ ;
	}
#檢查自己住的街
		&my_town_check($name);
		if ($return_my_town eq "$in{'town_no'}" && $k_id ne "$in{'ori_ie_id'}"){
			$cashback_flag = "on";
			$cashback_kingaku = int ($katta_nedan/10);
		}else{$cashback_flag = "off";}
		
	$motteru_flag =0;
	foreach (@my_item_list){
		&syouhin_sprit($_);
#如果持有
		if ($katta_syouhin eq "$syo_hinmoku" && $syo_syubetu ne "禮物商品" && $syo_syubetu ne "禮物"){
			if ($my_item_suu >= $syoyuu_gendosuu){&error("這個以上不能持有。攜帶品的所有限度數是$syoyuu_gendosuu。");}

				if ($syo_taikyuu_tani eq "回" || $syo_taikyuu_tani eq "日"){
						$nokotteru_taikyuu = $syo_taikyuu;
						$syo_taikyuu += $katta_taikyuu;
						if ($syo_taikyuu > $katta_taikyuu*$item_kosuuseigen){&error("這個物品不能再增加。");}		#ver.1.2
						if ($cashback_flag eq "on"){
							$tanka = int (($tanka*$nokotteru_taikyuu + $katta_nedan - $cashback_kingaku) / $syo_taikyuu);
						}else{
							$tanka = int (($tanka*$nokotteru_taikyuu + $katta_nedan) / $syo_taikyuu);
						}
						$motteru_flag =1;
				}
					if ($in{'siharaihouhou'} ne "現金"){
						$bank -= $katta_nedan;
						&kityou_syori("信用支付（$katta_syouhin）","$katta_nedan","",$bank,"普");
					}else{
						$money -= $katta_nedan;
					}
#ver.1.30到這裡
		}
		&syouhin_temp;
		push (@new_myitem_list,$syo_temp);
	}		#foreach閉上
	
	
#沒有的情況
	if ($motteru_flag ==0){
		if ($my_item_suu >= $syoyuu_gendosuu){&error("這個以上不能所有。攜帶品的所有限度數是$syoyuu_gendosuu。");}
		if ($gift_item_suu >= $kounyu_gift_gendo){&error("這個以上不能所有。達到著禮物的購買限度數$kounyu_gift_gendo。");}
#要是個人的店由個人的店記錄拷貝商品參數
		if ($in{'ori_ie_id'}){
			$omise_log_file="./member/$in{'ori_ie_id'}/omise_log.cgi";
			open(KOM,"$omise_log_file") || &error("Open Error : $omise_log_file");
				@kounyuu_hairetu = <KOM>;
			close(KOM);
#要是百貨商店由百貨商店記錄拷貝商品參數
		}else{
			open(KOM,"$depart_logfile") || &error("Open Error : $depart_logfile");
				@kounyuu_hairetu = <KOM>;
			close(KOM);
		}

		$kounyuu_ok = 0;
		foreach (@kounyuu_hairetu){
			&syouhin_sprit($_);
			if ($katta_syouhin eq "$syo_hinmoku"){		#ver.1.3
#記錄購買日
					$syo_kounyuubi = time;
#ver.1.30從這裡
					if ($cashback_flag eq "on"){
						$tanka = int (($katta_nedan - $cashback_kingaku) / $syo_taikyuu);
					}else{
						$tanka = int ($katta_nedan / $syo_taikyuu);
					}
					&syouhin_temp;
					push (@new_myitem_list,$syo_temp);
					if ($in{'siharaihouhou'} ne "現金"){
						$bank -= $katta_nedan;
						&kityou_syori("信用支付($katta_syouhin)","$katta_nedan","",$bank,"普");
					}else{
						$money -= $katta_nedan;
					}
#ver.1.30到這裡
					$kounyuu_ok = 1;
					last;
			}
		}
		if ($kounyuu_ok == 0){&error("不能購買$katta_syouhin。");}
	}		#沒有的情況閉上
	&lock;
	
#要是個人的店設置庫存入款&記帳錢
		if ($in{'ori_ie_id'}){
	$omise_log_file="./member/$in{'ori_ie_id'}/omise_log.cgi";
	open(SYO,"$omise_log_file") || &error("Open Error : $omise_log_file");
		@omise_zan = <SYO>;
	close(SYO);
	@new_omise_zan=();
	$syo_atta_fg=0;		#ver.1.22
	foreach (@omise_zan){
		&syouhin_sprit($_);
		if($katta_syouhin eq "$syo_hinmoku"){
			if ($syo_zaiko <= 0){&error("已沒有庫存");}
			$syo_zaiko = $syo_zaiko-1 ;
			$syo_atta_fg=1;		#ver.1.22
		}
		if ($syo_zaiko <= 0){next;}
		&syouhin_temp;
		push (@new_omise_zan,$syo_temp);
	}
	if($syo_atta_fg==0){&error("沒有庫存。");};		#ver.1.22

	open(OLOUT,">$omise_log_file") || &error("$omise_log_file不能寫入");
	print OLOUT @new_omise_zan;
	close(OLOUT);
#向對方的銀行匯入&記帳處理
	if ($k_id ne "$in{'ori_ie_id'}"){		#要是自己的店不收入銷售額
		&openAitelog ($in{'ori_ie_id'});
		$aite_bank += $katta_nedan;
		&aite_kityou_syori("銷售（$katta_syouhin）","",$katta_nedan,$aite_bank,"普",$in{'ori_ie_id'},"lock_off");
	
				&aite_temp_routin;
				open(OUT,">$aite_log_file") || &error("$aite_log_file不能打開");
				print OUT $aite_k_temp;
				close(OUT);
	}
#ver.1.30從這裡
#要是自己住的街的店的現金回贈
		if ($cashback_flag eq "on"){
				$money += $cashback_kingaku;
				$cashback_message = "<br>★近處店優惠、$cashback_kingaku元現金回贈。";
		}
#ver.1.30到這裡
#街的經濟力提高
	&town_keizaiup($katta_nedan,$in{'town_no'});
		}else{		#個人的店的情況閉上
#百貨商店設置庫存
	open(SYO,"$depart_logfile") || &error("Open Error : $depart_logfile");
		@depa_zan = <SYO>;
	close(SYO);
	@new_depa_zan=();
	$syo_atta_fg=0;		#ver.1.22
	foreach (@depa_zan){
		&syouhin_sprit($_);
		if($katta_syouhin eq "$syo_hinmoku"){
			if ($syo_zaiko <= 0){&error("已沒有庫存");}	#ver1.2
			$syo_zaiko = $syo_zaiko-1 ;
			$syo_atta_fg=1;		#ver.1.22
		}
		if ($syo_zaiko <= 0){next;}
		&syouhin_temp;
		push (@new_depa_zan,$syo_temp);
	}
	if($syo_atta_fg==0){&error("沒有庫存。");};		#ver.1.22

	open(OLOUT,">$depart_logfile") || &error("$depart_logfile不能寫入");
	print OLOUT @new_depa_zan;
	close(OLOUT);
	}	#百貨商店購買的情況閉上
#ver1.22
#自己的購買物文件的記錄更新
	$monokiroku_file="./member/$k_id/mono.cgi";
		open(MK,">$monokiroku_file") || &error("自己的購買物文件不能打開");
		print MK @new_myitem_list;
		close(MK);
	&unlock;
	
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
●購買了$katta_syouhin。$cashback_message
</span>
</td></tr></table>
<br>
	<a href=\"javascript:history.back()\"> [返回前畫面] </a>
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="返回">
	</form>
	</div>

	</body></html>
EOM
exit;

}

#信息發送
sub mail_sousin {		#ver.1.3 mail_sousin子程序全部
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
#打開自己的郵件記錄寫入存取時間讀入&記錄
		$message_file="./member/$k_id/mail.cgi";
		open(TIMEIN,"$message_file") || &error("Open Error : $message_file");
		$now_time= time;
		$last_m_check = <TIMEIN>;
#表示用的排列
		@my_mail_data = <TIMEIN>;
		$soumailkensuu = @my_mail_data;
		$last_m_check = "$now_time\n";
		close(TIMEIN);
#從攜帶品名單禮物排列作成
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(SP,"$monokiroku_file") || &error("Open Error : $monokiroku_file");
	@myitem_hairetu = <SP>;
	close(SP);
	foreach (@myitem_hairetu){
		&syouhin_sprit($_);
		if ($syo_syubetu eq "禮物"){
			$gift_select .= "<option value=\"$syo_hinmoku\">$syo_hinmoku</option>\n";
		}
	}
		
# 更新最後存取時間
	&lock;
#初始化寫入用的排列
		@my_kakikomi_mail_data = ();
		push (@my_kakikomi_mail_data,@my_mail_data);
		unshift (@my_kakikomi_mail_data,$last_m_check);
		if ($soumailkensuu > $mail_hozon_gandosuu){pop @my_kakikomi_mail_data;}		#ver.1.3
		open(TIMEOUT,">$message_file") || &error("Write Error : $message_file");
		print TIMEOUT @my_kakikomi_mail_data;
		close(TIMEOUT);
	&unlock;
	&header(item_style);
	print <<"EOM";
	<table width="95%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<!--ver.1.3-->
	<td bgcolor=#ffffff>能輸入對方的名字發發送息。信息殘留在接收箱和發送箱而對方被地址簿追加。如果從這個地址簿選名字，就沒有必要以名字欄的輸入。<br>
	※從保存在於信息「接收箱」「發送箱」共計以$mail_hozon_gandosuu事，超過這個的話舊的信息被刪掉。<br>
	※能如果持有著「禮物」類型的商品，用禮物發送選那個商品，郵件同時發送。</td>
	<td  bgcolor=#ffcc00 align=center><img src="$img_dir/mail_tytle.gif"></td>
	</tr></table><br>
EOM
	@address_match = ();
	LOOP : foreach $mail_data_add (@my_mail_data){
		&mail_sprit($mail_data_add);
						foreach $maenideta_ad (@address_match){
							if ($maenideta_ad eq "$m_name" ) {next LOOP;}
						}
						
		$addresstyou .= "<option value=\"$m_name\">$m_name</option>\n";
		push (@address_match ,$m_name);
	}
	
	&hooter("login_view","返回");
						print <<"EOM";
	<table width="100%" border="0" cellspacing="10" cellpadding="0" align=center>
	<tr><td width=50% valign=top>
	<table border="0" cellspacing="0" cellpadding="10" class=yosumi width=100%>
	<tr><td>
	<div class=tyuu>■信息發送</div>
	<form method="POST" action="$script">
	<input type=hidden name=mode value="mail_do">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	●發送目標的名字<br>
	<input type=text size=58 name="sousinsaki_name" value="$in{'sousinsaki_name'}"><br>
	<select name="sousinsaki_name2">
	<option value="">地址簿</option>
	$addresstyou
	</select><br>
	●信息<br>
	<textarea cols=58 rows=8 name=m_com wrap="soft"></textarea><br>
	●禮物發送<br>
	<select name=gift_souhu>
	<option value="">沒有</option>
	$gift_select
	</select><br><br>
	<div align=center><input type="submit" value=" O K "></div>
	</form></td></tr></table>
	<br>
	<table border="0" cellspacing="0" cellpadding="10" class=yosumi width=100%>
	<tr><td>
	<div class=tyuu>■發送箱</div>
EOM
	$i=0;
	foreach (@my_mail_data){
		&mail_sprit ($_);
		if ($m_syubetu eq "發送"){
			print "<hr size=1>";
			print "<div class=mainasu>○向$m_name君發送了的信息</div><br>";
			print "$m_com<div class=small>（$m_date）</div>";
			$i ++;
		}elsif($m_syubetu eq "表白發送"){
			print "<hr size=1>";
			print "<div style=\"color:#ff3366\">○向$m_name君發送了表白的信息</div><br>";
			print "$m_com<div class=small>（$m_date）</div>";
			$i ++;
		}elsif($m_syubetu eq "求婚發送"){
			print "<hr size=1>";
			print "<div style=\"color:#ff3366\">○向$m_name君發送了求婚的信息</div><br>";
			print "$m_com<div class=small>（$m_date）</div>";
			$i ++;
		}elsif($m_syubetu eq "答應求婚發送"){
			print "<hr size=1>";
			print "<div style=\"color:#ff3366\">○向$m_name君發送了的答應求婚的信息</div><br>";
			print "$m_com<div class=small>（$m_date）</div>";
			$i ++;
		}elsif($m_syubetu eq "同意交往發送"){
			print "<hr size=1>";
			print "<div style=\"color:#ff3366\">向$m_name君發送了的答應同意交往的信息</div><br>";
			print "$m_com<div class=small>（$m_date）</div>";
			$i ++;
		}
	}
	if ($i == 0){print "<br><br>暫時沒有發送了的信息。";}
	print <<"EOM";
	</td></tr></table>
	</td><td width=50% valign=top>
	<table border="0" cellspacing="0" cellpadding="10" class=yosumi width=100%>
	<tr><td>
	<div class=tyuu>■接收箱</div>
EOM
	$i=0;
	foreach (@my_mail_data){
		&mail_sprit ($_);
		if ($m_syubetu eq "接收"){
			print <<"EOM";
			<hr size=1>
			<div class=purasu>○來自$m_name君的信息</div><br>
			$m_com<div class=small>（$m_date）</div>
EOM
			$i ++;
		}elsif ($m_syubetu eq "表白接收"){
			print <<"EOM";
			<hr size=1>
			<div style="color:#ff3366">○來自$m_name君的表白信息</div><br>
			$m_com<div class=small>（$m_date）<br>
			<a href=kekkon.cgi?mode=assenjo&command=easySerch&serch_name=$m_name&town_no=$in{'town_no'}&name=$name&pass=$pass>恋人斡旋所で$m_nameさんのプロフィールを見る</a><!--ver.1.40-->
			</div>
	 <form method="POST" action="kekkon.cgi"><!--ver.1.40-->
	<input type=hidden name=mode value="kokuhaku">
	<input type=hidden name=command value="kousai_ok">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name="sousinsaki_name" value="$m_name">
	信息 <input type=text name=m_com size=30>
	<input type=submit value="ＯＫ交往"></form>
	※同意交往的話，請放入信息按「ＯＫ交往」按鈕。拒絕的話什麼都不需要做。
EOM
			$i ++;
		}elsif ($m_syubetu eq "求婚接收"){
			print <<"EOM";
			<hr size=1>
			<div style="color:#ff3366">○$m_name君向您求婚了。</div><br>
			$m_com<div class=small>（$m_date）
			</div>
	 <form method="POST" action="kekkon.cgi">
	<input type=hidden name=mode value="kokuhaku"><!--ver.1.40-->
	<input type=hidden name=command value="propose_ok">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name="sousinsaki_name" value="$m_name">
	信息 <input type=text name=m_com size=30>
	<input type=submit value="ＯＫ結婚"></form>
	※同意結婚的話，請放入信息按「ＯＫ結婚」按鈕。拒絕的話什麼都不需要做。
EOM
			$i ++;
		}elsif ($m_syubetu eq "答應求婚接收"){
			print <<"EOM";
			<hr size=1>
			<div style="color:#ff3366">○恭喜恭喜。$m_name君送來了結婚OK的回覆。</div><br>
			$m_com<div class=small>（$m_date）</div>
EOM
			$i ++;
		}elsif ($m_syubetu eq "同意交往接收"){
			print <<"EOM";
			<hr size=1>
			<div style="color:#ff3366">○恭喜恭喜。$m_name君送來了交往OK的回覆。</div><br>
			$m_com<div class=small>（$m_date）</div>
EOM
			$i ++;
		}elsif ($m_syubetu eq "生孩子"){
			print <<"EOM";
			<hr size=1>
			<div style="color:#009900">○跟$m_name君的生孩子。<span class=small>（$m_date）</span></div><br>
	 <form method="POST" action="kekkon.cgi"><!--ver.1.40-->
	<input type=hidden name=mode value="kodomo_naming">
	<input type=hidden name="kod_num" value="$m_com">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name="sousinsaki_name" value="$m_name">
	孩子的名字（全角10個字以內） <br>
	<input type=text name=kodomo_name size=20>
	<select name="umu_umanai">
		<option value="umu">用這個名字生孩子</option>
		<option value="umanai">不生了</option>
	</select>
	<input type=submit value=" O K "></form>
	※請決定孩子的名字按OK按鈕。請與對方商量之後決定。而不生孩子的情況，請選「不生了」按OK按鈕。同時$kodomo_sibou_time日內不做這個工作變得不能生孩子。
EOM
			$i ++;
		}
	}
	if ($i == 0){print "<br><br>暫時沒有接收了的信息。";}
	print "</td></tr></table></td></tr></table>";

		&hooter("login_view","返回");
	exit;
}

#郵件發送處理
sub mail_do {
		if ($in{'sousinsaki_name'} eq "" && $in{'sousinsaki_name2'} eq ""){&error("未輸入對方的名字");}
		if ($in{'m_com'} eq ""){&error("未輸入信息");}
		if ($in{'sousinsaki_name2'}){$aite_name = "$in{'sousinsaki_name2'}";}
		else{$aite_name = "$in{'sousinsaki_name'}";}
		&lock;
		&id_check ($aite_name);
			if ($in{'gift_souhu'}){
				if ($aite_name eq $name){&error("不能對自己贈送");}
				&gift_souhu_syori;
			}
			$message_file="./member/$return_id/mail.cgi";
			open(AIT,"$message_file") || &error("對方的郵件記錄文件($message_file)不開。");
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
		if ($in{'gift_souhu'}){
			$m_comment .= "<br><br><div class=honbun2>『$in{'gift_souhu'}』贈送。</div>";
		}
		&time_get;
		$new_mail = "接收<>$in{'name'}<>$m_comment<>$date2<>$date_sec<><><><><><>\n";
			unshift (@mail_cont,$new_mail);
			if (@mail_cont > $mail_hozon_gandosuu){pop @mail_cont;}		#ver.1.30
#如果沒有檢查最後郵件時間放入1
			if ($last_mail_check_time eq ""){$last_mail_check_time = "1\n";}
			unshift (@mail_cont,$last_mail_check_time);
			open(OUT,">$message_file") || &error("$message_file不能寫上");
			print OUT @mail_cont;
			close(OUT);
			
#自己的郵件發送完畢信息記錄(不是管理者郵件)
		if ($in{'command'} ne "from_system"){
			$my_sousin_file="./member/$k_id/mail.cgi";
			open(ZIB,"$my_sousin_file") || &error("$my_sousin_file不能打開。");
			$my_last_mail_check_time = <ZIB>;
			@my_mail_cont = <ZIB>;
			close(ZIB);
		$my_m_comment = $in{'m_com'};
		if ($in{'gift_souhu'}){
			$my_m_comment .= "<br><br><div class=honbun2>贈送了『$in{'gift_souhu'}』。</div>";
		}
		$sousin_mail = "發送<>$aite_name<>$my_m_comment<>$date2<>$date_sec<><><><><><>\n";
			unshift (@my_mail_cont,$sousin_mail);
			if (@my_mail_cont > $mail_hozon_gandosuu){pop @my_mail_cont;}		#ver.1.30
#如果沒有檢查最後郵件時間放入現在的時間
			if ($my_last_mail_check_time eq ""){$my_last_mail_check_time = "$date_sec\n";}
			unshift (@my_mail_cont,$my_last_mail_check_time);
			open(ZIBO,">$my_sousin_file") || &error("$my_sousin_file不能寫上");
			print ZIBO @my_mail_cont;
			close(ZIBO);
		}
		&unlock;
		if ($in{'command'} ne "from_system"){
			&message_only("發送了給$aite_name君的信息。");
			&hooter("mail_sousin","郵件畫面");
			&hooter("login_view","返回");
		}else{
			&message("發送了給$aite_name君的信息。","itiran","admin.cgi");		#ver.1.40
		}
	exit;
}

#禮物發送處理
sub gift_souhu_syori {
#從自己的攜帶品名單消去商品
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(SP,"$monokiroku_file") || &error("Open Error : $monokiroku_file");
	@myitem_hairetu = <SP>;
	close(SP);
	$monoatta_flag = 0;
	foreach (@myitem_hairetu){
		&syouhin_sprit($_);
		if ($syo_hinmoku eq "$in{'gift_souhu'}" && $monoatta_flag == 0 && $syo_syubetu ne "禮物商品"){$ageru_gift_copy = "$_"; $monoatta_flag = 1;next;}
		&syouhin_temp;
		push (@new_myitem_hairetu,$syo_temp);
	}
	if ($monoatta_flag == 0){&error("已經沒有商品。");}

#記錄購買日，單價0元，把類別做為禮物商品
					&syouhin_sprit($ageru_gift_copy);
					$syo_kounyuubi = time;
					$tanka = 0;
					$syo_syubetu = "禮物商品";
					$syo_comment .= "來自$name君的禮物。";
					&syouhin_temp;
					$okuraretamono = $syo_temp;
#在對方的攜帶品名單追加商品
	$aite_monokiroku_file="./member/$return_id/mono.cgi";
	open(ASP,"$aite_monokiroku_file") || &error("Open Error : $aite_monokiroku_file");
	@aite_item_hairetu = <ASP>;
	close(ASP);
	foreach (@aite_item_hairetu){
		&syouhin_sprit($_);
		if ($syo_syubetu eq "禮物商品"){$gift_count ++;}
	}
	if ($gift_count >= $gift_gendo){&error("對方的禮物超過限度數的$gift_gendo，所以不能發送");}
	push (@aite_item_hairetu,$okuraretamono);
#更新對方的所有物文件
			open(ASPO,">$aite_monokiroku_file") || &error("Write Error : $aite_monokiroku_file");
			print ASPO @aite_item_hairetu;
			close(ASPO);	
#更新自己的所有物文件
			open(OUT,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
			print OUT @new_myitem_hairetu;
			close(OUT);	
}

1;

