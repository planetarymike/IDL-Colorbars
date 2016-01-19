from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000198725080239126838, 0.0000195868017889189583, 0.0000195292895369690181],
[0.000367752759253028719, 0.000329236731423309076, 0.000356170271027306772],
[0.00107633118729484546, 0.000932217764983797603, 0.00103776267079091242],
[0.00211675250005073602, 0.00178864999243901509, 0.00203443565409631121],
[0.00347710940321485683, 0.00287730460025166414, 0.00333328498680539277],
[0.00515139019964547685, 0.00418392412661597757, 0.00492738955044476606],
[0.00713656297402937793, 0.00569792003897784480, 0.00681287928230459462],
[0.00943137346267760787, 0.00741095461928899680, 0.00898771765229378593],
[0.0120357400854832330, 0.00931620279974789897, 0.0114510852447921516],
[0.0149504104354296514, 0.0114079202032223853, 0.0142030278526820517],
[0.0181767495038295777, 0.0136811692986383605, 0.0172442384454568679],
[0.0217166010467263748, 0.0161316353114999457, 0.0205759137738186805],
[0.0255721925808926886, 0.0187554967793051274, 0.0241996556693597695],
[0.0297460678899393004, 0.0215493312253744705, 0.0281174006307900529],
[0.0342410376624586801, 0.0245100443977384480, 0.0323313681204971462],
[0.0390601425227099924, 0.0276348158887878906, 0.0368440216930951484],
[0.0440480989730968817, 0.0309210564818463186, 0.0416275398268546662],
[0.0489879386018966453, 0.0343663741049696908, 0.0464075949266159957],
[0.0538931895344873860, 0.0379685462388755640, 0.0511521377753441295],
[0.0587675040607514923, 0.0416927056245536484, 0.0558648705374202234],
[0.0636141054049711441, 0.0453694883870366175, 0.0605490634637844485],
[0.0684358576122337248, 0.0489985347702591376, 0.0652076251013378461],
[0.0732353213519979507, 0.0525826393370544473, 0.0698431583788983734],
[0.0780147989773339323, 0.0561243090345873233, 0.0744580059135877548],
[0.0827763712781191263, 0.0596258031534412439, 0.0790542869807619175],
[0.0875219277359781944, 0.0630891663094536037, 0.0836339279594927876],
[0.0922531916397041907, 0.0665162558933405645, 0.0881986876159820410],
[0.0969717410951705383, 0.0699087650903335023, 0.0927501782620354098],
[0.101679026725648047, 0.0732682423201347632, 0.0972898835871694456],
[0.106376386681614449, 0.0765961077600283424, 0.101819173785698020],
[0.111065059446267961, 0.0798936674728319696, 0.106339318466940641],
[0.115746194822047010, 0.0831621255539378712, 0.110851497735490162],
[0.120420863406009826, 0.0864025946291159252, 0.115356811750797344],
[0.125090064801973017, 0.0896161049706707402, 0.119856289015169204],
[0.129754734770460622, 0.0928036124493987480, 0.124350893592257927],
[0.134415751480626705, 0.0959660055002363177, 0.128841531421088368],
[0.139073940999040163, 0.0991041112480285369, 0.133329055861274137],
[0.143730082126830805, 0.102218700914684935, 0.137814272581578357],
[0.148384910677867521, 0.105310494608687855, 0.142297943885062866],
[0.153039123275410610, 0.108380165581467819, 0.146780792548759503],
[0.157693380732258609, 0.111428344021739428, 0.151263505243321661],
[0.162348311069253792, 0.114455620447874495, 0.155746735587896812],
[0.167004512218640017, 0.117462548749309587, 0.160231106887040953],
[0.171662554451838367, 0.120449648920457342, 0.164717214589535282],
[0.176322982565444736, 0.123417409524326976, 0.169205628503167199],
[0.180986317854452378, 0.126366289917805352, 0.173696894794699325],
[0.185653059897655653, 0.129296722266155351, 0.178191537800189065],
[0.190323688176800454, 0.132209113370565068, 0.182690061667398651],
[0.194998663548169471, 0.135103846329432953, 0.187192951849140754],
[0.199678429582846539, 0.137981282051404974, 0.191700676463950059],
[0.204363413789833137, 0.140841760635887048, 0.196213687538373593],
[0.209054028734403874, 0.143685602634810145, 0.200732422143383105],
[0.213750673062574947, 0.146513110207743491, 0.205257303435881777],
[0.218453732441234172, 0.149324568181005202, 0.209788741614948315],
[0.223163580422366947, 0.152120245020170936, 0.214327134801327035],
[0.227880579238809999, 0.154900393724298868, 0.218872869847683060],
[0.232605080538147158, 0.157665252649243942, 0.223426323086284462],
[0.237337426060585610, 0.160415046266621453, 0.227987861020025662],
[0.242077948266032239, 0.163149985864257413, 0.232557840962061668],
[0.246826970915016486, 0.165870270193338942, 0.237136611628744276],
[0.251584809607608706, 0.168576086066921843, 0.241724513690060871],
[0.256351772284052093, 0.171267608913977354, 0.246321880281329342],
[0.261128159690438622, 0.173945003292723055, 0.250929037479523942],
[0.265914265812430828, 0.176608423366607981, 0.255546304747260422],
[0.270710378279721164, 0.179258013345990369, 0.260173995347167120],
[0.275516778743662871, 0.181893907898244306, 0.264812416729105271],
[0.280333743230263555, 0.184516232528772667, 0.269461870892457433],
[0.285161542470539098, 0.187125103935161824, 0.274122654725499182],
[0.290000442210016418, 0.189720630336509183, 0.278795060323674293],
[0.294850703499030087, 0.192302911779764107, 0.283479375288427371],
[0.299712582965284413, 0.194872040424755644, 0.288175883008100098],
[0.304586333070046289, 0.197428100809425633, 0.292884862922257128],
[0.309472202349191539, 0.199971170096655548, 0.297606590770691792],
[0.314370435640228818, 0.202501318303949240, 0.302341338828248429],
[0.319281274296334794, 0.205018608517122447, 0.307089376126503000],
[0.324204956388328747, 0.207523097089057307, 0.311850968663254902],
[0.329141716895458736, 0.210014833824478608, 0.316626379600703500],
[0.334091787885783253, 0.212493862151635182, 0.321415869453105185],
[0.339055398686871012, 0.214960219281695952, 0.326219696264653691],
[0.344032776047489830, 0.217413936356596393, 0.331038115778253705],
[0.349024144290896621, 0.219855038586014462, 0.335871381595812535],
[0.354029725460289102, 0.222283545374099001, 0.340719745330623824],
[0.359049739456946959, 0.224699470436521331, 0.345583456752370011],
[0.364084404171537146, 0.227102821908371610, 0.350462763925235510],
[0.369133935609035735, 0.229493602443382794, 0.355357913339578724],
[0.374198548007666665, 0.231871809304926735, 0.360269150037583086],
[0.379278453952245520, 0.234237434449183435, 0.365196717733273835],
[0.384373864482286887, 0.236590464600855921, 0.370140858927258953],
[0.389484989195181097, 0.238930881321779254, 0.375101815016525508],
[0.394612036344775097, 0.241258661072726310, 0.380079826399605747],
[0.399755212935609949, 0.243573775268706716, 0.385075132577394175],
[0.404914724813101812, 0.245876190328015665, 0.390087972249889281],
[0.410090776749891472, 0.248165867715278432, 0.395118583409101720],
[0.415283572528605982, 0.250442763978702187, 0.400167203428371199],
[0.420493315021237435, 0.252706830781740999, 0.405234069148297737],
[0.425720206265332357, 0.254958014929352217, 0.410319416959496863],
[0.430964447537190987, 0.257196258389009946, 0.415423482882368300],
[0.436226239422234152, 0.259421498306620757, 0.420546502644046583],
[0.441505781882711501, 0.261633667017476312, 0.425688711752710780],
[0.446803274322891963, 0.263832692052362538, 0.430850345569397497],
[0.452118915651893272, 0.266018496138922478, 0.436031639377469138],
[0.457452904344264388, 0.268190997198378467, 0.441232828449872438],
[0.462805438498464394, 0.270350108337676420, 0.446454148114310778],
[0.468176715893340034, 0.272495737837134544, 0.451695833816458447],
[0.473566934042721710, 0.274627789133644495, 0.456958121181320231],
[0.478976290248241676, 0.276746160799466678, 0.462241246072851275],
[0.484404981650460253, 0.278850746516673853, 0.467545444651931541],
[0.489853205278406534, 0.280941435047241284, 0.472870953432790897],
[0.495321158097608516, 0.283018110198820172, 0.478218009337974703],
[0.500809037056709316, 0.285080650786185274, 0.483586849751932391],
[0.506317039132715085, 0.287128930588366360, 0.488977712573307188],
[0.511845361374991925, 0.289162818301433755, 0.494390836266004829],
[0.517394200948038341, 0.291182177486930149, 0.499826459909110621],
[0.522963755173121547, 0.293186866515907307, 0.505284823245718773],
[0.528554221568838245, 0.295176738508527048, 0.510766166730741822],
[0.534165797890638561, 0.297151641269185918, 0.516270731577759490],
[0.539798682169397859, 0.299111417217088615, 0.521798759804959489],
[0.545453072749058188, 0.301055903312214546, 0.527350494280229398],
[0.551129168323412522, 0.302984930976591238, 0.532926178765449454],
[0.556827167972063664, 0.304898326010792253, 0.538526057960033722],
[0.562547271195602550, 0.306795908505557824, 0.544150377543766051],
[0.568289677950065242, 0.308677492748431093, 0.549799384218975229],
[0.574054588680680600, 0.310542887125296097, 0.555473325752095293],
[0.579842204354973911, 0.312391894016681604, 0.561172451014642859],
[0.585652726495240583, 0.314224309688701742, 0.566897010023655446],
[0.591486357210443847, 0.316039924178469378, 0.572647253981628301],
[0.597343299227550029, 0.317838521173834543, 0.578423435315978396],
[0.603223755922351557, 0.319619877887257098, 0.584225807718074641],
[0.607351555427551482, 0.323290648145466541, 0.588164197965378222],
[0.609711691039784953, 0.328838643444914924, 0.590230767453264304],
[0.612075667409917146, 0.334354602941075052, 0.592313270354963062],
[0.614443682008419478, 0.339840387577557190, 0.594411687717014248],
[0.616815931649709714, 0.345297737999574972, 0.596526004219534278],
[0.619192612504970374, 0.350728285198425582, 0.598656208040741156],
[0.621573920115475298, 0.356133560000425009, 0.600802290728777888],
[0.623960049406390938, 0.361515001548672443, 0.602964247080432059],
[0.626351194701008418, 0.366873964904134320, 0.605142075026368742],
[0.628747549735376610, 0.372211727874282750, 0.607335775522523158],
[0.631149307673289361, 0.377529497162224836, 0.609545352447319888],
[0.633556661121626452, 0.382828413916404986, 0.611770812504408346],
[0.635969802145996521, 0.388109558750098116, 0.614012165130621401],
[0.638388922286682869, 0.393373956290718752, 0.616269422408887824],
[0.640814212574859154, 0.398622579311148861, 0.618542598985841630],
[0.643245863549064212, 0.403856352488609516, 0.620831711993886537],
[0.645684065271934449, 0.409076155830891741, 0.623136780977498139],
[0.648129007347164721, 0.414282827804862752, 0.625457827823545642],
[0.650580878936698137, 0.419477168197939121, 0.627794876695440207],
[0.653039868778150456, 0.424659940739562536, 0.630147953970928598],
[0.655506165202440205, 0.429831875506576810, 0.632517088183350729],
[0.657979956151645506, 0.434993671133643789, 0.634902309966205780],
[0.660461429197074734, 0.440145996847456145, 0.637303652000874576],
[0.662950771557555107, 0.445289494341430114, 0.639721148967347664],
[0.665448170117939553, 0.450424779505727846, 0.642154837497836639],
[0.667953811447848933, 0.455552444025869085, 0.644604756133137058],
[0.670467881820630662, 0.460673056861790442, 0.647070945281622345],
[0.672990567232566561, 0.465787165617971122, 0.649553447180770349],
[0.675522053422324742, 0.470895297814152347, 0.652052305861106740],
[0.678062525890669954, 0.475997962065225988, 0.654567567112478099],
[0.680612169920438270, 0.481095649177993801, 0.657099278452564328],
[0.683171170596800992, 0.486188833171765034, 0.659647489097540562],
[0.685739712827819203, 0.491277972229065496, 0.662212249934819197],
[0.688317981365310638, 0.496363509582146867, 0.664793613497796310],
[0.690906160826049720, 0.501445874340439080, 0.667391633942532314],
[0.693504435713311329, 0.506525482263613491, 0.670006367026312222],
[0.696112990438780721, 0.511602736484504383, 0.672637870088020007],
[0.698732009344863569, 0.516678028185733829, 0.675286202030283334],
[0.701361676727388583, 0.521751737233562718, 0.677951423303335243],
[0.704002176858778528, 0.526824232772155954, 0.680633595890549947],
[0.706653694011651567, 0.531895873781200734, 0.683332783295615753],
[0.709316412482942082, 0.536967009599527478, 0.686049050531309157],
[0.711990516618533964, 0.542037980417194198, 0.688782464109840231],
[0.714676190838451353, 0.547109117738253103, 0.691533092034740116],
[0.717373619662648343, 0.552180744816260449, 0.694301003794270732],
[0.720082987737413527, 0.557253177064408023, 0.697086270356335858],
[0.722804479862464988, 0.562326722441991778, 0.699888964164884886],
[0.725538281018733411, 0.567401681818818560, 0.702709159137785755],
[0.728284576396925121, 0.572478349318995439, 0.705546930666178795],
[0.731043551426874494, 0.577557012645453227, 0.708402355615290968],
[0.733815391807768003, 0.582637953386435759, 0.711275512326726922],
[0.736600283539275979, 0.587721447305088795, 0.714166480622236644],
[0.739398412953664486, 0.592807764613206500, 0.717075341808969036],
[0.742209966748949124, 0.597897170230092701, 0.720002178686235173],
[0.745035132023153745, 0.602989924027437230, 0.722947075553793783],
[0.747874096309760650, 0.608086281061021583, 0.725910118221688383],
[0.750727047614422105, 0.613186491790015165, 0.728891394021671801],
[0.753594174453034782, 0.618290802284562457, 0.731890991820248194],
[0.756475665891247373, 0.623399454422299715, 0.734909002033382275],
[0.759371711585536291, 0.628512686074397253, 0.737945516642925181],
[0.762282501825925607, 0.633630731281668802, 0.741000629214813355],
[0.765208227580497668, 0.638753820421250285, 0.744074434919107408],
[0.768149080541811968, 0.643882180364302337, 0.747167030551949329],
[0.771105253175376926, 0.649016034625153559, 0.750278514559512333],
[0.774076938770316914, 0.654155603502276084, 0.753408987064048574],
[0.777064331492443139, 0.659301104211410860, 0.756558549892131449],
[0.780067626439843287, 0.664452751011190945, 0.759727306605214481],
[0.783087019701266485, 0.669610755321501716, 0.762915362532637475],
[0.786122708417460125, 0.674775325834851447, 0.766122824807221714],
[0.789174890845756871, 0.679946668620941330, 0.769349802403622829],
[0.792243766428124330, 0.685124987224642545, 0.772596406179619333],
[0.795329535863006809, 0.690310482757509614, 0.775862748920537415],
[0.798432401181284224, 0.695503353982952488, 0.779148945387038938],
[0.801552565826674113, 0.700703797395173522, 0.782455112366523875],
[0.804690234741009314, 0.705912007291896515, 0.785781368728422525],
[0.807845614454804295, 0.711128175840933463, 0.789127835483696360],
[0.811018913183626622, 0.716352493140554048, 0.792494635848891571],
[0.814210340930793364, 0.721585147273621996, 0.795881895315140975],
[0.817420109597011502, 0.726826324355392184, 0.799289741722548519],
[0.820648433097659224, 0.732076208574837017, 0.802718305340456073],
[0.823895527488446966, 0.737334982229313929, 0.806167718954143409],
[0.827161611100347360, 0.742602825752336382, 0.809638117958589532],
[0.830446904684740028, 0.747879917734148747, 0.813129640460004688],
[0.833751631569889740, 0.753166434934738560, 0.816642427385934178],
[0.837076017829994301, 0.758462552288844294, 0.820176622604846251],
[0.840420292468207042, 0.763768442902442723, 0.823732373056243916],
[0.843784687615267037, 0.769084278040074398, 0.827309828892478061],
[0.847169438745564718, 0.774410227102284798, 0.830909143633632663],
[0.850574784912763837, 0.779746457592300213, 0.834530474337023986],
[0.854000969007409072, 0.785093135070927928, 0.838173981783119637],
[0.857448238039343003, 0.790450423098462251, 0.841839830679951606],
[0.860916843448163993, 0.795818483162199053, 0.845528189888422599],
[0.864407041445564017, 0.801197474587871383, 0.849239232671319622],
[0.867919093393902719, 0.806587554433065956, 0.852973136969303991],
[0.871453266226294265, 0.811988877360255046, 0.856730085707727351],
[0.875009832914259822, 0.817401595486718424, 0.860510267138810070],
[0.878589072990241582, 0.822825858208036554, 0.864313875224555606],
[0.882191273133587028, 0.828261811991224617, 0.868141110066802835],
[0.885816727830318840, 0.833709600132787942, 0.871992178392069439],
[0.889465740119111947, 0.839169362475972513, 0.875867294100413196],
[0.893138622438534369, 0.844641235080280328, 0.879766678889470355],
[0.896835697593800219, 0.850125349834800148, 0.883690562967284654],
[0.900557299865552552, 0.855621834004915649, 0.887639185870617964],
[0.904303776288404304, 0.861130809699522937, 0.891612797409389812],
[0.908075488133790909, 0.866652393242684838, 0.895611658762972107],
[0.911872812640567521, 0.872186694429477050, 0.899636043760651871],
[0.915696145048401688, 0.877733815640378112, 0.903686240387282291],
[0.919545901004442556, 0.883293850781267653, 0.907762552566635295],
[0.923422519434572209, 0.888866884006367708, 0.911865302290507884],
[0.927326465998776994, 0.894452988168198959, 0.915994832182756791],
[0.931258237289460555, 0.900052222920167400, 0.920151508616714131],
[0.935218365986431155, 0.905664632371604217, 0.924335725545560094],
[0.939207427261257166, 0.911290242157956842, 0.928547909264161198],
[0.943226046838632537, 0.916929055734740706, 0.932788524406919284],
[0.947274911294275657, 0.922581049622962945, 0.937058081614718041],
[0.951354781432042995, 0.928246167209762718, 0.941357147500986868],
[0.955466509997624613, 0.933924310512578737, 0.945686357857370319],
[0.959611065661918894, 0.939615328996462607, 0.950046435545475520],
[0.963789566350741755, 0.945319003994523510, 0.954438215377914623],
[0.968003327022871951, 0.951035026325120048, 0.958862679809655893],
[0.972253930784014675, 0.956762962910795989, 0.963321012098635632],
[0.976543339781731024, 0.962502204630854785, 0.967814679262416822],
[0.980874078712117625, 0.968251879887575329, 0.972345569450571490],
[0.985249563301498266, 0.974010699651702283, 0.976916238021737660],
[0.989674756434781089, 0.979776647499365327, 0.981530399431968958],
[0.994157715792150509, 0.985546247458993441, 0.986194088342931319],
[0.998714494489260862, 0.991312242299456137, 0.990919339219584194],
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
