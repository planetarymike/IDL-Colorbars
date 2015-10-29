from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.00038332241086516379, 0.00032198036060381686, 0.00036712997198830208],
[0.0011391944622792724, 0.00090328172650383672, 0.00107872],
[0.0022680552031778410, 0.0017198415324112765, 0.0021252895039000929],
[0.0037671510753686335, 0.0027469296019523473, 0.0034932175926621649],
[0.0056395818443054132, 0.0039669317857653642, 0.0051736600449242805],
[0.0078915, 0.00536599, 0.0071597775057893444],
[0.010530929222759120, 0.0069325375988034468, 0.0094456155078230571],
[0.013567221821681109, 0.0086565890384478605, 0.012025543584416194],
[0.017010667768185647, 0.010529265326696045, 0.014893938746946103],
[0.020872298290337168, 0.012542540820496158, 0.018044991698896437],
[0.025163728978907490, 0.014689058943016317, 0.021472581428222691],
[0.029897047885569607, 0.016962008150509220, 0.025170191105652526],
[0.035084728761428048, 0.019355034117683367, 0.029130850680227978],
[0.040734077010536350, 0.021862176219773270, 0.033347097784194979],
[0.0464963, 0.0244778, 0.037810951885506920],
[0.052246759471913658, 0.027196666984946063, 0.042449803340818319],
[0.057989460201497693, 0.030013700052393705, 0.047010828741949805],
[0.063727880812105842, 0.032924173031393104, 0.051489023065712618],
[0.069464914806524863, 0.035923592016398963, 0.055885763052186434],
[0.075202993590940903, 0.039007705791232292, 0.060202026717794739],
[0.080944156548265755, 0.042122972617492822, 0.064438463723820422],
[0.086690107234693614, 0.045166586743299132, 0.0685955],
[0.092442258989516718, 0.048150646303762708, 0.072673144920417126],
[0.098201772360294232, 0.0510779, 0.076671508212682066],
[0.10396958612375234, 0.053950848508433923, 0.080590353642000345],
[0.10974644324008573, 0.0567719, 0.084429365480058416],
[0.115533, 0.059543457268237294, 0.088188123927978673],
[0.12132940845532200, 0.062267546535594708, 0.091866125193379639],
[0.12713620481821827, 0.064946295168278961, 0.095462798960565282],
[0.132953, 0.067581706545463527, 0.098977523712594578],
[0.13878118205219062, 0.070175720032716188, 0.10240964026616703],
[0.14461933096432089, 0.072730221366132081, 0.10575846380534223],
[0.15046773637240435, 0.075247051578023694, 0.10902329464219421],
[0.156326, 0.077728014683340840, 0.11220342788738233],
[0.16219425136490573, 0.080174884306117217, 0.11529816217819849],
[0.16807163915602943, 0.082589409393540092, 0.118307],
[0.17395785224128782, 0.084973319139863029, 0.12122869278400111],
[0.17985236739101956, 0.087328327221936841, 0.12406317160405694],
[0.18575460559574428, 0.089656135431535500, 0.12680962896596282],
[0.19166393644027974, 0.091958436776129360, 0.12946748631489535],
[0.19757968210189802, 0.094236918108646872, 0.13203620656250709],
[0.20350112101757595, 0.096493262337605828, 0.13451529858513728],
[0.20942749125864146, 0.098729150261409548, 0.13690432130786953],
[0.21535799364553121, 0.10094626206427182, 0.13920288740062445],
[0.22129179463069887, 0.10314627850596744, 0.14141066660854818],
[0.22722802897383926, 0.10533088183316719, 0.143527],
[0.23316580223030903, 0.107502, 0.14555284629949508],
[0.23910419307088193, 0.10966058927358321, 0.14748689686802613],
[0.24504225544866498, 0.11180907007832736, 0.14932946509759837],
[0.25097902062700506, 0.11394889136920514, 0.15108054447822716],
[0.25691349908058386, 0.11608174827407228, 0.15274019880073536],
[0.26284468228043806, 0.11820933818217996, 0.15430856335512574],
[0.26877154437244566, 0.12033336023543351, 0.155786],
[0.27469304375776665, 0.12245551466913376, 0.15717232720629276],
[0.28060812458283119, 0.12457750201169165, 0.15846836180518772],
[0.28651571814569216, 0.12670102215214016, 0.15967437791684080],
[0.29241474422489128, 0.12882777328376571, 0.16079087760335278],
[0.29830411233640647, 0.13095945073181509, 0.16181843653637937],
[0.30418272292374488, 0.13309774567299260, 0.16275770359675351],
[0.31004946848579601, 0.13524434375433936, 0.16360940028769733],
[0.31590323464668962, 0.13740092361903938, 0.16437431997316104],
[0.32174290117154491, 0.13956915534674577, 0.16505332695330041],
[0.32756734293171219, 0.141751, 0.16564735538961473],
[0.33337543082283894, 0.14394720199756528, 0.16615740809279975],
[0.33916603263885858, 0.14616, 0.166585],
[0.344938, 0.14839160916766864, 0.16692993266413211],
[0.35069023867104210, 0.15064273337367481, 0.16719474084459923],
[0.35642157027182064, 0.152915, 0.16738024275720781],
[0.36213087204991867, 0.15521073186128373, 0.16748776245686228],
[0.367817, 0.15753070489153970, 0.16751868329513231],
[0.373479, 0.15987668573505639, 0.16747444616149587],
[0.379115, 0.16225016001602022, 0.16735654771313699],
[0.38472508613072454, 0.16465258434784660, 0.16716653861193490],
[0.39030723621023467, 0.16708538440810605, 0.16690602178798439],
[0.39586057361401977, 0.16954995304349518, 0.16657665074970679],
[0.40138397966975642, 0.17204764841433862, 0.16618012796135759],
[0.40687634055414573, 0.17457979218792130, 0.16571820330950299],
[0.41233654780583240, 0.17714766778965527, 0.16519267268083354],
[0.41776349882340996, 0.17975251872072492, 0.16460537667448988],
[0.42315609735005288, 0.18239554695041452, 0.16395819947292348],
[0.42851325394629980, 0.18507791139079016, 0.16325306789616342],
[0.43383388645248211, 0.187801, 0.16249195066523867],
[0.43911692044227946, 0.19056506074637847, 0.16167685790137901],
[0.44436128966887201, 0.19337193576177125, 0.16081],
[0.44956593650515703, 0.19622232481782670, 0.159893],
[0.45472981237949311, 0.19911715200056968, 0.15892844571036591],
[0.45985187820844470, 0.20205729126382083, 0.15791837804760328],
[0.46493110482799521, 0.20504356563813470, 0.15686500897365521],
[0.46996647342473136, 0.208077, 0.15577060326742059],
[0.47495697596848513, 0.21115755330533659, 0.15463747261580690],
[0.47990161564797423, 0.21428665257712726, 0.15346797805313689],
[0.48479940731096233, 0.21746465816283672, 0.15226453290765909],
[0.48964937791052571, 0.22069213074319116, 0.15102960628597095],
[0.49445056695899830, 0.22396957779976157, 0.14976572712503000],
[0.49920202699122290, 0.22729745363477821, 0.14847548883965112],
[0.50390282403875075, 0.23067615949690967, 0.14716155459080199],
[0.508552, 0.23410604380853867, 0.14582666319643964],
[0.51314876372467133, 0.23758740248954641, 0.14447363570186669],
[0.51769211036438156, 0.24112047937218811, 0.14310538262038666],
[0.522181, 0.24470546670125187, 0.14172491184712152],
[0.52661518298399990, 0.24834250571341532, 0.14033533723892858],
[0.53099320789101667, 0.25203168728947656, 0.13893988784106823],
[0.53531445285915302, 0.255773, 0.13754191772627519],
[0.53957811084324647, 0.25956659424874406, 0.13614491639379847],
[0.54378339334035419, 0.263412, 0.13475251965441806],
[0.54792953106988285, 0.26731, 0.13336852090205745],
[0.55201577468446594, 0.27125948488404733, 0.13199688264309239],
[0.55604139551350185, 0.275261, 0.13064174812058699],
[0.56000568634126502, 0.27931336686674835, 0.12930745283237627],
[0.56390796222147954, 0.28341717974753616, 0.12799853569931818],
[0.56774756133026749, 0.28757182243539103, 0.12671974959354093],
[0.57152384585933969, 0.291777, 0.125476],
[0.57523620295127687, 0.29603209543493486, 0.12427270762861903],
[0.57888404567873630, 0.30033687538100473, 0.12311510590905411],
[0.58246681406934331, 0.30469078648174153, 0.12200895391889374],
[0.58598397617800924, 0.30909330875781771, 0.12096018316849413],
[0.58943502920832347, 0.31354388616282647, 0.11997496630010054],
[0.59282, 0.31804192759564426, 0.11905971090660428],
[0.59613694967621600, 0.32258680789862337, 0.11822104877233486],
[0.59938696807520864, 0.32717786883955574, 0.11746581997903530],
[0.60256918192914755, 0.33181442007575884, 0.11680105137967217],
[0.60568325282970537, 0.33649574009901961, 0.11623392903932359],
[0.60872887935837461, 0.34122107716051853, 0.11577176438001233],
[0.61170579859002661, 0.34598965017521244, 0.11542195394687016],
[0.614614, 0.35080064960551743, 0.11519193293514835],
[0.61745266536014876, 0.35565323832446366, 0.11508912287634712],
[0.62022229386915373, 0.360547, 0.11512087416748906],
[0.62292258044196502, 0.36547970221284048, 0.11529440442611505],
[0.62555347923321192, 0.370452, 0.11561673394630653],
[0.62811499314891617, 0.37546182460218752, 0.11609461979601071],
[0.63060717576064307, 0.38050889520201170, 0.116734],
[0.63303, 0.38559199888395362, 0.11754238186894023],
[0.63538402656262871, 0.39071012801207405, 0.11852387991324562],
[0.63766907322733080, 0.39586225364304967, 0.11968406605612794],
[0.639886, 0.40104732625794015, 0.12102747301934053],
[0.64203379361756696, 0.406264, 0.12255804881478216],
[0.64411420562474975, 0.41151201584579084, 0.12427913124139650],
[0.64612725204896482, 0.41678943743804919, 0.12619343333276167],
[0.64807346698453483, 0.422095, 0.12830303992687347],
[0.64995345465708421, 0.42742881215653983, 0.13060941506566462],
[0.65176789177028827, 0.43278846610033245, 0.133113],
[0.65351752987016454, 0.43817320541234300, 0.13581533721992212],
[0.65520319771970337, 0.44358184229733416, 0.13871490960391331],
[0.65682580367584598, 0.44901317507593735, 0.14181137567693125],
[0.65838633806004376, 0.45446598898966767, 0.14510351677362521],
[0.65988587551280009, 0.45993905702809573, 0.14858970399202931],
[0.66132557732175823, 0.465431, 0.15226794686745840],
[0.66270669371197977, 0.47094099131565365, 0.15613594185877611],
[0.66403056608618827, 0.47646735008824598, 0.16019111943322903],
[0.66529862920177241, 0.48200894988033843, 0.16443068875733422],
[0.66651241327042454, 0.48756451577354182, 0.16885167923097472],
[0.66767354596531625, 0.49313276615745499, 0.17345097832534948],
[0.66878375431971260, 0.49871241377471570, 0.17822536539169792],
[0.66984486649999619, 0.50430216680419870, 0.18317154128930613],
[0.67085881343508746, 0.50990072998353597, 0.18828615383409528],
[0.67182763028330905, 0.51550680577186170, 0.19356581919168270],
[0.672753, 0.521119, 0.19900713943211201],
[0.67363854300303760, 0.52673630088272660, 0.20460671652971685],
[0.67448524086113193, 0.53235712477051966, 0.21036116313420511],
[0.67529601407200090, 0.53798027301186502, 0.21626711046172248],
[0.67607343381820151, 0.543604, 0.22232121366125956],
[0.67682017973082664, 0.54922838790720530, 0.22852015500587136],
[0.67753903961943995, 0.55485079258804770, 0.23486064524318639],
[0.67823290886106002, 0.56047040060917375, 0.24133942341831027],
[0.67890478942416410, 0.56608595299851083, 0.24795325545690056],
[0.67955778850380966, 0.57169620235518181, 0.254699],
[0.680195, 0.57729991443675299, 0.261573],
[0.68082008602702682, 0.58289586977565444, 0.268573],
[0.68143610680003930, 0.58848286532187266, 0.27569522807147828],
[0.68204668493114773, 0.59405971610871022, 0.28293655506563753],
[0.68265541806286423, 0.59962525693811519, 0.29029392020758515],
[0.68326599145344313, 0.60517834408181081, 0.297764],
[0.683882, 0.61071785699416870, 0.30534419363824256],
[0.68450780945117562, 0.61624270003253978, 0.31303080355262525],
[0.68514681774086916, 0.62175180418049059, 0.32082084714554804],
[0.68580318153590147, 0.62724412876919145, 0.32871114563433124],
[0.68648094289693762, 0.63271866319199577, 0.33669850252017547],
[0.68718419511419326, 0.63817442860706386, 0.34477970088408977],
[0.68791707470503172, 0.64361047962275231, 0.35295150107695677],
[0.68868375287392825, 0.64902590596032694, 0.36121063881722903],
[0.68948842645191588, 0.65441983408848869, 0.36955382370392181],
[0.69033530833826107, 0.65979142882411201, 0.37797773814757685],
[0.69122861747290965, 0.66513989489354497, 0.38647903671767186],
[0.69217256837410157, 0.67046447844883961, 0.39505434590137267],
[0.69317136028167081, 0.67576446853325745, 0.40370026426551298],
[0.69422916595243034, 0.68103919849049188, 0.41241336301113574],
[0.69535012016003850, 0.68628804731211024, 0.42119018690778270],
[0.69653830795735072, 0.69151044091784641, 0.43002725559290678],
[0.69779775276466716, 0.69670585336354307, 0.43892106522024649],
[0.69913240435226010, 0.701874, 0.44786809043974724],
[0.70054612678988870, 0.70701387837988994, 0.45686478669050662],
[0.70204268643986489, 0.71212568950236921, 0.46590759278736321],
[0.70362574007315093, 0.71720891840084111, 0.47499293378100232],
[0.70529882319020576, 0.72226329506023101, 0.48411722407085206],
[0.70706533862941334, 0.72728860306603271, 0.49327687074958554],
[0.70892854554622209, 0.732285, 0.50246827715767028],
[0.71089154884519490, 0.73725141881115430, 0.51168784662615774],
[0.71295728914522127, 0.74218876638049180, 0.520932],
[0.71512853335506266, 0.74709672557622231, 0.530197],
[0.71740786593221839, 0.75197535449934327, 0.53947964964074668],
[0.71979768089282259, 0.75682476669785148, 0.54877604416383141],
[0.72230017463400042, 0.76164513108938214, 0.55808275966288290],
[0.72491733962293514, 0.76643667177231389, 0.56739628578023316],
[0.72765095899881171, 0.7712, 0.57671314177322575],
[0.73050260212508999, 0.77593445240074343, 0.58602988097518738],
[0.73347362112021797, 0.78064141320069758, 0.59534309525057882],
[0.73656514838519316, 0.78532099085937301, 0.60464941942434658],
[0.739778, 0.78997367871302271, 0.61394553566606413],
[0.74311315094171249, 0.79460002187367207, 0.623228],
[0.74657078424929058, 0.79920061630613592, 0.63249413559324907],
[0.75015124388578758, 0.80377610781329500, 0.64174025879358521],
[0.75385456149500396, 0.80832719093454486, 0.65096346125174953],
[0.75768055487626840, 0.81285460776281082, 0.66016072476074483],
[0.76162883217502131, 0.817359, 0.66932910280780744],
[0.76569879687025710, 0.82184164105999003, 0.67846572415434914],
[0.76988965349689731, 0.82630296781824575, 0.68756779624028208],
[0.77420041403539275, 0.83074404602876051, 0.696633],
[0.77862990489597084, 0.83516583540325540, 0.70565753487702854],
[0.78317677442107780, 0.83956933476917073, 0.71464003762854356],
[0.78783950082633336, 0.84395558051311082, 0.72357766890462449],
[0.79261640049819382, 0.84832564500574015, 0.73246807359635502],
[0.79750563656484374, 0.85268063501880642, 0.74130899134033534],
[0.80250522765598298, 0.85702169014577578, 0.75009825837093125],
[0.80761305676673167, 0.86134998123851969, 0.75883380911065468],
[0.81282688014063997, 0.86566670887364683, 0.76751367748899968],
[0.81814433608687986, 0.869973, 0.77613599797955834],
[0.82356295364636301, 0.87427041582761855, 0.784699],
[0.82908, 0.87855993184570536, 0.79320104007247538],
[0.83469329367883949, 0.882843, 0.80164053849931227],
[0.84039960204485697, 0.88712081430051370, 0.81001604258686988],
[0.84619625868326331, 0.89139485962444820, 0.81832619434482412],
[0.85208, 0.89566646302951736, 0.82656973586336979],
[0.85804895643725110, 0.89993701715733609, 0.83474550792228941],
[0.86409900877955181, 0.90420793517230458, 0.84285244812933424],
[0.87022744084092163, 0.90848065083401597, 0.85088958852608931],
[0.87643111792978434, 0.91275661899238814, 0.85885605257878406],
[0.88270685311504016, 0.91703731660859678, 0.86675105144274622],
[0.88905140691524454, 0.92132424443699335, 0.87457387934861064],
[0.89546148489242838, 0.92561892954852754, 0.88232390790048110],
[0.90193373262700693, 0.929923, 0.89000057899210860],
[0.90846472734980699, 0.93423783457803899, 0.89760339592271132],
[0.91505096520639562, 0.93856528033572917, 0.90513191210590216],
[0.92168884266605233, 0.94290695156403059, 0.912586],
[0.92837462985744645, 0.94726459830104404, 0.91996441421174435],
[0.93510443242182795, 0.95164005374860683, 0.92726760069915959],
[0.94187413645837670, 0.95603526056096977, 0.93449482520861782],
[0.94867932756703410, 0.96045230917939761, 0.94164553858260613],
[0.95551516832726391, 0.96489349558454129, 0.94871901465773478],
[0.96237620525316692, 0.96936141210451565, 0.95571422625453273],
[0.96925604746468708, 0.97385909849846197, 0.96262963691088477],
[0.97614678991246195, 0.97839031329192461, 0.96946282162247999],
[0.98303786060227927, 0.98296007670076013, 0.97620969461952345],
[0.98991330399527822, 0.98757595201905180, 0.98286264930773026],
[0.99674319710202142, 0.99225210205500380, 0.989405],
[1, 0.99704378266210936, 0.99575555752072120]]

test_cm = LinearSegmentedColormap.from_list(__file__, cm_data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from pycam02ucs.cm.viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("pycam02ucs not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()
