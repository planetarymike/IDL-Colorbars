from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000198725080239126838, 0.0000195868017889189583, 0.0000195292895369690181],
[0.000335073214124412939, 0.000347498713171894491, 0.000304386410307293644],
[0.000950226282087409508, 0.00100258518797276784, 0.000839054588200738001],
[0.00182566226596878110, 0.00195090190913076102, 0.00157768804001528974],
[0.00294056684250323030, 0.00317609221528771055, 0.00249440243009106839],
[0.00428116315959378019, 0.00466813309864542395, 0.00357109879654545328],
[0.00583737731917731255, 0.00642026606243710930, 0.00479387568078331640],
[0.00760140839220156596, 0.00842770593313794426, 0.00615145499582860165],
[0.00956698495625761709, 0.0106869798173149701, 0.00763434915655891895],
[0.0117289305301942880, 0.0131955458235708915, 0.00923436710632636465],
[0.0140828883925003777, 0.0159515544920062445, 0.0109442975459624007],
[0.0166251368126174720, 0.0189536903550856124, 0.0127576938493387266],
[0.0193524592927130194, 0.0222010618029723078, 0.0146687214861547684],
[0.0222620501420838710, 0.0256931217098729792, 0.0166720459660707095],
[0.0253514437475298344, 0.0294296085265656378, 0.0187627481897578163],
[0.0286184603073002461, 0.0334105014865784325, 0.0209362589911354265],
[0.0320611633459152862, 0.0376359858407600695, 0.0231883075122528287],
[0.0356778258723123090, 0.0420595413394144121, 0.0255148797958062064],
[0.0394669030168980917, 0.0464491809830734417, 0.0279121850854609464],
[0.0433164935269793258, 0.0507976302546709821, 0.0303766280478055817],
[0.0471093219763570395, 0.0551082465553876313, 0.0329047856170841535],
[0.0508581059434524210, 0.0593840126422080852, 0.0354933875001603866],
[0.0545656907869269472, 0.0636275942743728673, 0.0381392996163228207],
[0.0582346346706288861, 0.0678413868243615270, 0.0408318700586662100],
[0.0618672486205698244, 0.0720275533472093388, 0.0434711268606494325],
[0.0654656295854762482, 0.0761880559591972539, 0.0460590080975389546],
[0.0690316879506205627, 0.0803246819186830829, 0.0485975187533718503],
[0.0725671706105844583, 0.0844390654701223653, 0.0510884854394826268],
[0.0760736804538361122, 0.0885327062688479605, 0.0535335771718816120],
[0.0795526929238981606, 0.0926069850231850955, 0.0559343230550960260],
[0.0830055701802725199, 0.0966631768543516345, 0.0582921274219678279],
[0.0864335732745045993, 0.100702462771101758, 0.0606082828663239773],
[0.0898378726739412770, 0.104725939576592097, 0.0628839815187829387],
[0.0932195574014669237, 0.108734628463346972, 0.0651203248486476593],
[0.0965796430091968861, 0.112729482504041578, 0.0673183322220850255],
[0.0999190785644512303, 0.116711393207855285, 0.0694789484051354100],
[0.103238752794781480, 0.120681196282002773, 0.0716030501669323305],
[0.106539499513583408, 0.124639676713937914, 0.0736914521119408639],
[0.109822102427485496, 0.128587573270309563, 0.0757449118485808703],
[0.113087299410209619, 0.132525582493014937, 0.0777641345841935672],
[0.116335786314131190, 0.136454362259880363, 0.0797497772220943924],
[0.119568220379747375, 0.140374534966982795, 0.0817024520247782993],
[0.122785223294145540, 0.144286690380968835, 0.0836227298977073874],
[0.125987383942018388, 0.148191388202557950, 0.0855111433401111731],
[0.129175260886501775, 0.152089160376447874, 0.0873681891025641089],
[0.132349384611855525, 0.155980513177846586, 0.0891943305855193158],
[0.135510259555571971, 0.159865929101680404, 0.0909900000082831950],
[0.138658365953807206, 0.163745868576984255, 0.0927556003739480883],
[0.141794161520849171, 0.167620771526001744, 0.0944915072524372956],
[0.144918082980667578, 0.171491058784982192, 0.0961980704009534893],
[0.148030547466301759, 0.175357133401499749, 0.0978756152386798528],
[0.151131953800895308, 0.179219381821265233, 0.0995244441904818422],
[0.154222683672475047, 0.183078174975824876, 0.101144837912561209],
[0.157303102713174298, 0.186933869281155934, 0.102737056411453864],
[0.160373561492293482, 0.190786807556005522, 0.104301340066418530],
[0.163434396431550555, 0.194637319867785596, 0.105837910564095722],
[0.166485930649913794, 0.198485724312953027, 0.107346971753294412],
[0.169528474744580382, 0.202332327738032169, 0.108828710426880471],
[0.172562327513961805, 0.206177426406761732, 0.110283297036954886],
[0.175587776627918191, 0.210021306618250359, 0.111710886348834582],
[0.178605099249889709, 0.213864245280523391, 0.113111618038735817],
[0.181614562615145220, 0.217706510443367085, 0.114485617239535625],
[0.184616424568896986, 0.221548361793993065, 0.115832995038511966],
[0.187610934067672375, 0.225390051118679713, 0.117153848930542426],
[0.190598331646998964, 0.229231822733238111, 0.118448263229871259],
[0.193578849858151686, 0.233073913884873252, 0.119716309443215124],
[0.196552713676459823, 0.236916555127757777, 0.120958046606686076],
[0.199520140883425123, 0.240759970674424617, 0.122173521588730904],
[0.202481342424705224, 0.244604378724878779, 0.123362769361051644],
[0.205436522745815642, 0.248449991775161139, 0.124525813239243111],
[0.208385880107242183, 0.252297016906936233, 0.125662665094689457],
[0.211329606880512721, 0.256145656059535487, 0.126773325539071391],
[0.214267889826624702, 0.259996106285762141, 0.127857784082671677],
[0.217200910358117449, 0.263848559992651222, 0.128916019267506954],
[0.220128844785967615, 0.267703205168271952, 0.129947998776172330],
[0.223051864552373247, 0.271560225595574745, 0.130953679517145316],
[0.225970136450431125, 0.275419801054190006, 0.131933007687174669],
[0.228883822831584094, 0.279282107511028388, 0.132885918811250586],
[0.231793081801707324, 0.283147317300441736, 0.133812337760548045],
[0.234698067406568234, 0.287015599294661972, 0.134712178748615158],
[0.237598929807380066, 0.290887119065168398, 0.135585345305975463],
[0.240495815447100858, 0.294762039035581513, 0.136431730233211895],
[0.243388867208069182, 0.298640518626644980, 0.137251215532486981],
[0.246278224561541581, 0.302522714393802350, 0.138043672317363975],
[0.249164023709636584, 0.306408780157844785, 0.138808960700679801],
[0.252046397720168347, 0.310298867129069122, 0.139546929660120667],
[0.254925476654796757, 0.314193124025353654, 0.140257416881050645],
[0.257801387690919426, 0.318091697184523514, 0.140940248576022220],
[0.260674255237676178, 0.321994730671358309, 0.141595239280295382],
[0.263544201046410020, 0.325902366379570152, 0.142222191622569660],
[0.266411344315927390, 0.329814744129046322, 0.142820896070007891],
[0.269275801792852987, 0.333732001758643482, 0.143391130646504189],
[0.272137687867364586, 0.337654275214792077, 0.143932660623001002],
[0.274997114664575271, 0.341581698636155062, 0.144445238178521951],
[0.277854192131803124, 0.345514404434570543, 0.144928602030415937],
[0.280709028121968129, 0.349452523372483781, 0.145382477032141993],
[0.283561728473327668, 0.353396184637076338, 0.145806573736736417],
[0.286412397085745674, 0.357345515911270117, 0.146200587923894537],
[0.289261135993693186, 0.361300643441781255, 0.146564200088383528],
[0.292108045436156427, 0.365261692104388358, 0.146897074887255869],
[0.294953223923605456, 0.369228785466565124, 0.147198860543061805],
[0.297796768302197756, 0.373202045847618902, 0.147469188199974705],
[0.300638773815341209, 0.377181594376472917, 0.147707671229401177],
[0.303479334162773173, 0.381167551047210951, 0.147913904481304842],
[0.306318541557269230, 0.385160034772509374, 0.148087463477058256],
[0.309156486779101569, 0.389159163435063127, 0.148227903539200040],
[0.311993259228382558, 0.393165053937109932, 0.148334758852975035],
[0.314828946975364399, 0.397177822248152956, 0.148407541453978914],
[0.317663636808825645, 0.401197583450971729, 0.148445740135611903],
[0.320497414282629123, 0.405224451786011075, 0.148448819269341448],
[0.323330363760535477, 0.409258540694226069, 0.148416217529995037],
[0.326162568459356650, 0.413299962858466763, 0.148347346517420015],
[0.328994110490546721, 0.417348830243468139, 0.148241589264839602],
[0.331825070900279850, 0.421405254134519625, 0.148098298623113328],
[0.334655529708096922, 0.425469345174878832, 0.147916795508818727],
[0.337485565944201704, 0.429541213401987254, 0.147696367002608714],
[0.340315257685441574, 0.433620968282553698, 0.147436264282641089],
[0.343144682090055553, 0.437708718746551317, 0.147135700375957135],
[0.345973915431247558, 0.441804573220188290, 0.146793847708519887],
[0.348803033129611417, 0.445908639657899786, 0.146409835432097013],
[0.351632109784496327, 0.450021025573402345, 0.145982746503295319],
[0.354461219204333156, 0.454141838069866688, 0.145511614486705326],
[0.357290434435977189, 0.458271183869239873, 0.144995420050250012],
[0.360119827793114022, 0.462409169340764759, 0.144433087116325937],
[0.362949470883764169, 0.466555900528730139, 0.143823478627093881],
[0.365779434636928358, 0.470711483179491352, 0.143165391876122788],
[0.368609789328412540, 0.474876022767793782, 0.142457553351413746],
[0.371440604605863978, 0.479049624522431994, 0.141698613026333658],
[0.374943338894884293, 0.482902042749876970, 0.145096869005604506],
[0.379126118798819300, 0.486427335645189418, 0.152596522614045382],
[0.383320242701764735, 0.489953985662909097, 0.159983262560861178],
[0.387525699629540810, 0.493482148814949617, 0.167271236161050441],
[0.391742479337765126, 0.497011981351346110, 0.174472378707238002],
[0.395970572343048777, 0.500543639758163739, 0.181596848167845631],
[0.400209969952501521, 0.504077280755486301, 0.188653357571123004],
[0.404460664291628413, 0.507613061295489665, 0.195649432844140658],
[0.408722648330699934, 0.511151138560614227, 0.202591615421182813],
[0.412995915909690092, 0.514691669961832798, 0.209485623311692182],
[0.417280461761845633, 0.518234813137027239, 0.216336480497652639],
[0.421576281535957276, 0.521780725949481550, 0.223148621886225751],
[0.425883371817414369, 0.525329566486493205, 0.229925979182040052],
[0.430201730148083994, 0.528881493058119601, 0.236672051712680520],
[0.434531355045090328, 0.532436664196058951, 0.243389965275856601],
[0.438872246018528200, 0.535995238652680506, 0.250082521367736621],
[0.443224403588201143, 0.539557375400205763, 0.256752238624855633],
[0.447587829299372075, 0.543123233630060986, 0.263401387915759011],
[0.451962525737628906, 0.546692972752393591, 0.270032022217624901],
[0.456348496542885951, 0.550266752395772274, 0.276646002182390382],
[0.460745746422533797, 0.553844732407081763, 0.283245018118416403],
[0.465154281163837002, 0.557427072851606531, 0.289830608974524562],
[0.469574107645539807, 0.561013934013332105, 0.296404178803808094],
[0.474005233848781848, 0.564605476395454886, 0.302967011097966921],
[0.478447668867304776, 0.568201860721119889, 0.309520281313841184],
[0.482901422916999057, 0.571803247934397851, 0.316065067858388671],
[0.487366507344835609, 0.575409799201494154, 0.322602361753590583],
[0.491842934637154838, 0.579021675912224532, 0.329133075166457234],
[0.496330718427399675, 0.582639039681741799, 0.335658048959611432],
[0.500829873503272127, 0.586262052352539587, 0.342178059393614009],
[0.505340415813341659, 0.589890875996735287, 0.348693824092099536],
[0.509862362473141317, 0.593525672918644665, 0.355206007364168352],
[0.514395731770746711, 0.597166605657654226, 0.361715224964637372],
[0.518940543171866220, 0.600813836991406780, 0.368222048361181775],
[0.523496817324455077, 0.604467529939307191, 0.374727008567701414],
[0.528064576062864721, 0.608127847766357532, 0.381230599595056674],
[0.532643842411536395, 0.611794953987333079, 0.387733281563416965],
[0.537234640588265089, 0.615469012371314350, 0.394235483514595142],
[0.541836996007005856, 0.619150186946580416, 0.400737605957745269],
[0.546450935280284988, 0.622838642005877574, 0.407240023177544042],
[0.551076486221167006, 0.626534542112074488, 0.413743085330309568],
[0.555713677844819287, 0.630238052104221458, 0.420247120350384362],
[0.560362540369670814, 0.633949337104016575, 0.426752435686394316],
[0.565023105218135480, 0.637668562522705318, 0.433259319884651217],
[0.569695405016966694, 0.641395894068413686, 0.439768044034958394],
[0.574379473597170009, 0.645131497753939853, 0.446278863092292644],
[0.579075345993513180, 0.648875539905021781, 0.452792017086317167],
[0.583783058443631320, 0.652628187169079776, 0.459307732229332688],
[0.588502648386687421, 0.656389606524481084, 0.465826221932107598],
[0.593234154461622976, 0.660159965290309625, 0.472347687735984067],
[0.597977616504965947, 0.663939431136689517, 0.478872320168770404],
[0.602733075548163244, 0.667728172095673034, 0.485400299531108914],
[0.607500573814484635, 0.671526356572704097, 0.491931796619327899],
[0.612280154715417413, 0.675334153358698841, 0.498466973390134294],
[0.617071862846573782, 0.679151731642755219, 0.505005983571970352],
[0.621875743983062890, 0.682979261025528084, 0.511548973227351378],
[0.626691845074337395, 0.686816911533286056, 0.518096081270063014],
[0.631520214238450173, 0.690664853632696030, 0.524647439940707172],
[0.636360900755702619, 0.694523258246358521, 0.531203175243718295],
[0.641213955061679330, 0.698392296769130394, 0.537763407348674449],
[0.646079428739573580, 0.702272141085281576, 0.544328250958419635],
[0.650957374511820786, 0.706162963586514314, 0.550897815646263722],
[0.655847846230944387, 0.710064937190910794, 0.557472206164292050],
[0.660750898869594372, 0.713978235362835112, 0.564051522724593801],
[0.665666588509695290, 0.717903032133863861, 0.570635861255023302],
[0.670594972330668004, 0.721839502124789423, 0.577225313630928549],
[0.675536108596613394, 0.725787820568773334, 0.583819967884105617],
[0.680490056642413243, 0.729748163335709687, 0.590419908390088843],
[0.685456876858650421, 0.733720706957879054, 0.597025216034722583],
[0.690436630675223539, 0.737705628656980750, 0.603635968360839437],
[0.695429380543596931, 0.741703106372634702, 0.610252239695714405],
[0.700435189917513745, 0.745713318792449731, 0.616874101259847651],
[0.705454123232076236, 0.749736445383781480, 0.623501621257492422],
[0.710486245880999512, 0.753772666427301785, 0.630134864949221884],
[0.715531624191934057, 0.757822163052509268, 0.636773894706697541],
[0.720590325399600440, 0.761885117275347912, 0.643418770049676625],
[0.725662417616569688, 0.765961712038101039, 0.650069547665157787],
[0.730747969801447739, 0.770052131251745986, 0.656726281408428703],
[0.735847051724195400, 0.774156559840982972, 0.663389022285629459],
[0.740959733928289510, 0.778275183792187408, 0.670057818417291062],
[0.746086087689388888, 0.782408190204541221, 0.676732714982133721],
[0.751226184970141042, 0.786555767344647938, 0.683413754140227980],
[0.756380098370697973, 0.790718104704971947, 0.690100974934410027],
[0.761547901074462463, 0.794895393066481160, 0.696794413168616567],
[0.766729666788525832, 0.799087824565932525, 0.703494101261542548],
[0.771925469678145459, 0.803295592768294431, 0.710200068073729152],
[0.777135384294618925, 0.807518892744853112, 0.716912338705861463],
[0.782359485495662255, 0.811757921157669871, 0.723630934265654169],
[0.787597848357421859, 0.816012876351106975, 0.730355871600263939],
[0.792850548077021156, 0.820283958451275885, 0.737087162990644584],
[0.798117659864403750, 0.824571369474385585, 0.743824815803637351],
[0.803399258822019346, 0.828875313445129769, 0.750568832096881189],
[0.808695419810723126, 0.833195996526417293, 0.757319208170752822],
[0.814006217299857004, 0.837533627162004635, 0.764075934060532314],
[0.819331725199274996, 0.841888416233817827, 0.770838992960764746],
[0.824672016670573660, 0.846260577236098044, 0.777608360572298762],
[0.830027163914321742, 0.850650326468885942, 0.784384004360696441],
[0.835397237929449088, 0.855057883253841689, 0.791165882712513202],
[0.840782308240236698, 0.859483470175971931, 0.797953943973245261],
[0.846182442585416417, 0.863927313355566606, 0.804748125347428234],
[0.851597706562655654, 0.868389642755565960, 0.811548351637198295],
[0.857028163220379002, 0.872870692530678283, 0.818354533790447980],
[0.862473872586890233, 0.877370701426035127, 0.825166567223093117],
[0.867934891124550689, 0.881889913234970457, 0.831984329871595651],
[0.873411271093597508, 0.886428577327884271, 0.838807679921059091],
[0.878903059806413589, 0.890986949267180250, 0.845636453140168776],
[0.884410298747736023, 0.895565291527304241, 0.852470459735791497],
[0.889933022529579065, 0.900163874344201420, 0.859309480615545129],
[0.895471257640313767, 0.904782976725687971, 0.866153262913664679],
[0.901025020934857812, 0.909422887663969170, 0.873001514590570293],
[0.906594317795466398, 0.914083907605022228, 0.879853897854370959],
[0.912179139868282141, 0.918766350248470975, 0.886710021065142851],
[0.917779462245713718, 0.923470544778711488, 0.893569428657723153],
[0.923395239913735955, 0.928196838667549540, 0.900431588436052866],
[0.929026403206883677, 0.932945601247646916, 0.907295875319280021],
[0.934672851896992007, 0.937717228346405807, 0.914161550201929796],
[0.940334447357660141, 0.942512148412246731, 0.921027731931739924],
[0.946011001946604035, 0.947330830796973111, 0.927893359335540180],
[0.951702264240655294, 0.952173797250014497, 0.934757138406683841],
[0.957407897859534063, 0.957041638374369064, 0.941617466549684479],
[0.963127449934944813, 0.961935038090771299, 0.948472319762311833],
[0.968860301928670453, 0.966854811744089049, 0.955319076624554620],
[0.974605588234021103, 0.971801969093437301, 0.962154226919841205],
[0.980362050457899259, 0.976777826949848715, 0.968972849870817332],
[0.986127746348338774, 0.981784233939262063, 0.975767571596889982],
[0.991899363246954491, 0.986824100131226234, 0.982526105278599515],
[0.997670044249856614, 0.991903072400029839, 0.989223459681055073],
[1, 0.997043782662109357, 0.995755557520721202]]

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
