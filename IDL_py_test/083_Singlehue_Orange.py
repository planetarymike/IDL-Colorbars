from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000208612309326197836, 0.0000200048714121613121, 0.0000198463295491030259],
[0.000395637927942037344, 0.000338432976515453678, 0.000302323080034115632],
[0.00116029935264347524, 0.000962008430255189423, 0.000833348358704904244],
[0.00228356196844970187, 0.00185165235714120123, 0.00156836269461679552],
[0.00375250114382007227, 0.00298693957488613488, 0.00248213864144227131],
[0.00556045525903135426, 0.00435439573603834361, 0.00355709366074524530],
[0.00770389030261813684, 0.00594419910167536762, 0.00477979024208387889],
[0.0101811168339311399, 0.00774876785327843504, 0.00613939200085427024],
[0.0129916478082246819, 0.00976202640039296882, 0.00762684393693472892],
[0.0161358355442999500, 0.0119789769178691996, 0.00923438497655160173],
[0.0196146487408156607, 0.0143954282444623723, 0.0109552347226512734],
[0.0234295269588598240, 0.0170078139807886899, 0.0127833803854271871],
[0.0275822811564042994, 0.0198130648229635289, 0.0147134254024304158],
[0.0320750231671824981, 0.0228085157100823936, 0.0167404781103681795],
[0.0369101141984315567, 0.0259918363068625778, 0.0188600675420928475],
[0.0420438849503761356, 0.0293609776910315999, 0.0210680782400134645],
[0.0471637942864339618, 0.0329141306310652415, 0.0233606987908903906],
[0.0522409325836536223, 0.0366496923639130570, 0.0257343805060237414],
[0.0572795234463901945, 0.0405641627713434968, 0.0281858037616723629],
[0.0622832603356757233, 0.0444724245912212282, 0.0307118502294914872],
[0.0672553974341604521, 0.0483340223679732325, 0.0333095797086629050],
[0.0721988212773838900, 0.0521521222278334209, 0.0359762106042261429],
[0.0771161079296581731, 0.0559295558613092034, 0.0387091033310036636],
[0.0820095691354102430, 0.0596688692683140301, 0.0414801950259215332],
[0.0868812899507808989, 0.0633723626214878488, 0.0441946278977992865],
[0.0917331597119335762, 0.0670421231643129056, 0.0468618965108947919],
[0.0965668977349263269, 0.0706800525877002150, 0.0494840809004433238],
[0.101384074808311131, 0.0742878899860269781, 0.0520630838823273948],
[0.106186131295040759, 0.0778672312418318691, 0.0546006517988118015],
[0.110974392478656619, 0.0814195455010332525, 0.0570983921846102902],
[0.115750081652325865, 0.0849461892595049506, 0.0595577888999055186],
[0.120514331345706993, 0.0884484184745207569, 0.0619802151650609076],
[0.125268193005161510, 0.0919273990320943757, 0.0643669448456295756],
[0.130012645381322373, 0.0953842158372470994, 0.0667191622693375230],
[0.134748601829972558, 0.0988198807441650062, 0.0690379708042663798],
[0.139476916694374425, 0.102235339503709916, 0.0713244003860215581],
[0.144198390907166712, 0.105631477874350899, 0.0735794141486876829],
[0.148913776925984953, 0.109009127017454910, 0.0758039142879290140],
[0.153623783097655231, 0.112369068277629047, 0.0779987472632603096],
[0.158329077530212470, 0.115712037432381870, 0.0801647084291815526],
[0.163030291539278394, 0.119038728481980216, 0.0823025461707279360],
[0.167728022724920434, 0.122349797039397856, 0.0844129656073549783],
[0.172422837726545708, 0.125645863371182637, 0.0864966319194903077],
[0.177115274696295649, 0.128927515132573028, 0.0885541733441135570],
[0.181805845525505327, 0.132195309833938596, 0.0905861838790938956],
[0.186495037853874890, 0.135449777070387939, 0.0925932257304497575],
[0.191183316886868238, 0.138691420542002841, 0.0945758315320212595],
[0.195871127043374893, 0.141920719888444930, 0.0965345063630974609],
[0.200558893452732590, 0.145138132358548222, 0.0984697295861906019],
[0.205247023317710608, 0.148344094332843152, 0.100381956524302207],
[0.209935907157929813, 0.151539022714681115, 0.102271619994592222],
[0.214625919946374366, 0.154723316203686540, 0.104139131713278044],
[0.219317422150096142, 0.157897356463585187, 0.105984883584797185],
[0.224010760684869636, 0.161061509195022795, 0.107809248886723996],
[0.228706269792403161, 0.164216125122738199, 0.109612583360589488],
[0.233404271847697409, 0.167361540905385769, 0.111395226217601201],
[0.238105078103299839, 0.170498079975350464, 0.113157501067242761],
[0.242808989376415485, 0.173626053315101198, 0.114899716775859834],
[0.247516296684204107, 0.176745760175896549, 0.116622168261567016],
[0.252227281831999994, 0.179857488744046390, 0.118325137231135885],
[0.256942217958687047, 0.182961516759378995, 0.120008892863933236],
[0.261661370043027031, 0.186058112090078054, 0.121673692447455656],
[0.266384995374341460, 0.189147533267637696, 0.123319781968547454],
[0.271113343990589894, 0.192230029985299117, 0.124947396663978694],
[0.275846659086616597, 0.195305843563004844, 0.126556761533706264],
[0.280585177395023533, 0.198375207381610741, 0.128148091819807908],
[0.285329129541922855, 0.201438347288830089, 0.129721593453808598],
[0.290078740379588862, 0.204495481979156846, 0.131277463474852224],
[0.294834229297846084, 0.207546823349801512, 0.132815890420950988],
[0.299595810515858374, 0.210592576834486456, 0.134337054695340408],
[0.304363693355832521, 0.213632941716786706, 0.135841128909783337],
[0.309138082500012512, 0.216668111424543508, 0.137328278206506366],
[0.313919178232219653, 0.219698273806751998, 0.138798660560301962],
[0.318707176665085690, 0.222723611394197274, 0.140252427062199925],
[0.323502269954019150, 0.225744301645010359, 0.141689722185989186],
[0.328304646498866037, 0.228760517176209988, 0.143110684038765423],
[0.333114491134144652, 0.231772425982210040, 0.144515444596583109],
[0.337931985308649652, 0.234780191641198510, 0.145904129926196863],
[0.342757307255168120, 0.237783973510209357, 0.147276860393805081],
[0.347590632150988010, 0.240783926909653334, 0.148633750861626807],
[0.352432132269820064, 0.243780203298003872, 0.149974910873085399],
[0.357281977125705585, 0.246772950437289529, 0.151300444827303343],
[0.362140333609447973, 0.249762312549988152, 0.152610452143564251],
[0.367007366118047795, 0.252748430467872487, 0.153905027416344764],
[0.371883236677601314, 0.255731441773319412, 0.155184260561473775],
[0.376768105060075964, 0.258711480933554616, 0.156448236953931036],
[0.381662128894354025, 0.261688679428269566, 0.157697037557766734],
[0.386565463771896267, 0.264663165871017625, 0.158930739048577047],
[0.391478263347367017, 0.267635066124765064, 0.160149413928947881],
[0.396400679434522230, 0.270604503411947250, 0.161353130637242798],
[0.401332862097651844, 0.273571598419357020, 0.162541953650085613],
[0.406274959738842922, 0.276536469398165119, 0.163715943578864737],
[0.411227119181308443, 0.279499232259358688, 0.164875157260556848],
[0.416189485749018151, 0.282460000664858435, 0.166019647843153317],
[0.421162203342842267, 0.285418886114560677, 0.167149464865945618],
[0.426145414513412202, 0.288375998029533287, 0.168264654334912000],
[0.431139260530888857, 0.291331443831579606, 0.169365258793429618],
[0.436143881451803550, 0.294285329019371766, 0.170451317388515433],
[0.441159416183149966, 0.297237757241339107, 0.171522865932792562],
[0.446186002543869586, 0.300188830365488435, 0.172579936962357044],
[0.451223777323877140, 0.303138648546318778, 0.173622559790710646],
[0.456272876340767686, 0.306087310288988057, 0.174650760558912876],
[0.461333434494318573, 0.309034912510873061, 0.175664562282092457],
[0.466405585818917612, 0.311981550600659963, 0.176663984892449971],
[0.471489463534019937, 0.314927318475094586, 0.177649045278869710],
[0.476585200092745020, 0.317872308633506795, 0.178619757323253942],
[0.481692927228706880, 0.320816612210230501, 0.179576131933679550],
[0.486812776001168512, 0.323760319025019061, 0.180518177074469988],
[0.491944876838618039, 0.326703517631556028, 0.181445897793269806],
[0.497089359580836498, 0.329646295364160458, 0.182359296245196256],
[0.502246353519539168, 0.332588738382770699, 0.183258371714139084],
[0.507415987437668026, 0.335530931716294389, 0.184143120631272583],
[0.512598389647394348, 0.338472959304399856, 0.185013536590835220],
[0.517793688026907950, 0.341414904037827926, 0.185869610363226273],
[0.523002010056042410, 0.344356847797292087, 0.186711329905464879],
[0.528223482850806891, 0.347298871491032279, 0.187538680369045946],
[0.533458233196865361, 0.350241055091094378, 0.188351644105230892],
[0.538706387582030710, 0.353183477668380708, 0.189150200667790591],
[0.543968072227807520, 0.356126217426542768, 0.189934326813230997],
[0.549243413120042878, 0.359069351734758846, 0.190703996498508416],
[0.554532536038723545, 0.362012957159455473, 0.191459180876250579],
[0.559835566586953992, 0.364957109495017307, 0.192199848287484237],
[0.565152630219178942, 0.367901883793526063, 0.192925964251871085],
[0.570483852268655722, 0.370847354393587236, 0.193637491455446731],
[0.575829357974235401, 0.373793594948268304, 0.194334389735848545],
[0.581189272506484889, 0.376740678452197830, 0.195016616065022019],
[0.586563720993169224, 0.379688677267862928, 0.195684124529380166],
[0.591952828544139442, 0.382637663151135066, 0.196336866307390279],
[0.596158108949445431, 0.386230792790580202, 0.199538350427064137],
[0.599163968497365529, 0.390470734380165552, 0.205294876761813350],
[0.602164006350762171, 0.394715358988969534, 0.211046192957863144],
[0.605158469232657481, 0.398964760982529754, 0.216793616545030654],
[0.608147602554619637, 0.403219034285008382, 0.222538340178932481],
[0.611131650471581134, 0.407478272421732846, 0.228281445686268403],
[0.614110855935192990, 0.411742568559527511, 0.234023916234425144],
[0.617085460745787850, 0.416012015544983793, 0.239766646917269510],
[0.620055705603009377, 0.420286705940792149, 0.245510453997299483],
[0.623021830155189304, 0.424566732060259855, 0.251256083002862007],
[0.625984073047517353, 0.428852186000128477, 0.257004215845666073],
[0.628942671969076494, 0.433143159671795286, 0.262755477096657974],
[0.631897863698790863, 0.437439744831034261, 0.268510439536145451],
[0.634849884150350596, 0.441742033106313048, 0.274269629075861166],
[0.637798968416169343, 0.446050116025780541, 0.280033529135674419],
[0.640745350810407177, 0.450364085043017226, 0.285802584545219174],
[0.643689264911138870, 0.454684031561611579, 0.291577205030386200],
[0.646630943601693264, 0.459010046958632956, 0.297357768335994366],
[0.649570619111221270, 0.463342222607071419, 0.303144623028710536],
[0.652508523054536882, 0.467680649897294798, 0.308938091018196248],
[0.655444886471277632, 0.472025420257587036, 0.314738469829306311],
[0.658379939864428665, 0.476376625173814683, 0.320546034653794887],
[0.661313913238251838, 0.480734356208270708, 0.326361040206266273],
[0.664247036135665603, 0.485098705017744047, 0.332183722405941406],
[0.667179537675113066, 0.489469763370854960, 0.338014299903080906],
[0.670111646586972642, 0.493847623164693383, 0.343852975466582444],
[0.673043591249527173, 0.498232376440801705, 0.349699937247255566],
[0.675975599724563447, 0.502624115400533200, 0.355555359929540626],
[0.678907899792617897, 0.507022932419817773, 0.361419405782935299],
[0.681840718987916206, 0.511428920063367265, 0.367292225623087221],
[0.684774284633061670, 0.515842171098342184, 0.373173959691372736],
[0.687708823873481867, 0.520262778507515344, 0.379064738460792194],
[0.690644563711710013, 0.524690835501942732, 0.384964683375145167],
[0.693581731041507998, 0.529126435533176065, 0.390873907527687137],
[0.696520552681904603, 0.533569672305030052, 0.396792516284801222],
[0.699461255411166327, 0.538020639784918320, 0.402720607859632707],
[0.702404066000753002, 0.542479432214790780, 0.408658273840118269],
[0.705349211249301611, 0.546946144121669864, 0.414605599675369085],
[0.708296918016690036, 0.551420870327807955, 0.420562665123983492],
[0.711247413258203398, 0.555903705960480332, 0.426529544667483607],
[0.714200924058886244, 0.560394746461416404, 0.432506307891760700],
[0.717157677668087801, 0.564894087595887107, 0.438493019839126252],
[0.720117901534295002, 0.569401825461452016, 0.444489741333311761],
[0.723081823340253504, 0.573918056496373064, 0.450496529279523161],
[0.726049671038485833, 0.578442877487700624, 0.456513436941467232],
[0.729021672887223082, 0.582976385579035750, 0.462540514197070041],
[0.731998057486824782, 0.587518678277973216, 0.468577807774444188],
[0.734979053816749661, 0.592069853463220719, 0.474625361469521223],
[0.737964891273140466, 0.596630009391401650, 0.480683216346614317],
[0.740955799707084695, 0.601199244703530811, 0.486751410923072891],
[0.743952009463646480, 0.605777658431169819, 0.492829981339064582],
[0.746953751421711720, 0.610365350002245011, 0.498918961513420800],
[0.749961257034757245, 0.614962419246534942, 0.505018383286400363],
[0.752974758372620623, 0.619568966400807164, 0.511128276550125604],
[0.755994488164357659, 0.624185092113596851, 0.517248669367371128],
[0.759020679842298818, 0.628810897449621598, 0.523379588079326830],
[0.762053567587387293, 0.633446483893813528, 0.529521057402860928],
[0.765093386375942375, 0.638091953354946284, 0.535673100517771838],
[0.768140372027950713, 0.642747408168844570, 0.541835739144450268],
[0.771194761257005590, 0.647412951101158929, 0.548008993612303041],
[0.774256791722068516, 0.652088685349669128, 0.554192882919262608],
[0.777326702081161946, 0.656774714546094374, 0.560387424782625154],
[0.780404732047203842, 0.661471142757387387, 0.566592635681442025],
[0.783491122446116295, 0.666178074486461491, 0.572808530890606127],
[0.786586115277442599, 0.670895614672324392, 0.579035124506759091],
[0.789689953777644948, 0.675623868689574580, 0.585272429466072386],
[0.792802882486348337, 0.680362942347202626, 0.591520457553923351],
[0.795925147315753812, 0.685112941886657390, 0.597779219406431306],
[0.799056995623502075, 0.689873973979107880, 0.604048724503761347],
[0.802198676289299528, 0.694646145721835917, 0.610328981155068839],
[0.805350439795618267, 0.699429564633691325, 0.616619996474886634],
[0.808512538312829987, 0.704224338649523496, 0.622921776350701672],
[0.811685225789205988, 0.709030576113493405, 0.629234325401413108],
[0.814868758046173980, 0.713848385771175486, 0.635557646926283582],
[0.818063392879353146, 0.718677876760328238, 0.641891742843935131],
[0.821269390165905500, 0.723519158600198664, 0.648236613620852387],
[0.824487011978776052, 0.728372341179244653, 0.654592258188765985],
[0.827716522708530022, 0.733237534741080221, 0.660958673850199685],
[0.830958189193488961, 0.738114849868493295, 0.667335856171343278],
[0.834212280859037647, 0.743004397465324651, 0.673723798861297074],
[0.837479069866999048, 0.747906288735979974, 0.680122493636592496],
[0.840758831276162244, 0.752820635162318674, 0.686531930069734786],
[0.844051843215104847, 0.757747548477640920, 0.692952095420329095],
[0.847358387068683827, 0.762687140637429373, 0.699382974447154027],
[0.850678747679669112, 0.767639523786489586, 0.705824549199298601],
[0.854013213567264895, 0.772604810222051186, 0.712276798784212240],
[0.857362077164450564, 0.777583112352356776, 0.718739699110192531],
[0.860725635076382889, 0.782574542650178784, 0.725213222600473384],
[0.864104188362418202, 0.787579213600624328, 0.731697337875631515],
[0.867498042844687345, 0.792597237642502561, 0.738192009400536864],
[0.870907509446622319, 0.797628727102397850, 0.744697197091452989],
[0.874332904565368274, 0.802673794120463468, 0.751212855878201746],
[0.877774550482629867, 0.807732550566799046, 0.757738935215454101],
[0.881232775819318137, 0.812805107947050631, 0.764275378536192318],
[0.884707916040208708, 0.817891577295680294, 0.770822122639183371],
[0.888200314015998194, 0.822992069055030528, 0.777379097000840291],
[0.891710320651460830, 0.828106692937986777, 0.783946223000047793],
[0.895238295590054744, 0.833235557771619728, 0.790523413042376277],
[0.898784608007347385, 0.838378771318666782, 0.797110569567414884],
[0.902349637508155555, 0.843536440073072935, 0.803707583919653912],
[0.905933775145376763, 0.848708669025018070, 0.810314335059221791],
[0.909537424582428700, 0.853895561389856561, 0.816930688083604473],
[0.913161003426120943, 0.859097218294124110, 0.823556492524943562],
[0.916804944763129459, 0.864313738410152799, 0.830191580379149197],
[0.920469698941286052, 0.869545217528763459, 0.836835763812336708],
[0.924155735647508525, 0.874791748056772733, 0.843488832476141037],
[0.927863546347894696, 0.880053418422547140, 0.850150550345134426],
[0.931593647173957540, 0.885330312368056815, 0.856820651965257807],
[0.935346582363562940, 0.890622508099580878, 0.863498837969443156],
[0.939122928398702261, 0.895930077260529090, 0.870184769672056269],
[0.942923299028627371, 0.901253083677893474, 0.876878062492126742],
[0.946748351432116109, 0.906591581816972414, 0.883578277868725781],
[0.950598793865775726, 0.911945614854936970, 0.890284913207861406],
[0.954475395281433214, 0.917315212248578926, 0.896997389219316044],
[0.958378997598600679, 0.922700386618998114, 0.903715033731666062],
[0.962310531628776000, 0.928101129695448224, 0.910437060660093889],
[0.966271038137635485, 0.933517406933559446, 0.917162542149774218],
[0.970261696327863299, 0.938949150216289885, 0.923890370856077614],
[0.974283863372929271, 0.944396247695624136, 0.930619207526320546],
[0.978339131016927710, 0.949858529212615044, 0.937347405867165473],
[0.982429409709964285, 0.955335744573387324, 0.944072900738174292],
[0.986557059635456146, 0.960827529642483857, 0.950793033848872482],
[0.990725107239741498, 0.966333350192042917, 0.957504265422603473],
[0.994937632294893404, 0.971852401324475035, 0.964201658267060835],
[0.999200539960174328, 0.977383406458508630, 0.970877847671487104],
[1.00000000000000000, 0.982924142947025126, 0.977520612812689316],
[1.00000000000000000, 0.988469939216566451, 0.984105190602352686],
[1.00000000000000000, 0.994000868618791888, 0.990528868543822605]]

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
