sub get_unit {
##################零件信息的定義(這兒被定義了的零件呈現在管理者菜單的「街的佈置作成」上。
	%unit = (
#想增加畫像零件(自己喜歡的零件畫像的情況，請參考追加這個格式。畫像數據請放入到img文件夾。畫像需要全部統一32px ×32px。
#零件定義就這樣更換畫像數據為同樣的文件名任意的畫像也是OK)
#　"記號"="><td><img src=$img_dir/圖像文件名></td>",
#　※「記號」任意安上容易識別的任意的文字，不過不要太變(盡可能2個字以內)。
#再者注意不要與其他重複。

#ver.1.30 零件的html記述幾個省略化
"交叉" => "<td><img src=$img_dir/kousa_r.gif></td>",
"道橫" => "<td><img src=$img_dir/yoko_r.gif></td>",
"道縱" => "<td><img src=$img_dir/tate_r.gif></td>",
"木1" => "<td><img src=$img_dir/tree1.gif></td>",
"木2" => "<td><img src=$img_dir/tree2.gif></td>",
"木3" => "<td><img src=$img_dir/tree3.gif></td>",
"木4" => "<td><img src=$img_dir/tree4.gif></td>",
"海" => "<td><img src=$img_dir/umi.gif></td>",

#如果是連結用零件(姊妹城市等街向其他的URL貼鏈接的格式。
#如果重新追加，複製這個格式之後，記號，URL，說明，如果有必要請變更圖像文件名)
#　"記號"="><td><a href=\"連結的URL\" target=_blank><img src='$img_dir/畫像名' width=32 height=32 border=0 onMouseOver='onMes5(\"鼠標指著的時候被表示的說明\")' onMouseOut='onMes5(\"\")'></a></td>",
#下是寫法為樣品。請別實際設置這個街。

"連結" => "<td><a href=\"http://brassiere.jp/03com/town2/town_maker.cgi\" target=_blank><img src='$img_dir/link.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"是試驗參加用的樣品設置程序。\")' onMouseOut='onMes5(\"\")'></a></td>",

#有了機能的零件(因此，成為對有了各自機能的建築物等的連結，基本上請不要做變更。如果有必要，可對說明，圖像文件名(src='$img_dir/○○.gif的部分)變更)

"區鄉" => "<form method=POST action=\"admin.cgi\"><td height=32 width=32><input type=hidden name=mode value=yakuba><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/yakuba.gif'  onMouseOver='onMes5(\"區鄉。能看新居民的登記和排名。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"銀行" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=ginkou><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><td height=32 width=32><input type=image src='$img_dir/bank.gif'  onMouseOver='onMes5(\"銀行。能存款、提款及貸款。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"醫院" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=byouin><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><td height=32 width=32><input type=image src='$img_dir/hospital.gif'  onMouseOver='onMes5(\"醫院。費用是很高，不過大部分的病能使之痊癒。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"卡" => "<form method=POST action=\"basic.cgi\"><input type=hidden name=mode value=donus><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><td height=32 width=32><input type=image src='$img_dir/donuts_tate.gif'  onMouseOver='onMes5(\"目的是抽出與之前的人抽了的卡不同數字的卡牌遊戲。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"食堂" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=syokudou><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/syokudou.gif'  onMouseOver='onMes5(\"中央食堂。種類豐富，價格比較高而庫存也較少。\")' onMouseOut='onMes5(\"\")'></td></form>",

"百貨" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=depart_gamen><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/depart.gif'  onMouseOver='onMes5(\"百貨商店。種類豐富，價格比較高而庫存也較少。\")' onMouseOut='onMes5(\"\")'></td></form>",

"練習" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=gym><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/gym.gif'  onMouseOver='onMes5(\"體育練習場。能鍛鍊身體。\")' onMouseOut='onMes5(\"\")'></td></form>",

"學校" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=school><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/school.gif'    onMouseOver='onMes5(\"學校。提高特定的能力而且有較大的效果，不過1日只是1課。\")' onMouseOut='onMes5(\"\")'></td></form>",

"職業介紹" => "<form method=POST action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=job_change><input type=hidden name=name value=$name><input type=hidden name=pass value=$pass><input type=hidden name=k_id value=$k_id><input type=hidden name=town_no value=$in{'town_no'}><input type=image src='$img_dir/work.gif'  width=32 height=32 border=0  onMouseOver='onMes5(\"職業介紹所。在這就業，轉業。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"空地" => "<td><img src=$img_dir/akiti.gif onMouseOver='onMes5(\"能在這個地方能建造家。\")' onMouseOut='onMes5(\"\")'></td>",

"批發商" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=orosi><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/tonya.gif\" onMouseOver='onMes5(\"有商店和企業的人，能通過這裡購入商品。\")' onMouseOut='onMes5(\"\")'></td></form>",

"建築" => "<form method=POST action=\"$script\"><td height=32 width=32><input type=hidden name=mode value=kentiku><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/kentiku.gif\"  onMouseOver='onMes5(\"建設公司。想建家的時候到這裡。\")' onMouseOut='onMes5(\"\")'></td></form>",

"賽馬" => "<form method=POST action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=keiba><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/keiba.gif\"  onMouseOver='onMes5(\"馬場。\")' onMouseOut='onMes5(\"\")'></td></form>",			#ver.1.40

"個人資料" => "<form method=POST action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=prof><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/prof.gif\"  onMouseOver='onMes5(\"登記居民的真正的個人資料。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"人物" => "<form method=POST action=\"game.cgi\"><td height=32 width=32><input type=hidden name=mode value=c_league><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/chara_battle.gif\"  onMouseOver='onMes5(\"決定最強的登場人物的『C聯盟』會場。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"街競" => "<form method=POST action=\"./mati_contest.cgi\"><td height=32 width=32><input type=hidden name=mode value=matikon><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/matikon.gif\"  onMouseOver='onMes5(\"街之名譽競爭的『週間街競賽』。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

"地" => "<td><img src=$img_dir/kentiku_yotei.gif width=32 height=32  width=32 height=32 border=0 onMouseOver='onMes5(\"建築預定地。\")' onMouseOut='onMes5(\"\")'></td>",

#如果根據版本升級等新的機能零件，請「從這裡」～「到這裡」之間追加。
####「從這裡」
#ver.1.1追加
"溫泉" => "<form method=POST action=\"basic.cgi\"><td height=32 width=32><input type=hidden name=mode value=onsen><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/onsen.gif\"  onMouseOver='onMes5(\"溫泉。治療累了的身體吧。入場費是$nyuuyokuryou元。\")' onMouseOut='onMes5(\"\")'></td></form>",	#ver.1.40

#ver.1.3追加
"戀人介紹" => "<form method=POST action=\"kekkon.cgi\"><td height=32 width=32><input type=hidden name=mode value=assenjo><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/assenjo.gif\"  onMouseOver='onMes5(\"戀人介紹所。想做虛擬的戀愛和結婚的玩者請到這裡登記。\")' onMouseOut='onMes5(\"\")'></td></form>",		#ver.1.40

####「到這裡」
);

################這兒是零件信息的定義
}

sub kozin_house {
#unit hash代入個人的家信息
	open(OI,"$ori_ie_list") || &error("Open Error : $ori_ie_list");
	@ori_ie_hairetu = <OI>;
	foreach (@ori_ie_hairetu) {
			&ori_ie_sprit($_);
			$unit{"$ori_k_id"} = "<form method=POST action=\"original_house.cgi\"><td><input type=hidden name=mode value=houmon><input type=hidden name=ori_ie_id value=$ori_k_id><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$ori_ie_image\"   onMouseOver='onMes5(\"$ori_ie_setumei\")' onMouseOut='onMes5(\"\")'></td></form>";		#ver.1.40
	}
	close(OI);
}

sub simaitosi {
#unit hash代入對其他的街的連結信息
	$i=0;
	$i2=1;
	foreach (@town_hairetu) {
			$unit{"街$i2"} = "<form method=POST action=\"$script\"><input type=hidden name=mode value=login_view><input type=hidden name=command value=mati_idou><td height=32 width=32><input type=hidden name=town_no value=$i><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=image src=\"$img_dir/mati_link.gif\"    onMouseOver='onMes5(\"向 $_ 移動\")' onMouseOut='onMes5(\"\")'></td></form>";
			$i ++;
			$i2 ++;
	}
}

sub admin_parts {
#unit hash代入給管理者作成BBS的連結信息
	$i=1;
	$i2=0;
	foreach (@admin_bbs_syurui) {
			$unit{"板$i"} = "<form method=POST action=\"original_house.cgi\"><td height=32 width=32><input type=hidden name=mode value=normal_bbs><input type=hidden name=ori_ie_id value=admin><input type=hidden name=bbs_num value=$i2><input type=hidden name=name value=$in{'name'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=town_no value=$in{'town_no'}><input type=image src=\"$img_dir/$admin_bbs_gazou[$i2]\"   onMouseOver='onMes5(\"$_\")' onMouseOut='onMes5(\"\")'></td></form>";		#ver.1.40
			$i ++;
			$i2 ++;
	}
}

1;
