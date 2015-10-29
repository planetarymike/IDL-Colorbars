from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.00031431840107123857, 0.00034776939602637743, 0.00038081684886509027],
[0.00086907153305176691, 0.0010039219614071610, 0.0011355586463693299],
[0.0016363264305419389, 0.0019545278462881435, 0.0022651577238770554],
[0.00258832, 0.0031836361732822662, 0.0037666882242970629],
[0.0037050372527372665, 0.0046816184141418391, 0.0056424931048027847],
[0.0049705825666087854, 0.0064421026960358903, 0.0078975613544209500],
[0.0063716413480329583, 0.00846068, 0.010538475509096508],
[0.0078966370434207962, 0.010734262997826470, 0.0135729],
[0.0095352462914609550, 0.0132607, 0.017009256993987139],
[0.011278087779458936, 0.016038403415912717, 0.020856618738008342],
[0.013116512472606864, 0.0190665, 0.025124523445133346],
[0.015042456102935158, 0.022344453493046618, 0.029822930561937432],
[0.017048332005262616, 0.025872010661814444, 0.034962156757968502],
[0.019126951249054794, 0.029649252823447343, 0.040551001904451524],
[0.021271461901570542, 0.033676477494272217, 0.046253491393475461],
[0.023475302104066533, 0.037954177342288516, 0.0519366],
[0.025732163377644741, 0.042420297945381817, 0.057604646153007567],
[0.028035961673701117, 0.046846619385783543, 0.063261446269254173],
[0.030380814402285163, 0.051233103499331890, 0.068910241249150572],
[0.032761022154855511, 0.055583046442552027, 0.074553870745247552],
[0.035171054170972549, 0.059899368093278650, 0.080194820749621809],
[0.037605536832997749, 0.064184669652601667, 0.0858353],
[0.040059244641252045, 0.068441280223824757, 0.091477161510956750],
[0.042462404204985309, 0.072671294860216840, 0.097122177845380742],
[0.044788750240400695, 0.076876605931037623, 0.10277182805174653],
[0.047045462160091846, 0.0810589, 0.10842744136690716],
[0.049234111661767339, 0.085219825658095827, 0.11409019238904700],
[0.051356127695512475, 0.089360719982094022, 0.11976111723960245],
[0.053412815032280230, 0.093482916163842550, 0.12544112719484143],
[0.055405370358093335, 0.097587610901143623, 0.13113102024962517],
[0.0573349, 0.10167590509223751, 0.13683149097967084],
[0.059202413967814178, 0.10574881376917361, 0.14254313899490709],
[0.061008873603811943, 0.10980727472303792, 0.14826647621948980],
[0.062755164729926788, 0.11385215602846879, 0.15400193318955163],
[0.064442124828481578, 0.11788426263696142, 0.15975],
[0.066070547409426889, 0.12190434217833410, 0.16551055370198695],
[0.067641189365964027, 0.12591309008562412, 0.17128421723734782],
[0.069154777763558328, 0.12991115413928556, 0.17707100836486542],
[0.070612016157253710, 0.13389913851082744, 0.18287102028586560],
[0.072013590518315795, 0.13787760737321458, 0.18868428905130155],
[0.073360174839850800, 0.141847, 0.19451079612970723],
[0.074652436481741691, 0.14580807434529505, 0.20035047070556999],
[0.075891041307502016, 0.14976102831369101, 0.20620319174638629],
[0.077076658659269354, 0.15370638347493171, 0.21206878987123789],
[0.078209966211768456, 0.15764454653357088, 0.217947],
[0.0792917, 0.16157589941131617, 0.22383770815205528],
[0.080322432844450869, 0.16550080102040204, 0.22974],
[0.081303031629136879, 0.16941958888215053, 0.23565496459761981],
[0.082234209415334131, 0.17333258060748596, 0.24158082654001473],
[0.083116756458256724, 0.17724007525400556, 0.24751761999748500],
[0.083951499722016765, 0.18114235457235564, 0.25346487789718736],
[0.084739307720805818, 0.18503968415307523, 0.25942209534940913],
[0.085481095445001015, 0.18893231448369754, 0.26538873064947666],
[0.086177829387148214, 0.19282048192472401, 0.27136420624674007],
[0.086830532680552019, 0.19670440961205998, 0.27734790968842277],
[0.087440290360787765, 0.20058430829262258, 0.28333919454526774],
[0.088008254757897086, 0.20446037709905002, 0.28933738132516495],
[0.088535651024031686, 0.20833280426878770, 0.29534175838027554],
[0.089023782798092060, 0.21220176781222400, 0.301352],
[0.089474038005075723, 0.21606743613405144, 0.30736608138213095],
[0.089887894783551359, 0.21992996861157443, 0.31338445142220855],
[0.090266927529752239, 0.22378951613329284, 0.31940586176431546],
[0.090612813041007045, 0.227646, 0.32542945367657467],
[0.090927336734850289, 0.23150022039635659, 0.331454],
[0.091212398912629528, 0.23535164081952031, 0.33747961521030217],
[0.091470021028160292, 0.23920060449343095, 0.34350433823154092],
[0.091702351912525237, 0.24304722674432427, 0.34952755162946392],
[0.091911673895699320, 0.24689161695512801, 0.35554827355982460],
[0.092100408754103330, 0.250734, 0.36156550064851534],
[0.092271123400672395, 0.25457411102704663, 0.36757820907919492],
[0.092426535220476780, 0.25841240679329763, 0.37358535570696472],
[0.092569516940655516, 0.26224885488209004, 0.37958587919852421],
[0.092703100908559266, 0.26608353947519497, 0.38557870119902177],
[0.092830482636933581, 0.26991654047812563, 0.39156272752560184],
[0.092955023460183167, 0.27374793373390233, 0.39753684938744760],
[0.0930803, 0.277578, 0.40349994463192274],
[0.093209865180121865, 0.28140618123907196, 0.409451],
[0.093347725831327999, 0.28523316857538655, 0.41538850750381373],
[0.093497861298470652, 0.28905881466610389, 0.42131167558459026],
[0.093664458237674386, 0.29288317773995776, 0.42721922061786755],
[0.093851856172883552, 0.29670631295310074, 0.43310997319672095],
[0.094064538703020756, 0.30052827251324027, 0.43898275853239277],
[0.094307122323917497, 0.30434910579420654, 0.44483639785715629],
[0.0945843, 0.308169, 0.45066970984394500],
[0.094901038465781434, 0.31198757747089007, 0.45648151204091864],
[0.0952621, 0.31580530135675811, 0.46227062231900956],
[0.095672607829239448, 0.31962207011759641, 0.46803586033038919],
[0.096137488601634152, 0.32343792039264607, 0.47377604897567299],
[0.096661808053241344, 0.32725288651438950, 0.47949001587760504],
[0.097250582304560879, 0.33106700057622024, 0.48517659485885317],
[0.097908779076798402, 0.33488029249615975, 0.49083462742148681],
[0.098641285500534553, 0.33869279007725511, 0.49646296422562314],
[0.099452874979680195, 0.34250451906531659, 0.50206046656468095],
[0.10034817368248120, 0.34631550320461552, 0.50762600783461986],
[0.10133162728849970, 0.35012576429215397, 0.51315847499450862],
[0.10240746865790579, 0.35393532223111673, 0.51865677001574118],
[0.10357968710355167, 0.35774419508407374, 0.52412],
[0.10485199993382011, 0.36155239912650972, 0.52954653518354122],
[0.10622782689469187, 0.36535994890121337, 0.53493589716424261],
[0.10771026807273426, 0.36916685727405935, 0.54028687345010795],
[0.10930208572984856, 0.37297313549166444, 0.54559846222515473],
[0.11100569042896977, 0.37677879324140501, 0.55086968499087030],
[0.11282313168402008, 0.38058383871422535, 0.55609958786035429],
[0.11475609323286864, 0.384388, 0.56128724281977727],
[0.11680589289663223, 0.38819211851042473, 0.56643174895466064],
[0.11897348685918055, 0.39199536234600713, 0.57153223363856753],
[0.12125947808312731, 0.39579801308042695, 0.57658785368185783],
[0.123664, 0.39960007248958690, 0.58159779643826681],
[0.12618737436400415, 0.40340154130937472, 0.58656128086715609],
[0.12882884469619976, 0.40720241932773466, 0.59147755854939132],
[0.13158788152902023, 0.41100270548188028, 0.59634591465492481],
[0.13446356213413502, 0.41480239796076052, 0.60116566886026579],
[0.13745472224350408, 0.41860149431286658, 0.60593617621416651],
[0.14055997989592703, 0.42239999155942115, 0.61065682794997178],
[0.14377775941581442, 0.42619788631294658, 0.61532705224322304],
[0.14710631510581876, 0.42999517490117955, 0.61994631491325680],
[0.15054375429509478, 0.433792, 0.62451412006766516],
[0.154088, 0.43758791824897070, 0.62903001068866959],
[0.15773710909804525, 0.44138336542820106, 0.633494],
[0.16148869744051989, 0.44517819156488309, 0.63790441773765283],
[0.165341, 0.448972, 0.642262],
[0.16929035249866600, 0.45276596904116412, 0.64656667596064321],
[0.17333574134214486, 0.45655891611228211, 0.65081753283286192],
[0.17747434165326032, 0.46035123392145833, 0.65501457477574754],
[0.18170376697452703, 0.46414292262128315, 0.65915762830006797],
[0.18602163225235296, 0.46793398357642196, 0.66324656132554694],
[0.19042556299833679, 0.47172441953299354, 0.66728128322636193],
[0.19491320317323557, 0.47551423479004312, 0.671262],
[0.19948222189175807, 0.47930343537265968, 0.675188],
[0.20413031904984397, 0.48309202920626876, 0.67905989704141845],
[0.20885522997665529, 0.48688002629163168, 0.68287769556932998],
[0.21365472921168643, 0.49066743888005621, 0.68664144914820746],
[0.21852663350366230, 0.49445428164832578, 0.69035131357332102],
[0.22346880412297510, 0.49824057187284304, 0.69400748480292052],
[0.22847914857343554, 0.50202632960248783, 0.69761019855701178],
[0.23355562178276612, 0.50581157782968111, 0.70115972986616371],
[0.23869622684447656, 0.50959634265916243, 0.70465639257200519],
[0.24389901537709069, 0.51338065347397832, 0.70810053878116763],
[0.24916208756009584, 0.51716454309820092, 0.71149255827451163],
[0.25448359189952385, 0.52094804795589933, 0.71483287787354211],
[0.259862, 0.52473120822590447, 0.71812196076599233],
[0.26529472977610946, 0.52851406799191714, 0.72136030579261024],
[0.27078089696468000, 0.53229667538753012, 0.72454844669723018],
[0.27631856192711374, 0.536079, 0.72768695134226868],
[0.28190610481118578, 0.53986134668267083, 0.73077642089179473],
[0.28754194927028082, 0.543644, 0.73381748896437648],
[0.29322456136829045, 0.54742569332996394, 0.73681082075791660],
[0.29895244845720548, 0.55120791205106712, 0.739757],
[0.30472415804140590, 0.55499025963288961, 0.74265708876686032],
[0.310538, 0.55877281611125618, 0.74551150505058872],
[0.31639342865936609, 0.56255566650457323, 0.74832114328114307],
[0.32228827527590415, 0.56633890089744421, 0.75108681260103594],
[0.32822151334822175, 0.57012261451620583, 0.75380934801748512],
[0.334192, 0.57390690779622944, 0.75648960939331778],
[0.340198, 0.577692, 0.75912848042746805],
[0.34623905795218923, 0.58147766147200675, 0.76172686762714570],
[0.35231350744250167, 0.58526434927200233, 0.76428569927373513],
[0.35842033175077720, 0.58905207161724527, 0.76680592438443040],
[0.364558, 0.59284095570307438, 0.769289],
[0.37072669270393199, 0.59663113416023050, 0.77173444850149919],
[0.37692409482396560, 0.600423, 0.77414473985503007],
[0.38314960111363494, 0.60421593192807011, 0.77652040729090255],
[0.38940221231032263, 0.60801084370738912, 0.77886248791434942],
[0.39568095503693695, 0.61180763476985067, 0.78117203335219088],
[0.40198488112441100, 0.61560646487725768, 0.78345],
[0.40831306696629494, 0.61940749915156179, 0.78569779169571752],
[0.41466461290403661, 0.62321090803462975, 0.78791617136255243],
[0.42103864264150864, 0.62701686724060413, 0.79010634738690422],
[0.42743430268729699, 0.63082555770108750, 0.792269],
[0.43385076182327798, 0.63463716550340410, 0.79440653390090143],
[0.44028721059793313, 0.63845188182220525, 0.79651878763576034],
[0.44674286084299980, 0.64226990284469876, 0.79860732235956433],
[0.45321694521194394, 0.64609142968979594, 0.80067327609237049],
[0.45970871673887875, 0.64991666832148898, 0.80271779180440206],
[0.46621744841652363, 0.65374582945676474, 0.80474201655307698],
[0.47274243279187839, 0.657579, 0.80674710064105726],
[0.47928298157836274, 0.66141678528294234, 0.80873419679606007],
[0.48583842528310178, 0.66525902427427153, 0.81070445937313440],
[0.492408, 0.66910607415301659, 0.81265904358001584],
[0.49899141130540764, 0.67295816785225437, 0.81459910472614361],
[0.50558770544123100, 0.676816, 0.81652579749584542],
[0.51219639747468682, 0.68067843884744417, 0.81844027524615048],
[0.518817, 0.68454710204756808, 0.82034368932963975],
[0.52544866939940504, 0.68842178062737491, 0.822237],
[0.53209113811221642, 0.692303, 0.82412191799946088],
[0.53874378177986748, 0.69619019630133905, 0.82599901953179144],
[0.54540608524568623, 0.70008444814732096, 0.82786963011542603],
[0.55207754902089878, 0.70398574461474472, 0.82973488182258426],
[0.55875768901204537, 0.70789435105326592, 0.83159590120115900],
[0.56544603625256895, 0.71181053576455200, 0.83345380878065545],
[0.57214213663788338, 0.71573456987039163, 0.83530971860498537],
[0.57884555066329502, 0.71966672718133717, 0.83716473779223788],
[0.58555585316414238, 0.72360728406621233, 0.83901996612150387],
[0.59227263305757571, 0.72755651932282706, 0.84087649564684708],
[0.59899549308534117, 0.731515, 0.84273541033849730],
[0.60572404955699788, 0.735482, 0.84459778575135125],
[0.61245793209301969, 0.73945911706690093, 0.846465],
[0.61919678336715134, 0.74344589793904747, 0.84833717708647482],
[0.62594025884744908, 0.74744278320836477, 0.850216],
[0.63268802653541301, 0.75145006364111910, 0.85210309491748559],
[0.63943976670256664, 0.75546803158920917, 0.85399859298003289],
[0.64619517162385154, 0.75949698088241624, 0.855904],
[0.65295394530716277, 0.76353720672481684, 0.85781976548563899],
[0.65971580321826728, 0.767589, 0.85974744922807789],
[0.66648047200038407, 0.77165267515536773, 0.86168785397123349],
[0.67324768918752853, 0.77572851415602206, 0.86364195898949270],
[0.68001720291075851, 0.77981682235838457, 0.86561073334480698],
[0.68678877159627760, 0.78391790045414433, 0.86759513590033066],
[0.69356216365434731, 0.78803204999480803, 0.869596],
[0.70033715715767697, 0.79215957332734921, 0.87161461037968957],
[0.70711353950804246, 0.79630077353708883, 0.87365154961775437],
[0.713891, 0.80045595439835093, 0.87570785194907930],
[0.72066966490621931, 0.80462542033341133, 0.87778442662195733],
[0.72744902620386853, 0.80880947638036083, 0.87988217349351960],
[0.73422901207065438, 0.813008, 0.88200198330179558],
[0.74100945101706483, 0.81722258191636321, 0.88414473798380633],
[0.74779017853032914, 0.82145224441020903, 0.88631131104327932],
[0.75457103660045255, 0.82569772303563049, 0.88850256797221150],
[0.76135187321378461, 0.82995932579171794, 0.89071936673126650],
[0.76813254180941459, 0.83423736133206350, 0.89296255829490956],
[0.77491290069294538, 0.83853213901976065, 0.89523298726824929],
[0.78169281240117516, 0.84284396900018810, 0.89753149258388920],
[0.78847214301011148, 0.84717316229362061, 0.899859],
[0.79525076137727191, 0.85152, 0.90221606443204150],
[0.802029, 0.85588488798938322, 0.90460378807039798],
[0.80880534562947126, 0.86026804796957213, 0.90702290440415123],
[0.81558105516708390, 0.86466982678831328, 0.90947423806848060],
[0.82235553758722280, 0.86909054212185199, 0.91195861460271699],
[0.82912866110045957, 0.87353051366792256, 0.91447686212920032],
[0.83590028998655352, 0.87799006348006026, 0.91702981327949718],
[0.84267028290957280, 0.88246951636265503, 0.919618],
[0.84943849097877300, 0.88696920033840154, 0.92224319320067249],
[0.85620475550006003, 0.89148944720278900, 0.92490533160597144],
[0.86296890534790072, 0.89603059318424427, 0.92760559942710585],
[0.86973075386763454, 0.90059297973381047, 0.93034489345148053],
[0.87649009519139998, 0.90517695447532254, 0.93312413542118189],
[0.88324669981431336, 0.90978287235671373, 0.93594427800148294],
[0.89000030922681084, 0.914411, 0.93880631202834430],
[0.896751, 0.91906200271823058, 0.94171127540465338],
[0.903497, 0.92373597611298430, 0.94466026415216509],
[0.91023999600666805, 0.928433, 0.94765444632674123],
[0.916978, 0.93315475346628340, 0.95069507980448054],
[0.92371136476843252, 0.93790042278698838, 0.95378353540636274],
[0.930439, 0.942671, 0.956921],
[0.93715990405820770, 0.94746669999038680, 0.96011015584175119],
[0.94387351106496564, 0.95228837975967762, 0.963352],
[0.95057847330697121, 0.95713656626875399, 0.96664901744904952],
[0.95727324241245937, 0.96201197506916170, 0.970004],
[0.96395579011755184, 0.96691544952254260, 0.97342038824639043],
[0.97062336831431251, 0.97184802389698233, 0.97690239485854258],
[0.97727207804921601, 0.97681103649150536, 0.98045592765126799],
[0.983896, 0.98180635596748311, 0.98408955249353036],
[0.99048517697176497, 0.98683691610502200, 0.987817],
[0.99701905657590883, 0.99190841212882452, 0.99166715078004997],
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
