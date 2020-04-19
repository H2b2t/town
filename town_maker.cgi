#!/perl/bin/perl
# ↑使用合乎服務器的路徑。
#+++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2003-2004 brassiere
$version = 'TOWN ver.1.40';
#  web：http://brassiere.jp/
#  mail：shohei@brassiere.jp
#因這個程序發生的事故不承擔責任。
#+++++++++++++++++++++++++++++++++++++

#※這個程序是免費軟件；不過，在遊戲內時常「文本廣告」被表示。
#同時，因為超過預想花費了費力和時間，歡迎著任意的使用費用的支付。
#一般認為有實際設置，運用了之後只是支付費用價值，可以支付認為是適當的額就非常高興。
#為了維持今後的開發維持能得到非常的幫助

#	  當然沒有支付義務，也沒有機能限制。
#支付了費用和沒有支付費用一方的沒有區別。
#因為普遍是不支付，亦不會怪怨(笑。
#儘管如此支付費用請這樣的，拜託到下列匯款目標匯款。

#　＜任意的費用支付處＞
#　みずほ銀行　集中第一支店　活期存款
#　支店號碼：822
#　戶口號碼：9502477
#　接收者名：イーバンクギンコウ(カ

#　※費用的目標(徹底用參考，這個以下也這個以上也不介意ｗ)
#　○滿足=500日元
#　○非常非常滿足=1000日元
#　○感動了！極好！=1500日元

#　<重要> 這個遊戲畫像面積很大，頻繁做讀入，
#特別在通信容量中需要注意(在這個網站的負荷實際完全不做規定的情況，10日為10G大的通信量)。
#設置時候確認了用那個服務器定了的通信容量之後盡量地安排「街的移動的時候間」及「行動的限制時間」，
#強烈推薦經常檢查通信量的推移。同時，把服務器複數帶著只畫像放在另外服務器(初始設置做畫像文件夾的指定)，
#使之分散通信量也有效。


#require './jcode.pl';
require './cgi-lib.pl';
require './top.pl';
require './town_ini.cgi';
require './command.pl';
require './event.pl';
require './town_lib.pl';		#ver.1.4
require './unit.pl';		#ver.1.4
&decode;

# 指定HOST訪問拒絕
	# 取得主機名
	$get_host = $ENV{'REMOTE_HOST'};
	$get_addr = $ENV{'REMOTE_ADDR'};
	if ($get_host eq "" || $get_host eq $get_addr) {
		$get_host = gethostbyaddr(pack("C4", split(/\./, $get_addr)), 2) || $get_addr;
	}
	if ($get_host eq "") { &error("對不起在HOST不能取得的環境下是不能訪問"); }
	foreach (@deny) {
		if ($_ eq "") { next; }
		$_ =~ s/\*/\.\*/g;
		if ($get_host =~ /$_/i) { &error("對不起從利用中的HOST不能訪問"); }
	}

	
#維護檢查
	if($mente_flag == 1 && $in{'admin_pass'} eq "" && $in{'mode'} ne ""){&error("$mente_message")}	#ver.1.2

sub joukenbunki {
}

$seigenyou_now_time = time;
#限制時間檢查
		$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $access_byou);
		if($seigenyou_now_time - $access_byou < $koudou_seigen){&error("暫時未能行動。請等候$ato_nanbyou秒以後。")}

#ver.1.40從這裡
#密碼記錄作成
	if ( !-e $pass_logfile){
		open(LOGF,"$logfile") || &error("Open Error : $logfile");
		@pass_sakuse = <LOGF>;
		close(LOGF);
		foreach (@pass_sakuse){
			&list_sprit($_);
			$henkan_temp = "$list_k_id<>$list_name<>$list_pass<>\n";
			push (@henkan_pass,$henkan_temp);
		}
		sub by_r_number {$b <=> $a;}
		@henkan_pass = sort by_r_number @henkan_pass;
		open(PSS,">$pass_logfile") || &error("Write Error : $pass_logfile");
		print PSS @henkan_pass;
		chmod 0666,"$pass_logfile";
		close(PSS);
	}
#條件分歧
	if($in{'mode'} eq "login_view"){&login_view;}
	if($in{'mode'} eq "orosi"){&orosi;}
	if($in{'mode'} eq "buy_orosi"){&buy_orosi;}
	if($in{'mode'} eq "gym"){&gym;}
	if($in{'mode'} eq "training"){&training;}
	if($in{'mode'} eq "syokudou"){&syokudou;}
	if($in{'mode'} eq "syokuzisuru"){&syokuzisuru;}
	if($in{'mode'} eq "school"){&school;}
	if($in{'mode'} eq "do_school"){&do_school;}
	if($in{'mode'} eq "depart_gamen"){&depart_gamen;}
	if($in{'mode'} eq "buy_syouhin"){&buy_syouhin;}
	if($in{'mode'} eq "kentiku"){&kentiku;}
	if($in{'mode'} eq "kentiku_do"){&kentiku_do;}
	if($in{'mode'} eq "aisatu"){&aisatu;}
	if($in{'mode'} eq "mail_sousin"){&mail_sousin;}
	if($in{'mode'} eq "mail_do"){&mail_do;}
#ver.1.40到這裡
	&main_view($in{'town_no'});
exit;


###################子程序

#進入畫面
sub login_view {
#如果日期更變的事件
	&time_get;
	my ($hutuu_risoku,$teiki_risoku);
	if ($access_time ne "$date"){
		$access_time = $date;
#存款的利息計算
		$hutuu_risoku = int ($bank*0.005);
		if ($hutuu_risoku > 0){
			$bank += $hutuu_risoku;
			&kityou_syori("活期存款利息","",$hutuu_risoku,$bank,"普");
		}
		$teiki_risoku = int ($super_teiki*0.01);
		if ($teiki_risoku > 0){
			$super_teiki += $teiki_risoku;
			&kityou_syori("超級定期利息","",$teiki_risoku,$super_teiki,"定");
		}
#安揭貸款
		if ($loan_kaisuu > 0){
			$bank -= $loan_nitigaku;
			$loan_kaisuu --;
			&kityou_syori("安揭支付","$loan_nitigaku","",$bank,"普");
		}
#來自孩子的生活補貼處理
		&kodomo_siokuri;
	}
#事故的情況
	if ($in{'ziko_flag'} eq "on" && $in{'ziko_idousyudan'} ne "徒步"){
		$monokiroku_file="./member/$k_id/mono.cgi";
		open(CAR,"$monokiroku_file") || &error("Open Error : $monokiroku_file");
		@mycar_hairetu = <CAR>;
		close(CAR);
		$ziko_sya_flg=0;
#ver.1.40從這裡
		foreach  (@mycar_hairetu) {
			&syouhin_sprit($_);
			if ($in{'ziko_idousyudan'} eq "$syo_hinmoku"){
				if ($ziko_sya_flg==0){
					$syo_taikyuu -- ;
					if ($syo_taikyuu <= 0){$taiha_comment = "$in{'ziko_idousyudan'}被嚴重毀壞。";$ziko_sya_flg=1;next;}else{
			$taiha_comment = "殘餘的耐久（$syo_taikyuu）";}
					$ziko_sya_flg=1;
				}
			}
#ver.1.40到這裡
			&syouhin_temp;
			push (@new_mycar_hairetu,$syo_temp);
		}
#更新自己的所有物文件
			&lock;
			open(OUT,">$monokiroku_file") || &error("Write Error : $monokiroku_file");
			print OUT @new_mycar_hairetu;
			close(OUT);	
			&unlock;
		&message("<font color=#ff6600>發生了交通事故！<br>「$in{'ziko_idousyudan'}」的耐久度減少了1。<br>$taiha_comment</font>","login_view");
	}		#是事故的情況閉上
	&event_happen;
	$k_sousisan = $money + $bank + $super_teiki - ($loan_nitigaku * $loan_kaisuu);
	&main_view("$in{'town_no'}");
exit;
}

#首頁畫面右部分
sub top_gamen {
open(IN,"$maintown_logfile") || &error("Open Error : $maintown_logfile");
			$maintown_para = <IN>;
			if ($maintown_para eq ""){&error("$maintown_logfile有問題。麻煩您向管理員（$master_ad）聯絡。");}			#空ログチェック		ver.1.22
			&main_town_sprit($maintown_para);
close(IN);
&time_get;
#如果日期變成在今天的日期裡就更新，批發標誌把食堂標誌做為0 Main town 記錄更新，批發時刻，明天的批發時刻
	if($date ne $mt_today){
			$mt_today=$date;
			$mt_t_time=$mt_y_time;
			$mt_y_time=int(rand(20))+1;		#ver.1.3
			$mt_orosiflag=0;
			$mt_syokudouflag=0;
			$mt_departflag=0;
			&main_town_temp;
			&lock;
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			print OUT $mt_temp;
			close(OUT);	
			&list_log_backup;
			&unlock;
	}

	open(IN,"$logfile") || &error("Open Error : $logfile");
	@rankingMember = <IN>;
	$sankasyasuu = @rankingMember;
	close(IN);
	my $mt_keizai_hyouzi = int ($mt_keizai / (int(($date_sec - $mt_yobi8)/(60*60*24))+1));
	my $mt_henei_hyouzi = int ($mt_hanei / (int(($date_sec - $mt_yobi8)/(60*60*24))+1));
			if ($tajuukinsi_flag==1){$tajuucomment = "<br>※禁止多重登記。";}
			if ($tajuukinsi_deny==1){$tajuucomment .= "注意，被發現多重登記你將不能進入遊戲。";}
	print <<"EOM";
      <table width="100%" border="0" cellspacing="0" cellpadding="7">
        <tr>
          <td>
            <div align="center"><font size="5"><b>$title</b></font></div>
          </td>
        </tr>
        <tr>
          <td  class="yosumi">人口：$sankasyasuu人　<span  onMouseOver='onMes5(\"居民的店的平均1日銷售額(街全體)\")' onMouseOut='onMes5(\"\")'>經濟力：$mt_keizai_hyouzi元</span>　<span  onMouseOver='onMes5(\"留言板的平均1日的寫入數(街全體)\")' onMouseOut='onMes5(\"\")'>繁榮度：$mt_henei_hyouzi</span></td>
        </tr>
        <tr>
          <td>	$osirase
<!-- ver.1.30從這裡 -->
EOM
if ($genzaino_ninzuu >= $douzi_login_ninzuu){
	print <<"EOM";
		<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>現在，超過著$douzi_login_ninzuu人同時進入的限制。真對不起，請稍後再進入。</td></tr></table>
EOM
	}else{
	print <<"EOM";
     <form method="POST" action="$script">
	<input type=hidden name=mode value="login_view">
        ●進入(已完成登記)<br>
        名字：
        <input type="text" name="name" size="18" value=$ck{'name'}><br>
        密碼： 
        <input type="password" name="pass" size="18" value=$ck{'pass'}><br>
EOM
	if ($sanka_hyouzi_kinou == 1){
		print <<"EOM";
		參加者之名字一覽 <input type="radio" name="sanka_hyouzi_on" value="off">不表示 
		<input type="radio" name="sanka_hyouzi_on" value="on" checked>表示<br>
EOM
	}
		print <<"EOM";
        <div align=center><input type="submit" value="OK"></div>
      </form>
	<hr size=1>
EOM
	if ($sankasyasuu >= $saidai_ninzuu){
		print "※因為現在達到著最大登記人數，所以不接受新登記。";
	}elsif($new_touroku_per == 1) {
		print "※現在暫停接受新登記。";
	}else{
		print <<"EOM";
     <form method="POST" action="game.cgi">
	<input type=hidden name=mode value="new">
		●新玩者登記（最大登記人數：$saidai_ninzuu人）$tajuucomment<br>
        名字： 
        <input type="text" name="name" size="18"> <br>
        密碼： 
        <input type="password" name="pass" size="18"><br>
		性別： 
        <input type="radio" name="sex" value="m">男 
		<input type="radio" name="sex" value="f">女<br>
        <div align=center><input type="submit" value="OK"></div>
      </form>
EOM
	}
}		#沒超過限制人數的情況閉上
# ver.1.30到這裡
	print <<"EOM";
	<hr size=1>
	<form method=POST action="admin.cgi">
	<input type=hidden name=mode value="admin">
	密碼 <input type=password size=8 name="admin_pass"> <input type=submit value="管理者選單">
	</form>
		  </td>
        </tr>
      </table>
EOM
}

#街信息窗的輸出
sub town_jouhou {
	$keizai_hyouzi = int ($keizai / (int(($date_sec - $t_yobi2)/(60*60*24))+1));
	$hanei_hyouzi = int ($hanei / (int(($date_sec - $t_yobi2)/(60*60*24))+1));
	print <<"EOM";
<table width="100%" border="0" cellspacing="0" cellpadding="2" align=center class="yosumi">
<tr><td><div align=center><span  class="tyuu">「$title」内</span><br><span  class="midasi">$town_name</span></div></td><td>地 價：$town_tika_hairetu[@_[0]]萬<br><span  onMouseOver='onMes5(\"這條街的居民的店的平均1日銷售額\")' onMouseOut='onMes5(\"\")'>經濟力：$keizai_hyouzi元</span><br><span  onMouseOver='onMes5(\"這條街的留言板的平均1日寫入數\")' onMouseOut='onMes5(\"\")'>繁榮度：$hanei_hyouzi</span></td></tr></table><br>
EOM
}

#命令按鈕的輸出
sub command_botan {			#ver.1.3	戀愛按鈕，配偶家設定按鈕追加，育兒按鈕追加，可愛的我家按鈕刪掉，按鈕的排列數變更
#打開購買物文件
	$monokiroku_file="./member/$k_id/mono.cgi";
	if (! -e $monokiroku_file){
		open (MOF,">$monokiroku_file") || &error("不能作成自己的購買物文件");
		close(MOF);
	}
	open(MK,"$monokiroku_file") || &error("自己的購買物文件不能打開");
	@my_kounyuu_list =<MK>;
	@mono_name_keys = ();
	@mono_kouka_keys = ();
	foreach (@my_kounyuu_list){
		&syouhin_sprit($_);
		if ($syo_taikyuu <= 0){next;}
		push (@mono_name_keys ,$syo_hinmoku);
		push (@mono_kouka_keys ,$syo_kouka);
	}
	$botanyou_mono_check = join("<>",@mono_name_keys);
	$botanyou_kouka_check = join("<>",@mono_kouka_keys);
	close(MK);
	
	if ($renai_system_on == 1){$botan_narabi_suu = 7;}else{$botan_narabi_suu = 6;}
	$kaigyou_flag=1;
	$top_botan  .= <<"EOM";
<form method=POST action=\"$script\"><td><input type=hidden name=mode value="login_view">	<input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/reload.gif' width=32 height=32  onMouseOver='onMes5(\"更新畫面。「力」休息後，按這個按鈕慢慢的增加。\")' onMouseOut='onMes5(\"\")'></td></form>
EOM

	if ($job ne "學生"){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"basic.cgi\"><td><input type=hidden name=mode value="do_work">	<input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=hidden name=cond value="$condition"><input type=image src='$img_dir/go_work.gif' width=32 height=32  onMouseOver='onMes5(\"外出工作。現在，經驗值:$job_keiken 工作數:$job_kaisuu回\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM
	}
	
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value="item"><td><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/item.gif' width=32 height=32  onMouseOver='onMes5(\"使用物品。\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"$script\"><td><input type=hidden name=mode value="aisatu">	<input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/aisatu.gif' width=32 height=32  onMouseOver='onMes5(\"以今天的事情和心情等寒暄吧。\")' onMouseOut='onMes5(\"\")'></td></form>
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"$script\"><td><input type=hidden name=mode value="mail_sousin">	<input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/mail.gif' width=32 height=32  onMouseOver='onMes5(\"向這街的居民發送信息。\")' onMouseOut='onMes5(\"\")'></td></form>
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"game.cgi\"><td><input type=hidden name=mode value="doukyo">	<input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/doukyo.gif' width=32 height=32  onMouseOver='onMes5(\"培育自己的人物。\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM

	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .= "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"game.cgi\"><td><input type=hidden name=mode value="battle">	<input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/battle.gif' width=32 height=32  onMouseOver='onMes5(\"出街比賽。\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM

	if ($unit{$k_id} ne ""){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"original_house.cgi\"><td><input type=hidden name=mode value="my_house_settei">	<input type=hidden name=iesettei_id value="$k_id"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/my_housein.gif' width=32 height=32  onMouseOver='onMes5(\"進行有關自己的家的各種設定。\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM
	}

	if ($unit{$house_type} ne ""){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"original_house.cgi\"><td><input type=hidden name=mode value="my_house_settei"><input type=hidden name=iesettei_id value="$house_type"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/my_housein2.gif' width=32 height=32  onMouseOver='onMes5(\"進行有關配偶的家的各種設定。\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM
	}
	
	if ($love >= $need_love && $renai_system_on == 1){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"kekkon.cgi\"><td><input type=hidden name=mode value="renai"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/renai.gif' width=32 height=32  onMouseOver='onMes5(\"與戀人約會、求婚。\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM
	}
	
	if ($love >= $need_love && $renai_system_on == 1){
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan  .=  "</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"kekkon.cgi\"><td><input type=hidden name=mode value="kosodate"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/kosodate.gif' width=32 height=32  onMouseOver='onMes5(\"育兒。\")' onMouseOut='onMes5(\"\")'></td></form><!--ver.1.40-->
EOM
	}
	
	$kaigyou_flag ++;
	if($kaigyou_flag % $botan_narabi_suu == 0){$top_botan .="</tr><tr>";}
	$top_botan  .= <<"EOM";
<form method=POST action=\"game.cgi\"><td><input type=hidden name=mode value="data_hozon">	<input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/off.gif' width=32 height=32  onMouseOver='onMes5(\"數據保存。最後保存了的吃飯時間超過$deleteUser日的話用戶將被刪掉。\")' onMouseOut='onMes5(\"\")'></td></form><!-- ver.1.40 -->
EOM

	print "<table boader=0 width=100%><tr>$top_botan</tr></table>";
}

#個人參數輸出
sub loged_gamen {
#力的MAX值計算
	$energy_max = int(($looks/12) + ($tairyoku/4) + ($kenkou/4) + ($speed/8) + ($power/8) + ($wanryoku/8) + ($kyakuryoku/8));
	$nou_energy_max = int(($kokugo/6) + ($suugaku/6) + ($rika/6) + ($syakai/6) + ($eigo/6)+ ($ongaku/6)+ ($bijutu/6));
	my ($date_sec) = time;
	
#身體力計算		#ver.1.3
	if ($in{'iiyudane'} eq "one"){
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku*$onsen_times);
	}elsif($in{'iiyudane'} eq "two"){
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku*$tokubetu_times);
	}else{
		$energy = $energy + int(($date_sec - $last_ene_time)/$sintai_kaihuku);
	}
	$last_ene_time= $date_sec;

	if($energy > $energy_max){$energy = $energy_max;}
	if($energy < 0){$energy = 0;}
#頭腦力計算		#ver.1.3
	if ($in{'iiyudane'} eq "one"){
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku*$onsen_times);
	}elsif($in{'iiyudane'} eq "two"){
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku*$tokubetu_times);
	}else{
		$nou_energy = $nou_energy + int(($date_sec - $last_nouene_time)/$zunou_kaihuku);
	}
	$last_nouene_time= $date_sec;

	if($nou_energy > $nou_energy_max){$nou_energy = $nou_energy_max;}
	if($nou_energy < 0){$nou_energy = 0;}

#new郵件的檢查
	$message_file="./member/$k_id/mail.cgi";
	open(MS,"$message_file") || &error("自己的郵件log file不能打開");
	$lastCheckTime=<MS>;		#最後郵件時間的取得
	@lastMailTime=<MS>;		#郵件數據排列
	close(MS);
	foreach (@lastMailTime){
		&mail_sprit($_);
		if ($m_syubetu ne "發送"){$saigono_kita_mail = $m_byou;last;}
	}
	@lastMailTime=split(/<>/,$lastMailTime);
	if($lastCheckTime < $saigono_kita_mail){$happend_ivent .= "<div style=color:#ff3300>★接收箱有新的信息！</div>";}
	
#身體力百分比(％)算出
	if(! $energy_max){$energy_max =1;}
	$ener_parcent = int($energy / $energy_max * 100);
	$nokori_parcent = 100-$ener_parcent;
	if ($ener_parcent >59){$energy_bar = "energy_ao.gif";}
	elsif ($ener_parcent >19){$energy_bar = "energy_ki.gif";}
	else{$energy_bar = "energy_aka.gif";}
	
#頭腦力百分比(％)算出	
	if(! $nou_energy_max){$nou_energy_max =1;}
	$nou_ener_parcent = int($nou_energy / $nou_energy_max * 100);
	$nou_nokori_parcent = 100-$nou_ener_parcent;
	if ($nou_ener_parcent >59){$nou_energy_bar = "energy_ao.gif";}
	elsif ($nou_ener_parcent >19){$nou_energy_bar = "energy_ki.gif";}
	else{$nou_energy_bar = "energy_aka.gif";}

#日期變換最後進餐了的時間
	&byou_hiduke($last_syokuzi);
	$last_syokuzi_henkan = $bh_full_date;
#算出空腹度
	$tabetenaizikan = $date_sec - $last_syokuzi ;
	$manpuku_time = $syokuzi_kankaku*60;
	if ($tabetenaizikan < $manpuku_time){$kuuhukudo = "<font color=#ff3300>吃飽(暫時不能吃飯)</font>";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*2 ){$kuuhukudo = "剛剛好";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*12 ){$kuuhukudo = "稍稍肚餓";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*24 ){$kuuhukudo = "肚餓";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*48 ){$kuuhukudo = "相當肚餓";}
	elsif ($tabetenaizikan < $manpuku_time + 60*60*24*4 ){$kuuhukudo = "極度肚餓";}		#ver.1.3
	elsif ($tabetenaizikan < $manpuku_time + 60*60*24*($deleteUser - 3)){$kuuhukudo = "快要死了。。";}		#ver.1.3
	else{$kuuhukudo = "危險！在死亡的咫尺之間。";}		#ver.1.3
	
#檢查BMI
	$taijuu = sprintf ("%.1f",$taijuu);
	&check_BMI($sintyou,$taijuu);

##狀況計算
#調整剩餘力
$condition_sisuu = ($nou_ener_parcent + $ener_parcent)/2;
#調整健康值
$condition_sisuu += $kenkou / 100;
#調整空腹度
if ($kuuhukudo eq "<font color=#ff3300>吃飽(還不能吃飯)</font>"){$condition_sisuu *= 0.8;}elsif ($kuuhukudo eq "剛剛好"){$condition_sisuu *= 1;} elsif ($kuuhukudo eq "稍稍肚餓"){$condition_sisuu *= 0.9;} elsif ($kuuhukudo eq "肚餓"){$condition_sisuu *= 0.7;} elsif ($kuuhukudo eq "相當肚餓"){$condition_sisuu *= 0.6;} elsif ($kuuhukudo eq "極度肚餓"){$condition_sisuu *= 0.5;}else{$condition_sisuu *= 0.3;} 
#調整體係指數
if ($taikei eq "肥胖"){$condition_sisuu *= 0.8;}elsif ($taikei eq "稍稍胖"){$condition_sisuu *= 0.95;} elsif ($taikei eq "標準"){$condition_sisuu *= 1;} elsif ($taikei eq "瘦"){$condition_sisuu *= 0.95;} else{$condition_sisuu *= 0.8;} 

if($condition_sisuu > 98) {$condition = "最高"; $byouki_sisuu += 2}
elsif($condition_sisuu > 75) {$condition = "良好"; $byouki_sisuu += 1}
elsif($condition_sisuu > 50) {$condition = "一般";}
elsif($condition_sisuu > 30) {$condition = "不良"; $byouki_sisuu -= -1}
elsif($condition_sisuu > 10) {$condition = "壞"; $byouki_sisuu -= 3}
else{$condition = "最壞";}

if ($byouki_sisuu < -100){$byoumei = "癌";}
elsif  ($byouki_sisuu < -70){$byoumei = "腦瘤";}
elsif  ($byouki_sisuu < -40){$byoumei = "結核";}
elsif  ($byouki_sisuu < -20){$byoumei = "肺炎";}
elsif  ($byouki_sisuu < -10){$byoumei = "感冒";}
elsif  ($byouki_sisuu < 0){$byoumei = "少許感冒";}
else {$byoumei = "";}

if ($byoumei){$condition = "<font color=#ff6600>$byoumei</font>";}

#Job Level算出
	$job_level = int($job_keiken / 100) ;

#HOST保存
	$host = $get_host;
	
#登入非表示on off		#ver.1.30
	if ($in{'sanka_hyouzi_on'} eq "on"){$mise_type = "on";}		#ver.1.30
	if ($in{'sanka_hyouzi_on'} eq "off"){$mise_type = "off";}		#ver.1.30

#最後訪問保存
	$last_access_byou = $access_byou;
	if ($in{'mode'} ne "syokudou" && $in{'mode'} ne "school" && $in{'mode'} ne "gym"){
		$access_byou = $date_sec;
	}

#記錄更新
			&temp_routin;
			&log_kousin($my_log_file,$k_temp);

#個人參數表示
	print <<"EOM";
<table width="100%" border="0" cellspacing="0" cellpadding="3" align=center>
<tr><td valign="top" width=65%>

<table  width="100%"  height="100% "border="0"  cellspacing="0" cellpadding="2" style=" border: $st_win_wak; border-style: solid; border-width: 1px;" bgcolor=$st_win_back>
<tr><td>
EOM

#要是登入模式表示命令按鈕
if ($in{'mode'} eq "login_view"){
	&command_botan;
#如果有限制時間則表示限製
#	&error("$koudou_seigen");
		if ($koudou_seigen > 0){
					if ($koudou_seigen > 999){$seigen_width = 5;}elsif($koudou_seigen > 99){$seigen_width = 4;}else{$seigen_width = 3;}
					$ato_nanbyou=$koudou_seigen-($seigenyou_now_time - $last_access_byou);
					$saikoroprint="<span style=\"color:#666666; font-size: 9px; \">　到能行動還需等待<input type=text name=cdown value=\"$koudou_seigen\" size=$seigen_width style='color:#ff3300; height: 10px; font-size: 10px; border: 0'>秒</span>";
		}
	
	print <<"EOM";
<table width="98%" border="0" cellspacing="0" cellpadding="5" align=center>
<tr><form  name=form1 method=POST action=\"$script\"><input type=hidden name=mode value="mail_sousin"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}>
<td  style="$message_window">
$happend_ivent$saikoroprint
</td></tr></form></table>
EOM
}
$next_levelup = 100 - ($job_keiken % 100);

#ver.1.3從這裡
if ($money =~ /^[-+]?\d\d\d\d+/g) {
  for ($i = pos($money) - 3, $j = $money =~ /^[-+]/; $i > $j; $i -= 3) {
    substr($money, $i, 0) = ',';
  }
}
if ($k_sousisan =~ /^[-+]?\d\d\d\d+/g) {
  for ($i = pos($k_sousisan) - 3, $j = $k_sousisan =~ /^[-+]/; $i > $j; $i -= 3) {
    substr($k_sousisan, $i, 0) = ',';
  }
}
#ver.1.3到這裡

	print <<"EOM";
<span class=honbun2>名　前</span>：$name<br>
<span class=honbun2  onMouseOver='onMes5(\"總資產＝所持資金 + 活期存款 + 超級定期 - 貸款額\")' onMouseOut='onMes5(\"\")'>所持金</span>：$money元<br>（總資產：<span class=small>$k_sousisan</span>元）<br>
<span class=honbun2  onMouseOver='onMes5(\"經驗值：$job_keiken（到下次的昇Level 是 $next_levelup 以後）　工作數：$job_kaisuu回\")' onMouseOut='onMes5(\"\")'>職　業</span>：$job（Level $job_level）<br>

<!-- 力百分比的表示 -->
<span class=honbun2  onMouseOver='onMes5(\"MAX值是身體參數的增加上限。\")' onMouseOut='onMes5(\"\")'>身體力</span>：$energy （MAX值：$energy_max）<br><img src="$img_dir/$energy_bar" width="$ener_parcent" height="8"><img src="$img_dir/nokori_bar.gif" width="$nokori_parcent" height="8"><br>
<span class=honbun2 onMouseOver='onMes5(\"MAX值是頭腦參數的增加上限。\")' onMouseOut='onMes5(\"\")'>頭腦力</span>：$nou_energy（MAX值：$nou_energy_max）<br><img src="$img_dir/$nou_energy_bar" width="$nou_ener_parcent" height="8"><img src="$img_dir/nokori_bar.gif" width="$nou_nokori_parcent" height="8"> <br>
<span class=honbun2  onMouseOver='onMes5(\"狀況影響「力」的復甦度(也有其他各種各樣的原因)\")' onMouseOut='onMes5(\"\")'>狀況</span>：$condition<br>
<span class=honbun2>身　　長</span>：$sintyou cm<br>
<span class=honbun2>體　　重</span>：$taijuu kg<br>
<span class=honbun2 onMouseOver='onMes5(\"身體質量指數(BMI) = 體重(kg) ÷ 身長(m) ÷ 身長(m)\")' onMouseOut='onMes5(\"\")'>身體質量指數</span>：$BMI（$taikei）<br>
<span class=honbun2  onMouseOver='onMes5(\"上次吃飯：$last_syokuzi_henkan\")' onMouseOut='onMes5(\"\")'>空腹度</span>：$kuuhukudo<br>
<!--ver.1.3從這裡-->
EOM
#配偶，戀人的表示
					open(COA,"$couple_file") || &error("$couple_file不能寫上");
						@all_couple = <COA>;
					close(COA);
					foreach (@all_couple){
						($cn_number,$cn_name1,$cn_name2,$cn_joutai,$cn_total_aijou,$cn_omoide1,$cn_omoide2,$cn_omoide3,$cn_omoide4,$cn_omoide5,$cn_kodomo,$cn_yobi1,$cn_yobi2,$cn_yobi3,$cn_yobi4,$cn_yobi5)= split(/<>/);
						if ($name eq "$cn_name1"){
							if ($cn_joutai eq "戀人"){$my_koibito .= "$cn_name2　";}
							elsif ($cn_joutai eq "配偶"){$my_haiguusya = "$cn_name2";}
						}
						if ($name eq "$cn_name2"){
							if ($cn_joutai eq "戀人"){$my_koibito .= "$cn_name1　";}
							elsif ($cn_joutai eq "配偶"){$my_haiguusya = "$cn_name1";}
						}
					}
					print <<"EOM";
					<span class=honbun2>配  偶</span>：$my_haiguusya<br>
					<span class=honbun2>戀　人</span>：$my_koibito<br>
					<span class=honbun2>所有物</span>：
EOM
#所有物的表示
	foreach (@my_kounyuu_list){
		&syouhin_sprit ($_);
		if ($syo_taikyuu <=0){next;}
		if ($syo_hinmoku eq "可愛的我家"){
			print <<"EOM";
<table boader=0 width=100%><tr><form method=POST action=\"original_house.cgi\"><td><input type=hidden name=mode value="houmon"><input type=hidden name=name value="$in{'name'}"><input type=hidden name=pass value="$in{'pass'}"><input type=hidden name=k_id value="$k_id"><input type=hidden name=town_no value=$in{'town_no'}><input type=hidden name=ori_ie_id value=$k_id><input type=image src='$img_dir/go_home2.gif' width=100 height=10  onMouseOver='onMes5(\"到自己的家去。\")' onMouseOut='onMes5(\"\")'></td></form></tr></table><!--ver.1.40-->
EOM
			next;
		}
		print <<"EOM";
		○$syo_hinmoku　
EOM
	}
#ver.1.3到這裡
	$nouryoku_goukeiti = $kokugo + $suugaku + $rika + $syakai + $eigo + $ongaku + $bijutu + $looks + $tairyoku + $kenkou + $speed + $power + $wanryoku + $kyakuryoku;
	foreach (6..22){
		$nouryoku_bar[$_] = int (($nouryoku_suuzi_hairetu[$_] / $nouryoku_goukeiti)*100*$nouryoku_goukeiti*0.002);
	}

	print <<"EOM";
<br>
<font color=#ff6633>※結束遊戲的時候請必定按保存按鈕。</font><br><!-- ver.1.30 -->
※工作能得到的經驗值會根據“狀況”而變化。
</td><tr>
</table>
</td><td align=right>
<!-- ver.1.30從這裡 -->
<table border="0"  cellspacing="0" cellpadding="1" style=" border: $st_win_wak; border-style: solid; border-width: 1px; font-size: 11px; line-height: 11px; color: #006699" bgcolor=$st_win_back width=100% height=100%>
<tr>
<td colspan=2 align=center><span class=tyuu>頭  腦</span></td></tr>
<tr><td align=right>國語：</td><td><table class=small><tr><td width=$nouryoku_bar[6] bgcolor=#ffcc00>$kokugo</td></tr></table></td></tr>
<tr><td align=right>數學：</td><td><table class=small><tr><td width=$nouryoku_bar[7] bgcolor=#ffcc00>$suugaku</td></tr></table></td></tr>
<tr><td align=right>理科：</td><td><table class=small><tr><td width=$nouryoku_bar[8] bgcolor=#ffcc00>$rika</td></tr></table></td></tr>
<tr><td align=right>社會：</td><td><table class=small><tr><td width=$nouryoku_bar[9] bgcolor=#ffcc00>$syakai</td></tr></table></td></tr>
<tr><td align=right>英語：</td><td><table class=small><tr><td width=$nouryoku_bar[10] bgcolor=#ffcc00>$eigo</td></tr></table></td></tr>
<tr><td align=right>音樂：</td><td><table class=small><tr><td width=$nouryoku_bar[11] bgcolor=#ffcc00>$ongaku</td></tr></table></td></tr>
<tr><td align=right>美術：</td><td><table class=small><tr><td width=$nouryoku_bar[12] bgcolor=#ffcc00>$bijutu</td></tr></table></td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>身  體</span></td></tr>
<tr><td  align=right nowrap>容貌：</td><td><table class=small><tr><td width=$nouryoku_bar[13] bgcolor=#ffcc00>$looks</td></tr></table></td></tr>
<tr><td align=right>體力：</td><td><table class=small><tr><td width=$nouryoku_bar[14] bgcolor=#ffcc00>$tairyoku</td></tr></table></td></tr>
<tr><td align=right>健康：</td><td><table class=small><tr><td width=$nouryoku_bar[15] bgcolor=#ffcc00>$kenkou</td></tr></table></td></tr>
<tr><td align=right nowrap>速度：</td><td><table class=small><tr><td width=$nouryoku_bar[16] bgcolor=#ffcc00>$speed</td></tr></table></td></tr>
<tr><td align=right>力：</td><td><table class=small><tr><td width=$nouryoku_bar[17] bgcolor=#ffcc00>$power</td></tr></table></td></tr>
<tr><td align=right>腕力：</td><td><table class=small><tr><td width=$nouryoku_bar[18] bgcolor=#ffcc00>$wanryoku</td></tr></table></td></tr>
<tr><td align=right>脚力：</td><td><table class=small><tr><td width=$nouryoku_bar[19] bgcolor=#ffcc00>$kyakuryoku</td></tr></table></td></tr>
<tr style=" border: $st_win_wak; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px">
<td  colspan=2 align=center><span class=tyuu>其  他</span></td>
<tr><td align=right>LOVE：</td><td><table class=small><tr><td width=$nouryoku_bar[20] bgcolor=#ffcc00>$love</td></tr></table></td></tr>
<tr><td align=right>有趣：</td><td><table class=small><tr><td width=$nouryoku_bar[21] bgcolor=#ffcc00>$unique</td></tr></table></td></tr>
<tr><td align=right>淫蕩：</td><td><table class=small><tr><td width=$nouryoku_bar[22] bgcolor=#ffcc00>$etti</td></tr></table></td></tr>
</table>
<!-- ver.1.30到這裡 -->
</td></tr></table>
EOM
}

###記錄備份處理
sub list_log_backup {
#	if ($in{'admin_pass'} ne $admin_pass){&error("密碼不對");}		#ver.1.22
#取得文件夾內的文件名作成備份記錄
					use DirHandle;
					$dir = new DirHandle ("./log_dir");
					while($file_name = $dir->read){ #讀入1個$folder_name代入
							if($file_name eq '.' || $file_name eq '..' || $file_name =~ /^backup_/ || $file_name eq '.DS_Store'){next;}
							my $backup_name = "backup_" ."$file_name";
							open (BK,"./log_dir/$file_name")  || &error("Open Error : ./log_dir/$file_name");
							my @back_data = <BK>;
							close (BK);
							if (@back_data != ""){
								open (BKO,">./log_dir/backup_dir/$backup_name") || &error("Write Error : ./log_dir/backup_dir/$backup_name");
								print BKO @back_data;
								close (BKO);
							}
					}
					$dir->close;  #閉上目錄
}
