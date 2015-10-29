from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.00036459020734933635, 0.00033974076691130421, 0.00026783592050853405],
[0.0010674556771732876, 0.00097089514668502388, 0.000703287],
[0.0021038140826161872, 0.0018740490842830534, 0.0012730633582099026],
[0.0034670515841587132, 0.0030278993122563815, 0.0019463168204166556],
[0.0051572637426046050, 0.0044174684723897436, 0.0027013079235686357],
[0.0071781817111815178, 0.0060309751058536523, 0.0035214255119031352],
[0.0095358678330682550, 0.0078585152989432694, 0.0043934025765259817],
[0.012238036483345798, 0.0098913895714030833, 0.0053063572872843112],
[0.015293652399147442, 0.012121717189509195, 0.00625122],
[0.0187127, 0.014542197467037611, 0.0072203420520713839],
[0.022505856582320814, 0.017145953772975973, 0.0082072720834679772],
[0.026684653210628927, 0.019926427485625887, 0.0092065370009916103],
[0.031261080259928589, 0.022877303804072928, 0.010213520693309868],
[0.0362477, 0.0259925, 0.011224354434481774],
[0.041626840380765341, 0.029265921037653478, 0.012235833154700611],
[0.047061427992540074, 0.032691843835104359, 0.013245348009129994],
[0.0524939, 0.036264484835084959, 0.014250831072064879],
[0.057928245393932827, 0.039978191454814640, 0.0152507],
[0.063367596104295210, 0.043693166830909770, 0.016243865483544652],
[0.068814772933444318, 0.047332350368749755, 0.017229605408403171],
[0.074272134607711454, 0.050904763616958733, 0.018207628974914573],
[0.079741683235482613, 0.054412824618171617, 0.019178005631971914],
[0.085225113409716974, 0.057858699611546112, 0.020141152816484691],
[0.090723852623880691, 0.061244341698658576, 0.021097817166302883],
[0.096239094858769664, 0.064571522758530009, 0.022049058115529759],
[0.10177182873919732, 0.067841860017915590, 0.022996233594664125],
[0.10732286132758639, 0.071056838348371121, 0.023940987618687029],
[0.11289283837780889, 0.074217829115975520, 0.024885239592500472],
[0.118482, 0.077326106226943247, 0.025831175198715653],
[0.12409150408212580, 0.080382859874972706, 0.026781238760311372],
[0.12972082235058827, 0.083389208391693420, 0.027738126992076773],
[0.13537, 0.0863462, 0.028704784071430088],
[0.14104020009788046, 0.0892549, 0.029684397972227133],
[0.14673028806209762, 0.092116135298619645, 0.030680398015335113],
[0.15244052526938118, 0.094930942755365039, 0.031696453597658353],
[0.158171, 0.097700176481724160, 0.032736474067411363],
[0.16392066661655139, 0.10042469991652406, 0.033804609718113929],
[0.16969002190067425, 0.10310535507053978, 0.034905253877287240],
[0.17547843894325624, 0.10574296689445062, 0.036043046068385737],
[0.181286, 0.10833834721667163, 0.037222876226263295],
[0.18711076798630824, 0.11089229830850983, 0.038449889947573999],
[0.19295372057420568, 0.113406, 0.039729494758042737],
[0.19881382275103388, 0.115879, 0.0410543],
[0.20469049496955183, 0.11831352167605044, 0.042407350045159893],
[0.21058312266817364, 0.12070969515580290, 0.043800638263727772],
[0.21649105860869366, 0.123068, 0.045237676886084023],
[0.22241362499722495, 0.12539047535957665, 0.046721886637503672],
[0.22835, 0.12767669877039126, 0.048256581633043479],
[0.23429979654909428, 0.12992790444304353, 0.049844963464817309],
[0.24026190982967660, 0.13214492675890743, 0.051490115892434442],
[0.24623567284087344, 0.13432861352402428, 0.053195],
[0.25222, 0.13647982747726212, 0.054962451635751426],
[0.25821490710195882, 0.13859944770571672, 0.056795176018375811],
[0.26421870574937806, 0.14068837097418413, 0.058695748187215603],
[0.27023081104155405, 0.14274751297432164, 0.060666610676888118],
[0.27625, 0.14477780949801627, 0.062710073590284882],
[0.28227638890815598, 0.14678021753851253, 0.064828315312404100],
[0.28830804245260472, 0.14875571632197423, 0.067023384060828833],
[0.29434436608496589, 0.15070530827136436, 0.069297200204096049],
[0.30038441086617984, 0.15263001990380975, 0.071651559264566511],
[0.30642721324578026, 0.15453090266196806, 0.0740881],
[0.31247179563259875, 0.15640903367932407, 0.076608486040397550],
[0.31851716692600107, 0.15826551647880391, 0.079214055237740694],
[0.32456232301225685, 0.160101, 0.081906179515138289],
[0.33060624723031767, 0.16191808717869838, 0.084686092216983144],
[0.33664791081099971, 0.163717, 0.087554928596152548],
[0.34268627329328644, 0.16549799295635592, 0.090513730766324851],
[0.34872028292124924, 0.16726375135936566, 0.093563452545952580],
[0.354749, 0.16901506721542892, 0.096704964118858566],
[0.360771, 0.17075324239960771, 0.099939056446814389],
[0.36678551560500927, 0.17247960815035304, 0.10326644538014529],
[0.37279138343324580, 0.17419552507417735, 0.10668777542305191],
[0.37878748313637523, 0.17590238305776129, 0.110204],
[0.38477270282875481, 0.17760160108387191, 0.11381450004434981],
[0.39074592181853490, 0.179295, 0.11752085536155507],
[0.39670601095328267, 0.18098293686825845, 0.12132307798302880],
[0.40265183297005974, 0.18266803499662407, 0.12522149828941428],
[0.40858224285198924, 0.18435145280884044, 0.129216],
[0.41449608819327582, 0.18603474838914211, 0.13330796830369360],
[0.420392, 0.18771950559529427, 0.13749639594729984],
[0.42626944095044517, 0.18940733310522559, 0.14178177783815388],
[0.43212661005081504, 0.19109986334246629, 0.14616416364799500],
[0.43796253879783670, 0.19279875127859722, 0.15064354676546088],
[0.44377604374003832, 0.194506, 0.15521986351689371],
[0.44956593650515703, 0.19622232481782670, 0.15989299212732994],
[0.45533102427322164, 0.19795042058189327, 0.164663],
[0.46107011027133177, 0.19969169109742735, 0.16952889949426492],
[0.46678199429154160, 0.20144788174729744, 0.174491],
[0.47246547323321181, 0.20322075066066003, 0.17954907952993585],
[0.47811934167115172, 0.20501206665090355, 0.18470230779004126],
[0.48374239245082867, 0.206824, 0.18995031339383636],
[0.48933341731187224, 0.20865715535702450, 0.19529252291013172],
[0.49489120754107735, 0.21051449896499363, 0.20072829053065039],
[0.50041455465604823, 0.21239742653985039, 0.20625689594465307],
[0.50590225112059506, 0.214308, 0.21187754222050165],
[0.51135309109295646, 0.21624717927543574, 0.217589],
[0.51676587120785899, 0.21821756464841768, 0.22339137404152026],
[0.52213939139340349, 0.22022064882639913, 0.22928256408795961],
[0.52747245572370005, 0.22225818660246804, 0.23526180015262604],
[0.53276387330813602, 0.22433191740590475, 0.241328],
[0.53801245921809993, 0.22644356232262952, 0.24747948205716030],
[0.54321703545193822, 0.22859482108671531, 0.253715],
[0.54837643193884955, 0.23078736905439612, 0.26003367426595425],
[0.55348948758236294, 0.23302285417227558, 0.26643320768962925],
[0.55855505134397310, 0.23530289395161658, 0.27291217904459547],
[0.56357198336743741, 0.23762907246067511, 0.27946883108327047],
[0.56853915614413841, 0.24000293734702055, 0.28610131220317941],
[0.57345545571985201, 0.24242599690165856, 0.292808],
[0.57831978294314645, 0.24489971717656273, 0.29958588166435263],
[0.58313105475553095, 0.24742551916689748, 0.30643379309947166],
[0.587888, 0.250005, 0.31334918032253212],
[0.59259018841153233, 0.25263881062322069, 0.32032971960325701],
[0.59723597679826101, 0.25532889255537056, 0.32737299447901114],
[0.60182456573135357, 0.25807623611947234, 0.33447649694129822],
[0.60635497342464850, 0.26088199775687904, 0.34163762889990956],
[0.61082624279440456, 0.26374727387568009, 0.34885370392835158],
[0.61523744303461470, 0.26667309875876749, 0.35612194929307595],
[0.61958767123021885, 0.26966044260669519, 0.36343950826790428],
[0.62387605400697377, 0.27271020972087007, 0.37080344273386928],
[0.62810174921652173, 0.275823, 0.37821073606350297],
[0.63226394765501159, 0.279, 0.38565829628738713],
[0.63636187481336948, 0.28224207112897154, 0.39314295953953710],
[0.64039479265710320, 0.28554920098319708, 0.40066149377693872],
[0.64436200143326516, 0.28892223389682942, 0.40821060276728871],
[0.64826284150196101, 0.29236164898999068, 0.41578693033772324],
[0.65209669518952185, 0.29586785100426827, 0.42338706487604200],
[0.65586298866018034, 0.299441, 0.43100754407467923],
[0.65956119380285516, 0.30308185953599265, 0.43864485990642937],
[0.66319083012932467, 0.30679009919829581, 0.44629546381970492],
[0.666751, 0.310566, 0.45395577213992772],
[0.67024272393185891, 0.31440956431599459, 0.46162217166249681],
[0.673664, 0.31832076882411170, 0.46929102542168183],
[0.67701585107499307, 0.32229948183898088, 0.476959],
[0.68029723623817906, 0.32634550532442319, 0.48462146469163397],
[0.68350827641050693, 0.330459, 0.49227571150763921],
[0.68664887766600491, 0.33463832234278068, 0.49991774765968783],
[0.68971900876258252, 0.33888435310899612, 0.50754390884608669],
[0.69271870293117332, 0.34319617082352993, 0.51515054431300678],
[0.69564805962449494, 0.34757321678313863, 0.52273402333840646],
[0.69850724621893345, 0.35201486364060736, 0.53029074173569679],
[0.70129649966287688, 0.35652041687612446, 0.53781712835512929],
[0.70401612806467151, 0.36108911639359748, 0.54530965156071043],
[0.70666651221322929, 0.36572013823797295, 0.55276482566036211],
[0.70924810702420371, 0.37041259642940810, 0.56017921726711750],
[0.71176144290457533, 0.37516554490990128, 0.56754945156929915],
[0.71420712702841926, 0.379978, 0.57487221848794234],
[0.71658584451659746, 0.38484884054487833, 0.58214427870014718],
[0.71889835951314485, 0.389777, 0.58936246950758164],
[0.72114551615111133, 0.39476133571632044, 0.59652371053002551],
[0.72332823940072721, 0.39980059146492308, 0.60362500920462436],
[0.725448, 0.40489352147009816, 0.61066346607239819],
[0.72750449401065942, 0.41003882203792019, 0.61763627983454750],
[0.72950028534321842, 0.41523514840500281, 0.62454075216217775],
[0.731436, 0.42048111745611844, 0.63137429224422559],
[0.73331346723676749, 0.42577531049569550, 0.63813442105963880],
[0.73513361541817412, 0.43111627606592162, 0.644819],
[0.73689811179180087, 0.43650253280396734, 0.65142511135947356],
[0.73860854218787631, 0.44193257233069094, 0.65795130809783375],
[0.74026657450782596, 0.44740486216304604, 0.66439537050890063],
[0.74187395804096046, 0.45291784864228929, 0.670755],
[0.74343252259880166, 0.45846995987005162, 0.67702975758934802],
[0.74494417746331421, 0.46405960864428703, 0.68321674450589809],
[0.74641091014578143, 0.46968519538713144, 0.68931492538967831],
[0.747835, 0.47534511105676630, 0.69532296895266044],
[0.749218, 0.48103774003547145, 0.70123968118433566],
[0.75056259219482169, 0.48676146298619699, 0.70706400607631004],
[0.75187102159617858, 0.49251465967015379, 0.71279502601628986],
[0.75314558282127064, 0.49829571171816250, 0.718432],
[0.75438869581804913, 0.50410300534873809, 0.72397417266166075],
[0.75560284461788563, 0.50993493402618673, 0.72942115514715022],
[0.75679057453120990, 0.51578990105233413, 0.73477254281057280],
[0.75795448915137476, 0.52166632208584918, 0.74002810477174130],
[0.75909724716995075, 0.52756262758349903, 0.74518774432849588],
[0.76022155900735655, 0.533477, 0.75025149724099360],
[0.76133018326363111, 0.53940870184858458, 0.75521952975667117],
[0.762426, 0.545355, 0.76009213638897766],
[0.76351162182163323, 0.55131595083025964, 0.76486973746359077],
[0.76459015987681655, 0.55728881344073400, 0.76955287644638371],
[0.76566444960053470, 0.563273, 0.77414221706782216],
[0.76673743139141581, 0.56926584435935501, 0.77863854025885104],
[0.76781206912374111, 0.57526723336153329, 0.78304274091356907],
[0.76889134554109828, 0.58127540505302033, 0.78735582449415686],
[0.76997825753794336, 0.58728905180470026, 0.79157890349362081],
[0.771076, 0.59330690131502284, 0.79571319377189975],
[0.77218701760552522, 0.59932771783730321, 0.79976001078081527],
[0.77331488643413526, 0.60535030329690998, 0.80372076569318662],
[0.77446242234281493, 0.61137349829905285, 0.80759696145122328],
[0.77563261917914739, 0.61739618302826416, 0.81139018874900670],
[0.77682845501464537, 0.62341727804104730, 0.81510212196354825],
[0.77805288702554520, 0.62943574495349586, 0.81873451504851247],
[0.77930884637916031, 0.63545058702605028, 0.82228919740423701],
[0.78059923314314073, 0.64146084964779704, 0.82576806973722794],
[0.78192691123519298, 0.647466, 0.82917309992176391],
[0.78329470343114949, 0.65346403096316685, 0.83250631887571191],
[0.784705, 0.65945525408677219, 0.83576981646208581],
[0.78616168612912185, 0.66543850693179041, 0.83896573742727898],
[0.78766627272203815, 0.67141304948281555, 0.84209627738631898],
[0.78922175631228519, 0.67737818481752832, 0.84516367886487209],
[0.79083068238484811, 0.683333, 0.84817022740711401],
[0.79249552755757224, 0.68927766075661900, 0.85111824775799627],
[0.79421869549362645, 0.69521082144317259, 0.85401010012781309],
[0.796003, 0.70113221446622909, 0.85684817654641421],
[0.79784922639570755, 0.70704135500380128, 0.85963489731382636],
[0.79976099795634681, 0.71293779952484804, 0.86237270755351625],
[0.80173990279257801, 0.718821, 0.865064],
[0.80378792582883762, 0.72469102974271993, 0.86771148114400931],
[0.80590695909925691, 0.730547, 0.87031742938606305],
[0.80809879930031037, 0.73638916214456229, 0.87288443079269196],
[0.81036514561708983, 0.742217, 0.875415],
[0.812708, 0.74803007708228697, 0.87791168570839539],
[0.81512765469540616, 0.75382858061772184, 0.88037699939535163],
[0.81762671263294262, 0.75961225598357362, 0.88281348155449746],
[0.82020606466845825, 0.76538100331667214, 0.88522366503315819],
[0.82286689968229731, 0.77113475722462321, 0.88761007973008599],
[0.82561030192878737, 0.77687348596181460, 0.88997525057036131],
[0.82843725083201014, 0.78259719059369348, 0.89232169563025687],
[0.83134862104938911, 0.78830590415253798, 0.89465192441570118],
[0.83434518279437830, 0.794, 0.89696843629838729],
[0.83742760240767533, 0.79967864491416218, 0.89927371911415877],
[0.84059644316473958, 0.805343, 0.90157024792909257],
[0.84385216630564053, 0.810993, 0.90386048397969687],
[0.84719513227154886, 0.81662789250955425, 0.90614687379492209],
[0.85062560213054261, 0.82224903633991686, 0.90843184850932246],
[0.85414373917366904, 0.82785624408855507, 0.91071782337872320],
[0.85774961066045052, 0.83344977409653087, 0.91300719751231107],
[0.86144318969121947, 0.83902990917775167, 0.91530235383824654],
[0.86522435718169355, 0.84459695584889061, 0.91760565932392624],
[0.86909290391300398, 0.85015124358192873, 0.91991946547704428],
[0.873049, 0.85569312408227871, 0.92224610916001803],
[0.87709086014119886, 0.86122297059563424, 0.92458791375844718],
[0.88121941942790338, 0.86674117724695776, 0.92694719075471910],
[0.88543366165016701, 0.87224815841536774, 0.92932624177133638],
[0.889733, 0.87774434814915114, 0.931727],
[0.894117, 0.88323019962575944, 0.93415283928440906],
[0.89858380946155825, 0.88870618466245743, 0.936605],
[0.90313372211215748, 0.89417279328434540, 0.93908603825533732],
[0.90776540642354042, 0.89963053335793641, 0.94159836123488638],
[0.91247785483542621, 0.90507993030027956, 0.94414426115282102],
[0.91726998526060721, 0.91052152687616172, 0.94672609241017713],
[0.92214063989081030, 0.91595588309928500, 0.94934625030520092],
[0.92708858286925577, 0.92138357625787959, 0.95200718657810712],
[0.93211249645470551, 0.92680520109160325, 0.95471142945778042],
[0.93721097514299945, 0.93222137015548723, 0.95746160990682416],
[0.94238251696399722, 0.93763271441946827, 0.96026049660420021],
[0.94762551077149160, 0.94303988417068274, 0.96311104358049515],
[0.95293821767310905, 0.94844355031354144, 0.96601645675435044],
[0.95831874357262759, 0.953844, 0.96898028975914963],
[0.96376499762713397, 0.95924317023047012, 0.97200658720362087],
[0.96927462714142376, 0.96464058942902497, 0.97510010902170741],
[0.97484491025989362, 0.97003744466065911, 0.97826670326333798],
[0.98047256600382238, 0.97543455807993829, 0.98151397613224878],
[0.98615338119070584, 0.98083280406706630, 0.98485263580270777],
[0.99188134952053841, 0.98623312458048440, 0.98829967505462724],
[0.99764601872660819, 0.99163654075644503, 0.99188849142401769],
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
