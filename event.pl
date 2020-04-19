sub event_happen {
	$hassei_rand = int(rand(10))+1;
	if ($hassei_rand == 1){
#事件發生的情況
			$event_rand = int(rand(25))+1;		#ver.1.30
			$happend_ivent .= <<"EOM";
<font color="#000000">事件發生！</font><br>
EOM
			if ($event_rand == 1){
					$syou_rand = int(rand(10000))+1;
					if ($money <= 0){
						$happend_ivent .= "<div class=purasu>●被小偷光顧了，不過因為沒有可以偷的錢剩下而即時走了。</div>";
					}else{ 
						if($money < $syou_rand){$syou_rand=$money;}
						$money -= $syou_rand;
						$happend_ivent .= "<div class=mainasu>●被小偷光顧了。$syou_rand元被偷了。</div>";
					}
			}
			
			if ($event_rand == 2){
					$syou_rand = int(rand(10000))+1;
					$happend_ivent .= "<div class=purasu>●在街上拾到了錢包。裡面有$syou_rand元，於是把它拾起來了。</div>";
					$money += $syou_rand;
			}
			
			if ($event_rand == 3){
					if (int(rand(2))+1 == 1){
						$happend_ivent .= "<div class=purasu>●遇見傳教師，親切的跟他談話後，學到了英語。英語力3提高！</div>";
						$eigo += 3;
						&motimono_kensa("英文解釋教室");
						if ($kensa_flag == 1){
							$happend_ivent .= "<div class=purasu>●取出英文解釋教室，得到英語老師很熱心講解。英語力5提高！</div>";
							$eigo += 5;
						}
					}else{
						$happend_ivent .= "<div class=mainasu>●被英語老師放棄了。英語力3下降！</div>";
						$eigo -= 3;
					}
			}
			
			if ($event_rand == 4){
					$happend_ivent .= "<div class=mainasu>●患感冒了。</div>";
					$byouki_sisuu = -15;
			}
			
			if ($event_rand == 5){
					$happend_ivent .= "<div class=mainasu>●NHK的賬單來。支付了100元。</div>";
					$money -= 100;
			}
			
			if ($event_rand == 6){
					$happend_ivent .= "<div class=purasu>●因為失戀而暴飲暴食了。體重增加了1kg。</div>";
					$taijuu += 1;
			}
			
			if ($event_rand == 7){
					if (int(rand(2))+1 == 1){
					$happend_ivent .= "<div class=purasu>●對文學覺醒了。國語力3提高！</div>";
					$kokugo += 3;
					}else{
					$happend_ivent .= "<div class=mainasu>●忘記了很多詞彙。國語力3下降！</div>";
					$kokugo -= 3;
					}
			}
			
			if ($event_rand == 8){
					if (int(rand(2))+1 == 1){
					$happend_ivent .= "<div class=purasu>●玩數學謎題。數學力3提高！</div>";
					$suugaku += 3;
					}else{
					$happend_ivent .= "<div class=mainasu>●得了數字恐懼症。數學力3下降！</div>";
					$suugaku -= 3;
					}
			}
			
			if ($event_rand == 9){
					if (int(rand(2))+1 == 1){
					$happend_ivent .= "<div class=purasu>●在電視收看了科學的節目。理科的力量3提高！</div>";
					$rika += 3;
					}else{
					$happend_ivent .= "<div class=mainasu>●理科的實驗弄碎了試管。理科的力量3下降！</div>";
					$rika -= 3;
					}
			}
			
			if ($event_rand == 10){
					if (int(rand(2))+1 == 1){
					$happend_ivent .= "<div class=purasu>●讀了歷史的書。社會的力量3提高！</div>";
					$syakai += 3;
					}else{
					$happend_ivent .= "<div class=mainasu>●對社會的關心像退潮一樣。社會的力量3下降！</div>";
					$syakai -= 3;
					}
			}
			
			if ($event_rand == 11){
					if (int(rand(2))+1 == 1){
					$happend_ivent .= "<div class=purasu>●做了鋼琴的練習。音樂的力量3提高！</div>";
					$ongaku += 3;
					}else{
					$happend_ivent .= "<div class=mainasu>●在聚會喧嘩過多導致喉嚨痛。音樂的力量3下降！</div>";
					$ongaku -= 3;
					}
					&motimono_kensa("爆發");
					if ($kensa_flag == 1){
							$happend_ivent .= "<div class=purasu>●看「爆發」後對音樂的幹勁沸騰了。音樂5提高</div>";
							$ongaku += 3;
					}
			}
			
			if ($event_rand == 12){
					if (int(rand(2))+1 == 1){
					$happend_ivent .= "<div class=purasu>●對藝術覺醒了。美術的力量3提高！</div>";
					$bijutu += 3;
					}else{
					$happend_ivent .= "<div class=mainasu>●在美術的授課打瞌睡。美術的力量3下降！</div>";
					$bijutu -= 3;
					}
			}
			
			if ($event_rand == 13){
					#$kuzi_rand = int(rand(15))+1;
					#$kuzi_gaku = $kuzi_rand * 10000;
					#$money += $kuzi_gaku;
					#改造1.0
					$marksix_rand = int(rand(50))+1;
					if($marksix_rand == 7){
						$marksix_rand = 5000000;
						$marksix_msg = "哇哇哇，六合彩中了頭獎！得到五百萬元！";
					} elsif ($marksix_rand >= 49){
						$marksix_rand = 500000;
						$marksix_msg = "哇，六合彩中了二獎！得到五十萬元！";
					} elsif ($marksix_rand >= 43){
						$marksix_rand = 50000;
						$marksix_msg = "Yeah~！六合彩中了三獎！得到五萬元！";
					} elsif ($marksix_rand >= 34){
						$marksix_rand = 5000;
						$marksix_msg = "六合彩中了四獎！得到五千元！";
					} elsif ($marksix_rand >= 20){
						$marksix_rand = 500;
						$marksix_msg = "六合彩中了五獎！得到五百元！";
					} else {
						$marksix_rand = 50;
						$marksix_msg = "六合彩中了安慰獎！得到五十元！";
					}
					$happend_ivent .= "<div class=purasu>●$marksix_msg</div>";
					$money += $marksix_rand;
			}
			
			if ($event_rand == 14){
					$happend_ivent .= "<div class=purasu>●突然對事情有很深的感受。LOVE度5提高！</div>";
					$love += 5;
			}
			
			if ($event_rand == 15){
					$happend_ivent .= "<div class=mainasu>●大概因為裸睡，好像著涼了，影響了健康狀態。</div>";
					$byouki_sisuu = -8;
			}
			
			if ($event_rand == 16){
				if ($money <= 0){
					$happend_ivent .= "<div class=mainasu>●遇上扒手，不過因為「根本沒有錢」，他空手而回了。</div>";
				}else{
				$happend_ivent .= "<div class=mainasu>●遇上扒手。所持金減半。</div>";
					$money = int ($money/2);
				}
			}
			
			if ($event_rand == 17){
							$myranded=int(rand(2))+1;
							&motimono_kensa("外婆的智囊");
							if ($kensa_flag == 1){
									$happend_ivent .= "<div class=purasu>●收了出了的書的印花稅300元。</div>";
									$money=$money+300;
							}elsif($myranded == 1){
									$happend_ivent .= "<div class=purasu>●收了出了的書的印花稅100元。</div>";
									$money=$money+100;
							}else{
									$happend_ivent .= "<div class=purasu>●收了出了的書的印花稅50元。</div>";
									$money=$money+50;
							}

			}
			if ($event_rand == 18){
							$myranded=int(rand(2))+1;
							&motimono_kensa("呼拉圈");
							if ($kensa_flag == 1){
									$happend_ivent .= "<div class=purasu>●在家門外玩呼拉圈！拾到77元。</div>";
									$money=$money+77;
							}elsif($myranded == 1){
									$happend_ivent .= "<div class=purasu>●在家門外拾到100元。</div>";
									$money=$money+10;
							}else{
									$happend_ivent .= "<div class=mainasu>●在家門外拾到錢包，不過被發現了，被人索取了500元。</div>";
									$money=$money-50;
							}

			}
			
			if ($event_rand == 19){
							&motimono_kensa("谷保天滿宮的守護符");
							if ($kensa_flag == 1){
									$happend_ivent .= "<div class=purasu>●差點被車撞倒，得到『谷保天滿宮的守護符』的守護，得到3千元作為道歉費。</div>";
									$money=$money+3000;
							}elsif($speed <= 180){
									$happend_ivent .= "<div class=mainasu>●被車撞倒負了輕傷。住院費花了3千元。</div>";
									$money=$money-3000;
							}else{
									$happend_ivent .= "<div class=purasu>●差點被車撞倒，不過只是有驚無險。</div>";
							}

			}
			
			if ($event_rand == 20){
							$myranded=int(rand(2))+1;
							&motimono_kensa("幸福香水");
							if ($kensa_flag == 1){
									$happend_ivent .= "<div class=purasu>●因為使用「幸福香水」而留在家中而得到橫財，所持金增加為二倍！</div>";
									$money=$money * 2;
							}elsif($myranded == 1){
									$happend_ivent .= "<div class=purasu>●在家門外掉了30元。</div>";
									$money=$money+30;
							}else{
									$happend_ivent .= "<div class=mainasu>●玩彈珠機花了1千元。。</div>";
									$money=$money-1000;
							}
			}
			
			if ($event_rand == 21){
							$myranded=int(rand(2))+1;
							&motimono_kensa("威而鋼");
							if ($kensa_flag == 1){
									$happend_ivent .= "<div class=purasu>●在家使用了「威而鋼」LOVE度及淫蕩度3提高！</div>";
									$love += 3;
									$etti += 3;
							}elsif($myranded == 1){
									$happend_ivent .= "<div class=purasu>●收到朋友送的甲魚精。淫蕩度3提高！</div>";
									$etti += 3;
							}else{
									$happend_ivent .= "<div class=mainasu>●腹瀉令性慾也不感興趣。。淫蕩度3下降。。</div>";
									$etti -= 3;
							}
			}
			
			if ($event_rand == 22){
				if (int(rand(2))+1 == 1){
					$happend_ivent .= "<div class=mainasu>●地震發生了!!所持金變成了原先的3分之一。</div>";
					$money = int ($money/3);
				}else{
					$happend_ivent .= "<div class=purasu>●在資產運用上成功，所持金變成了原先的二倍。</div>";
					$money = int ($money*2);
				}
			}
#ver.1.30從這裡
			if ($event_rand == 23){
							$myranded=int(rand(4))+1;
							&motimono_kensa("黑卡");
							if ($kensa_flag == 1){
								if ($myranded == 1){
									$happend_ivent .= "<div class=purasu>●「黑卡」優惠♪　相當現金1千元！</div>";
									$money += 1000;
								}elsif ($myranded == 2){
									$happend_ivent .= "<div class=purasu>●「黑卡」優惠♪　相當現金1萬元！</div>";
									$money += 10000;
								}elsif ($myranded == 3){
									$happend_ivent .= "<div class=purasu>●「黑卡」優惠♪　相當現金5萬元！</div>";
									$money += 50000;
								}elsif ($myranded == 4){
									$happend_ivent .= "<div class=purasu>●「黑卡」優惠♪　相當現金10萬元！</div>";
									$money += 100000;
								}
							}else{
									$nouzeigaku = int ($k_sousisan * 0.01);
									if ($nouzeigaku < 0){$nouzeigaku = 0;}
									$money -= $nouzeigaku;
									if ($nouzeigaku == 0){
										$happend_ivent .= "<div class=purasu>●稅務局來了，不過因為太貧窮避免了納稅。</div>";
									}else{
										if ($nouzeigaku =~ /^[-+]?\d\d\d\d+/g) {for ($i = pos($nouzeigaku) - 3, $j = $nouzeigaku =~ /^[-+]/; $i > $j; $i -= 3) {substr($nouzeigaku, $i, 0) = ',';}}
										$happend_ivent .= "<div class=mainasu>●向稅務局納了總資產的1％稅$nouzeigaku元。</div>";
									}
							}
			}
			if ($event_rand == 24){
				if (int(rand(10))+1 == 1){
					$kuzi_rand = int(rand(10))+1;
					$kuzi_gaku = $kuzi_rand * 100000;
					$kuzi_hyouzi = $kuzi_rand . "0";
					$happend_ivent .= "<div class=purasu>●彩票中了！得到$kuzi_hyouzi萬元！</div>";
					$money += $kuzi_gaku;
				}else{
					$happend_ivent .= "<div class=mainasu>●用300元購買了彩票還是落空了。</div>";
					$money -= 300;
				}
			}
			if ($event_rand == 25){
					$happend_ivent .= "<div class=mainasu>●玩遊戲太多導致神經過敏。體重減少了1kg。</div>";
					$taijuu -= 1;
			}
#ver.1.30到這裡
			
$happend_ivent .= <<"EOM";
<OBJECT classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
 codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0"
 WIDTH="5" HEIGHT="5" id="happen">
 <PARAM NAME=movie VALUE="$img_dir/happen.swf"> <PARAM NAME=loop VALUE=false> <PARAM NAME=quality VALUE=low> <PARAM NAME=wmode VALUE=transparent> <PARAM NAME=bgcolor VALUE=#ffffaa> <EMBED src="$img_dir/happen.swf" loop=false quality=low wmode=transparent bgcolor=#ffffaa  WIDTH="5" HEIGHT="5" NAME="happen" TYPE="application/x-shockwave-flash" PLUGINSPAGE="http://www.macromedia.com/go/getflashplayer"></EMBED>
</OBJECT>
EOM
#廣告表示
	#}elsif ($hassei_rand == 2){
	#				$happend_ivent .= "<IFRAME src=\"http://macler.com/ranran_banner_text/ranran_banner.cgi\"  width=100% height=40 scrolling=no marginheight=0 FRAMEBORDER=0></IFRAME>";
	
#寒暄的情況
	}else{
		open(IN,"$aisatu_logfile") || &error("Open Error : $aisatu_logfile");
		@aisatu_data = <IN>;
		close(IN);
				srand(time^$$);
				$a_randed=rand($#aisatu_data+1);
				$aisatu_data=splice(@aisatu_data,$a_randed,1);
				local($a_num,$a_name,$a_date,$a_com,$a_syurui,$a_yobi2)= split(/<>/, $aisatu_data);
				if ($a_num eq ""){
					$happend_ivent .= "";
				}else{
					if ($a_yobi2){$icon_hyouzi_a = "$a_yobi2";}else{$icon_hyouzi_a = "";}
					$happend_ivent .= "$icon_hyouzi_a<span style=\"color:#ff6600\">$a_name君的『$a_syurui』</span>:$a_com $a_date";
				}
	}
}


####寒暄
sub aisatu {
	my(@all_data,$a_total_kizisuu,$top);
	if ($in{'command'} eq "icon_touroku"){
		$kounyuu = $in{'my_icon'};
		&temp_routin;
		&log_kousin($my_log_file,$k_temp);
			&message("做了圖標的設定。","login_view");
			exit;
#留言處理的情況
	}elsif ($in{'command'} eq "aisatu_do"){
		if (length($in{'a_com'}) > 120) {&error("寒暄是60字以內");}
		if ($in{'a_com'} eq "") {&error("未輸入評語");}
			&lock;
		#log file更新
			# 讀入記錄
			open(IN,"$aisatu_logfile") || &error("Open Error : $aisatu_logfile");
			# 取得前往前頭
			$top = <IN>;
			@all_data = <IN>;
			$a_total_kizisuu = @all_data;
			local($a_num,$a_name,$a_date,$a_com,$a_syurui,$a_yobi2)= split(/<>/, $top);
#a_yobi2 = 圖標的URL
			close(IN);
		
		#HTML標記禁止處理
				$in{'a_com'} =~ s/</&lt;/g;
				$in{'a_com'} =~ s/>/&gt;/g;
				$in{'a_com'} =~ s/([^=^\"]|^)(https?\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\%]+)/$1<a href=\"$2\" target=\"_blank\">$2<\/a>/g;
#ver.1.40從這裡
			$name_seikei = $in{'name'} . "<input type=hidden name=sousinsaki_name value=$in{'name'}>";
			if ($name_seikei eq "$a_name" && $in{'a_com'} eq "$a_com") {
				&error("不可重複留言");
			}
#ver.1.40到這裡
			
			&time_get;
		#定義更新陣列
			$a_num ++;
			if ($kounyuu){$icon_hensuu = "<img src=$kounyuu width=32 height=32 align=left>";}
			else{$icon_hensuu = "";}
			$a_toukou = "$a_num<>$in{'name'}<input type=hidden name=sousinsaki_name value=$in{'name'}><>（$date2）<input type=submit value=\"發郵件\" style=\"font-size:12px;border-style: solid; border-width: 0px;\"><>$in{'a_com'}<>$in{'a_syurui'}<>$icon_hensuu<>\n";
		
			@new_all_data = ();
			$new_all_data[0] = $a_toukou;
			$new_all_data[1] = $top;
			$i = 0;
			foreach (@all_data){
				$i ++ ;
				push (@new_all_data,$_);
				if ($i >= $aisatu_max - 2){last;}
			}
			
		# 更新記錄
			open(OUT,">$aisatu_logfile") || &error("Write Error : $aisatu_logfile");
			print OUT @new_all_data;
			close(OUT);
		# 鎖解除
			&unlock;
#取得錢
	$randed += int(rand(10))+1;
	if ($randed == 7){
		$randed += int(rand(1000))+500;
		$money += $randed;
		$message_in = "這是獎金!取得$randed元。";
	}else{
		$randed += int(rand(200))+100;
		$money += $randed;
		$message_in = "得到了$randed元。";
	}
	&temp_routin;
	&log_kousin($my_log_file,$k_temp);
			&message("留了言。$message_in","login_view");
			exit;
	}	#留言的情況閉上
	
	foreach (@aisatu_keyword){
		$aisatu_syurui .= "<option value=$_>$_</option>\n"
	}
	if ($kounyuu){
		$icon_hyouzi_url = "$kounyuu";
		$icon_hyouzi = "<img src=$kounyuu width=32 height=32>";
	}else{
		$icon_hyouzi_url = "http://";
		$icon_hyouzi = "";
	}
	&header("");
	print <<"EOM";
	<form method="POST" action="$script">
	<input type=hidden name=mode value="aisatu">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=command value="aisatu_do">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<br><br><table  width=550 border="0" cellspacing="0" cellpadding="15" align=center class=yosumi>
	<tr><td bgcolor=#ffffcc>
	<div align=center><select name=a_syurui>
	$aisatu_syurui
	</select><br><br>
	<input type=text name=a_com size=80></div>
	<br>※在這裡留了言的評語在信息窗上被random表示。文字數是60字以內。禁止HTML標記。<br><br><div align=center>
	<input type=submit value=" O K "></div>
  </td>
</tr>
</table>
	</form>
	
	<form method="POST" action="$script">
	<input type=hidden name=mode value="aisatu">
	<input type=hidden name=name value="$in{'name'}">
	<input type=hidden name=pass value="$in{'pass'}">
	<input type=hidden name=command value="icon_touroku">
	<input type=hidden name=town_no value=$in{'town_no'}>
	<br><br><table width=550 border="0" cellspacing="0" cellpadding="15" align=center class=yosumi>
	<tr><td>
	<div class=honbun2>○自己的圖標畫像設定</div>
	$icon_hyouzi<br>
	※能設定在自己的圖標畫像。請指定http://～開始的絕對URL。尺寸限制是32×32。<br>
	畫像的URL <input type=text name=my_icon size=60 value="$icon_hyouzi_url"></div>
	<br>※設定了的圖標，以寒暄窗口和街比賽被表示。<br><br><div align=center>
	<input type=submit value=" O K "></div>
  </td>
</tr>
</table>
	</form>
EOM
	&hooter("login_view","返回");
	exit;
}

###攜帶品檢查子程序
sub motimono_kensa {		#ver.1.40
	$monokiroku_file="./member/$k_id/mono.cgi";
	if (! -e $monokiroku_file){open (MOF,">$monokiroku_file") || &error("不能作成自己的購買物文件");}
	close(MOF);
	open(MK,"$monokiroku_file") || &error("自己的購買物文件不能打開");
	@my_kounyuu_list =<MK>;
	close(MK);
	$kensa_flag=0;
	foreach $one_kounyuu_item (@my_kounyuu_list){
		&syouhin_sprit ($one_kounyuu_item);
		if ($syo_taikyuu <= 0){next;}
		foreach $check_item (@_){
			if ($check_item eq "$syo_hinmoku"){$kensa_flag=1;last;}
		}
	}
}

1;

