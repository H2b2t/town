#------------------以下，初始設置項目-------------------
#街的名字
$title='TOWN';

#管理者名(由於在這兒設定的是管理者名和密碼，所以新登記時能免費製作家)
$admin_name = '1234';

#管理者密碼
$admin_pass = '1234';

#維護中標誌(通常是0。變成1能使之中斷以維護遊戲)
$mente_flag = '0';

#維護時候的消息
$mente_message = '現在維護中。。。請等候5分左右';

#畫像文件夾(img)的指定。開始於來自程序的當面路徑 or http://～的絕對路徑 ※最後的「/」不要。
$img_dir = './img';

#返回主頁
$homepage = '';

#管理者郵件地址(諮詢用)
$master_ad = 'info@realdreamer.com';

#在首頁的資訊內容(HTML標記可)
$osirase = <<"EOM";



※登記後，名字不能變更。

EOM

#製作街的名字(最左的街是最初被表示的街。作為例子設定著4個，不過，光是1個、或4個以上也可以。※重要:如果在遊戲途中增加街，請必定在最後增加)
@town_hairetu = ("Main Street","She resort","County town","Downtown");

#街的地價(指定了在上面的街的地價。從左面按順序與上面使之對應。單位是萬元)
@town_tika_hairetu = ("460","320","60","30");

#街的背景風格(指定了在上面的街的背景風格設定。從左面按順序與上面使之對應。可指定風格畫像)
@page_back = ("background-color:#ffffcc","background-image : url( img/umi.gif)","background-color:#99cc66","background-color:#cccc99");

#請以參加者能建造的家的畫像和價格('畫像名','價格'的形式設定。價格的單位是(萬元)。家的畫像需要預先放入到img文件夾。)
%ie_hash=('house1.gif','15','house2.gif','15','house3.gif','15','house4.gif','80','house5.gif','80','house6.gif','80','house7.gif','180','house8.gif','180','house9.gif','180','house10.gif','320','house11.gif','320','house12.gif','320','house13.gif','440','house14.gif','440','house15.gif','440','house16.gif','360','house17.gif','380','house18.gif','360','house19.gif','320','kamakura.gif','15','bil2.gif','400','bil3.gif','440','bil4.gif','460','bil5.gif','460');

#內裝費用(左面A～D排位。A排位表示能4個內容，D排位表示可能只1個內容。單位萬元)
@housu_nedan = ("120","80","40","10");

#在區鄉的排列次序表示數
$rankMax='100';

#不進餐幾天會死(用戶刪掉期間)
$deleteUser = '30';

#每隔幾分能吃飯
$syokuzi_kankaku = '30';

#身體能源的復甦率(幾秒恢復1點？數少的那樣復甦快)
$sintai_kaihuku = "30";

#頭腦能源的復甦率(幾秒恢復1點？數少的那樣復甦快)
$zunou_kaihuku = "30";

#在批發商排列的商品數
$orosi_sinakazu = "120";

#批發商的庫存調整(「syouhin.dat」指定的庫存的幾倍的數？店增加了而批發商的庫存數可考慮不夠增加這個數字。1.5等的指定也可)
$ton_zaiko_tyousei = '2';

#在中央食堂裡排列的食品的種類數
$syokudou_sinakazu = "30";

#在百貨商店排列的商品的種類數
$depart_sinakazu = "80";

#所有物的限度數
$syoyuu_gendosuu = '10';

#在食堂和百貨商店的用這個數字跌破了庫存調節值(基準的庫存數的數在鋪面排列，這個數字很大的話庫存很少，很小的話庫存變得多)
$zaiko_tyousetuti ="5";

#店的類別(這個遊戲內的店上市的商品的數據，在「dat_dir」內的「shouhin.dat」創造。需要「shouhin.dat」文件的最左有商品類別，對應這裡的「店的類別」。※但表示食堂的「食」是「shouhin.dat」有的類別)
@global_syouhin_syubetu = ("超市","書籍","食品","藥","體育用品","電器","美容","成人","DVD","快餐食品","日用品","花","甜品","禮物","酒精","交通工具","遊戲","飲料");

#寒暄的種類
@aisatu_keyword = ("寒暄","今天的事情","現在的心情");

#寒暄記錄的保存件數
$aisatu_max = '10';

#最大登記人數
$saidai_ninzuu = '1000';

#自動文件生成文件夾的permission(777=1，755=2)※要是1錯誤請試驗2。
$zidouseisei = "1";

#消息窗的風格設定
$message_window ="border: #ff9933; border-style: dotted; border-width: 1px; background-color:#ffffaa; color:336699";

#狀態窗的框框顏色
$st_win_wak = "#ff9966";
#狀態窗的背景顏色
$st_win_back = "#ffffff";

#請以「,」聯結設置了的留言板('留言板的名字'的形式設定。在這裡的名字是裝上了鼠標時在窗口上使之表示的名字。頁內的標題和各種設計·設定進行管理選單的「管理者作成BBS的設定」。實際配置到街任意的位置留言板，請決定管理者選單的「街的佈置作成」。)
@admin_bbs_syurui =('公眾的廣場。這是綜合留言板。','疑問解決BBS。關於一般感到疑問的事。','推薦信息BBS。把你推薦的告訴大家。','Happy留言板。請在你覺得愉快的瞬間留言。','Main Street居民專用留言板','She resort居民專用留言板','County town居民專用留言板','Downtown居民專用留言板');

#從上述留言板的畫像(左面與上面使之對應)
@admin_bbs_gazou =('bbs1.gif','bbs2.gif','bbs3.gif','bbs4.gif','bbs5.gif','bbs5.gif','bbs5.gif','bbs5.gif','bbs6.gif','bbs6.gif','bbs6.gif','bbs6.gif');

#BBS的保存筆數(選擇式個人資料項目)
$bbs_kizi_max = '100';

# 訪問拒絕的主機名
@deny = ("*.host.xx.jp","xxx.xxx.xx.");

#多重登記禁止(以1禁止，以0不禁止)
$tajuukinsi_flag = '0';

#多重登記的人不能進入(以1做，0不做)
$tajuukinsi_deny = '0';

#開始時的資金
$new_money = 5000;

#Ｃ聯賽1大會的日數
$c_nissuu = '14';

#Ｃ聯賽的比賽數
$c_siaisuu = "100";

#Ｃ聯賽的比賽間隔(以分為單位)
$c_siai_kankaku = '30';

#選擇式個人資料項目(不指定的情況，成為自由尺寸)
$chara_x_size = '80';	#橫尺寸
$chara_y_size = '80';	#縱尺寸

#一週街競賽的賞金額(以萬元為單位)
$mati_con_syoukin = '30';

#街競賽的日數
$mati_con_nissuu = '7';

#個人資料的1頁表示數
$hyouzi_max_grobal = '10';

##以下，在個人資料的可供選擇的方案
#性別的select
		@sex_array=('','男','女','中間');

#年齡的select
		@age_array=('','～14歳','15～18歳','19～22歳','23～26歳','27～30歳','31～34歳','35～38歳','39～42歳','43～46歳','47～50歳','51歳～');

#地址的select
		#@address_array=('','北海道','青森','岩手','宮城','秋田','山形','福島','群馬','栃木','茨城','埼玉','千葉','東京','神奈川','新潟','富山','石川','福井','山梨','長野','岐阜','静岡','愛知','三重','滋賀','京都','大阪','兵庫','奈良','和歌山','鳥取','島根','岡山','広島','山口','徳島','香川','愛媛','高知','福岡','佐賀','長崎','熊本','大分','宮崎','鹿児島','沖縄','海外');
		@address_array=
		('','海外','台北市', '台北縣', '基隆市', '宜蘭縣', '桃園縣', '新竹市', '新竹縣', '苗栗縣', 
		'台中市', '台中縣', '彰化縣', '南投縣', '嘉義市', '嘉義縣', '雲林縣', 
		'台南市', '台南縣', '高雄市', '高雄縣', '澎湖縣', '屏東縣', 
		'台東縣', '花蓮縣', '金門縣', '連江縣', '南海諸島',
		'澳門','山頂','中環','上環','金鐘','西環','石塘咀','筲箕灣',
		'北角','西灣河','側魚涌','柴灣','跑馬地','灣仔','銅鑼灣',
		'赤柱','半山','石澳','淺水灣','深水灣','香港仔','鴨利洲','薄扶林',
		'紅磡','尖沙咀','油麻地','何文田','旺角','太子','佐敦',
		'荃灣','青衣','葵涌','藍田','觀塘','九龍城','九龍塘','九龍灣',
		'土瓜灣','大角咀','深水步','長沙灣','荔枝角','石硤尾',
		'牛頭角','油塘','鯉魚門','樂富','鑽石山','黃大仙','慈雲山','新蒲崗','將軍澳',
		'上水','大埔','元朗','屯門','西貢','沙田','粉嶺','深井','天水圍','馬鞍山',
		'坪洲','長洲','大嶼山','赤臘角','南丫島','愉景灣','馬灣',
		'安徽','北京','福建','广东','广西','贵州','海南','河北','河南','黑龙江','湖北','湖南','吉林',
		'江苏','江西','辽宁','内蒙古','山东','山西','陕西','上海','四川','天津','云南','浙江','重庆',
		'甘肃','宁夏','青海','新疆','西藏');
		
#選擇式個人資料項目1
		$prof_name1='吸引點';
		@prof_array1=('','帥','聰明','個子高','體格健壯','具男人味','有風度','富有','擁有車','單身生活','氣質','坦率','認真','誠實','有趣','可愛','漂亮','擁有漂亮胸部','擁有漂亮雙腿','豐滿的身材','重視家庭','擅長體育','唱歌很好聽','擅長烹飪','淫蕩','壞人');

#選擇式個人資料項目2
		$prof_name2='現況';
		@prof_array2=('','戀人募集中','朋友募集中','網友募集中','嗜好朋友募集中','飲食朋友募集中','交友聯誼會朋友募集中','網站宣傳中','性伴件募集中','情人募集中','一心一意工作中','新婚中','別居中','不道德中','熱戀中','同居中','斷絕父子關系中','私奔中','平凡生活中','單戀中');

#選擇式個人資料項目3
		$prof_name3='身長';
		@prof_array3=('','秘密','矮的','稍稍矮的','一般','稍稍高的','高的');

#選擇式個人資料項目4
		$prof_name4='體重';
		@prof_array4=('','秘密','瘦的','稍微瘦的','一般','稍稍肥','肥胖');

#選擇式個人資料項目5
		$prof_name5='職業';
		@prof_array5=('','飛特族(無固定工作者)','學生','無職業','ＯＬ','上班族','公務員','主婦','營業員','技術員','公司職員','銀行職員','資深程序編寫員','飛行員','空中小姐','警察','消防員','僧侶','潮流相關','計劃制訂者','編輯','創作人','銷售員','理髮師','木匠','宣傳媒體','樹木工','公司幹事','事務工作','計算機','飲食業','教師','醫生','美術家','設計家','演員','護士','保姆','顧問','個體戶(自雇)','夜店','音樂相關','藝人','運動員','其他');
		
#選擇式個人資料項目
	@kijutu_prof = ('相似的名人','趣味','主頁','弱點','喜歡的名人','喜歡的體育','喜歡的電影','喜歡的TV節目','喜歡的音樂','喜歡的異性的類型','將來的夢想','討厭的東西','現在最想去的地方','現在最想做的事','一句評語');

##以下各種設計的風格設定
#消息窗的風格設定
$message_win ="border: #000000; border-style: dotted; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; background-color:#ffffff; color:000000";

$town_stylesheet =<< "EOM";
.dai {  font-size: 14px; font-weight: bold;color: #000000}	/*大的文字*/
.tyuu {  font-size: 12px; color: #ff6600}	/*狀態小標題*/
.honbun2 {  font-size: 11px; line-height: 16px; color: #006699}	/*狀態項目部分*/
.honbun3 {  font-size: 11px; line-height: 11px; color: #006699}	/*參數項目部分*/
.honbun5 {  font-size: 11px; line-height: 11px; color: #339900}	/*字符的參數項目部分*/
.honbun4 {  font-size: 12px; line-height: 22px; color: #006699}	/*中等程度的文字*/
.job_messe {  font-size: 11px; line-height: 22px; color: #000000}	/*參數消息*/
.small {  font-size: 10px; color: #444444}	/*小的文字*/
.midasi {  font-size: 16px; font-weight: bold; text-align: center;color: #666666}	/*街的名字*/
.gym_style { background-color:#ffcc33; background-image:url($img_dir/shop_bak.gif)}	/*健身中心的背景*/
.syokudou_style { background-color:#ccff66; background-image:url($img_dir/shop_bak.gif)}	/*食堂的背景*/
.orosi_style { background-color:#996633; background-image:url($img_dir/shop_bak.gif)}	/*批發商的背景*/
.job_style { background-color:#669966; background-image:url($img_dir/shop_bak.gif)}	/*職業介紹所的背景*/
.school_style { background-color:#339999; background-image:url($img_dir/shop_bak.gif)}	/*學校的背景*/
.ginkou_style { background-color:#999999; background-image:url($img_dir/shop_bak.gif)}	/*銀行的背景*/
.yakuba_style { background-color:#336699; background-image:url($img_dir/shop_bak.gif)}	/*區鄉的背景*/
.item_style { background-color:#ffcc66; background-image:url($img_dir/command_bak.gif)}	/*選擇式個人資料項目*/
.kentiku_style { background-color:#996666; background-image:url($img_dir/command_bak.gif)}	/*建築公司的背景*/
.omise_list_style { background-color:#b293ad; background-image:url($img_dir/shop_bak.gif)}	/*個人店的商品名單背景*/
.prof_style { background-color:#ccff99; background-image:url($img_dir/shop_bak.gif)}	/*個人資料畫面背景*/
.keiba_style { background-color:#99cc66; }	/*賽馬背景*/

.yosumi {  border: #666666; border-style: solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; background-color:#ffffff}	/*街狀態窗*/

.sumi {  border: #000000; border-style: solid; border-top-width: 0px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 0px}
.migi {  border: #000000; border-style: solid; border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px}
.sita {  border: #000000; border-style: solid; border-top-width: 0px; border-right-width: 0px; border-bottom-width: 0px; border-left-width: 0px}
.sita2 {  border: #666666; border-style: solid; border-top-width: 0px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px}
.jouge {  border: #000000; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px}
.message {  font-size: 12px; line-height: 16px; color: #000000;}


.purasu {color: #009900;}
.mainasu { color: #ff3300;}
.kuro {  font-size: 13px; text-align: left;color: #000000}
.honbun {  font-size: 11px; line-height: 16px; color: #000000}
.loto {  font-size: 28px; color: #000000;line-height:180%;}
.naka {  border: #000000; border-style: solid; border-top-width: 1px; border-right-width: 0px; border-bottom-width: 1px; border-left-width: 0px}
a {color:#333333;text-decoration: none}
a:hover {text-decoration: underline}
body {font-size:11px;color:#000000 }
table {font-size:11px;color:#000000;}
EOM

##########################ver.1.1增加
#禮物所有限度數(被贈送了的禮物)
$gift_gendo = '10';

#禮物購買限度數
$kounyu_gift_gendo = '5';

#自己的店能放的商品物品數
$mise_zaiko_gendo = '15';

#物品數要是限度以上同樣的物品也不能增加庫存(不能增加=1，能增加=0)
$douitem_ok = '1';

#潯溫泉時通常的幾倍快恢復力
$onsen_times = '10';

#在溫泉使用的畫像的數目(溫泉的畫像，img/onsen文件夾內的○.jpg(○是以1開始的連續數字)的文件名放入)
$on_gazou_suu = '10';

#溫泉入場費(以元為單位)
$nyuuyokuryou = '50';

#gzip的路徑(服務器與gzip壓縮沒對應的情況請要空白欄(※如果畫面變得雪白等沒對應的可能性高)。但，gzip壓縮能使用的話文本的轉送量能相當小)
$gzip = '';

#以徒步對街的移動的時間(以秒指定)
$matiidou_time = '20';

#每各交通工具有關的移動時間('交通工具','懸掛的秒數'的格式。如果交通工具不是在syouhin.dat有的商品就沒有意義。但沒有必要作為「交通工具」的商品類別。我想在評語中加入了「※是移動手段」熱情。再請從快的東西先排列)
%idou_syudan =('米格25','0','法拉利','2','保時捷','3','Lotus Europe','4','Alpha Romeo','4','Jaguar','4','BMW','4','Skyline GTR','4','勞斯萊斯','5','Motors','5','Benz','5','Fair lady Z','6','Cadillac','6','Volvo','7','Corolla','7','Nanahan','7','Ducati','10','Suparcab','10','單車','15');

#在街移動時引起事故的概率(以幾分的一概率指定。默認10分之一的意義)
$ziko_kakuritu = '10';

#行動限制時間(秒指定。不安上限制的情況=0)
$koudou_seigen = '0';

#能玩卡牌遊戲的間隔(單位:分)
$crad_game_time = '30';

##########################ver.1.2增加

#同樣物品的所有件數的限度
$item_kosuuseigen = '3';

#能工作的間隔(單位:分。沒有限制的情況是指定0)
$work_seigen_time = '10';

#賽馬的購買限度張數(單位:枚)
$keiba_gendomaisuu = '100000';

##########################ver.1.21增加
#成員記錄的文件鎖方式(以0設置鎖，0不妥的情況要改為1)
$mem_lock_num = '0';


##########################ver.1.3增加
#戀人介紹個人資料記錄文件
$as_profile_file='./log_dir/as_pfofilelog.cgi';
#情侶記錄文件
$couple_file='./log_dir/couplelog.cgi';
#孩子記錄文件
$kodomo_file='./log_dir/kodomolog.cgi';
#選擇式個人資料項目
$news_file='./log_dir/mati_news.cgi';

#選擇式個人資料項目
$news_kensuu = '100';

#店放置於庫存的上限數
$mise_zaiko_limit = '30';

#郵件的保存件數
$mail_hozon_gandosuu = '50';

#特別風呂以幾倍的速度恢復
$tokubetu_times = '20';

#用特別風呂有關的費用(元)
$tokubetuburo_hiyou = '5000';

#是否使用戀愛系統(1=使用，0=不使用 ※0的心&孩子圖標變得不被出現。同時，0的情況「戀人介紹所」也請別在街設置)
$renai_system_on = '1';

#戀愛必要的LOVE參數的數值
$need_love = '200';

#准許同性的戀愛(不許可=0，准許=1)
$douseiai_per = '0';

#同時能與多少人交往(配偶+戀人)
$koibito_seigen = '5';

#對結婚必要的愛愛度(回憶值的共計)
$aijou_kijun = '500';

#對結婚必要的回憶值(回憶的最低值)
$omoide_kijun = '80';

#與戀人幾天不約會就分手
$wakare_limit_koibito = '7';

#與配偶幾天不約會就分手
$wakare_limit_haiguu = '14';

#對方是配偶的情況有孩子的概率(要是10則是10分之一的概率)
$kodomo_kakuritu1 = '10';

#對方是戀人的情況有孩子的概率(要是80則是80分之一的概率)
$kodomo_kakuritu2 = '80';

#育兒的間隔(單位:小時)
$kosodate_kankaku = '3';

#生孩子的參數1懸掛的費用(元)
$youikuhiyou = '1000';

#不給予孩子幾天吃飯會死
$kodomo_sibou_time = '7';

#孩子到幾歲生活(生活補貼被發送的期間)
$kodomo_sibou_time2 = '40';

#以下，在婚姻介紹所的變更可能的個人資料項目
#年齡的select
		@as_age_array=('','～14歳','15～18歳','19～22歳','23～26歳','27～30歳','31～34歳','35～38歳','39～42歳','43～46歳','47～50歳','51歳～');
		
#住所的select
		#@as_address_array=('','北海道','青森','岩手','宮城','秋田','山形','福島','群馬','栃木','茨城','埼玉','千葉','東京','神奈川','新潟','富山','石川','福井','山梨','長野','岐阜','静岡','愛知','三重','滋賀','京都','大阪','兵庫','奈良','和歌山','鳥取','島根','岡山','広島','山口','徳島','香川','愛媛','高知','福岡','佐賀','長崎','熊本','大分','宮崎','鹿児島','沖縄','海外');
		@as_address_array=
		('','海外','台北市', '台北縣', '基隆市', '宜蘭縣', '桃園縣', '新竹市', '新竹縣', '苗栗縣', 
		'台中市', '台中縣', '彰化縣', '南投縣', '嘉義市', '嘉義縣', '雲林縣', 
		'台南市', '台南縣', '高雄市', '高雄縣', '澎湖縣', '屏東縣', 
		'台東縣', '花蓮縣', '金門縣', '連江縣', '南海諸島',
		'澳門','山頂','中環','上環','金鐘','西環','石塘咀','筲箕灣',
		'北角','西灣河','側魚涌','柴灣','跑馬地','灣仔','銅鑼灣',
		'赤柱','半山','石澳','淺水灣','深水灣','香港仔','鴨利洲','薄扶林',
		'紅磡','尖沙咀','油麻地','何文田','旺角','太子','佐敦',
		'荃灣','青衣','葵涌','藍田','觀塘','九龍城','九龍塘','九龍灣',
		'土瓜灣','大角咀','深水步','長沙灣','荔枝角','石硤尾',
		'牛頭角','油塘','鯉魚門','樂富','鑽石山','黃大仙','慈雲山','新蒲崗','將軍澳',
		'上水','大埔','元朗','屯門','西貢','沙田','粉嶺','深井','天水圍','馬鞍山',
		'坪洲','長洲','大嶼山','赤臘角','南丫島','愉景灣','馬灣',
		'安徽','北京','福建','广东','广西','贵州','海南','河北','河南','黑龙江','湖北','湖南','吉林',
		'江苏','江西','辽宁','内蒙古','山东','山西','陕西','上海','四川','天津','云南','浙江','重庆',
		'甘肃','宁夏','青海','新疆','西藏');
		
#選擇式個人資料項目1
		$as_prof_name2='吸引點';
		@as_prof_array2=('','帥','聰明','個子高','體格健壯','男性化','有風度','富有','擁有車','單身生活','氣質','素直','認真','誠實','有趣','可愛','漂亮','擁有漂亮胸部','擁有漂亮雙腿','豐滿的身材','重視家庭','擅長體育','唱歌很好聽','擅長烹飪','淫蕩','壞人');

#選擇式個人資料項目2
		$as_prof_name3='住的街';
		@as_prof_array3=('','沒有家',"Main Street","She resort","County town","Downtown");

#選擇式個人資料項目3
		$as_prof_name4='想要的孩子的數目';
		@as_prof_array4=('','不想要孩子','一個就可以','2個左右','3個左右','想要4、5個','6個以上');

#選擇式個人資料項目4
		$as_prof_name5='對方的年齡是';
		@as_prof_array5=('','年齡不介意','與自己同樣','比較年長','年歲比較少','上了年紀的','很年輕的');

#選擇式個人資料項目5
		$as_prof_name6='對對方期望的是';
		@as_prof_array6=('','帥','聰明','個子高','體格健壯','具男人味','和善','富裕度','單身生活','氣質','坦率','認真','誠實','有趣','可愛','漂亮','胸的大小','雙腿漂亮','豐滿的身材','重視家庭','擅長體育','唱歌很好聽','擅長烹飪','淫蕩');

#是否在街下表示寒暄(表示=1，不表示=0)
$top_aisatu_hyouzi = '1';

#如果在上面要了，表示的表示件數
$top_aisatu_hyouzikensuu = '6';
#如果在上面要了，表示的名字的顏色
$top_aisatu_hyouzi_iro1 = '#333399';
#如果在上面要了，表示的內容的顏色
$top_aisatu_hyouzi_iro2 = '#333333';

#首頁街下自由表示html(EOM～EOM之間html記述)
$top_information =<< "EOM";

EOM

##########################ver.1.30增加
# 表示參加者(1=表示，0=不表示)
$sanka_hyouzi_kinou = '1';

# 如果在上面要了「表示」，表示位置(1=上，0=下)
$sanka_hyouzi_iti = '0';

#同時能進入的人數
$douzi_login_ninzuu = 100;

##########################ver.1.40增加
# 參加者文件(ver.1.30 是 "./log_dir/guestlog.cgi" 的指定變更)
$guestfile = "./guestlog.cgi";

#不遊戲到退出為止的時間(秒)
$logout_time = '1200';

#接受新登記(1=不接受，0=接受)
$new_touroku_per = '0';

#名字&密碼記錄文件
$pass_logfile = './log_dir/passlog.cgi';

#在自己和配偶的店不可以買商品(1=不可以買，0=可以買)
$kaenai_seigen = '1';

#------------------設定變更到這兒(以下如果有必要請變更)
#腳本的名字
$script='./town_maker.cgi';
#個人記錄數據文件
$logfile='./log_dir/memberlog.cgi';
#Ｃ聯賽記錄數據文件
$doukyo_logfile='./log_dir/doukyo_log.cgi';
#原創家list file
$ori_ie_list='./log_dir/ori_ie_log.cgi';
#主街參數記錄文件
$maintown_logfile='./log_dir/maintownlog.cgi';
#批發商品記錄文件
$orosi_logfile='./log_dir/orosilog.cgi';
#今天的食堂菜單記錄文件
$syokudou_logfile='./log_dir/syokudoulog.cgi';
#今天的百貨商店的商品齊全記錄文件
$depart_logfile='./log_dir/departlog.cgi';
#寒暄記錄記錄文件
$aisatu_logfile='./log_dir/aisatulog.cgi';
#街競賽log file
$maticon_logfile='./log_dir/maticonlog.cgi';
#街競賽有功的人log file
$kourousya_logfile='./log_dir/kourousyalog.cgi';
#炸面圈遊戲log file
$donuts_logfile='./log_dir/donutslog.cgi';
#賽馬log file
$keiba_logfile='./log_dir/keibalog.cgi';
#賽馬排列次序log file
$keibarank_logfile='./log_dir/keibaranklog.cgi';
#lockfile名
$lockfile = './lock/town.lock';
#賽馬lockfile名
$keibalockfile = './lock/keiba.lock';
#個人資料記錄文件
$profile_file='./log_dir/pfofilelog.cgi';

1;
