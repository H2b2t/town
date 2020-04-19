sub kozin_sprit{
($k_id,$name,$pass,$money,$bank,$job,$kokugo,$suugaku,$rika,$syakai,$eigo,$ongaku,$bijutu,$looks,$tairyoku,$kenkou,$speed,$power,$wanryoku,$kyakuryoku,$love,$unique,$etti,$first_access,$kounyuu,$sex,$access_byou,$access_time,$host,$house_name,$house_type,$byoumei,$mise_type,$last_mailcheck,$super_teiki,$energy,$last_ene_time,$next_tra,$last_syokuzi,$sintyou,$taijuu,$nou_energy,$last_nouene_time,$job_keiken,$job_kaisuu,$last_school,$byouki_sisuu,$loan_nitigaku,$loan_kaisuu,$k_sousisan,$jobsyu,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/);
#k_yobi3=多重登記人 jobsyu=完全掌握了的職業 kounyuu=圖標URL house_name=最後工作了的時間 house_type=配偶的ID識別號 mise_type=登入非表示 last_mailcheck=未使用
}

sub kozin_sprit2 {
($k_id,$name,$pass,$money,$bank,$job,$kokugo,$suugaku,$rika,$syakai,$eigo,$ongaku,$bijutu,$looks,$tairyoku,$kenkou,$speed,$power,$wanryoku,$kyakuryoku,$love,$unique,$etti,$first_access,$kounyuu,$sex,$access_byou,$access_time,$host,$house_name,$house_type,$byoumei,$mise_type,$last_mailcheck,$super_teiki,$energy,$last_ene_time,$next_tra,$last_syokuzi,$sintyou,$taijuu,$nou_energy,$last_nouene_time,$job_keiken,$job_kaisuu,$last_school,$byouki_sisuu,$loan_nitigaku,$loan_kaisuu,$k_sousisan,$jobsyu,$k_yobi3,$k_yobi4,$k_yobi5)= split(/<>/,@_[0]);
@nouryoku_suuzi_hairetu =  split(/<>/,@_[0]);
}

sub temp_routin {
	$k_temp="$k_id<>$name<>$pass<>$money<>$bank<>$job<>$kokugo<>$suugaku<>$rika<>$syakai<>$eigo<>$ongaku<>$bijutu<>$looks<>$tairyoku<>$kenkou<>$speed<>$power<>$wanryoku<>$kyakuryoku<>$love<>$unique<>$etti<>$first_access<>$kounyuu<>$sex<>$access_byou<>$access_time<>$host<>$house_name<>$house_type<>$byoumei<>$mise_type<>$last_mailcheck<>$super_teiki<>$energy<>$last_ene_time<>$next_tra<>$last_syokuzi<>$sintyou<>$taijuu<>$nou_energy<>$last_nouene_time<>$job_keiken<>$job_kaisuu<>$last_school<>$byouki_sisuu<>$loan_nitigaku<>$loan_kaisuu<>$k_sousisan<>$jobsyu<>$k_yobi3<>$k_yobi4<>$k_yobi5<>\n";
}

sub aite_sprit {
($aite_k_id,$aite_name,$aite_pass,$aite_money,$aite_bank,$aite_job,$aite_kokugo,$aite_suugaku,$aite_rika,$aite_syakai,$aite_eigo,$aite_ongaku,$aite_bijutu,$aite_looks,$aite_tairyoku,$aite_kenkou,$aite_speed,$aite_power,$aite_wanryoku,$aite_kyakuryoku,$aite_love,$aite_unique,$aite_etti,$aite_first_access,$aite_kounyuu,$aite_sex,$aite_access_byou,$aite_access_time,$aite_host,$aite_house_name,$aite_house_type,$aite_byoumei,$aite_mise_type,$aite_last_mailcheck,$aite_super_teiki,$aite_energy,$aite_last_ene_time,$aite_next_tra,$aite_last_syokuzi,$aite_sintyou,$aite_taijuu,$aite_nou_energy,$aite_last_nouene_time,$aite_job_keiken,$aite_job_kaisuu,$aite_last_school,$aite_byouki_sisuu,$aite_loan_nitigaku,$aite_loan_kaisuu,$aite_sousisan,$aite_jobsyu,$aite_yobi3,$aite_yobi4,$aite_yobi5)= split(/<>/,@_[0]);
@aite_nouryoku_suuzi_hairetu =  split(/<>/,@_[0]);
#aite_yobi3＝多重登記
}

sub aite_temp_routin {
	$aite_k_temp="$aite_k_id<>$aite_name<>$aite_pass<>$aite_money<>$aite_bank<>$aite_job<>$aite_kokugo<>$aite_suugaku<>$aite_rika<>$aite_syakai<>$aite_eigo<>$aite_ongaku<>$aite_bijutu<>$aite_looks<>$aite_tairyoku<>$aite_kenkou<>$aite_speed<>$aite_power<>$aite_wanryoku<>$aite_kyakuryoku<>$aite_love<>$aite_unique<>$aite_etti<>$aite_first_access<>$aite_kounyuu<>$aite_sex<>$aite_access_byou<>$aite_access_time<>$aite_host<>$aite_house_name<>$aite_house_type<>$aite_byoumei<>$aite_mise_type<>$aite_last_mailcheck<>$aite_super_teiki<>$aite_energy<>$aite_last_ene_time<>$aite_next_tra<>$aite_last_syokuzi<>$aite_sintyou<>$aite_taijuu<>$aite_nou_energy<>$aite_last_nouene_time<>$aite_job_keiken<>$aite_job_kaisuu<>$aite_last_school<>$aite_byouki_sisuu<>$aite_loan_nitigaku<>$aite_loan_kaisuu<>$aite_sousisan<>$aite_jobsyu<>$aite_yobi3<>$aite_yobi4<>$aite_yobi5<>\n";
	@aite_k_temp = ();
	push (@aite_k_temp,$aite_k_temp);
}

sub list_sprit{
($list_k_id,$list_name,$list_pass,$list_money,$list_bank,$list_job,$list_kokugo,$list_suugaku,$list_rika,$list_syakai,$list_eigo,$list_ongaku,$list_bijutu,$list_looks,$list_tairyoku,$list_kenkou,$list_speed,$list_power,$list_wanryoku,$list_kyakuryoku,$list_love,$list_unique,$list_etti,$list_first_access,$list_kounyuu,$list_sex,$list_access_byou,$list_access_time,$list_host,$list_house_name,$list_house_type,$list_byoumei,$list_mise_type,$list_last_mailcheck,$list_super_teiki,$list_energy,$list_last_ene_time,$list_next_tra,$list_last_syokuzi,$list_sintyou,$list_taijuu,$list_nou_energy,$list_last_nouene_time,$list_job_keiken,$list_job_kaisuu,$list_last_school,$list_byouki_sisuu,$list_loan_nitigaku,$list_loan_kaisuu,$list_sousisan,$list_jobsyu,$list_k_yobi3,$list_k_yobi4,$list_k_yobi5)= split(/<>/,@_[0]);
}

sub list_temp {
	$list_temp="$list_k_id<>$list_name<>$list_pass<>$list_money<>$list_bank<>$list_job<>$list_kokugo<>$list_suugaku<>$list_rika<>$list_syakai<>$list_eigo<>$list_ongaku<>$list_bijutu<>$list_looks<>$list_tairyoku<>$list_kenkou<>$list_speed<>$list_power<>$list_wanryoku<>$list_kyakuryoku<>$list_love<>$list_unique<>$list_etti<>$list_first_access<>$list_kounyuu<>$list_sex<>$list_access_byou<>$list_access_time<>$list_host<>$list_house_name<>$list_house_type<>$list_byoumei<>$list_mise_type<>$list_last_mailcheck<>$list_super_teiki<>$list_energy<>$list_last_ene_time<>$list_next_tra<>$list_last_syokuzi<>$list_sintyou<>$list_taijuu<>$list_nou_energy<>$list_last_nouene_time<>$list_job_keiken<>$list_job_kaisuu<>$list_last_school<>$list_byouki_sisuu<>$list_loan_nitigaku<>$list_loan_kaisuu<>$list_sousisan<>$list_jobsyu<>$list_k_yobi3<>$list_k_yobi4<>$list_k_yobi5<>\n";
}

sub main_town_sprit{
($mt_zinkou,$mt_keizai,$mt_hanei,$mt_today,$mt_orosiflag,$mt_t_time,$mt_y_time,$mt_syokudouflag,$mt_departflag,$total_ninzuu,$mt_yobi8,$mt_yobi9,$mt_yobi10,$mt_yobi11,$mt_yobi12,$mt_yobi13,$mt_yobi14)= split(/<>/,@_[0]);
#mt_yobi8=創設日(店的銷售額及留言板寫入日)mt_yobi9=批發更新日時 total_ninzuu=未使用
}

sub main_town_temp{
	$mt_temp="$mt_zinkou<>$mt_keizai<>$mt_hanei<>$mt_today<>$mt_orosiflag<>$mt_t_time<>$mt_y_time<>$mt_syokudouflag<>$mt_departflag<>$total_ninzuu<>$mt_yobi8<>$mt_yobi9<>$mt_yobi10<>$mt_yobi11<>$mt_yobi12<>$mt_yobi13<>$mt_yobi14<>\n";
	@mt_temp = ();
	push (@mt_temp,$mt_temp);
}

sub town_sprit{
($town_name,$zinkou,$keizai,$hanei,$t_x0,$t_x1,$t_x2,$t_x3,$t_x4,$t_x5,$t_x6,$t_x7,$t_x8,$t_x9,$t_x10,$t_x11,$t_x12,$t_x13,$t_x14,$t_x15,$t_x16,$t_a0,$t_a1,$t_a2,$t_a3,$t_a4,$t_a5,$t_a6,$t_a7,$t_a8,$t_a9,$t_a10,$t_a11,$t_a12,$t_a13,$t_a14,$t_a15,$t_a16,$t_b0,$t_b1,$t_b2,$t_b3,$t_b4,$t_b5,$t_b6,$t_b7,$t_b8,$t_b9,$t_b10,$t_b11,$t_b12,$t_b13,$t_b14,$t_b15,$t_b16,$t_c0,$t_c1,$t_c2,$t_c3,$t_c4,$t_c5,$t_c6,$t_c7,$t_c8,$t_c9,$t_c10,$t_c11,$t_c12,$t_c13,$t_c14,$t_c15,$t_c16,$t_d0,$t_d1,$t_d2,$t_d3,$t_d4,$t_d5,$t_d6,$t_d7,$t_d8,$t_d9,$t_d10,$t_d11,$t_d12,$t_d13,$t_d14,$t_d15,$t_d16,$t_e0,$t_e1,$t_e2,$t_e3,$t_e4,$t_e5,$t_e6,$t_e7,$t_e8,$t_e9,$t_e10,$t_e11,$t_e12,$t_e13,$t_e14,$t_e15,$t_e16,$t_f0,$t_f1,$t_f2,$t_f3,$t_f4,$t_f5,$t_f6,$t_f7,$t_f8,$t_f9,$t_f10,$t_f11,$t_f12,$t_f13,$t_f14,$t_f15,$t_f16,$t_g0,$t_g1,$t_g2,$t_g3,$t_g4,$t_g5,$t_g6,$t_g7,$t_g8,$t_g9,$t_g10,$t_g11,$t_g12,$t_g13,$t_g14,$t_g15,$t_g16,$t_h0,$t_h1,$t_h2,$t_h3,$t_h4,$t_h5,$t_h6,$t_h7,$t_h8,$t_h9,$t_h10,$t_h11,$t_h12,$t_h13,$t_h14,$t_h15,$t_h16,$t_i0,$t_i1,$t_i2,$t_i3,$t_i4,$t_i5,$t_i6,$t_i7,$t_i8,$t_i9,$t_i10,$t_i11,$t_i12,$t_i13,$t_i14,$t_i15,$t_i16,$t_j0,$t_j1,$t_j2,$t_j3,$t_j4,$t_j5,$t_j6,$t_j7,$t_j8,$t_j9,$t_j10,$t_j11,$t_j12,$t_j13,$t_j14,$t_j15,$t_j16,$t_k0,$t_k1,$t_k2,$t_k3,$t_k4,$t_k5,$t_k6,$t_k7,$t_k8,$t_k9,$t_k10,$t_k11,$t_k12,$t_k13,$t_k14,$t_k15,$t_k16,$t_l0,$t_l1,$t_l2,$t_l3,$t_l4,$t_l5,$t_l6,$t_l7,$t_l8,$t_l9,$t_l10,$t_l11,$t_l12,$t_l13,$t_l14,$t_l15,$t_l16,$t_m0,$t_m1,$t_m2,$t_m3,$t_m4,$t_m5,$t_m6,$t_m7,$t_m8,$t_m9,$t_m10,$t_m11,$t_m12,$t_m13,$t_m14,$t_m15,$t_m16,$t_n0,$t_n1,$t_n2,$t_n3,$t_n4,$t_n5,$t_n6,$t_n7,$t_n8,$t_n9,$t_n10,$t_n11,$t_n12,$t_n13,$t_n14,$t_n15,$t_n16,$tika,$t_yobi2,$t_yobi3,$t_yobi4,$t_yobi5,$t_yobi6,$t_yobi7)= split(/<>/,@_[0]);
@town_sprit_matrix =  split(/<>/,@_[0]);
#t_yobi2=街設立日(那個街的日銷售額)
}

sub job_sprit {
($job_no,$job_name,$job_kokugo,$job_suugaku,$job_rika,$job_syakai,$job_eigo,$job_ongaku,$job_bijutu,$job_BMI_min,$job_BMI_max,$job_looks,$job_tairyoku,$job_kenkou,$job_speed,$job_power,$job_wanryoku,$job_kyakuryoku,$job_kyuuyo,$job_siharai,$job_love,$job_unique,$job_etti,$job_sex,$job_sintyou,$job_energy,$job_nou_energy,$job_rank,$job_syurui,$job_bonus,$job_syoukyuuritu)= split(/<>/,@_[0]);
}

sub syouhin_sprit{
($syo_syubetu,$syo_hinmoku,$syo_kokugo,$syo_suugaku,$syo_rika,$syo_syakai,$syo_eigo,$syo_ongaku,$syo_bijutu,$syo_kouka,$syo_looks,$syo_tairyoku,$syo_kenkou,$syo_speed,$syo_power,$syo_wanryoku,$syo_kyakuryoku,$syo_nedan,$syo_love,$syo_unique,$syo_etti,$syo_taikyuu,$syo_taikyuu_tani,$syo_kankaku,$syo_zaiko,$syo_cal,$syo_siyou_date,$syo_sintai_syouhi,$syo_zunou_syouhi,$syo_comment,$syo_kounyuubi,$tanka,$tokubai)= split(/<>/,@_[0]);
}

sub syouhin_temp{
	$syo_temp="$syo_syubetu<>$syo_hinmoku<>$syo_kokugo<>$syo_suugaku<>$syo_rika<>$syo_syakai<>$syo_eigo<>$syo_ongaku<>$syo_bijutu<>$syo_kouka<>$syo_looks<>$syo_tairyoku<>$syo_kenkou<>$syo_speed<>$syo_power<>$syo_wanryoku<>$syo_kyakuryoku<>$syo_nedan<>$syo_love<>$syo_unique<>$syo_etti<>$syo_taikyuu<>$syo_taikyuu_tani<>$syo_kankaku<>$syo_zaiko<>$syo_cal<>$syo_siyou_date<>$syo_sintai_syouhi<>$syo_zunou_syouhi<>$syo_comment<>$syo_kounyuubi<>$tanka<>$tokubai<>\n";
}

sub gym_sprit{
($gym_name,$gym_looks,$gym_tairyoku,$gym_kenkou,$gym_speed,$gym_power,$gym_wanryoku,$gym_kyakuryoku,$gym_nedan,$gym_kouka,$gym_etti,$gym_kankaku,$gym_syouhi)= split(/<>/,@_[0]);
}


sub school_sprit{
($sc_name,$sc_kokugo,$sc_suugaku,$sc_rika,$sc_syakai,$sc_eigo,$sc_ongaku,$sc_bijutu,$sc_nedan,$sc_kouka,$sc_syouhi)= split(/<>/,@_[0]);
}

sub ginkou_meisai_sprit {
($meisai_date,$meisai_naiyou,$meisai_hikidasi,$meisai_azuke,$meisai_zandaka,$meisai_syubetu)= split(/<>/,@_[0]);
}

sub ori_ie_sprit {
($ori_k_id,$ori_ie_name,$ori_ie_setumei,$ori_ie_image,$ori_ie_syubetu,$ori_ie_kentikubi,$ori_ie_town,$ori_ie_tateziku,$ori_ie_yokoziku,$ori_ie_sentaku_point,$ori_ie_rank,$ori_ie_yobi7,$ori_ie_yobi8,$ori_ie_yobi9,$ori_ie_yobi10)= split(/<>/,@_[0]);
}

sub ori_ie_temp {
$ori_ie_temp = "$ori_k_id<>$ori_ie_name<>$ori_ie_setumei<>$ori_ie_image<>$ori_ie_syubetu<>$ori_ie_kentikubi<>$ori_ie_town<>$ori_ie_tateziku<>$ori_ie_yokoziku<>$ori_ie_sentaku_point<>$ori_ie_rank<>$ori_ie_yobi7<>$ori_ie_yobi8<>$ori_ie_yobi9<>$ori_ie_yobi10<>\n";
}

#自己的家的設定文件分割
sub oriie_settei_sprit {
($my_con1,$my_con2,$my_con3,$my_con4,$my_con1_title,$my_con2_title,$my_con3_title,$my_con4_title,$my_yobi5,$my_yobi6,$my_yobi7,$my_yobi8,$my_yobi9,$my_yobi10,$my_yobi11,$my_yobi12,$my_yobi13,$my_yobi14,$my_yobi15,$my_yobi16,$my_yobi17,$my_yobi18)= split(/<>/,@_[0]);
	@oriie_settei_sprit = split(/<>/,@_[0]);
}

sub oriie_settei_temp {
$ori_ie_settei_temp = "$my_con1<>$my_con2<>$my_con3<>$my_con4<>$my_con1_title<>$my_con2_title<>$my_con3_title<>$my_con4_title<>$my_yobi5<>$my_yobi6<>$my_yobi7<>$my_yobi8<>$my_yobi9<>$my_yobi10<>$my_yobi11<>$my_yobi12<>$my_yobi13<>$my_yobi14<>$my_yobi15<>$my_yobi16<>$my_yobi17<>$my_yobi18<>\n";
}

sub log_kousin {
		&lock;	
		open(OUT,">@_[0]") || &error("@_[0]不能打開");
		print OUT @_[1];
		close(OUT);
		&unlock;
}

sub  mail_sprit {
	($m_syubetu,$m_name,$m_com,$m_date,$m_byou,$m_yobi1,$m_yobi2,$m_yobi3,$m_yobi4,$m_yobi5)= split(/<>/,@_[0]);
}

sub openMylog {
		$my_log_file = "./member/@_[0]/log.cgi";
		open(MYL,"$my_log_file") || &error("log file($my_log_file)不能打開。<br>如果再次登入也有同樣情況請到管理者($master_ad)給我電郵。");
		$my_prof = <MYL>;
		if($my_prof == ""){&error("log file問題發生了。<br>麻煩您，請到管理者($master_ad)給我郵件。");}
		&kozin_sprit2($my_prof);
		close(MYL);
}

sub openAitelog {
					$aite_log_file = "./member/@_[0]/log.cgi";
					open(AIT,"$aite_log_file") || &error("對方的log file($aite_log_file)不能打開。");
					$aite_prof = <AIT>;
					if($aite_prof == ""){&error("對方的log file有問題。");}
					&aite_sprit($aite_prof);
					close(AIT);
}


sub check_pass {
		if($in{'k_id'} eq ""){
				if($in{'name'} eq ""){&error("請做登入。");}
			&id_check($in{'name'});
			$k_id = $return_id;
		}else{$k_id = $in{'k_id'};}
		$my_log_file = "./member/$k_id/log.cgi";
	open(MYL,"$my_log_file") || &error("log file($my_log_file)不能打開。<br>如果再次登入也有同樣情況請到管理員($master_ad)請給我郵件。");
		$my_prof = <MYL>;
		if($my_prof == ""){&error("log file問題發生了。<br>麻煩您，到管理員($master_ad)請給我郵件。");}
			&kozin_sprit2($my_prof);
				if($in{'pass'} ne $pass){
					&error("名字和密碼不對！");
				}
				if ($tajuukinsi_deny==1){
					if($k_yobi3 ne ""){
						&error("多重登記的人不能遷入。<br>$k_yobi3");
					}
				}
	close(MYL);
}

####BMI算出子程序
sub check_BMI {
	$BMI = int (@_[1] / (@_[0] /100) / (@_[0] /100) );
	if($BMI >= 26){$taikei = "肥胖";}
	elsif($BMI >= 24){$taikei = "稍稍胖";}
	elsif($BMI >= 20){$taikei = "標準";}
	elsif($BMI >= 18){$taikei = "瘦";}
	elsif($BMI <= 17){$taikei = "太瘦";}
}

#######頁頂輸出
sub header {
	$heder_flag=1;
print "Content-type: text/html;charset=UTF-8\n";
#gzip對應
		if($ENV{'HTTP_ACCEPT_ENCODING'} =~ /gzip/ && $gzip ne ''){  
		  if($ENV{'HTTP_ACCEPT_ENCODING'} =~ /x-gzip/){
		    print "Content-encoding: x-gzip\n\n";
		  }else{
		    print "Content-encoding: gzip\n\n";
		  }
		  open(STDOUT,"| $gzip -1 -c");
		}else{
		  print "\n";
		}
	print "<html>\n<head>\n";
	if ($in{'command'} eq "mati_idou"){
			while(($syudan_name,$sokudo) = each %idou_syudan){
				push @syudan_names,$syudan_name;
				push @sokudos,$sokudo;
			}
#移動手段選擇
		$idousyudan = "徒步";
		$ziko_idousyudan = "徒步";
		$matiidou_time2 = $matiidou_time;
		foreach (@syudan_names){
			&motimono_kensa("$_");
			if ($kensa_flag == 1){
				$idousyudan = "$_";
				$ziko_idousyudan = "$_";
				$matiidou_time2 = $idou_syudan{$_};
				last;
			}
		}
#事故發生
		$randed = int (rand($ziko_kakuritu)+1);
		if ($randed == 1 ){ $ziko_flag  = "on";}else{$ziko_flag  = "off";}
#名字和密碼編碼
			$en_name =$in{'name'};
			$en_pass =$in{'pass'};
			$en_name=~ s/(\W)/sprintf("%%%02X",unpack("C" , $1))/eg;
			$en_pass=~ s/(\W)/sprintf("%%%02X",unpack("C" , $1))/eg;
			$ziko_idousyudan=~ s/(\W)/sprintf("%%%02X",unpack("C" , $1))/eg;
		print "<meta http-equiv=\"refresh\" content=\"$matiidou_time2;URL=$script?mode=login_view&town_no=$in{'town_no'}&name=$en_name&pass=$en_pass&command=idousyuuryou&ziko_flag=$ziko_flag&ziko_idousyudan=$ziko_idousyudan\">";
	}
	print "<title>$title</title>\n";
	print <<"EOM";
<Script Language="JavaScript">
<!--
///////////////////////////////////////////////////
// メッセージ No.5.1 Produced by「CLUB とむやん君」
// URL http://www2s.biglobe.ne.jp/~club_tom/
// 上面的2行是著作權表示請別消去
///////////////////////////////////////////////////

// 是在form寫入消息的部分。
function onMes5(mes){
	document.foMes5.TeMes5.value=mes;
}

function pfvsetInterval(){
	retval = setInterval('countdown()',1000)
}

function countdown(){
	if(document.form1==null){clearInterval(retval);return;}
	if(document.form1.cdown==null){clearInterval(retval);return;}
	if(document.form1.cdown.value!='O K'){
		min = document.form1.cdown.value;
		min--;
		document.form1.cdown.value = min;
		if(document.form1.cdown.value==0){
			document.form1.cdown.value='O K'
			clearInterval(retval);
		}
	}
	else{clearInterval(retval);}
}

// End -->
</Script>
<style type="text/css">
<!--
$town_stylesheet
-->
</style>
EOM
	if ($in{'mode'} eq "login_view" || @_[1] eq "sonomati"){$sonomati_style_settei ="$page_back[$in{'town_no'}]";}
	print "</head><body style=\"$sonomati_style_settei\" class=@_[0] leftmargin=5 topmargin=5 marginwidth=5 marginheight=5r  onLoad=\"pfvsetInterval()\">\n";
}

sub ori_header {
print "Content-type: text/html;charset=utf-8\n";
#gzip對應
		if($ENV{'HTTP_ACCEPT_ENCODING'} =~ /gzip/ && $gzip ne ''){  
		  if($ENV{'HTTP_ACCEPT_ENCODING'} =~ /x-gzip/){
		    print "Content-encoding: x-gzip\n\n";
		  }else{
		    print "Content-encoding: gzip\n\n";
		  }
		  open(STDOUT,"| $gzip -1 -c");
		}else{
		  print "\n";
		}
	print "<html>\n<head>\n";
	print "<title>$title</title>\n";
	print <<"EOM";
<Script Language="JavaScript">
<!--
///////////////////////////////////////////////////
// 信息 No.5.1 Produced by「CLUB とむやん君」
// URL http://www2s.biglobe.ne.jp/~club_tom/
// 上面的2行是著作權表示請別消去
///////////////////////////////////////////////////

// 是在form寫入消息的部分。
function onMes5(mes){
	document.foMes5.TeMes5.value=mes;
}

// End -->
</Script>
<style type="text/css">
<!--
a   {@_[2]}
input  {@_[1]}
select  {@_[1]}
body {@_[0]}
-->
</style>
EOM
	print "</head><body leftmargin=5 topmargin=5 marginwidth=5 marginheight=5>\n";
}

#####頁底
sub hooter {
	if(@_[2]){$yobidasi_script = "@_[2]";}else{$yobidasi_script = "$script";}
	if(@_[1] ne ""){
	print <<"EOM";
	<div align=center><form method=POST action="$yobidasi_script">
	<input type=hidden name=mode value="@_[0]">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">		<!--ver.1.3-->
	<input type=hidden name=name value=$in{'name'}>
	<input type=hidden name=pass value=$in{'pass'}>
	<input type=hidden name=admin_pass value=$in{'admin_pass'}>
	<input type=hidden name=town_no value=$in{'town_no'}>
	<input type=submit value="@_[1]">
	</form></div>
EOM
	}
	if ($in{'mode'} eq "login_view" || $in{'mode'} eq ""){
	if ($homepage){$home_hyouzi = "<a href=\"$homepage\" target=_top>[HOME]</a><br>";}else{$home_hyouzi = "";}
	print <<"EOM";
	<div align=center>
	$home_hyouzi
	<a href="http://brassiere.jp/" target=_blank>- $version script by brassiere -</a>　<a href=mailto:$master_ad>■詢問</a>		<!--ver.1.40-->
	</div>
EOM
	}
	print "</body></html>";
}


#信息畫面輸出
sub message {
&header("","sonomati");
	# 如果有鎖旗標刪掉鎖目錄
	if ($lockflag) { &unlock; }
	if(@_[2]){$yobidasi_script = "@_[2]";}else{$yobidasi_script = "$script";}
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>$_[0]</td></tr></table><br>

	<form method=POST action="$yobidasi_script">
	<input type=hidden name=mode value="@_[1]">
	<input type=hidden name=iesettei_id value="$in{'iesettei_id'}">		<!--ver.1.3-->
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

sub message_only {
	&header;
	# 如果有鎖旗標刪掉鎖目錄
	if ($lockflag) { &unlock; }
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win"><tr><td>$_[0]</td></tr></table><br>
	</div>
EOM
}


#錯誤畫面輸出
sub error {
#ver.1.30從這裡
#if (@_[1] ne "not_header"){		#ver.1.40
if ($heder_flag ne "1"){		#ver.1.40
	&header("","sonomati");
}
#ver.1.30到這裡
	# 如果有鎖旗標刪掉鎖目錄
	if ($lockflag) { &unlock; }
	print <<"EOM";
	<div align=center><br><table  border=0  cellspacing="5" cellpadding="0" width=300 style="$message_win">
	<tr><td>
	<center><h3><font color=#ff3300>ERROR !</font></h3>
	$_[0]
	<br><br><a href=\"javascript:history.back()\"> [返回前畫面] </a>
	</td></tr></table></div>
	</body></html>
EOM
	exit;
}

#時間取得
sub time_get {
	$date_sec = time ;
	$ENV{'TZ'} = "JST-9";
	my($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(time);
	@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
# 日期和時間的格式
	$full_date = sprintf("%04d/%02d/%02d(%s) %02d:%02d:%02d",
			$year+1900,$mon+1,$mday,$week[$wday],$hour,$min,$sec);
	$date = sprintf("%04d/%02d/%02d",
			$year+1900,$mon+1,$mday);
	$date2 = sprintf("%04d/%02d/%02d %02d:%02d",
			$year+1900,$mon+1,$mday,$hour,$min);
	$return_hour=$hour;
}

#time值(秒)日期變換
sub byou_hiduke {
	$ENV{'TZ'} = "CST-8";
	my($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime(@_[0]);
	@week = ('日','一','二','三','四','五','六');
# 日期和時間的格式
	$bh_full_date = sprintf("%02d月%02d日 %02d時%02d分",
			$mon+1,$mday,$hour,$min);
	$bh_date = sprintf("%04d/%02d/%02d",
			$year+1900,$mon+1,$mday);
	$bh_tukihi = sprintf("%02d/%02d",
			$mon+1,$mday);
	$bh_return_hour=$hour;
}

# 取得主機名
sub get_host {
	$return_host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($return_host eq "" || $return_host eq $addr) {
		$return_host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2) || $addr;
	}
}

# 鎖處理
sub lock {
	local($retry, $mtime);

	# 1分鐘以上舊的鎖刪掉
	if (-e $lockfile) {
		($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 60) { &unlock; }
	}

	# retry10次
	$retry = 20;
	while (!mkdir($lockfile, 0755)) {
		if (--$retry <= 0) { &error('現在網站繁忙。請稍等一下。'); }
		sleep(1);
	}
	# 立起鎖旗標
	$lockflag=1;
}


######## 鎖解除  
sub unlock {
	# 鎖目錄刪掉
	rmdir($lockfile);

	# 解除鎖旗標
	$lockflag=0;
}

######取得COOKIE
sub get_cookie {
	local($key, $val, @cook);

	@cook = split(/;/, $ENV{'HTTP_COOKIE'});
	foreach (@cook) {
		($key, $val) = split(/=/);
		$key =~ s/\s//g;
		$cook{$key} = $val;
	}
	%ck = split(/<>/, $cook{'town_maker'});

	# 留言後表示COOKIE信息
		if ($in{'name'}) { $ck{'name'} = $in{'name'}; }
		if ($in{'email'}) { $ck{'pass'} = $in{'pass'}; }
		if ($in{'hp'}) { $ck{'hp'} = $in{'hp'}; }

}


#####發行  COOKIE
sub set_cookie {
	local($gmt, $cook, @w, @m, @t);

	# 週、月定義
	@w = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
	@m = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');

	# 把國際標準時間做為基本保存時間60日
	@t = gmtime(time + 60*24*60*60);
	$gmt = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT",
			$w[$t[6]], $t[3], $m[$t[4]], $t[5]+1900, $t[2], $t[1], $t[0]);

	# 定義COOKIE信息
	$cook = "name<>$in{'name'}<>pass<>$in{'pass'}<>hp<>$in{'hp'}<>";

	print "Set-Cookie: town_maker=$cook; expires=$gmt\n";
}


#ID號碼獲得子程序
sub id_check{		#ver.1.40
	my($pass_id,$pass_name);
	open(IN,"$pass_logfile") || &error("Open Error : $pass_logfile");
	$name_flag=0;
	while (<IN>) {
		($pass_id,$pass_name)= split(/<>/);
		if($pass_name eq @_[0]){$name_flag=1;$return_id=$pass_id;last;}
	}
	
	if($name_flag==0){$return_id="";&error("那個名字沒被登記");}
	close(IN);
}

sub ie_sakujo_syori {		#ver.1.3排除鎖
#給家名單的寫入
	open(IN,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
		@ori_ie_para = <IN>;
	close(IN);
		@new_ori_ie_list = ();
		$iearuka_flag=0;
		foreach (@ori_ie_para){
				&ori_ie_sprit($_);
				if (@_[0] eq "$ori_ie_name"){
#town信息取得換行用信息
						$my_town_is = $ori_ie_town;
						$my_point_is = $ori_ie_sentaku_point;
						$iearuka_flag=1;
						next;
				}
				&ori_ie_temp;
				push (@new_ori_ie_list,$ori_ie_temp);
		}
#如果有家記錄更新
		if ($iearuka_flag != 0){
			#在town信息寫入
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
		}
}


#decoding處理
sub decode {
	local($buf, $key, $val, @buf);
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		&ReadParse;
		while (($key,$value)=each %in){
			if ($key ne "upfile"){
				#&jcode'convert(*value,"sjis");
#			$value =~ s/,/，/g;
				$value =~ s/\r\n/<br>/g;
				$value =~ s/\r/<br>/g;
				$value =~ s/\n/<br>/g;
			}
			$in{$key} = $value;
		}
	} else { $buf = $ENV{'QUERY_STRING'}; }
	@buf = split(/&/, $buf);
	foreach (@buf) {
		($key, $val) = split(/=/);
		$val =~ tr/+/ /;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		# 文字コード変換 (Shift-JISコード)
		#&jcode'convert(*val,'sjis');
		$in{$key} = $val;
	}
	
#拒絕以GET的訪問
	if($in{'mode'} ne "" && $in{'mode'} ne "houmon" && $in{'ori_ie_id'} ne "admin" && $in{'mode'} ne "parts_taiou_hyou" && $in{'mode'} ne "itiran" && $in{'mode'} ne "kensaku" && $in{'command'} ne "idousyuuryou" && $in{'command'} ne "easySerch"){
			if ($ENV{'REQUEST_METHOD'} ne "POST") {
				&error("因為不正確訪問被強行終止。");
			}
	}

#密碼檢查
	if ($in{'admin_pass'} ne "$admin_pass"){
		if($in{'mode'} ne "" && $in{'mode'} ne "new" && $in{'mode'} ne "parts_taiou_hyou"){
				&check_pass;
		}
	}

}

#多重檢查處理
sub tajuucheck {
	&get_host;
	open(IN,"$logfile") || &error("Open Error : $logfile");
	@rankingMember = <IN>;
	close(IN);
		foreach (@rankingMember) {
			($list_k_id,$list_name,$list_pass,$list_money,$list_bank,$list_job,$list_kokugo,$list_suugaku,$list_rika,$list_syakai,$list_eigo,$list_ongaku,$list_bijutu,$list_looks,$list_tairyoku,$list_kenkou,$list_speed,$list_power,$list_wanryoku,$list_kyakuryoku,$list_love,$list_unique,$list_etti,$list_first_access,$list_kounyuu,$list_sex,$list_access_byou,$list_access_time,$list_host)= split(/<>/);		#ver.1.30
			if ($list_name eq $name){next;}
			if($return_host eq $list_host && $in{'admin_pass'} ne "$admin_pass"){
				$k_yobi3 = "$list_name：$name";
				&temp_routin;
				&log_kousin($my_log_file,$k_temp);	
#ver.1.40從這裡
					&openAitelog ($list_k_id);
					$aite_yobi3 = "$list_name：$name";
					&aite_temp_routin;
				&lock;
				open(OUT,">$aite_log_file") || &error("$aite_log_file不能打開");
				print OUT $aite_k_temp;
				close(OUT);
				&unlock;
#ver.1.40到這裡
				&error("禁止多重登記。這個記錄被保存了。<br>$list_name：$name");
			}
		}	
}

#######記帳處理
sub kityou_syori {
	my (@my_tuutyou);
	&lock;
	$ginkoumeisai_file="./member/$k_id/ginkoumeisai.cgi";
	open(GM,"$ginkoumeisai_file") || &error("自己的存款存摺文件不能打開");
	@my_tuutyou = <GM>;
	close(GM);
	&time_get;
	$torihikinaiyou = "$date<>@_[0]<>@_[1]<>@_[2]<>@_[3]<>@_[4]<>\n";
#("詳細",存款額,提款額,餘額,普or定)
	unshift (@my_tuutyou,$torihikinaiyou);
	$meisai_kensuu = @my_tuutyou;
	if ($meisai_kensuu > 100){pop (@my_tuutyou);}
	open(GMO,">$ginkoumeisai_file") || &error("自己的存款存摺文件不能寫上");
	print GMO @my_tuutyou;
	close(GMO);
	&unlock;
}

#######對方的記帳處理
sub aite_kityou_syori {
	my (@aite_tuutyou);
	if (@_[6] ne "lock_off"){
		&lock;
	}
	$ginkoumeisai_file="./member/@_[5]/ginkoumeisai.cgi";
	open(GM,"$ginkoumeisai_file") || &error("對方的存款存摺文件不能打開");
	@aite_tuutyou = <GM>;
	close(GM);
	&time_get;
	$torihikinaiyou = "$date<>@_[0]<>@_[1]<>@_[2]<>@_[3]<>@_[4]<>\n";
#("詳細",存款額,提款額,餘額,普or定,匯款目標ID,"lock_off or 沒有")
	unshift (@aite_tuutyou,$torihikinaiyou);
	$meisai_kensuu = @aite_tuutyou;
	if ($meisai_kensuu > 100){pop (@aite_tuutyou);}
	open(GMO,">$ginkoumeisai_file") || &error("對方的存款存摺文件不能寫上");
	print GMO @aite_tuutyou;
	close(GMO);
	if (@_[6] ne "lock_off"){
		&unlock;
	}
}

#新聞記錄子程序		ver.1.3
sub news_kiroku {
	&time_get;
	open(NS,"$news_file") || &error("$news_file不能打開。");
	@town_news = <NS>;
	close(NS);
	$new_news_kizi = "$date2<>@_[0]<>@_[1]<>\n";
	unshift (@town_news,$new_news_kizi);
	$i = 0;
	@new_town_news = ();
	foreach (@town_news){
		push (@new_town_news,$_);
		$i ++;
		if ($i >= $news_kensuu){last;}
	}
	open(NSO,">$news_file") || &error("$news_file不能寫上");
	print NSO @new_town_news;
	close(NSO);
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

######街的經濟力提高
sub town_keizaiup {
	my $town_data = "./log_dir/townlog".@_[1].".cgi";
	open(TW,"$town_data") || &error("Open Error : $town_data");
	my $keizai_town_hairetu = <TW>;
	close(TW);
		my @town_sprit_matrix =  split(/<>/,$keizai_town_hairetu);
		if ($town_sprit_matrix[260]  == ""){$town_sprit_matrix[260] = time;}
		$town_sprit_matrix[2] += @_[0];
		my $town_temp=join("<>",@town_sprit_matrix);
#town信息更新
	open(TWO,">$town_data") || &error("$town_data不能寫上");
	print TWO $town_temp;
	close(TWO);

#主要town信息的更新
	open(MT,"$maintown_logfile") || &error("Open Error : $maintown_logfile");
	my $maintown_para = <MT>;
	close(MT);
	my @main_town_sprit_matrix =  split(/<>/,$maintown_para);
	if ($main_town_sprit_matrix[10]  == ""){$main_town_sprit_matrix[10] = time;}
		$main_town_sprit_matrix[1] += @_[0];
		$main_town_temp=join("<>",@main_town_sprit_matrix);
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			print OUT $main_town_temp;
			close(OUT);	
}

######街的繁榮度提高
sub town_haneiup {
	my $town_data = "./log_dir/townlog".@_[0].".cgi";
	open(TW,"$town_data") || &error("Open Error : $town_data");
	my $keizai_town_hairetu = <TW>;
	close(TW);
		my @town_sprit_matrix =  split(/<>/,$keizai_town_hairetu);
		if ($town_sprit_matrix[260]  == ""){$town_sprit_matrix[260] = time;}
		$town_sprit_matrix[3] ++ ;
		my $town_temp=join("<>",@town_sprit_matrix);
#town信息更新
	open(TWO,">$town_data") || &error("$town_data不能寫上");
	print TWO $town_temp;
	close(TWO);

#主要town信息的更新
	open(MT,"$maintown_logfile") || &error("Open Error : $maintown_logfile");
	my $maintown_para = <MT>;
	close(MT);
	my @main_town_sprit_matrix =  split(/<>/,$maintown_para);
	if ($main_town_sprit_matrix[10]  == ""){$main_town_sprit_matrix[10] = time;}
		$main_town_sprit_matrix[2] ++ ;
		$main_town_temp=join("<>",@main_town_sprit_matrix);
			open(OUT,">$maintown_logfile") || &error("Write Error : $maintown_logfile");
			print OUT $main_town_temp;
			close(OUT);	
}

sub data_save {
	my($data_path, @WRITE_DATA) = @_;
	my($err) = '';
	$data_path =~ /(.+)\..+$/;
	my($filename) = $1;
	if ($filename !~ /.+/) { $err = 'bad Filename(Not Extension?)'; }
	if (!$err) {
		my($tmpfile) = "$filename.tmp";
		my($tmpflag) = 0;
		foreach (1 .. 10) {
			unless (-f $tmpfile) { $tmpflag = 1; last; }
			$tmpflag = 0;
			sleep(1);
		}
		if ($tmpflag) {
			$tmp_dummy = "$$\.tmp";
			if (!open(TMP,">$tmp_dummy")) { $err = 'bad New TemporaryFile'; }
			if (!$err) {
				close(TMP);
				chmod 0666,$tmp_dummy;
				if (!open(TMP,">$tmp_dummy")) { $err = 'bad New TemporaryFile'; }
				if (!$err) {
					binmode TMP;
					print TMP @WRITE_DATA;
					close(TMP);
					foreach (1 .. 10) {
						unless (-f $tmpfile) {
							if (!open(TMP,">$tmpfile")) {
								$err = 'bad LockFile System';
								last;
							}
							if (!$err) {
								close(TMP);
								rename($tmp_dummy, $data_path);
								unlink $tmpfile;
								last;
							}
						}
						sleep(1);
					}
				}
			}
		}
	}
	$err;
}

sub data_read {
	my($data_path) = @_;
	my(@READ_DATA);
	if (open(DB,"$data_path")) {
		@READ_DATA = <DB>;
		close(DB);
	}
	@READ_DATA;
}

#來自自立後的孩子的生活補貼
sub kodomo_siokuri {
#hash代入每職業的工資
	open(SP,"./dat_dir/job.dat") || &error("Open Error : ./dat_dir/job.dat");
	$top_koumoku = <SP>;
	@job_hairetu = <SP>;
	close(SP);
	foreach  (@job_hairetu) {
		&job_sprit($_);
		$job_kihonkyuu {$job_name} = $job_kyuuyo;
	}
	open(KOD,"$kodomo_file") || &error("Open Error : $kodomo_file");
	@all_kodomo=<KOD>;
	close(KOD);
	$now_time= time;
	$kodomoiruka_flag=0;
	foreach  (@all_kodomo) {
		($kod_num,$kod_name,$kod_oya1,$kod_oya2,$kod_job,$kod_kokugo,$kod_suugaku,$kod_rika,$kod_syakai,$kod_eigo,$kod_ongaku,$kod_bijutu,$kod_looks,$kod_tairyoku,$kod_kenkou,$kod_speed,$kod_power,$kod_wanryoku,$kod_kyakuryoku,$kod_love,$kod_unique,$kod_etti,$kod_yobi1,$kod_yobi2,$kod_yobi3,$kod_yobi4,$kod_yobi5,$kod_yobi6,$kod_yobi7,$kod_yobi8,$kod_yobi9,$kod_yobi10)=split(/<>/);
		if ($kod_yobi8 != 1){next;}
		if ($kod_oya1 eq $name || $kod_oya2 eq $name){
				$kono_nenrei = int (($now_time - $kod_yobi1)/(60*60*24));
				$siokuri_kingaku = ($job_kihonkyuu {$kod_job} * $kono_nenrei) + ($kod_yobi4 * 10);
				$siokuri_kingaku = int ($siokuri_kingaku / 4);
				$bank += $siokuri_kingaku;
				&kityou_syori("生活補貼←$kod_name","",$siokuri_kingaku,$bank,"普");
		}
	}
}

1;
