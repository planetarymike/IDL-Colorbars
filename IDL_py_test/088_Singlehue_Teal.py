from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000198725080239126838, 0.0000195868017889189583, 0.0000195292895369690181],
[0.000318672542981708140, 0.000348813614325084790, 0.000353932035433379482],
[0.000886300659105585670, 0.00100802183814207441, 0.00102909514851713397],
[0.00167697475423316780, 0.00196408895287925522, 0.00201437674841593384],
[0.00266473688010205635, 0.00320139645902097186, 0.00329623242079283511],
[0.00383123868101592794, 0.00471061368676854979, 0.00486717909137051024],
[0.00516219240008611042, 0.00648564794234021778, 0.00672283415110135150],
[0.00664582408710666025, 0.00852236387854753141, 0.00886068223889542768],
[0.00827205897239877835, 0.0108179289650575088, 0.0112794492756313602],
[0.0100320399638169286, 0.0133704365770170863, 0.0139787442746276240],
[0.0119178196515095838, 0.0161786705364002845, 0.0169588369294678999],
[0.0139221515535405752, 0.0192419489977033523, 0.0202205110278286387],
[0.0160383421922333305, 0.0225600161172719443, 0.0237649633445496215],
[0.0182601425057239211, 0.0261329641242077047, 0.0275937313604790804],
[0.0205816658035902246, 0.0299611756009299929, 0.0317086400753611303],
[0.0229973242705328700, 0.0340452796892045662, 0.0361117619335922305],
[0.0255017788129290081, 0.0383861181833465778, 0.0407984980341031325],
[0.0280898987428500960, 0.0428980293869965293, 0.0455129594957851061],
[0.0307567288696793256, 0.0473641775123490108, 0.0501906681848824157],
[0.0334974622725827467, 0.0517919434741507881, 0.0548353553216531717],
[0.0363074174998529245, 0.0561846793448105356, 0.0594503173261463000],
[0.0391820192669765019, 0.0605453648946262454, 0.0640384864103326623],
[0.0420694876667837350, 0.0648766649804192186, 0.0686024869814879645],
[0.0448839956638869622, 0.0691809759397915558, 0.0731446812141498537],
[0.0476373050752248936, 0.0734604634768454834, 0.0776672062440063593],
[0.0503312706916400829, 0.0777170938842408343, 0.0821720048036212458],
[0.0529675385041458516, 0.0819526599895427088, 0.0866608506685360713],
[0.0555475695075910367, 0.0861688028830936981, 0.0911353699557273522],
[0.0580726597375791007, 0.0903670302419420091, 0.0955970590768485951],
[0.0605439572293209952, 0.0945487318839538793, 0.100047299970695974],
[0.0629624764404993764, 0.0987151930505750785, 0.104487373105543763],
[0.0653291105685145645, 0.102867605813573099, 0.108918468640320176],
[0.0676446421064711700, 0.107007078921902005, 0.113341696055557245],
[0.0699097519154456004, 0.111134646343460847, 0.117758092504586909],
[0.0721250270381731395, 0.115251274708535023, 0.122168630088209884],
[0.0742909674378708640, 0.119357869823901397, 0.126574222218841542],
[0.0764079918128903468, 0.123455282396548488, 0.130975729210589337],
[0.0784764426113710722, 0.127544313081953797, 0.135373963208097942],
[0.0804965903486133116, 0.131625716952523425, 0.139769692547981411],
[0.0824686373123696692, 0.135700207466139977, 0.144163645631267323],
[0.0843927207269100366, 0.139768460001995692, 0.148556514372732346],
[0.0862689154347892895, 0.143831115020431083, 0.152948957282727949],
[0.0880972361453448427, 0.147888780894873284, 0.157341602228634469],
[0.0898776392906024679, 0.151942036456836099, 0.161735048916066493],
[0.0916100245221648235, 0.155991433289004111, 0.166129871124132661],
[0.0932942358766111202, 0.160037497796455208, 0.170526618724172685],
[0.0949300626316484652, 0.164080733081915703, 0.174925819507316366],
[0.0965172398706401202, 0.168121620647427306, 0.179327980842758694],
[0.0980554487690263876, 0.172160621941832820, 0.183733591185735956],
[0.0995443166124265200, 0.176198179770964608, 0.188143121451714135],
[0.100983416552777094, 0.180234719585270042, 0.192557026271187565],
[0.102372267105668740, 0.184270650657764684, 0.196975745137691727],
[0.103710331388944893, 0.188306367163627697, 0.201399703460081458],
[0.104997016099628360, 0.192342249171393365, 0.205829313528797297],
[0.106231670223226493, 0.196378663554519994, 0.210264975404694077],
[0.107413583466403922, 0.200415964831100302, 0.214707077738011010],
[0.108541984400822494, 0.204454495938592273, 0.219155998524200313],
[0.109616038302526114, 0.208494588949690640, 0.223612105802576899],
[0.110634844667651749, 0.212536565734774030, 0.228075758303101783],
[0.111597434381202953, 0.216580738575788911, 0.232547306046031077],
[0.112502766511206748, 0.220627410735908858, 0.237027090898664306],
[0.113349724695606252, 0.224676876988858520, 0.241515447092983282],
[0.114137113083608327, 0.228729424111390689, 0.246012701707578385],
[0.114863651786768217, 0.232785331342053869, 0.250519175116922177],
[0.115527971787688310, 0.236844870809077068, 0.255035181410740996],
[0.116128609245632342, 0.240908307929918797, 0.259561028785966763],
[0.116663999128332169, 0.244975901784784955, 0.264097019913512032],
[0.117132468087520203, 0.249047905466200037, 0.268643452281898065],
[0.117532226481876528, 0.253124566406523532, 0.273200618519575167],
[0.117861359434636020, 0.257206126685123049, 0.277768806697605730],
[0.118117816793526204, 0.261292823316770284, 0.282348300614225389],
[0.118299401837254847, 0.265384888522673668, 0.286939380062668448],
[0.118403758544480015, 0.269482549985450182, 0.291542321083513412],
[0.118428357207034735, 0.273586031089211756, 0.296157396202699652],
[0.118370478127486134, 0.277695551145851760, 0.300784874656266965],
[0.118227193090150007, 0.281811325608519014, 0.305425022602779594],
[0.117995344231878657, 0.285933566273186224, 0.310078103324314624],
[0.117671519861132695, 0.290062481469145927, 0.314744377416826315],
[0.117252026676791327, 0.294198276239195200, 0.319424102970625401],
[0.116732857716253052, 0.298341152510216090, 0.324117535741659968],
[0.116109655208207929, 0.302491309254793894, 0.328824929314224634],
[0.115377667308800863, 0.306648942644473843, 0.333546535255675902],
[0.114531697447229464, 0.310814246195203869, 0.338282603263694415],
[0.113566044678991868, 0.314987410905472165, 0.343033381306578511],
[0.112474433015910563, 0.319168625387607929, 0.347799115757035038],
[0.111249927134377230, 0.323358075992683736, 0.352580051519882254],
[0.109884831104421737, 0.327555946929417252, 0.357376432154061341],
[0.108370565755082415, 0.331762420377448353, 0.362188499989317236],
[0.106697518883988513, 0.335977676595336283, 0.367016496237882961],
[0.104854860562442337, 0.340201894023603180, 0.371860661101486245],
[0.102830313025783354, 0.344435249383113373, 0.376721233873963279],
[0.100609860674921836, 0.348677917769078582, 0.381598453039753427],
[0.0981773799190556462, 0.352930072740936962, 0.386492556368526030],
[0.0955141599381866269, 0.357191886408355641, 0.391403781006175067],
[0.0925982722307667483, 0.361463529513578241, 0.396332363562399481],
[0.0894037261031378205, 0.365745171510325651, 0.401278540195073141],
[0.0858993138393102651, 0.370036980639451396, 0.406242546691601147],
[0.0820469935314595000, 0.374339124001528911, 0.411224618547432641],
[0.0777995608662341021, 0.378651767626551117, 0.416224991041905468],
[0.0730971857941729308, 0.382975076540890136, 0.421243899311574521],
[0.0678620545114496931, 0.387309214831680182, 0.426281578421173646],
[0.0619896727125804001, 0.391654345708759566, 0.431338263432346936],
[0.0553338743670283642, 0.396010631564300330, 0.436414189470281599],
[0.0476788876356181376, 0.400378234030257907, 0.441509591788359745],
[0.0386746024602307101, 0.404757314033750815, 0.446624705830948876],
[0.0286991749827948221, 0.409148031850482763, 0.451759767294434067],
[0.0182590358749233940, 0.413550547156311676, 0.456915012186596858],
[0.00734328655856836699, 0.417965019077059019, 0.462090676884433227],
[-0.00405914842689382611, 0.422391606236654338, 0.467286998190502068],
[-0.0159595244308840881, 0.426830466803701736, 0.472504213387892225],
[-0.0283692797452970193, 0.431281758536543658, 0.477742560293880791],
[-0.0413000387066107949, 0.435745638826906867, 0.483002277312366835],
[-0.0547636148474367826, 0.440222264742198666, 0.488283603485148599],
[-0.0687720140983939243, 0.444711793066518701, 0.493586778542109028],
[-0.0833374380414626248, 0.449214380340458963, 0.498912042950381218],
[-0.0984722872157920148, 0.453730182899745593, 0.504259637962547025],
[-0.114189164476912450, 0.458259356912785132, 0.509629805663934121],
[-0.130500878410545168, 0.462802058417165985, 0.515022789019057625],
[-0.147420446802051852, 0.467358443355173236, 0.520438831917268141],
[-0.164961100162471619, 0.471928667608357333, 0.525878179217648567],
[-0.183136285312516800, 0.476512887031211696, 0.531341076793208189],
[-0.201959669025329081, 0.481111257483996024, 0.536827771574422630],
[-0.221445141729499584, 0.485723934864756124, 0.542338511592157069],
[-0.241606821273163824, 0.490351075140569803, 0.547873546020018809],
[-0.262459056750644793, 0.494992834378066238, 0.553433125216172051],
[-0.284016432392629414, 0.499649368773247671, 0.559017500764656838],
[-0.306293771521243652, 0.504320834680652586, 0.564626925516248823],
[-0.329306140571222761, 0.509007388641890657, 0.570261653628884813],
[-0.320482386379758899, 0.512841273728784852, 0.574148343832794561],
[-0.278720096387452543, 0.515817304197300541, 0.576281487346257171],
[-0.236231797439420854, 0.518801734571243234, 0.578432729821187430],
[-0.193012779680059893, 0.521794679090695324, 0.580601989599640711],
[-0.149058285629142362, 0.524796251508246270, 0.582789190432193793],
[-0.104363509243571254, 0.527806565112110104, 0.584994261270706750],
[-0.0589235949892884595, 0.530825732749000023, 0.587217136072080814],
[-0.0127336369222866147, 0.533853866846759173, 0.589457753612389501],
[0.0342113222219853491, 0.536891079436768171, 0.591716057310783361],
[0.0730749016507796501, 0.539937482176129913, 0.593991995062624456],
[0.100443695003656991, 0.542993186369644887, 0.596285519081332982],
[0.122642748310471450, 0.546058302991581535, 0.598596585748464194],
[0.141787687881664570, 0.549132942707258320, 0.600925155471565109],
[0.158874328892453065, 0.552217215894438507, 0.603271192549394208],
[0.174462505876210372, 0.555311232664553733, 0.605634665044098353],
[0.188902642868501142, 0.558415102883755177, 0.608015544659993079],
[0.202430630310804882, 0.561528936193816608, 0.610413806628584910],
[0.215213858465537145, 0.564652842032884128, 0.612829429599521247],
[0.227375968144235274, 0.567786929656088013, 0.615262395537159335],
[0.239011212735881329, 0.570931308156030104, 0.617712689622470501],
[0.250193299152664861, 0.574086086483141855, 0.620180300160010467],
[0.260981093287264099, 0.577251373465944573, 0.622665218489707573],
[0.271422447171642767, 0.580427277831195965, 0.625167438903232009],
[0.281556850413973769, 0.583613908223952094, 0.627686958564720898],
[0.291417318072698606, 0.586811373227546618, 0.630223777435661159],
[0.301031766840964665, 0.590019781383496200, 0.632777898203727540],
[0.310424038931316537, 0.593239241211342527, 0.635349326215393639],
[0.319614677617431675, 0.596469861228444143, 0.637938069412152808],
[0.328621524047980451, 0.599711749969725427, 0.640544138270173313],
[0.337460183048068074, 0.602965016007391275, 0.643167545743254854],
[0.346144391296436427, 0.606229767970622779, 0.645808307208927568],
[0.354686311677525456, 0.609506114565260715, 0.648466440417575618],
[0.363096771057298373, 0.612794164593489454, 0.651141965444450577],
[0.371385454174021468, 0.616094026973534437, 0.653834904644465698],
[0.379561063110913199, 0.619405810759380615, 0.656545282609657610],
[0.387631449501109948, 0.622729625160525102, 0.659273126129218956],
[0.395603724928424105, 0.626065579561779328, 0.662018464152001718],
[0.403484353742533830, 0.629413783543133709, 0.664781327751406526],
[0.411279231578223992, 0.632774346899688256, 0.667561750092579786],
[0.418993752166923472, 0.636147379661677892, 0.670359766401835144],
[0.426632864494389807, 0.639532992114592358, 0.673175413938233436],
[0.434201121946981849, 0.642931294819416021, 0.676008731967259746],
[0.441702724769652999, 0.646342398633000026, 0.678859761736533951],
[0.449141556908907169, 0.649766414728575104, 0.681728546453501116],
[0.456521218116847260, 0.653203454616432810, 0.684615131265057575],
[0.463845052035827432, 0.656653630164791058, 0.687519563239063269],
[0.471116170858124461, 0.660117053620850047, 0.690441891347709391],
[0.478337477054036231, 0.663593837632078465, 0.693382166452696125],
[0.485511682580442361, 0.667084095267730937, 0.696340441292205181],
[0.492641325915160022, 0.670587940040631936, 0.699316770469629589],
[0.499728787208197078, 0.674105485929242465, 0.702311210444055201],
[0.506776301796050488, 0.677636847400033937, 0.705323819522465034],
[0.513785972288282489, 0.681182139430197786, 0.708354657853669689],
[0.520759779404710632, 0.684741477530718123, 0.711403787423952161],
[0.527699591715986238, 0.688314977769834302, 0.714471272054431727],
[0.534607174418685438, 0.691902756796924478, 0.717557177400149349],
[0.541484197258018329, 0.695504931866847587, 0.720661570950890562],
[0.548332241695911104, 0.699121620864778137, 0.723784522033764088],
[0.555152807409265869, 0.702752942331566377, 0.726926101817553239],
[0.561947318192168366, 0.706399015489676652, 0.730086383318882426],
[0.568717127326383687, 0.710059960269735835, 0.733265441410225205],
[0.575463522476379996, 0.713735897337756886, 0.736463352829802798],
[0.582187730158326033, 0.717426948123065067, 0.739680196193433504],
[0.588890919826293158, 0.721133234847011306, 0.742916052008379624],
[0.595574207613965179, 0.724854880552514236, 0.746171002689277385],
[0.602238659765548245, 0.728592009134506280, 0.749445132576221695],
[0.608885295785706604, 0.732344745371351857, 0.752738527955101988],
[0.615515091334980613, 0.736113214957321294, 0.756051277080294404],
[0.622128980894118833, 0.739897544536213259, 0.759383470199822219],
[0.628727860218258439, 0.743697861736198007, 0.762735199583126078],
[0.635312588599482586, 0.747514295206016977, 0.766106559551585908],
[0.641883990954326578, 0.751346974652627786, 0.769497646511962730],
[0.648442859751030998, 0.755196030880439517, 0.772908558992951633],
[0.654989956789748695, 0.759061595832262737, 0.776339397685052779],
[0.661526014847452881, 0.762943802632141344, 0.779790265483995659],
[0.668051739198126770, 0.766842785630231227, 0.783261267537983974],
[0.674567809017603492, 0.770758680449918132, 0.786752511299054436],
[0.681074878681451334, 0.774691624037386561, 0.790264106578887349],
[0.687573578963379783, 0.778641754713873535, 0.793796165609437110],
[0.694064518140754316, 0.782609212230881535, 0.797348803108810289],
[0.700548283013101680, 0.786594137828633411, 0.800922136352867353],
[0.707025439838741110, 0.790596674298112090, 0.804516285253080943],
[0.713496535193967385, 0.794616966047064666, 0.808131372441265539],
[0.719962096758684833, 0.798655159170383988, 0.811767523361865973],
[0.726422634031681613, 0.802711401525359691, 0.815424866372587598],
[0.732878638978213703, 0.806785842812339338, 0.819103532854270733],
[0.739330586611961493, 0.810878634661428510, 0.822803657331022231],
[0.745778935512860341, 0.814989930725935952, 0.826525377601781908],
[0.752224128281687166, 0.819119886783388540, 0.830268834884667628],
[0.758666591931698719, 0.823268660845048905, 0.834034173975649828],
[0.765106738216911331, 0.827436413275028704, 0.837821543423349690],
[0.771544963895957947, 0.831623306920250549, 0.841631095722042311],
[0.777981650929609137, 0.835829507252724202, 0.845462987525292808],
[0.784417166609160388, 0.840055182525855204, 0.849317379883057111],
[0.790851863611924943, 0.844300503946780245, 0.853194438505579078],
[0.797286079978802631, 0.848565645867100704, 0.857094334058010832],
[0.803720139007550349, 0.852850785994822447, 0.861017242490411672],
[0.810154349053707201, 0.857156105630823895, 0.864963345408665374],
[0.816589003229082233, 0.861481789933847719, 0.868932830492950448],
[0.823024378985323990, 0.865828028218817436, 0.872925891971751744],
[0.829460737566978912, 0.870195014294280034, 0.876942731161084787],
[0.835898323314735792, 0.874582946846073628, 0.880983557080729285],
[0.842337362794802313, 0.878992029875882430, 0.885048587161932021],
[0.848778063724289322, 0.883422473205433767, 0.889138048064482600],
[0.855220613654798289, 0.887874493059707559, 0.893252176625448313],
[0.861665178366299633, 0.892348312745957384, 0.897391220967596048],
[0.868111899910301910, 0.896844163449863063, 0.901555441803043589],
[0.874560894223701868, 0.901362285176121047, 0.905745113977688532],
[0.881012248211329618, 0.905902927868805108, 0.909960528315407413],
[0.887466016162981930, 0.910466352757871911, 0.914201993839373173],
[0.893922215326520275, 0.915052833993314496, 0.918469840473191579],
[0.900380820396106563, 0.919662660649864794, 0.922764422360292547],
[0.906841756585312186, 0.924296139215747825, 0.927086121991080758],
[0.913304890824243598, 0.928953596723624542, 0.931435355402049248],
[0.919770020424663604, 0.933635384748619290, 0.935812578822569518],
[0.926236858257949103, 0.938341884600535803, 0.940218297315969509],
[0.932705013018870766, 0.943073514198522700, 0.944653076230969502],
[0.939173962378902827, 0.947830737379010357, 0.949117556718659938],
[0.945643015529304631, 0.952614076832376644, 0.953612477313858897],
[0.952111259304054047, 0.957424132651339632, 0.958138704897171789],
[0.958577477750787499, 0.962261609946500784, 0.962697280817675805],
[0.965040026381576488, 0.967127361924904449, 0.967289492876724943],
[0.971496623594070408, 0.972022461204294808, 0.971916994546348278],
[0.977943976495365575, 0.976948327525076876, 0.976582018557160203],
[0.984377031957642257, 0.981906982974872888, 0.981287803905725231],
[0.990787206497793060, 0.986901654314918164, 0.986039603962251321],
[0.997156769620680783, 0.991938681360657326, 0.990847881714461809],
[1.00341087707828258, 0.997043782662109357, 0.995755557520721202]]

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
