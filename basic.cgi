#!/perl/bin/perl
# ↑使用合乎服務器的路徑。

$this_script = 'basic.cgi';
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
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("還不能行動。請等候$ato_nanbyou秒以後。")}
		
#條件分歧
	if($in{'mode'} eq "keiba"){&keiba;}
	elsif($in{'mode'} eq "donus"){&donus;}
	elsif($in{'mode'} eq "byouin"){&byouin;}
	elsif($in{'mode'} eq "onsen"){&onsen;}
	elsif($in{'mode'} eq "prof"){&prof;}
	elsif($in{'mode'} eq "item"){&item;}
	elsif($in{'mode'} eq "item_do"){&item_do;}
	elsif($in{'mode'} eq "job_change"){&job_change;}
	elsif($in{'mode'} eq "job_change_go"){&job_change_go;}
	elsif($in{'mode'} eq "do_work"){&do_work;}
	elsif($in{'mode'} eq "ginkou"){&ginkou;}
	elsif($in{'mode'} eq "ginkoumeisai"){&ginkoumeisai;}
	elsif($in{'mode'} eq "ginkoufurikomi"){&ginkoufurikomi;}
	elsif($in{'mode'} eq "loan"){&loan;}
	else{&error("請用「返回」按鈕返回街");}
exit;
	
#############以下子程序
###########銀行
sub ginkou {
		&openMylog($in{'k_id'});
				if ($in{'command'} eq "存款"){
								if($in{'azukegaku'} =~ /[^0-9]/){&error("金額請用半角數字輸入");}
								if($in{'azukegaku'} <= 0){&error("負數的錢不能存款！");}
								if($in{'azukegaku'} > $money){&error("現金不足！");}
								$bank=$bank+$in{'azukegaku'};
								$money=$money-$in{'azukegaku'};
								$message_in = "存款$in{'azukegaku'}元到銀行。";
								&kityou_syori("存入","",$in{'azukegaku'},$bank,"普");
				}elsif ($in{'command'} eq "提款"){
								if($in{'orosigaku'} =~ /[^0-9]/){&error("金額請用半角數字輸入");}	#ver.1.40
								if($in{'orosigaku'} <= 0){&error("不能取出負數的錢！");}
								if($in{'orosigaku'} > $bank){&error("沒那麼多存款在銀行！");}
								$bank=$bank-$in{'orosigaku'};
								$money=$money+$in{'orosigaku'};
								$message_in = "從銀行取出了$in{'orosigaku'}元。";
								&kityou_syori("提款","$in{'orosigaku'}","",$bank,"普");
				}elsif ($in{'command'} eq "超級"){
								if($in{'azukegaku'} =~ /[^0-9]/){&error("金額請用半角數字輸入");}
								$super_azuke_kin = ($in{'azukegaku'}*10000);
								if($super_azuke_kin > $money){&error("現金不足！");}
								$super_teiki=$super_teiki+$super_azuke_kin;
								$money=$money-$super_azuke_kin;
								$message_in = "存款$super_azuke_kin元為超級定期。";
								&kityou_syori("存入","",$in{'azukegaku'}*10000,$super_teiki,"定");
				}elsif ($in{'command'} eq "解除"){
								$money=$money+$super_teiki;
								$orosumaeno_super_teiki = $super_teiki;
								$message_in = "解除了超級定期($super_teiki元)。";
								$super_teiki=0;
								&kityou_syori("解除","$orosumaeno_super_teiki","",$super_teiki,"定");
				}else{
#銀行畫面輸出
	&header(ginkou_style);
			if($bank eq  ""){$ima_azuke = "沒有";}else{$ima_azuke="$bank元";}
			if($super_teiki > 0){$super_gaku = "●超級定期存款額:$super_teiki元";}
#ver.1.3從這裡
			my $saidai_teiki = int($money * 0.0001);
			if ($saidai_teiki <= 0){$saidai_teiki = "";}
			if ($money > 0){$saidai_azuke = $money;}else{$saidai_azuke = "";}
			if ($money > 1000000){$issen = $money - 1000000; $zandaka_keisan .= "<option value=$issen>留下100萬</option>";}
			if ($money > 500000){$gohyaku = $money - 500000; $zandaka_keisan .= "<option value=$gohyaku>留下50萬</option>";}
			if ($money > 100000){$hyaku = $money - 100000; $zandaka_keisan .= "<option value=$hyaku>留下10萬</option>";}
			if ($money > 50000){$gojuu = $money - 50000; $zandaka_keisan .= "<option value=$gojuu>留下5萬</option>";}
			if ($money > 10000){$juu = $money - 10000; $zandaka_keisan .= "<option value=$juu>留下1萬</option>";}
			if ($money > 1000){$iti = $money - 1000; $zandaka_keisan .= "<option value=$iti>留下1千</option>";}
			if ($zandaka_keisan eq ""){$zandaka_keisan = "<option value=>餘額不能指定</option>";}
#ver.1.3到這裡
			print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>歡迎光臨。<div class="honbun2">●$name君的現金:$money元</div></td>
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/ginkou_tytle.gif"></td>
	</tr></table><br>
	
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi><tr>
	
	<td width=50% valign=top><span style=font-size:14px;color:#ff3300>■一般戶口</span><span class="honbun2">●現在的儲蓄額：$ima_azuke</span><br><br>
			※一般戶口存款，附有日息0.5％的利息。同時，自己家的錢，店的商品出售了時的入款等也能利用。<br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkou">
	<input type=hidden name=command value="存款">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<!--ver.1.3從這裡-->
	◆存  款 <input type=text name=azukegaku value="$saidai_azuke" size=12>元 <input type=submit value="存款">
	</form>

	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkou">
	<input type=hidden name=command value="存款">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	◆餘額存入 <select name = "azukegaku">$zandaka_keisan</select>　<input type=submit value="存款">
	</form>


	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkou">
	<input type=hidden name=command value="提款">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	◆提  款 <input type=text name=orosigaku size=12>元 <input type=submit value="提款">
	</form><hr size=1></td>
	
	<td valign=top><span style=font-size:14px;color:#ff3300>■超級定期</span><span class="honbun2">$super_gaku</span><br><br>
		※超級定期附有日息1％的利息。但儲蓄額是以萬元為單位，取出錢的時候必須以“解除”全額提出。<br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkou">
	<input type=hidden name=command value="超級">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	◆最大限度額 <input type=text name=azukegaku value="$saidai_teiki" size=6> 萬 <input type=submit value="限度額存款">
	</form>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkou">
	<input type=hidden name=command value="超級">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	◆存  款 <input type=text name=azukegaku size=6> 萬 <input type=submit value="存款">
	</form>
<!--ver.1.3到這裡-->
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkou">
	<input type=hidden name=command value="解除">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	◆解  除 <input type=submit value="解除">
	</form>
	<hr size=1></td></tr>
	<tr>
	<td valign=top><span style=font-size:14px;color:#ff3300>■存取詳細</span><br><br>
		※能看活期存款的入存取詳細。<br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkoumeisai">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=syubetu value="活期存款存取詳細">
	<input type=submit value="看存取詳細">
	</form>
	<hr size=1></td>
	
	<td valign=top><span style=font-size:14px;color:#ff3300>■超級定期詳細</span><br><br>
		※能看超級定期的存取詳細。<br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkoumeisai">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=syubetu value="超級定期詳細">
	<input type=submit value="看存取詳細">
	</form>
	<hr size=1></td></tr>
	<tr>
	<td valign=top><span style=font-size:14px;color:#ff3300>■匯入</span><br><br>
		※指定參加者名字匯款。自己的錢由一般戶口扣下。<br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="ginkoufurikomi">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	匯款目標的名字 <input type=text name=aitenonamae size=16>
	匯款金額 <input type=text name=hurikomigaku size=8>元
	<input type=submit value="匯入">
	</form>
	</td>
	
	<td valign=top><span style=font-size:14px;color:#ff3300>■貸款</span><br><br>
EOM
	if ($loan_kaisuu > 0){
	$loan_zandaka_kei = $loan_nitigaku * $loan_kaisuu;
	print <<"EOM";
	●現在的貸款餘款＝$loan_zandaka_kei元（$loan_nitigaku元×$loan_kaisuu期）<br>
	※一攬子返還餘款請按下面的按鈕。那個情況，由一般自戶口扣下。
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="loan">
	<input type=hidden name=command value="ikkatu_hensai">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="一攬子返還貸款">
	</form>
EOM
	}else{
		print <<"EOM";
		※能按照對這個銀行的利用度和收入借錢。也能用一攬子進行返還。<br>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="loan">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="融資額的核定">
	</form>
EOM

	}
	print <<"EOM";
	</td></tr>
	</table>
	<div align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
	</body></html>
EOM
	exit;
			}		#else(銀行畫面輸出)閉上
#畫面輸出以外的情況的記錄更新處理
					&temp_routin;
					&log_kousin($my_log_file,$k_temp);
					&message($message_in,"login_view");

}	#sub ginkou閉上

####銀行匯款處理
sub ginkoufurikomi {
	if ($in{'command'} ne "from_system"){
		if($in{'hurikomigaku'} < 0){&error("負數的金額不能匯入");}
		if($in{'hurikomigaku'} =~ /[^0-9]/){&error("金額請用半角數字輸入");}
		if ($bank < $in{'hurikomigaku'}){&error("一般戶口的錢不夠。");}
		if ($name eq $in{'aitenonamae'}){&error("不能向自己匯入。");}		#ver.1.3
		$bank -= $in{'hurikomigaku'};
	}
	&id_check ($in{'aitenonamae'});
	&openAitelog ($return_id);
	$aite_bank += $in{'hurikomigaku'};
	
	if ($in{'command'} ne "from_system"){
		&kityou_syori("匯款→$in{'aitenonamae'}","$in{'hurikomigaku'}","",$bank,"普");
	}
	if ($in{'hurikomigaku'} < 0){
		&aite_kityou_syori("減錢",$in{'hurikomigaku'},"",$aite_bank,"普",$return_id,"");
	}else{
		&aite_kityou_syori("匯款←$in{'name'}","",$in{'hurikomigaku'},$aite_bank,"普",$return_id,"");
	}
#記錄更新
	&lock;	
	if ($in{'command'} ne "from_system"){
			&temp_routin;
			open(OUT,">$my_log_file") || &error("@$my_log_file不能打開");
			print OUT $k_temp;
			close(OUT);
	}
			
			&aite_temp_routin;
				open(OUT,">$aite_log_file") || &error("$aite_log_file不能打開");
				print OUT $aite_k_temp;
				close(OUT);
	&unlock;
	if ($in{'command'} ne "from_system"){
		&message("向$in{'aitenonamae'}君的一般戶口匯入了$in{'hurikomigaku'}元。","login_view");
	}else{
		&message("向$in{'aitenonamae'}君的一般戶口匯入了$in{'hurikomigaku'}元。","itiran","admin.cgi");
	}
}



#######貸款
sub loan {
#借款處理的情況
	if ($in{'hensai_kaisuu'}){
		if ($loan_kaisuu > 0){&error("到還清貸款前不能有新的融資。");}
		my ($nitigaku,$nitigaku_kaisuu) = split(/×/,$in{'hensai_kaisuu'});
		$loan_nitigaku = "$nitigaku";
		$loan_kaisuu = "$nitigaku_kaisuu";
		$bank += $in{'yuusi_kanougaku'};
		&kityou_syori("安揭","",$in{'yuusi_kanougaku'},$bank,"普");
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			&message("向活期存款戶口匯入了$in{'yuusi_kanougaku'}元。","login_view");
#一攬子返還的情況
	}elsif ($in{'command'} eq "ikkatu_hensai"){
		$ikkatu_hensai_gaku = $loan_nitigaku * $loan_kaisuu;
		if ($bank < $ikkatu_hensai_gaku){&error("一般戶口沒有充分的存款");}
		$bank -= $ikkatu_hensai_gaku;
		$loan_nitigaku = 0;
		$loan_kaisuu = 0;
		&kityou_syori("安揭一攬子返還","$ikkatu_hensai_gaku","",$bank,"普");
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			&message("完成安揭的一攬子返還。","login_view");
#核定處理畫面輸出
	}else{
	open(SP,"./dat_dir/job.dat") || &error("Open Error : ./dat_dir/job.dat");
	$top_koumoku = <SP>;
	@job_hairetu = <SP>;
	close(SP);
	foreach  (@job_hairetu) {
			&job_sprit($_);
			if($job_name eq "$job"){
				last;
			}
	}
	$yuusi_kanougaku = int(($job_kyuuyo * ($job_keiken/50) * ($job_kaisuu/50)) + ($bank * 2)+($super_teiki * 2.5));
	$yuusi_kanougaku -= $yuusi_kanougaku % 10000;
	$kai12 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.05))/12);
	$kai24 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.06))/24);
	$kai36 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.07))/36);
	$kai48 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.08))/48);
	$kai60 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.09))/60);
	$kai72 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.1))/72);
	$kai84 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.11))/84);
	$kai96 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.12))/96);
	$kai108 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.13))/108);
	$kai120 = int(($yuusi_kanougaku + ($yuusi_kanougaku*0.14))/120);
	
	&header(ginkou_style);
	print <<"EOM";
		<table width="400" border="0" cellspacing="0" cellpadding="20" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>
	<div class=dai align=center>核  定</div><hr size=1><br>
	<div class=job_messe>本銀行對$name君的貸款額<br>
	職業，經驗，從工齡期間等核定，<br>
	能融資的金額為以下。
	<br><br><div class=dai>$yuusi_kanougaku元</div>
	
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="loan">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name=yuusi_kanougaku value="$yuusi_kanougaku">
	返還按照每天(登入時)，返還回數附有了5～14％的利息的額自活期存款戶口扣下。<br>
	同時，到還清前不能再借錢。

	<select name="hensai_kaisuu">
	<option value="$kai12×12">12期付款(日額$kai12元)</option>
	<option value="$kai24×24">24期付款(日額$kai24元)</option>
	<option value="$kai36×36">36期付款(日額$kai36元)）</option>
	<option value="$kai48×48">48期付款(日額$kai48元)</option>
	<option value="$kai60×60">60期付款(日額$kai60元)</option>
	<option value="$kai72×72">72期付款(日額$kai72元)</option>
	<option value="$kai84×84">84期付款(日額$kai84元)</option>
	<option value="$kai96×96">96期付款(日額$kai96元)</option>
	<option value="$kai108×108">108期付款(日額$kai108元)</option>
	<option value="$kai120×120">120期付款(日額$kai120元)</option>
	</select>
	<input type=submit value="借">
	</form>
	</td></tr>
	</table>
	<div align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
	</body></html>
EOM
	exit;
	}		#else(沒有借款處理的情況)的閉上
}



#######銀行詳細
sub ginkoumeisai {
	$ginkoumeisai_file="./member/$k_id/ginkoumeisai.cgi";
	if (! -e $ginkoumeisai_file){
		open(GM,">$ginkoumeisai_file") || &error("不能作成自己的存款存摺文件");
		close(GM);
	}
	open(GM,"$ginkoumeisai_file") || &error("自己的存款存摺文件不能打開");
	@my_tuutyou = <GM>;
	close(GM);

	&header(ginkou_style);
	print <<"EOM";
	<table width="90%" border="0" cellspacing="1" cellpadding="5" align=center class=yosumi>
	<tr class=sita><td colspan=5>■$in{'syubetu'}　※詳細活期存款，超級定期合計100件被記帳。</td></tr>
	<tr class=sita bgcolor=#cccc99 align=center>
	<td>年　月　日</td><td>交易內容</td><td>提　款　額</td><td>存　款　額</td><td>存取餘額</td></tr>
EOM
	foreach (@my_tuutyou){
		&ginkou_meisai_sprit($_);
		if ($in{'syubetu'} eq "活期存款存取詳細"){if ($meisai_syubetu ne "普"){next;}}
		if ($in{'syubetu'} eq "超級定期詳細"){if ($meisai_syubetu ne "定"){next;}}
#ver.1.3從這裡
if ($meisai_zandaka =~ /^[-+]?\d\d\d\d+/g) {
  for ($i = pos($meisai_zandaka) - 3, $j = $meisai_zandaka =~ /^[-+]/; $i > $j; $i -= 3) {
    substr($meisai_zandaka, $i, 0) = ',';
  }
}
if ($meisai_hikidasi =~ /^[-+]?\d\d\d\d+/g) {
  for ($i = pos($meisai_hikidasi) - 3, $j = $meisai_hikidasi =~ /^[-+]/; $i > $j; $i -= 3) {
    substr($meisai_hikidasi, $i, 0) = ',';
  }
}
if ($meisai_azuke =~ /^[-+]?\d\d\d\d+/g) {
  for ($i = pos($meisai_azuke) - 3, $j = $meisai_azuke =~ /^[-+]/; $i > $j; $i -= 3) {
    substr($meisai_azuke, $i, 0) = ',';
  }
}
#ver.1.3到這裡
	print <<"EOM";
		<tr class=sita><td>$meisai_date</td><td>$meisai_naiyou</td><td align=right><font color=#ff3333>$meisai_hikidasi</font></td><td align=right><font color=#009933>$meisai_azuke</font></td><td align=right>$meisai_zandaka元</td></tr>
EOM
	}
	print <<"EOM";
		</table>
		<div align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
		</body></html>
EOM
	exit;
}

####賽馬
sub keiba {
	my $now_time = time;
my (@umaname)=('◇舞伴','◇氣槽','◇琵琶晨光','◇石野週日','◇森林寶穴','◇曼城茶座','◇莫名其妙','◇小栗帽','◇櫻花會長','◇空中神宮','◇琵琶海蒂','◇成田拜仁','◇海洋駿驥','◇東海帝皇','◇期待浪漫');
my (@umakakeritu)=('8','28','2','12','16','4','30','3','5');
%umagazou =("◇舞伴","danpa.gif","◇氣槽","groove.gif","◇琵琶晨光","hayahide.gif","◇石野週日","ishisun.gif","◇森林寶穴","junpoke.gif","◇曼城茶座","manhattan.gif","◇莫名其妙","noreason.gif","◇小栗帽","oguri.gif","◇櫻花會長","sakura_predi.gif","◇空中神宮","shakur.gif","◇琵琶海蒂","heidi.gif","◇成田拜仁","brian.gif","◇海洋駿驥","tm_ocean.gif","◇東海帝皇","tokai_teio.gif","◇期待浪漫","roman.gif");

#包含排列次序的文件讀入
	open(KR,"$keibarank_logfile") || &error("Open Error : $keibarank_logfile");
		@keiba_ranking =<KR>;
	close(KR);
	foreach (@keiba_ranking){
			$key=(split(/<>/,$_))[1];		#選排序的要素
			push @alldata,$_;
			push @keys,$key;
	}
		sub bykeys{$keys[$b] <=> $keys[$a];}
		@alldata=@alldata[ sort bykeys 0..$#alldata]; 
	$i = 0;
	foreach (@alldata){
		($kr_name,$kr_moukegaku,$kr_tounyuugaku,$kr_kakutokugaku,$kr_yobi1,$kr_yobi2,$kr_yobi3,$kr_yobi4)= split(/<>/);
#kr_yobi1 = 最後遊戲時間
		$rank_html .= "<tr><td>$kr_name</td><td align=right>$kr_moukegaku元</td><td align=right>$kr_tounyuugaku元</td><td align=right>$kr_kakutokugaku元</td></tr>";
		$i ++;
		if ($i >= 10){last;}
	}
	
	
#把馬做為random排列調換
	@new_entry = ();
	foreach (@umaname){
			my $r = rand @new_entry+1;
			push (@new_entry,$new_entry[$r]);
			$new_entry[$r] = $_;
	}
	
#把機會率做為random排列調換
	@new_kakeritu = ();
	foreach (@umakakeritu){
			my $s = rand @new_kakeritu+1;
			push (@new_kakeritu,$new_kakeritu[$s]);
			$new_kakeritu[$s] = $_;
	}
	
	foreach (0..5){
		$umaname{$new_entry[$_]} = "$new_kakeritu[$_]";
	}
#賭的畫面
	if ($in{'command'} eq ""){
	&header(keiba_style);
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffff99>馬票1張是10元。請輸入購買張數按「賽事開始」按鈕。只能賭2匹。<br>
	$name君的所持金：$money元<br>
	※同時能購買$keiba_gendomaisuu張馬票。<br>
	※從排列次序開始$deleteUser日不玩遊戲的用戶會被刪掉。</td>
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/keiba_tytle.gif"></td>
	</tr></table><br>
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>

	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="keiba">
	<input type=hidden name=command value="start">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<tr><td valign=top>
	<table cellspacing="0" cellpadding="8" width=100% class=yosumi>
	<tr bgcolor=#99cc66>
	<td align=center colspan=3>本日的參戰馬</td></tr>
	<tr bgcolor=#ffff99>
	<td align=center>馬</td><td align=center>賠率</td><td align=center>購入數</td></tr>
EOM
		foreach (0..5){
				$hid_name = "uma"."$_";
				$hid_kake = "kake"."$_";
				$hid_kane = "kane"."$_";
				print <<"EOM";
			<tr><td>
			<input type=hidden name="$hid_name" value="$new_entry[$_]">
			$new_entry[$_] 
			</td>
			<td align=right>
			<input type=hidden name="$hid_kake" value="$new_kakeritu[$_]">
			$new_kakeritu[$_]倍
			</td>
			<td align=right><input type=text name="$hid_kane" size=10> 張</td></tr>
EOM
		}
	print <<"EOM";
		<tr><td align=center colspan=3><input type=submit value="賽事開始"></td></tr>
		</table></form>
		</td><td  valign=top width=60%>
		<table cellspacing="0" cellpadding="4" class=yosumi width=100%>
		<tr bgcolor=#ff9900><td colspan=4 align=center>
		賭博王最佳10位
		</td></tr>
		<tr bgcolor=#ffffcc><td align=center>名字</td><td align=center>總數利額</td><td align=center>總投入額</td><td align=center>總獲得額</td></tr>
		$rank_html
		</table>
		</tr></table>
EOM
	&hooter("login_view","返回");
	exit;
	}
#開始畫面
	if ($in{'command'} eq "start"){
	&keibalock;
		$start_html  .= <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="keiba">
	<input type=hidden name=command value="go">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table border=0 width=620 bgcolor=#cc9933 align=center cellspacing="0" cellpadding="0">
	<tr><td width=20>
	<table border=0 width=20 height=100% bgcolor=#ffff99><tr><td align=center><img src=$img_dir/goal.gif width=11 height=33></td></tr></table>
	</td><td align=right>
	<table border=0 bgcolor=#ffffff><tr><td width=120 align=center>馬</td><td width=40 align=center>賠率</td><td width=40 align=center>購入</td></tr></table>
	<hr size=2 color=#ffffff>
EOM
	foreach (0..5){
		if($in{'kane'.$_} =~ /[^0-9]/){&keibaunlock; &error("購買數不妥。");}		#ver.1.3
		if ($in{'kane'.$_}){$kaketaumanokazu ++;}
		$kyori = int((rand(60)+10)/(1+($in{'kake'.$_}/70)));
		$keiba_temp = "$in{'uma'.$_}<>$in{'kake'.$_}<>$in{'kane'.$_}<>$kyori<>\n";
		$hikarerugaku += $in{'kane'.$_} * 10;
		$kounyuu_soumaisuu += $in{'kane'.$_};		#ver.1.2
		push (@now_race,$keiba_temp);
		if ($in{'kane'.$_}){$kakekin = "$in{'kane'.$_}張";}else{$kakekin = "";}
		$start_html  .=  <<"EOM";
		<table border=0 cellspacing="0" cellpadding="0">
		<tr>
		<td width=$kyori align=left><img src=$img_dir/uma/$umagazou{"$in{'uma'.$_}"} width=30 height=30></td>
		<td width=120>$in{'uma'.$_}</td>
		<td width=40 align=right>$in{'kake'.$_}倍</td>
		<td width=40 align=right>$kakekin</td>
		</tr></table><hr size=2 color=#ffffff noshade>
EOM
	}
	if ($hikarerugaku == 0){&keibaunlock; &error("未購買馬票");}
	if ($money < $hikarerugaku){&keibaunlock; &error("錢不夠");}
	if ($kounyuu_soumaisuu > $keiba_gendomaisuu){&keibaunlock; &error("同時只能購買$keiba_gendomaisuu張馬票");}		#ver.1.2
	if ($kaketaumanokazu > 2){&keibaunlock; &error("不能賭2頭以上");}
	&header;
	print <<"EOM";
	$start_html
		※請按「GO ! GO !」按鈕驅使比賽繼續。<br>
		※這個畫面的狀態不使之結束的話(投注的錢就白花了)。
		
	</td><tr></table>
	<br><br><div align=center><input type=submit value="GO ! GO !"></div>
	</form>
	</body></html>
EOM
	open(KB,">$keiba_logfile")|| &error("Open Error : $keiba_logfile");
	print KB @now_race;
	close(KB);
	
	$money -= $hikarerugaku;
#數據更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
	exit;
	
	}
#搖擺舞畫面
	if ($in{'command'} eq "go"){
	if (!-e $keibalockfile) {&error("時間完了，當作棄權論。");}
	open(KB,"$keiba_logfile")|| &error("Open Error : $keiba_logfile");
		@keiba_hairetu =<KB>;
	close(KB);
	&header;
		print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="keiba">
	<input type=hidden name=command value="go">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table border=0 width=620 bgcolor=#cc9933 align=center cellspacing="0" cellpadding="0">
	<tr><td width=20>
	<table border=0 width=20 height=100% bgcolor=#ffff99><tr><td align=center><img src=$img_dir/goal.gif width=11 height=33></td></tr></table>
	</td><td align=right>
	<table border=0 bgcolor=#ffffff><tr><td width=120 align=center>馬</td><td width=40 align=center>賠率</td><td width=40 align=center>購入</td></tr></table>
	<hr size=2 color=#ffffff>
EOM
	@now_race = ();
	@kekkahantei = ();
#１回
	foreach (@keiba_hairetu){
		($umaname,$ods,$kane,$kyori) = split(/<>/);
		$kyori += int((rand(100)+0)/(1+($ods/80)));
		if ($kyori >= 400){$kyori = 400;}
		push (@kekkahantei , $kyori);
		$keiba_temp = "$umaname<>$ods<>$kane<>$kyori<>\n";
		push (@now_race,$keiba_temp);
		if ($kane){$kakekin = "$kane張";}else{$kakekin = "";}
		print <<"EOM";
		<table border=0 cellspacing="0" cellpadding="0">
		<tr>
		<td width=$kyori align=left><img src=$img_dir/uma/$umagazou{"$umaname"} width=30 height=30></td>
		<td width=120>$umaname</td>
		<td width=40 align=right>$ods倍</td>
		<td width=40 align=right>$kakekin</td>
		</tr></table><hr size=2 color=#ffffff noshade>
EOM
	}
#結果判斷
	foreach (0..5){
		if ($kekkahantei[$_] >= 400){
			($winner) = split (/<>/ , $now_race[$_] );
			push (@win_hairetu ,$winner);
		}
	}
#中彩時
	if (@win_hairetu){
			if (@win_hairetu >=2){
				$syasin_randed=rand($#win_hairetu+1);
				$kekkahappyou = "@win_hairetu似乎同時到達終點，不過根據相片決定勝敗的結果，@win_hairetu[$syasin_randed]首先到達終點得第1名！";
				$win_uma = "@win_hairetu[$syasin_randed]";
			}else{
				$kekkahappyou ="@win_hairetu以第1名跑到終點！";
				$win_uma = "@win_hairetu";
			}
			foreach (@now_race){
				($umaname,$ods,$kane,$kyori) = split(/<>/);
				if ($umaname eq "$win_uma"){
						$kakutokugaku = $ods * $kane * 10;
						if ($kakutokugaku == 0){
							$kakutokuhyouzi = "很遺憾，祝您下次好運";
						}else{
						$kakutokuhyouzi = "$kakutokugaku元";
						}
				}
				$soukounyuu += $kane*10;
			}
		print <<"EOM";
		<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
		<div  class=tyuu>$kekkahappyou</div>
		購買金額：$soukounyuu元<br>
		獲得金額：$kakutokuhyouzi
		</td></tr></table><br>
		</td></tr>
		</table>
		</form>
		
	<div align=center><form method=POST action="$this_script">
	<input type=hidden name=mode value="keiba">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=admin_pass value=$in{'admin_pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="再挑戰">
	</form></div>

EOM
		&hooter("login_view","返回");
		print "</body></html>";

		$money += $kakutokugaku;
#數據更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
#排列次序文件更新
	open(KR,"$keibarank_logfile") || &error("Open Error : $keibarank_logfile");
		@keiba_ranking =<KR>;
	close(KR);
	$kizon_flag=0;
	foreach (@keiba_ranking){
		($kr_name,$kr_moukegaku,$kr_tounyuugaku,$kr_kakutokugaku,$kr_yobi1,$kr_yobi2,$kr_yobi3,$kr_yobi4)= split(/<>/);
		if ($name eq "$kr_name"){
			$kr_tounyuugaku += $soukounyuu;
			$kr_kakutokugaku += $kakutokugaku;
			$kr_moukegaku = $kr_kakutokugaku - $kr_tounyuugaku;
			$kizon_flag=1;
			$kr_yobi1 = $now_time;
		}
#		if ($now_time - $kr_yobi1> 60*60*24*$deleteUser){next;}
		$kr_rank_temp = "$kr_name<>$kr_moukegaku<>$kr_tounyuugaku<>$kr_kakutokugaku<>$kr_yobi1<>$kr_yobi2<>$kr_yobi3<>$kr_yobi4<>\n";
		push (@new_keiba_ranking ,$kr_rank_temp);
	}
	if ($kizon_flag == 0){
		$moukegaku = $kakutokugaku - $soukounyuu;
		$kr_rank_temp = "$name<>$moukegaku<>$soukounyuu<>$kakutokugaku<>$now_time<><><><>\n";
		push  (@new_keiba_ranking ,$kr_rank_temp);
	}
	open(KRO,">$keibarank_logfile")|| &error("Open Error : $keibarank_logfile");
	print KRO @new_keiba_ranking;
	close(KRO);
	
	&keibaunlock;
#賽事繼續
	}else{
		print <<"EOM";
		※請按「GO ! GO !」按鈕驅使比賽繼續。<br>
		※這個畫面的狀態不使之結束的話(投注的錢就白花了)。
		
		</td></tr>
		</table>
		<br><br><div align=center><input type=submit value="GO ! GO !"></div>
		</form>
		</body></html>
EOM
		open(KB,">$keiba_logfile")|| &error("Open Error : $keiba_logfile");
		print KB @now_race;
		close(KB);
	}
	exit;
	}		#go指令的情況閉上
}


#賽馬用鎖處理
sub keibalock {
	local($retry, $mtime);

	# 5分以上舊的鎖刪掉
	if (-e $keibalockfile) {
		($mtime) = (stat($keibalockfile))[9];
		if ($mtime < time - 300) { &keibaunlock; }
	}

	# retry10次
	$retry = 1;
	while (!mkdir($keibalockfile, 0755)) {
		if (--$retry <= 0) { &error('現在賽事進行中。請稍等一下。'); }
		sleep(1);
	}
	# 立起鎖旗標
	$keibalockflag=1;
}
sub keibaunlock {
		open(KB,">$keiba_logfile")|| &error("Open Error : $keiba_logfile");
		print KB @clear;
		close(KB);
	# 鎖目錄刪掉
	rmdir($keibalockfile);

	# 解除鎖旗標
	$keibalockflag=0;
}


####炸面圈遊戲
sub donus {
	if ($tajuukinsi_flag==1){&tajuucheck;}
	open(MA,"$donuts_logfile") || &error("$donuts_logfile不能打開");
	$saigonohito = <MA>;
	@donuts_alldata = <MA>;
	close(MA);
	$sankasyasuu = @donuts_alldata;
	($do_name,$do_hantei,$do_hiitakard,$do_narandacard,$do_yobi1,$do_last)= split(/<>/,$saigonohito);
#do_yobi1 = 支付額
	if ($do_narandacard eq ""){$do_narandacard = 1;}
	$card_suu = length $do_narandacard;
	$my_card = "<img src=$img_dir/donuts/ura.gif width=64 heith=84>";
#抽的指令的情況
	if ($in{'command'} eq "hiku"){
		$now_time = time ;
		if ($name eq $do_name){&error("同樣的人不能繼續抽卡");}
		foreach (@donuts_alldata){
			($do2_name,$do2_hantei,$do2_hiitakard,$do2_narandacard,$do2_yobi1,$do2_last)= split(/<>/);
				if ($name eq $do2_name){
					if ($now_time - $do2_last < 60*$crad_game_time){&error("遊戲之後還有$crad_game_time分未過。");}
				}
		}
		$randed= int(rand(5))+1;
		$my_card_gazou = "$img_dir/donuts/"."$randed"."a.gif";
		$my_card = "<img src=$my_card_gazou width=64 heith=84>";
		$kingaku = $card_suu * 10000;
#Out的情況
		if ($randed == $do_hiitakard){
				$money -= $kingaku * 1;
				$do_hantei = "out";
				$do_narandacard = "$randed";
				$out_gaku = $card_suu*1;
				$comment = "<div class=mainasu>Out！！ <br>支付$out_gaku萬元！</div>";
				$siharai= $card_suu * 1;
				$card_suu = 1;
#Safe的情況
		}else{
				$money += $kingaku;
				$do_hantei = "safe";
				$do_narandacard = "$do_narandacard" . "$randed";
				$comment = "<div class=purasu>Safe！！<br>取得$card_suu萬元！</div>";
				$siharai= $card_suu;
		}
		$next_temp = "$name<>$do_hantei<>$randed<>$do_narandacard<>$siharai<>$now_time<>\n";
		unshift @donuts_alldata,$saigonohito;
		unshift @donuts_alldata,$next_temp;
		if ($sankasyasuu >= 19){pop @donuts_alldata;}
#數據更新
		&lock;
	open(KB,">$donuts_logfile")|| &error("Open Error : $donuts_logfile");
	print KB @donuts_alldata;
	close(KB);
		&unlock;
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);		
	}		#抽的情況閉上
	&header(gym_style);
			print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>●規則說明<br>
	抽了的卡與前面的人的卡不同，就能得到桌子上的卡的數目×1萬元的錢，之後那個卡會放到桌子上。<br>・如果出現了同樣的數出，就要反過來支付卡的數目×1萬元的錢。之後桌子上的卡再從1張開始。<br>※同樣的人不能持續抽卡。※遊戲間隔是$crad_game_time分。
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/donuts_tytle.gif"></td>
	</tr></table><br>
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi><tr><td>
	<div align=center>
	$my_card
	$comment
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="donus">
	<input type=hidden name=command value="hiku">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="抽卡">
	</form></div>
EOM

	if ($do_hiitakard ne ""){
	$your_card = "$img_dir/donuts/$do_hiitakard" .".gif";
	print <<"EOM";
	<div align=center><img src=$your_card width=60 heith=80></div>
	<div align=center>前面的人抽了的卡</div>
EOM
	}

	for ($i=0; $i < $card_suu; $i ++){
		$card_bangou = substr ($do_narandacard,$i,1);
		$table_card_image = "$img_dir/donuts/$card_bangou". ".gif";
			$line .= "<img src=$table_card_image width=30 height=40>\n";

	}

	print <<"EOM";
	</td><td width=60% valign=top>
		<div class=job_messe><到現在為止的被抽了的卡></div>
		<table  border="0" cellspacing="0" cellpadding="10" width=100% height=80% bgcolor=#66cc33 style="border: #663300; border-style: solid; border-width: 2px;">
		<tr><td>
		$line
		</td></tr></table>
	</td></tr></table>
	
<br><table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td>
	<div class=honbun2>■最近的遊戲</div>
EOM
	if ($in{'command'} eq ""){
		unshift @donuts_alldata,$saigonohito;
	}
	if (length $saigonohito != 0){
		foreach (@donuts_alldata){
			($do_name,$do_hantei,$do_hiitakard,$do_narandacard,$do_yobi1,$do_last)= split(/<>/);
			$ikura = length $do_narandacard;
			if ($do_hantei eq "out"){
				print "<div class=mainasu>$do_name君支付了$do_yobi1萬元。</div>";
			}else{
				print "<div class=purasu>$do_name君取得了$do_yobi1萬元。</div>";
			}
		}
	}
	print <<"EOM";
	</td></tr></table>
EOM
	&hooter("login_view","返回");
	exit;
}

###醫院
sub byouin {
	if ($in{'command'}){
		if ($in{'command'} eq "少許感冒"){
			$tiryouhi = 1800;
		}elsif($in{'command'} eq "感冒"){
			$tiryouhi = 2800;
		}elsif($in{'command'} eq "肺炎"){
			$tiryouhi = 3500;
		}elsif($in{'command'} eq "結核"){
			$tiryouhi = 4800;
		}elsif($in{'command'} eq "癌"){
			$tiryouhi = 8800;
		}elsif($in{'command'} eq "健康"){
			$tiryouhi = 1000;
		}
		if ($money < $tiryouhi){&error("錢不夠");}
			$money -= $tiryouhi;
			$byouki_sisuu = 50;
			$byoumei = "";
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			&message("疾病已經治療。閣下可以放心了。患病時請利用這間醫院。","login_view");
	}
	&header(ginkou_style);
			if($bank eq  ""){$ima_azuke = "沒有";}else{$ima_azuke="$bank元";}
			if($super_teiki > 0){$super_gaku = "●超級定期存款額$super_teiki元";}
			print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>歡迎光臨。怎樣的病也立刻痊癒。</td>
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/byouin_tytle.gif"></td>
	</tr></table><br>
	
	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center class=yosumi><tr>
	<td>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="byouin">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
EOM
	if ($byoumei eq "少許感冒"){
		print <<"EOM";
		<div class=honbun4 align=center>
		好像輕度的感冒的。<br>預先打針吧。<br>治療費是1800元。<br>接受治療嗎？<br>
		<input type=hidden name=command value="少許感冒">
		<input type=submit value="拜託您了"></form>
		</div>
EOM
		&hooter("login_view","敲竹槓呀！免了！");
		
	}elsif($byoumei eq "感冒"){
		print <<"EOM";
		<div class=honbun4 align=center>
		嗯。是單純的感冒。如果打針馬上醫好喲。<br>治療費是2800元。<br>接受治療嗎？<br>
		<input type=hidden name=command value="感冒">
		<input type=submit value="拜託您了"></form>
		</div>
EOM
		&hooter("login_view","敲竹槓呀！免了！");

	}elsif($byoumei eq "肺炎"){
		print <<"EOM";
		<div class=honbun4 align=center>
		痛苦嗎。是肺炎呀。就是患感冒之後不理會喲。<br>但是請放心。<br>打針馬上就醫好喲。<br>費用只是3500元。<br>很便宜喲。<br>
		<input type=hidden name=command value="肺炎">
		<input type=submit value="拜託您了"></form>
		</div>
EOM
		&hooter("login_view","以自力使之痊癒可以了");

	}elsif($byoumei eq "結核"){
		print <<"EOM";
		<div class=honbun4 align=center>
		呀。。不行啊。好像結核的。。<br>應早點來就吧。。<br>但也不要緊。本來需要住院，不過如果<br>打針一轉眼地醫好了喲。<br>治療費用4800元。。<br>呀，為了治好這個結核已經很便宜。。。<br>
		<input type=hidden name=command value="結核">
		<input type=submit value="拜託您了"></form>
		</div>
EOM
		&hooter("login_view","貴！免了！");
	
	}elsif($byoumei eq "腦瘤"){
		print <<"EOM";
		<div class=honbun4 align=center>
		呀，首先有心理準備。這個醫院診斷了的檢驗結果，是腦瘤。。<br>這樣生死尤關。<br>立刻動手術吧！<br>那樣的話馬上醫好。<br>手術費連治療費為6400元，不過這不是計較錢的時候。<br>
		<input type=hidden name=command value="腦瘤">
		<input type=submit value="拜託您了"></form>
		</div>
EOM
		&hooter("login_view","太是貴！免了！");
	
	}elsif($byoumei eq "癌"){
		print <<"EOM";
		<div class=honbun4 align=center>
		嗚呼哀哉。哦，這是！！嚴重的事<br>患上癌症！這是可以醫好喲。<br>但，最先需要手術！<br>如果被稱作了這個街的黑傑克的我出手<br>即使是癌病也馬上可痊癒。<br>但費用稍微。。。<br>需要8800元。<br>但是比起就這樣死了！<br>根本不需考慮吧！<br>
		<input type=hidden name=command value="癌">
		<input type=submit value="拜託您了"></form>
		</div>
EOM
		&hooter("login_view","情願死！也不支付那樣的錢！");
		
	}elsif($byoumei eq ""){
		print <<"EOM";
		<div class=honbun4 align=center>
		好像沒有甚麼問題。<br>為慎重起見預先打針嗎？<br>費用為1000元。。<br><br>
		<input type=hidden name=command value="健康">
		<input type=submit value="拜託您了"></form>
		</div>
EOM
		&hooter("login_view","立即離開");
	}else{
			print <<"EOM";
		<div class=honbun4 align=center>
		mumumumumu？？　這個呢。。。是我無法負責的病。。。<br>請另覓名醫。</div>
EOM
		&hooter("login_view","失意地離開那醫院");
	}
	
	
	print <<"EOM";
	</td></tr></table>
EOM
	&hooter("login_view","返回");
	exit;
}

###溫泉
sub onsen {
	if ($in{'onsensyurui'} eq "koukyuu"){
		$onsensyurui = "two";
		$o_kakaruhiyou = $tokubetuburo_hiyou;
	}else{
		$onsensyurui = "one";
		$o_kakaruhiyou = $nyuuyokuryou;
	}
	$money -= $o_kakaruhiyou;
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
	my $gazou_bangou =int(rand($on_gazou_suu))+1;
	my $onsen_gazou = "$gazou_bangou".".jpg";
	&ori_header("background-color : #336699; background-repeat : no-repeat; background-position : center center; background-image : url( $img_dir/onsen/$onsen_gazou)");
	print <<"EOM";
	<table  border=0  cellspacing="5" cellpadding="0" width=100% height=70%><tr><td valign=top>
	<br><table  border=0  cellspacing="2" cellpadding="0" width=370 align=center bgcolor=#ffffcc><tr><td>
EOM
	if ($in{'onsensyurui'} eq "koukyuu"){
		print "<div style=\"font-size:11px\">特別風呂比會通常的快$tokubetu_times倍恢復力。</div>";
	}else{
		print "<div style=\"font-size:11px\">風呂比通常快$onsen_times倍恢復力。
	<br>※$tokubetuburo_hiyou元支付特別風呂的話快$tokubetu_times倍恢復力。</div>";
	}
	print <<"EOM";
	</td></tr></table><br>
	<table  border=0  cellspacing="5" cellpadding="0" width=200 align=center><tr><td>
	<div align=center><img src="$img_dir/nyuuyoku.gif" width="110" height="30"></div>
	</td></tr></table>
	</td></tr></table>
	<div align=center>
EOM
	if ($in{'onsensyurui'} ne "koukyuu"){
	print <<"EOM";
	<form method=POST action="$this_script">
	<input type=hidden name=mode value="onsen">
	<input type=hidden name=onsensyurui value="koukyuu">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="特別風呂">
	</form>
EOM
	}
	print <<"EOM";
	<form method=POST action="$script">
	<input type=hidden name=mode value="login_view">
	<input type=hidden name=iiyudane value="$onsensyurui">
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="從浴池中離開">
	</form>
	</div>
	</body></html>
EOM
	exit;
}

sub prof {
	open(IN,"$profile_file") || &error("Open Error : $profile_file");
	@alldata=<IN>;
	$total_touroku_suu = @alldata;
	close(IN);

#登記form的輸出
	if ($in{'command'} eq "touroku_form"){
		&prof_form;
		exit;
	}
	
#登記的情況
	if ($in{'command'} eq "touroku"){
		$atta_flag=0;
		@new_alldata = ();
		foreach (@alldata){
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
#修正的情況
			if ($name eq "$pro_name"){next;} 
			push (@new_alldata,$_);
		}

		my($new_entry) = "$name<>$in{'pro_sex'}<>$in{'pro_age'}<>$in{'pro_addr'}<>$in{'pro_p1'}<>$in{'pro_p2'}<>$in{'pro_p3'}<>$in{'pro_p4'}<>$in{'pro_p5'}<>$in{'pro_p6'}<>$in{'pro_p7'}<>$in{'pro_p8'}<>$in{'pro_p9'}<>$in{'pro_p10'}<>$in{'pro_p11'}<>$in{'pro_p12'}<>$in{'pro_p13'}<>$in{'pro_p14'}<>$in{'pro_p15'}<>$in{'pro_p16'}<>$in{'pro_p17'}<>$in{'pro_p18'}<>$in{'pro_p19'}<>$in{'pro_p20'}<>\n";
		unshift (@new_alldata,$new_entry);
		
#記錄更新
	&lock;
	open(OUT,">$profile_file") || &error("$profile_file不能寫上");
	print OUT @new_alldata;
	close(OUT);
	&unlock;
	&message("進行了個人資料的登記。","prof","basic.cgi");
	exit;
	}
	
	&header(prof_style);
		print <<"EOM";
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>不是虛擬，登記真的個人資料，閱覽的地方。現在登記數：$total_touroku_suu人
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="prof">
	<input type=hidden name=command value="touroku_form">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="個人資料登記&修正">
	</form>
	</td>
	<td  bgcolor=#333333 align=center width=35%><img src="$img_dir/prof_tytle.gif">
	</td></tr></table><br>

	<table width="90%" border="0" cellspacing="0" cellpadding="8" align=center bgcolor=#ffcc66>
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="prof">
	<input type=hidden name=command value="easySerch">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<tr>
EOM

#檢索形式
# 名字
	print "<td>名　字 <input type=text name=serch_name size=20></td>\n";
# 性別
	print "<td><select name=sex>\n";
	print "<option value=\"99\">性別\n";
		for($i=1;$i<@sex_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'sex'} eq $sex_array[$i]);
				print ($option,$sex_array[$i]);
		}
	print "</select></td>\n";
# 年齡
	print "<td><select name=age>\n";
	print "<option value=\"99\">年齡\n";
		for($i=1;$i<@age_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'age'} eq $age_array[$i]);
				print ($option,$age_array[$i]);
		}
	print "</select></td>\n";
	
# 住址
	print "<td><select name=address>\n";
	print "<option value=\"99\">住址\n";
		for($i=1;$i<@address_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'address'} eq $address_array[$i]);
				print ($option,$address_array[$i]);
		}
	print "</select></td>\n";
	
# 個人資料1
	print "<td valign=top nowrap>\n";
	print "<select name=p1>\n";
	print "<option value=\"99\">$prof_name1\n";
		for($i=1;$i<@prof_array1;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p1'} eq $prof_array1[$i]);
				print ($option,$prof_array1[$i]);
		}
	print "</select></td></tr><tr>\n";
	
# 個人資料2
	print "<td valign=top nowrap>\n";
	print "<select name=p2>\n";
	print "<option value=\"99\">$prof_name2\n";
		for($i=1;$i<@prof_array2;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p2'} eq $prof_array2[$i]);
				print ($option,$prof_array2[$i]);
		}
	print "</select></td>\n";
	
# 個人資料3
	print "<td valign=top nowrap>\n";
	print "<select name=p3>\n";
	print "<option value=\"99\" selected>$prof_name3\n";
		for($i=1;$i<@prof_array3;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p3'} eq $prof_array3[$i]);
				print ($option,$prof_array3[$i]);
		}
	print "</select></td>\n";
	
# 個人資料4
	print "<td valign=top nowrap>\n";
	print "<select name=p4>\n";
	print "<option value=\"99\" selected>$prof_name4\n";
		for($i=1;$i<@prof_array4;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p4'} eq $prof_array4[$i]);
				print ($option,$prof_array4[$i]);
		}
	print "</select></td>\n";
	
# 個人資料5
	print "<td valign=top nowrap>\n";
	print "<select name=p5>\n";
	print "<option value=\"99\" selected>$prof_name5\n";
		for($i=1;$i<@prof_array5;$i++){
				my $option='<option>';
				$option='<option selected>' if($in{'p5'} eq $prof_array5[$i]);
				print ($option,$prof_array5[$i]);
		}

	print <<"EOM";
	</select></td>
	<td>
	<input type=submit value=" 檢索 ">
	</form>
	  </td>
    </tr>
  </table><br>
EOM
	&hooter("login_view","返回街");
	
	
# 簡易檢索的情況
		if ($in{'command'} eq "easySerch"){
				$i=0;
				foreach (@alldata) {
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
					if ($in{'serch_name'} ne "" && $in{'serch_name'} ne $pro_name) { next; }		#條件沒相符的時刻下面的人
					if ($in{'sex'} != 99 && $in{'sex'} ne $pro_sex) { next; }
					if ($in{'age'} != 99 && $in{'age'} ne $pro_age) { next; }		
					if ($in{'address'} != 99 && $in{'address'} ne $pro_addr) { next; }
					if ($in{'p1'} != 99 && $in{'p1'} ne $pro_p1) { next; }
					if ($in{'p2'} != 99 && $in{'p2'} ne $pro_p2) { next; }
					if ($in{'p3'} != 99 && $in{'p3'} ne $pro_p3) { next; }
					if ($in{'p4'} != 99 && $in{'p4'} ne $pro_p4) { next; }
					if ($in{'p5'} != 99 && $in{'p5'} ne $pro_p5) { next; }
					$i++;
					push(@newrank,$_);
				}
				@alldata=@newrank;
				print "<div align=center class=sub2>條件符合的有$i個。</div><br>";
				&hooter("prof","全部表示","basic.cgi");
		}
		
	$page=$in{'page'};	
	if ($page eq "") { $page = 0; }
	$i3=0;
	
##記錄表示處理
		foreach (@alldata) {
			($pro_name,$pro_sex,$pro_age,$pro_addr,$pro_p1,$pro_p2,$pro_p3,$pro_p4,$pro_p5,$pro_p6,$pro_p7,$pro_p8,$pro_p9,$pro_p10,$pro_p11,$pro_p12,$pro_p13,$pro_p14,$pro_p15,$pro_p16,$pro_p17,$pro_p18,$pro_p19,$pro_p20)= split(/<>/);
			@my_prof_hairetu = split(/<>/);
		$i3++;
		if ($i3 < $page + 1) { next; }
		if ($i3 > $page + $hyouzi_max_grobal) { last; }
		
			if($pro_sex eq "男"){
					$sex_style="border: #99ccff; border-style: solid; border-width: 3px; background-color:#ffffcc";
			}elsif($pro_sex eq "女"){
					$sex_style="border: #ff9999; border-style: solid; border-width: 3px; background-color:#ffffcc";
			}else{
					$sex_style="border: #cccccc; border-style: solid; border-width: 3px; background-color:#ffffcc";
			}
			
			print "<table style=\"$sex_style\" align=center width=450>";
			$i=1;
			foreach (@my_prof_hairetu){
					$_ =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
					if ($i == 1){$pr_koumokumei ="名字";}
					elsif ($i == 2){$pr_koumokumei ="性別";}
					elsif ($i == 3){$pr_koumokumei ="年齡";}
					elsif ($i == 4){$pr_koumokumei ="住址";}
					elsif ($i == 5){$pr_koumokumei ="$prof_name1";}
					elsif ($i == 6){$pr_koumokumei ="$prof_name2";}
					elsif ($i == 7){$pr_koumokumei ="$prof_name3";}
					elsif ($i == 8){$pr_koumokumei ="$prof_name4";}
					elsif ($i == 9){$pr_koumokumei ="$prof_name5";}
					else {$pr_koumokumei = $kijutu_prof[$i-10];}
				if ($_ ne "" && $_ ne "\n"){
					print <<"EOM";
					<tr><td align=right width=120><div class=honbun2>$pr_koumokumei</div></td>
					<td>：$_</td></tr>
EOM
				}
					$i ++; 
		}	#foreach閉上
			print <<"EOM";
     <tr><td colspan=2 align=center><form method="POST" action="$script">
	<input type=hidden name=mode value="mail_sousin">
	<input type=hidden name=name value="$name">
	<input type=hidden name=pass value="$pass">
	<input type=hidden name=id value="$k_id">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=hidden name="sousinsaki_name" value="$pro_name">
	<input type=submit value="信息發送"></form>
	</td></tr>
	</table><br>
EOM

		}	#foreach閉上(記錄表示處理到這裡)

		$next = $page + $hyouzi_max_grobal;
		$back = $page - $hyouzi_max_grobal;
		print "<div align=center><table border=0><tr>";
		if ($back >= 0) {
#檢索的情況的按鈕
				if($in{'command'} eq "easySerch"){
					print <<"EOM";
			<form method=POST action=\"$this_script\">
			<input type=hidden name=mode value=prof>
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
			<input type=hidden name=page value="$back">
			<input type=submit value="BACK">
			</form>
EOM
				}else{
#通常的情況
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="prof">
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
			<input type=hidden name=mode value=prof>
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
			<input type=hidden name=page value="$next">
			<input type=submit value="NEXT">
</form>
EOM
				}else{
					print <<"EOM";
			<td><form method="POST" action="$this_script">
			<input type=hidden name=mode value="prof">
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
sub prof_form {
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
	
	&header(prof_style);
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="prof">
	<input type=hidden name=command value="touroku">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>選擇了或記述了的項目才會公開，不想公開的可以留空。無論什麼時候都能修正・更新。
	</td>
	<td  bgcolor=#ff6633 align=center width=35%><div style="font-size:13px; color:#ffffff">個人資料登記</div>
	</td></tr></table><br>
	
	<table width="90%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr><td>
EOM
print '性別<br><select name="pro_sex">';
		for($i=0;$i<@sex_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($pro_sex eq $sex_array[$i]);
				print ($option,$sex_array[$i]);
		}
		print '</select></td><td>';

		print ' 年齡<br><select name="pro_age">';
		for($i=0;$i<@age_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($pro_age eq $age_array[$i]);
				print ($option,$age_array[$i]);
		}
		print '</select></td><td>';


		print ' 住址<br><select name="pro_addr">';
		for($i=0;$i<@address_array;$i++){
				my $option='<option>';
				$option='<option selected>' if($pro_addr eq $address_array[$i]);
				print ($option,$address_array[$i]);
		}
		print '</select></td><td>';

 		print "$prof_name1<br><select name=\"pro_p1\">";
		for($i=0;$i<@prof_array1;$i++){
				$option='<option>';
				$option='<option selected>' if($pro_p1 eq $prof_array1[$i]);
				print ($option,$prof_array1[$i]);
		}
		print '</select></td></tr><tr><td>';

		print "$prof_name2<br><select name=\"pro_p2\">";
		for($i=0;$i<@prof_array2;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p2 eq $prof_array2[$i]);
				print ($option,$prof_array2[$i]);
		}
		print '</select></td><td>';
 
 		print "$prof_name3<br><select name=\"pro_p3\">";
		for($i=0;$i<@prof_array3;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p3 eq $prof_array3[$i]);
				print ($option,$prof_array3[$i]);
		}
		print '</select></td><td>';
 
 		print "$prof_name4<br><select name=\"pro_p4\">";
		for($i=0;$i<@prof_array4;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p4 eq $prof_array4[$i]);
				print ($option,$prof_array4[$i]);
		}
		print '</select></td><td>';
 
 		print "$prof_name5<br><select name=\"pro_p5\">";
		for($i=0;$i<@prof_array5;$i++){
				$option=' <option>';
				$option='<option selected>' if($pro_p5 eq $prof_array5[$i]);
				print ($option,$prof_array5[$i]);
		}
		print '</select></td></tr>';
		$i = 6;
		$i2=9;
		foreach (@kijutu_prof){
			print "<tr><td align=right>$_</td><td colspan=3><input type=text name=pro_p$i size=80 value=$my_prof_hairetu[$i2]></td></tr>\n";
			$i ++;
			$i2 ++;
		}
		print <<"EOM";
	<tr><td colspan=4 align=center>
	<input type=submit value=" O K "><br>
	</td></tr></table>
	</form>
		
EOM
	&hooter("prof","返回","basic.cgi");
}

##########物品使用
sub item {
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(SP,"$monokiroku_file") || &error("Open Error : $monokiroku_file");
	@myitem_hairetu = <SP>;
	close(SP);
	
#類別分類
				foreach (@myitem_hairetu){
						$data=$_;
						$key=(split(/<>/,$data))[0];
						push @alldata,$data;
						push @keys,$key;
				}
				sub by_syu_keys{$keys[$a] cmp $keys[$b];}
				@alldata=@alldata[ sort by_syu_keys 0..$#alldata]; 
	
	&header(item_style);
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="item_do">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="100%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi>
	<tr>
	<td bgcolor=#ffffff>揀選想使用的物品，選「使用」或「賣掉」後按OK按鈕。<br>
	※備考(※圖標)的商品，有新的圖標出現。「使用」丟失了的效果也消失。<br>
	※自己購買了的「禮物」會在郵件發送畫面的選擇菜單出現。而不會在這個名單表示。<br>
	現在的$name君的身體能量:$energy 頭腦能量:$nou_energy</td>
	<td  bgcolor=#ffcc00 align=center><img src="$img_dir/item_tytle.gif"></td>
	</tr></table><br>
	
	<table width="100%" border="0" cellspacing="1" cellpadding="5" align=center class=yosumi>
	<tr><td colspan=26><font color=#336699>凡例:(國)=國語up值，(數)=數學up值，(理由)=理科up值，(社)=社會up值，(英)=英語up值，(音)=音樂up值，(美)=美術up值，(容)=容貌up值，(體)=體力up值，(健)=健康up值，(速)=速度up值，(力)=力up值，(腕)=腕力up值，(腳)=腳力up值，(愛)=LOVEup值，(趣)=有趣up值，(淫)=淫蕩up值<br>
	※耐久，○回指能使用的回數，○日指能使用的日數。<br>
	※卡路里是能攝取的數值。<br>
	</font></td></tr>
		<tr bgcolor=#ccff33><td align=center nowrap>商品</td><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td align=center nowrap>卡路里</td><td align=center>使用<br>間隔</td><td align=center>身體<br>能量<br>消費</td><td align=center>頭腦<br>能量<br>消費</td><td align=center>出售<br>價格</td><td align=center nowrap>　備　考　</td><td align=center nowrap>購入日</td><td align=center nowrap>餘下</td></tr>
EOM
	$now_time = time;			#ver.1.3
	@new_myitem_hairetu = ();			#ver.1.3
	foreach (@alldata) {
			&syouhin_sprit($_);
#ver.1.30從這裡
				if ($syo_taikyuu_tani eq "日"){
						$keikanissuu = int (($now_time - $syo_kounyuubi) / (60*60*24));
						$nokorinissuu = $syo_taikyuu - $keikanissuu;
						if ($nokorinissuu <= 0){next;}
				}
#ver.1.30到這裡
			if ($syo_taikyuu <=0){next;}
			if ($syo_syubetu ne "禮物"){			#ver.1.3
			if($syo_cal > 0){$calory_hyouzi = "$syo_cal kcal";}else{$calory_hyouzi = "<div align=center>ー</div>";}
			if($syo_kankaku <= 0){$syo_kankaku = "<div align=center>ー</div>";}
			if ($maeno_syo_syubetu ne "$syo_syubetu"){
				print "<tr bgcolor=#ffff66><td colspan=26>▼$syo_syubetu</td></tr>";
			}
#ver.1.3從這裡
			if ($syo_taikyuu_tani eq "日"){
				$taikyuu_hyouzi_seikei = "$nokorinissuu日";
				$baikyaku_hyouzi = ($tanka * $nokorinissuu);
			}else{
				$taikyuu_hyouzi_seikei = "$syo_taikyuu"."$syo_taikyuu_tani";
				$baikyaku_hyouzi = ($tanka * $syo_taikyuu);
			}
#ver.1.3到這裡
		&byou_hiduke($syo_kounyuubi);
		print <<"EOM";
		<tr bgcolor=#ccff99 align=center><td nowrap align=left><input type=radio value=\"$syo_hinmoku\" name=\"syo_hinmoku\">$syo_hinmoku</td><td>$syo_kokugo</td><td>$syo_suugaku</td><td>$syo_rika</td><td>$syo_syakai</td><td>$syo_eigo</td><td>$syo_ongaku</td><td>$syo_bijutu</td><td>$syo_looks</td><td>$syo_tairyoku</td><td>$syo_kenkou</td><td>$syo_speed</td><td>$syo_power</td><td>$syo_wanryoku</td><td>$syo_kyakuryoku</td><td>$syo_love</td><td>$syo_unique</td><td>$syo_etti</td><td align=right>$calory_hyouzi</td><td nowrap>$syo_kankaku分</td><td>$syo_sintai_syouhi</td><td>$syo_zunou_syouhi</td><td align=right nowrap>$baikyaku_hyouzi元</td><td align=left>$syo_comment</td><td nowrap>$bh_tukihi</td><td nowrap>$taikyuu_hyouzi_seikei</td></tr>
EOM
		$maeno_syo_syubetu = "$syo_syubetu";
		}			#沒有禮物的情況閉上		ver.1.3
		&syouhin_temp;			#ver.1.3
		push (@new_myitem_hairetu,$syo_temp);			#ver.1.3
	}		#foreach閉上
	if (! @alldata){print "<tr><td colspan=26>現在沒有所持的物品。</td></tr>";}
	print <<"EOM";
	<tr><td colspan=26>
	<div align=center>
	<select name="command">
	<option value="siyou">使用</option>
	<option value="baikyaku">賣掉</option>
	</select>
	<input type=submit value=" O K "></div></td></tr>
	</table></form>
EOM
#更新自己的所有物文件
			&lock;
			open(OUT,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
			print OUT @new_myitem_hairetu;
			close(OUT);	
			&unlock;
	&hooter("login_view","返回");
	exit;
}

#######物品使用
sub item_do {
	if ($in{'syo_hinmoku'} eq ""){&error("未選擇物品。");}
	$monokiroku_file="./member/$k_id/mono.cgi";
	open(SP,"$monokiroku_file") || &error("Open Error : $monokiroku_file");
	@myitem_hairetu = <SP>;
	close(SP);
	$siyouzumi_flag = 0;
	foreach  (@myitem_hairetu) {
		&syouhin_sprit($_);
		if ($in{'syo_hinmoku'} eq "$syo_hinmoku" && $syo_syubetu ne "禮物"){
#「使用」指令的情況
		if ($in{'command'} eq "siyou" && $siyouzumi_flag == 0){
				$siyouzumi_flag = 1;
				$now_time = time;
				if ($syo_syubetu eq "食品" || $syo_syubetu eq "快餐食品"){
				if($now_time < $last_syokuzi + ($syokuzi_kankaku*60)){&error("暫時不能吃飯。");}
					$print_messe .= "●吃了$in{'syo_hinmoku'}。<br>";
					$last_syokuzi = $now_time;
				}else{
					$print_messe .= "●使用$in{'syo_hinmoku'}。<br>";
				}
				if($syo_siyou_date + ($syo_kankaku*60) > $now_time){&error("因為間隔太短所以暫時不能使用。");}
				if($energy < $syo_sintai_syouhi){&error("身體力不夠。");}
				if($nou_energy < $syo_zunou_syouhi){&error("頭腦力不夠。");}
				
				if($syo_kokugo){$kokugo += $syo_kokugo; $print_messe .= "・國語$syo_kokugo提高。<br>";}
				if($syo_suugaku){$suugaku += $syo_suugaku; $print_messe .= "・數學$syo_suugaku提高。<br>";}
				if($syo_rika){$rika += $syo_rika; $print_messe .= "・理科$syo_rika提高。<br>";}
				if($syo_syakai){$syakai += $syo_syakai; $print_messe .= "・社會$syo_syakai提高。<br>";}
				if($syo_eigo){$eigo += $syo_eigo; $print_messe .= "・英語$syo_eigo提高。<br>";}
				if($syo_ongaku){$ongaku += $syo_ongaku; $print_messe .= "・音樂$syo_ongaku提高。<br>";}
				if($syo_bijutu){$bijutu += $syo_bijutu; $print_messe .= "・美術$syo_bijutu提高。<br>";}
				
				if($syo_looks){$looks += $syo_looks; $print_messe .= "・容貌值$syo_looks提高。<br>";}
				if($syo_tairyoku){$tairyoku += $syo_tairyoku; $print_messe .= "・體力$syo_tairyoku提高。<br>";}
				if($syo_kenkou){$kenkou += $syo_kenkou; $print_messe .= "・健康值$syo_kenkou提高。<br>";}
				if($syo_speed){$speed += $syo_speed; $print_messe .= "・速度$syo_speed提高。<br>";}
				if($syo_power){$power += $syo_power; $print_messe .= "・力$syo_power提高。<br>";}
				if($syo_wanryoku){$wanryoku += $syo_wanryoku; $print_messe .= "・腕力$syo_wanryoku提高。<br>";}
				if($syo_kyakuryoku){$kyakuryoku += $syo_kyakuryoku; $print_messe .= "・腳力$syo_kyakuryoku提高。<br>";}
				if($syo_love){$love += $syo_love; $print_messe .= "・LOVE度$syo_love提高。<br>";}
				if($syo_unique){$unique += $syo_unique; $print_messe .= "・有趣$syo_unique提高。<br>";}
				if($syo_etti){$etti += $syo_etti; $print_messe .= "・淫蕩度$syo_etti提高。<br>";}
#效果的設定
				if($syo_kouka ne "無"){
						($koukahadou,$sonoiryoku) = split(/,/,$syo_kouka);
						if ($koukahadou eq "萬能"){
								$byouki_sisuu += $sonoiryoku;
						}
						if ($koukahadou eq "感冒"){
								if ($byoumei =~ /感冒/){$byouki_sisuu += $sonoiryoku;}
						}
						if ($koukahadou eq "肺炎"){
								if ($byoumei =~ /肺炎/){$byouki_sisuu += $sonoiryoku;}
						}
						if ($koukahadou eq "結核"){
								if ($byoumei =~ /結核/){$byouki_sisuu += $sonoiryoku;}
						}
						if ($koukahadou eq "增重"){
								$taijuu += $sonoiryoku;
								$print_messe .= "・體重增加了$sonoiryoku kg。<br>";
						}
						if ($koukahadou eq "減肥"){
								$taijuu -= $sonoiryoku;
								$print_messe .= "・體重減少了$sonoiryoku kg。<br>";
						}
						if ($koukahadou eq "身長"){
								$sintyou += $sonoiryoku;
								$print_messe .= "・身長伸長了$sonoiryoku cm。<br>";
						}
						if ($koukahadou eq "縮小"){
								$sintyou -= $sonoiryoku;
								$print_messe .= "・身長縮小了$sonoiryoku cm。<br>";
						}
				}

				$syo_siyou_date = $now_time;
				if($syo_sintai_syouhi){$energy -= $syo_sintai_syouhi;$print_messe .= "・使用了$syo_sintai_syouhi的身體能源。<br>";}
				if($syo_zunou_syouhi){$nou_energy -= $syo_zunou_syouhi;$print_messe .= "・使用了$syo_zunou_syouhi的頭腦能源。<br>";}
				if($syo_cal){
						$taijuu_hue = $syo_cal / 1000;
						$taijuu += $taijuu_hue; $print_messe .= "・$taijuu_hue kg體重增加了。<br>";
				}
				
				if ($syo_taikyuu_tani eq "回"){
						$syo_taikyuu -- ;
				}
#出售的情況
		}elsif($in{'command'} eq "baikyaku" && $siyouzumi_flag == 0){
#ver.1.3從這裡
			$now_time = time;
			if ($syo_taikyuu_tani eq "日"){
				$keikanissuu = int (($now_time - $syo_kounyuubi) / (60*60*24));
				$nokorinissuu = $syo_taikyuu - $keikanissuu;
				$baikyaku_hyouzi = ($tanka * $nokorinissuu);
			}else{
				$baikyaku_hyouzi = ($tanka * $syo_taikyuu);
			}
				 $siyouzumi_flag = 1;
#ver.1.3到這裡
				$money += $baikyaku_hyouzi;
				$print_messe .= "●賣掉$in{'syo_hinmoku'}得到了、$baikyaku_hyouzi元。";
				next;
		}#if(「出售」指令的情況)的閉上
		
		}		#if(物品名一致)閉上
		if ($syo_taikyuu <= 0){next;}
		&syouhin_temp;
		push (@new_myitem_hairetu,$syo_temp);
	}		#foreach的閉上

#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			
#更新自己的所有物文件
			&lock;
			open(OUT,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
			print OUT @new_myitem_hairetu;
			close(OUT);	
			&unlock;
			
&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
$print_messe
</span>
</td></tr></table>
<br>

<div align="center"><a href=\"javascript:history.back()\"> [返回前畫面] </a></div>
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

######職業介紹所
sub job_change {
	open(SP,"./dat_dir/job.dat") || &error("Open Error : ./dat_dir/job.dat");
	$top_koumoku = <SP>;
	@job_hairetu = <SP>;
	close(SP);
#檢查BMI
	$taijuu = sprintf ("%.1f",$taijuu);
	&check_BMI($sintyou,$taijuu);
#從名單排除條件不足的職業
	foreach (@job_hairetu){
		&job_sprit($_);
		if($kokugo < $job_kokugo){next;}
		if($suugaku < $job_suugaku){next;}
		if($rika < $job_rika){next;}
		if($syakai < $job_syakai){next;}
		if($eigo < $job_eigo){next;}
		if($ongaku < $job_ongaku){next;}
		if($bijutu < $job_bijutu){next;}
		if($BMI < $job_BMI_min){next;}
		if ($job_BMI_max) { if($BMI > $job_BMI_max){next;}}
		if($looks < $job_looks){next;}
		if($tairyoku < $job_tairyoku){next;}
		if($kenkou < $job_kenkou){next;}
		if($speed < $job_speed){next;}
		if($power < $job_power){next;}
		if($wanryoku < $job_wanryoku){next;}
		if($kyakuryoku < $job_kyakuryoku){next;}
		if($love < $job_love){next;}
		if($unique < $job_unique){next;}
		if($etti < $job_etti){next;}
		if ($job_sex) {if($sex ne "$job_sex"){next;}}
		if($sintyou < $job_sintyou){next;}
		if ($job_syurui) {if($job_syurui ne $jobsyu){next;}}
		if($job_rank eq "2") {$job_hosi = "*";}elsif ($job_rank eq "3") {$job_hosi = "**";}elsif ($job_rank eq "4") {$job_hosi = "***";}elsif ($job_rank eq "5") {$job_hosi = "****";}else{$job_hosi = "";}
		
		$job_option .="<option value=$job_no>$job_name$job_hosi</option>";
	}
	
	if ($job_option eq ""){$job_option = "<option value=\"\">現在沒有可以就職的職業</option>";}
	&header(job_style);
	print <<"EOM";
	<form method="POST" action="$this_script">
	<input type=hidden name=mode value="job_change_go">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=k_id value="$in{'k_id'}">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<table width="95%" border="0" cellspacing="0" cellpadding="10" align=center class=yosumi><tr>
	<td bgcolor=#ffffff>如果滿足著必要的參數條件，便能對那個職業就職。自己想成為的職業為目標，致力於學習，練習等吧。再者，轉業的話經驗值、上班回數會變回0。<br>
	※職業的Level超過15的話就完全掌握了那個職業，提高水平了的職業有出現(職業名後邊的「*」是Level表)。
	</td>
	<td bgcolor=#333333 align=center width=300><img src="$img_dir/job_tytle.gif"></td></tr>
	<tr><td colspan=2>
	<span class="tyuu">$name君能從事的職業</span><img src=$img_dir/space.gif width=10 height=1>
	<select name="job_sentaku">
        $job_option
     </select><img src=$img_dir/space.gif width=10 height=1>
	 <input type=submit value="從事這個職業">
	 </td></tr></table></form>
EOM

#性別的表示整形
	if($sex eq "m") {$sex = "男";}else{$sex = "女";}
	
	print <<"EOM";
	<table width="95%" border="0" cellspacing="1" cellpadding="4" align=center class=yosumi>
	<tr><td colspan=25><font color=#336699>凡例:(國)=國語，(數)=數學，(理)=理科，(社)=社會，(英)=英語，(音)=音樂，(美)=美術，(容)=容貌，(身體)=體力，(健)=健康，(速)=速度，(pa)=力，(腕)=腕力，(腳)=腳力，(淫)=淫蕩</font></td></tr>
	<tr bgcolor=#ff9933 align=center><td nowrap rowspan=2>職業</td><td colspan=17>必要的參數</td><td align=center colspan=3>条　件</td><td rowspan=2 align=center>工  資<br>(1次上班)</td><td rowspan=2 align=center>獎金</td><td rowspan=2>支薪</td><td rowspan=2 nowrap>身體<br>能量<br>消費</td><td rowspan=2 nowrap>頭腦<br>能量<br>消費</td></tr>
	<tr bgcolor=#ffcc33 align=center><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td nowrap>身體質量指數</td><td nowrap>性別</td><td nowrap>身長</td></tr>
	
	<tr bgcolor=#ffff33 align=center><td>現在$name君的參數</td><td>$kokugo</td><td>$suugaku</td><td>$rika</td><td>$syakai</td><td>$eigo</td><td>$ongaku</td><td>$bijutu</td><td>$looks</td><td>$tairyoku</td><td>$kenkou</td><td>$speed</td><td>$power</td><td>$wanryoku</td><td>$kyakuryoku</td><td>$love</td><td>$unique</td><td>$etti</td><td nowrap>$BMI</td><td>$sex</td><td>$sintyou</td><td align=center nowrap>-</td><td nowrap>-</td><td>-</td><td>-</td><td>-</td></tr>
EOM
	$i=1;
	foreach  (@job_hairetu) {
			&job_sprit($_);
			if ($job_syurui) {if($job_syurui ne $jobsyu){next;}}
			if ($job_BMI_min eq "" && $job_BMI_max eq ""){$BMI_hani = "";}
			elsif ($job_BMI_min eq "" ){$BMI_hani = "$job_BMI_max以下";}
			elsif ($job_BMI_max eq "" ){$BMI_hani = "$job_BMI_min以上";}
			else {$BMI_hani = "$job_BMI_min～$job_BMI_max";}
			
			if ($job_siharai eq "1"){$sihrai_seikei = "支薪";}
			else{$sihrai_seikei = "$job_siharai回上班";}
			
			if ($job_sintyou){$job_sintyou = "$job_sintyou以上";}
			if($job_sex eq "m") {$job_sex = "男";}elsif($job_sex eq "f"){$job_sex = "女";}
			if($job_rank eq "2") {$job_hosi = "*";}elsif ($job_rank eq "3") {$job_hosi = "**";}elsif ($job_rank eq "4") {$job_hosi = "***";}elsif ($job_rank eq "5") {$job_hosi = "****";}else{$job_hosi = "";}
		print <<"EOM";		#ver.1.30
	<tr bgcolor=#ffcc66 align=center><td nowrap>$job_name$job_hosi</td><td>$job_kokugo</td><td>$job_suugaku</td><td>$job_rika</td><td>$job_syakai</td><td>$job_eigo</td><td>$job_ongaku</td><td>$job_bijutu</td><td>$job_looks</td><td>$job_tairyoku</td><td>$job_kenkou</td><td>$job_speed</td><td>$job_power</td><td>$job_wanryoku</td><td>$job_kyakuryoku</td><td>$job_love</td><td>$job_unique</td><td>$job_etti</td><td nowrap>$BMI_hani</td><td>$job_sex</td><td nowrap>$job_sintyou</td><td align=right nowrap>$job_kyuuyo元</td><td nowrap>×$job_bonus</td><td nowrap>$sihrai_seikei</td><td>$job_energy</td><td>$job_nou_energy</td></tr>
EOM
		if ($i % 10 == 0){print <<"EOM";
	<tr bgcolor=#ff9933 align=center><td nowrap rowspan=2>職業</td><td colspan=17>必要的參數</td><td align=center colspan=3>條  件</td><td rowspan=2 align=center>工  資<br>(1次上班)</td><td rowspan=2 align=center>獎金</td><td rowspan=2>支薪</td><td rowspan=2 nowrap>身體<br>能量<br>消費</td><td rowspan=2 nowrap>頭腦<br>能量<br>消費</td></tr>
	<tr bgcolor=#ffcc33 align=center><td>國</td><td>數</td><td>理</td><td>社</td><td>英</td><td>音</td><td>美</td><td>容</td><td>體</td><td>健</td><td>速</td><td>力</td><td>腕</td><td>腳</td><td>愛</td><td>趣</td><td>淫</td><td nowrap>身體質量指數</td><td nowrap>性別</td><td nowrap>身長</td></tr>
	<tr bgcolor=#ffff33 align=center><td>現在$name君的參數</td><td>$kokugo</td><td>$suugaku</td><td>$rika</td><td>$syakai</td><td>$eigo</td><td>$ongaku</td><td>$bijutu</td><td>$looks</td><td>$tairyoku</td><td>$kenkou</td><td>$speed</td><td>$power</td><td>$wanryoku</td><td>$kyakuryoku</td><td>$love</td><td>$unique</td><td>$etti</td><td nowrap>$BMI</td><td>$sex</td><td>$sintyou</td><td align=center nowrap>-</td><td nowrap>-</td><td>-</td><td>-</td><td>-</td></tr>
EOM
		}
		$i ++;
	}
	print <<"EOM";
	</table>
EOM
	&hooter("login_view","返回");
	exit;
}

######職業交換處理
sub job_change_go {
	open(SP,"./dat_dir/job.dat") || &error("Open Error : ./dat_dir/job.dat");
	$top_koumoku = <SP>;
	@job_hairetu = <SP>;
	close(SP);
	foreach  (@job_hairetu) {
			&job_sprit($_);
			if($in{'job_sentaku'} eq "$job_no"){
				$job = $job_name;
				$job_keiken = 0;
				$job_kaisuu = 0;
				last;
			}
	}
#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
			
			&message("職業變成$job_name。","login_view");
}

####工作
sub do_work {
	$date_sec = time;
#ver.1.2
	if ($date_sec - $house_name < 60*$work_seigen_time){&error("能工作的間隔是$work_seigen_time分。");}
	open(SP,"./dat_dir/job.dat") || &error("Open Error : ./dat_dir/job.dat");
	$top_koumoku = <SP>;
	@job_hairetu = <SP>;
	close(SP);
	foreach  (@job_hairetu) {
			&job_sprit($_);
			if($job_name eq "$job"){
				last;
			}
	}
#檢查工作的能力
	if ($kokugo < $job_kokugo || $suugaku < $job_suugaku || $rika < $job_rika || $syakai < $job_syakai || $eigo < $job_eigo || $ongaku < $job_ongaku || $bijutu < $job_bijutu || $looks < $job_looks || $tairyoku < $job_tairyoku || $kenkou < $job_kenkou || $speed < $job_speed || $power < $job_power || $wanryoku < $job_wanryoku || $kyakuryoku < $job_kyakuryoku || $love < $job_love || $unique < $job_unique || $etti < $job_etti){&error("因為低於對這個工作必要的能力值所以不能工作。");}
#檢查BMI
	$taijuu = sprintf ("%.1f",$taijuu);
	&check_BMI($sintyou,$taijuu);
	if($energy < "$job_energy"){&error("身體力不夠！<br>要工作需要$job_energy的身體力。");}
	if($nou_energy < "$job_nou_energy"){&error("頭腦力不夠！<br>要工作需要$job_nou_energy的頭腦力。");}
	if($job_BMI_min){
			if($BMI < "$job_BMI_min"){&error("身體質量指數因為在條件值以下不能工作！");}
	}
	if($job_BMI_max){
			if($BMI > "$job_BMI_max"){&error("身體質量指數因為在條件值以上不能工作！");}
	}
#身體力計算
$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku);
$last_ene_time= $date_sec;
$energy_max = int(($tairyoku/2) + ($kenkou/3) + ($power/5) + ($wanryoku/8) + ($kyakuryoku/8));
if($energy > $energy_max){$energy = $energy_max;}
if($energy < 0){$energy = 0;}
#頭腦力計算
$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku);
$last_nouene_time= $date_sec;
$nou_energy_max = int(($kokugo/4) + ($suugaku/4) + ($rika/4) + ($syakai/4) + ($eigo/4)+ ($ongaku/4)+ ($bijutu/4));
if($nou_energy > $nou_energy_max){$nou_energy = $nou_energy_max;}
if($nou_energy < 0){$nou_energy = 0;}
	
	$mae_job_level = int($job_keiken / 100) ;
#加經驗值
if($in{'cond'} eq "最高") {$randed = "15";}
elsif($in{'cond'} eq "良好") {$randed = "10";}
elsif($in{'cond'} eq "一般") {$randed = "5";}
elsif($in{'cond'} eq "不良") {$randed = "1";}
elsif($in{'cond'} eq "壞") {$randed = "-5";}
elsif($in{'cond'} eq "<font color=#ff6600>少許覺感冒</font>") {$randed = "-8";}
elsif($in{'cond'} eq "<font color=#ff6600>感冒</font>") {$randed = "-14";}
elsif($in{'cond'} eq "<font color=#ff6600>肺炎</font>") {$randed = "-20";}
else{&error("這樣的身體不能工作！");}
	$randed += int(rand(5))+1;
	$job_keiken += $randed;
	
if($randed > 0) {$print_messe .= "・得到了$randed的經驗值。<br>";}
elsif($randed < 0) {$print_messe .= "・經驗值$randed減少了。<br>";}
else{$print_messe .= "・不能取得經驗。<br>";}
	
#每(100經驗值)提高Level計算，加薪額計算
	$ato_job_level = int($job_keiken / 100) ;
	$syoukyuugaku = ($job_kyuuyo*$ato_job_level/100)*$job_syoukyuuritu;
	$job_kyuuyo += $syoukyuugaku;
#Level up表示
	if($ato_job_level > $mae_job_level){
			$print_messe .= "・昇Level了！<br>";
			$print_messe .= "・$job_kyuuyo元/1回的加薪了。<br>";
			$bonusgaku = $job_kyuuyo * $job_bonus;
			$money += $bonusgaku;
			if($bonusgaku > 0){
					$print_messe .= "・得到$bonusgaku元的獎金！<br>";
			}
			if ($ato_job_level >= 15){
				if ($jobsyu ne "$job"){
					$jobsyu = "$job";
					$print_messe .= "・完全掌握了$job的工作！<br>";
				}
			}
	}
	
#加工作回數
	$job_kaisuu ++;
#如果以支薪規定回能除得開工資支薪
	if($job_kaisuu % $job_siharai ==0){
			$kyounosiharai = $job_kyuuyo * $job_siharai;
			$money += $kyounosiharai;
			if ($job_siharai == 1){
				$print_messe .= "・得到了$kyounosiharai元的工資！<br>";
			}else{
				$print_messe .= "・得到$kyounosiharai元($job_kyuuyo日元×$job_siharai回上班)的工資！<br>";
			}
	}
	
#設置身體力和頭腦力
	$energy -= $job_energy;
	$nou_energy -= $job_nou_energy;
#從體重中扣減能源份兒
	$taijuu_heri = ($job_energy / 100);
	$taijuu -= $taijuu_heri;
	$print_messe .= "・$taijuu_heri kg體重減少了。";
	
#記錄最後工作了的時間（v1.11）
	$house_name = $date_sec;

#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);
	&header("","sonomati");
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>
<span class="job_messe">
●出去工作的第($job_kaisuu回)<br>
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
