from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.00032810685327877727, 0.00035244089938882105, 0.00028353389105414294],
[0.00092102745855198625, 0.0010221442703086006, 0.00076304560430270668],
[0.0017526776458603533, 0.0019974298711579455, 0.0014106983865535276],
[0.0027955870339589207, 0.0032646029406948403, 0.0022005646679716909],
[0.0040289615550324559, 0.0048163378931693791, 0.0031154762229258191],
[0.0054353581639852754, 0.0066486356411903126, 0.0041431557724349328],
[0.0069992718606431050, 0.0087595421570431722, 0.0052744904280123284],
[0.0087064107481634040, 0.011148490089495719, 0.0065026072834087796],
[0.010543279625673932, 0.013815916795401570, 0.0078223206383264340],
[0.012496922119850616, 0.016763023348286599, 0.0092297757539827278],
[0.014554752352980513, 0.019991612715187162, 0.010722206553783540],
[0.016704440855262539, 0.023503975662244454, 0.012297764058227551],
[0.018933835188878707, 0.027302807049622142, 0.013955391125436081],
[0.021230903790473449, 0.031391142330808863, 0.015694728828843624],
[0.023583695928989311, 0.035772307963009564, 0.017516045227177247],
[0.025980313209052218, 0.0404499, 0.019420180463208855],
[0.028408889579697335, 0.045178970567043404, 0.021408504079065631],
[0.0308576, 0.049877122814552123, 0.0234829],
[0.033314540676901171, 0.054548074064156078, 0.025645648882962186],
[0.035767946708110863, 0.059195125752750120, 0.027899591081986520],
[0.038205968239618054, 0.0638212, 0.0302479],
[0.040613755956147725, 0.068428845115165393, 0.032694301233269177],
[0.042901689441373923, 0.073020386469656640, 0.035242767100356370],
[0.045070359817421433, 0.077597860302327598, 0.037897789295972317],
[0.047119173859416087, 0.082163097228081683, 0.040660284722193581],
[0.049047234247721456, 0.086717737887368002, 0.043429946481289374],
[0.050853349626455511, 0.091263254781083131, 0.0462055],
[0.052536039453002496, 0.095800970681629460, 0.048990499199659913],
[0.054093534007767515, 0.10033207425661106, 0.051788249241867833],
[0.055523769732574647, 0.10485763340580143, 0.054602],
[0.056824379884109273, 0.10937860670871893, 0.057434672226027099],
[0.057992680312448371, 0.11389585330081078, 0.0602893],
[0.059025649991848471, 0.11841014143475911, 0.063168695273877667],
[0.059919905729323646, 0.12292215593533490, 0.066075488694058049],
[0.060671670242137800, 0.12743250471833351, 0.069012277718430381],
[0.061276732511216105, 0.131942, 0.071981539576677328],
[0.061730398961643278, 0.13645028591149680, 0.074985654628927423],
[0.062027433563940242, 0.14095859782083137, 0.078026910534573057],
[0.062161984349292480, 0.14546701143447685, 0.081107505858240087],
[0.062127493028810050, 0.14997582375623006, 0.084229553194721390],
[0.0619166, 0.15448528075588400, 0.087395081881526337],
[0.061520922032256405, 0.15899558019890145, 0.090606040356732392],
[0.060931044986009118, 0.16350687419334270, 0.0938643],
[0.060136136512602974, 0.16801927149033113, 0.097171647972079528],
[0.059123747217285576, 0.17253283956937410, 0.10052980666352079],
[0.057879427805489721, 0.17704760653569082, 0.10394041715406482],
[0.056386246878794448, 0.18156356285319009, 0.10740504933426220],
[0.054624144879269983, 0.18608066293377268, 0.11092520113320597],
[0.052569051138329097, 0.19059882660111793, 0.114502],
[0.050191649055628319, 0.19511794044496134, 0.11813770062782825],
[0.047455602048250910, 0.19963785908004084, 0.12183269164062890],
[0.044314922303210540, 0.20415840632231730, 0.125588],
[0.040709916055329441, 0.20867937629370975, 0.12940624482674889],
[0.036606460290449047, 0.21320053446542414, 0.13328703641855666],
[0.032164110530606291, 0.21772161864893175, 0.13723187723521338],
[0.027384888885040096, 0.222242, 0.14124171172223299],
[0.022266496384624884, 0.22676238364257612, 0.14531741649510463],
[0.016807312188829769, 0.23128141012103987, 0.14945980038250803],
[0.011006419736188097, 0.23579905568395237, 0.15366960440463373],
[0.0048636327326471692, 0.24031493340788512, 0.15794750169027039],
[-0.0016204790932678747, 0.244829, 0.16229409733623310],
[-0.0084445645429223962, 0.24933972643719460, 0.16670992821267402],
[-0.015606465885493678, 0.25384775913131924, 0.17119546271788100],
[-0.023103194262264953, 0.25835226038704395, 0.17575110048628076],
[-0.030930905641436336, 0.26285273939339299, 0.180377],
[-0.039084877410452329, 0.26734868700986292, 0.18507393848264358],
[-0.047559485695646005, 0.27184, 0.189842],
[-0.056348183501621282, 0.27632486486356672, 0.19468025033580161],
[-0.065443479765029094, 0.28080399271884915, 0.19958996670239604],
[-0.074836919419579845, 0.285276, 0.20457071886843292],
[-0.084519064570779248, 0.289741, 0.20962241388096742],
[-0.094479476880430791, 0.29419860454646451, 0.21474488651302376],
[-0.10470670126196867, 0.29864721506318032, 0.219938],
[-0.11518825098835043, 0.303087, 0.22520113928903013],
[-0.12591059431461052, 0.30751631722861628, 0.23053422302070053],
[-0.13685914271683405, 0.31193553026958132, 0.23593669056098676],
[-0.14801824084878284, 0.31634365127280672, 0.24140800777861238],
[-0.15937115831613929, 0.32074002112433264, 0.24694756536146878],
[-0.17090008336664572, 0.32512397474269727, 0.25255467841672191],
[-0.18258611859217341, 0.32949484221079722, 0.25822858611338201],
[-0.19440927873574265, 0.33385194993668627, 0.26396845137443081],
[-0.206348, 0.33819462184308213, 0.26977336062565310],
[-0.21838159579607533, 0.342522, 0.27564232360833058],
[-0.23048535445334384, 0.34683394879562529, 0.28157427326294687],
[-0.24263545323305183, 0.35112925035714793, 0.287568],
[-0.25480651444797764, 0.35540741169937123, 0.29362248020195825],
[-0.26697210831151619, 0.35966776312078708, 0.29973621945220375],
[-0.27910476771842146, 0.36390964013289523, 0.30590790968281450],
[-0.29117600569838220, 0.368132, 0.31213610106264900],
[-0.30315633558182531, 0.37233534724869194, 0.318419],
[-0.31501529390812771, 0.37651788681633103, 0.32475581043085694],
[-0.32672146609706548, 0.38067937371673888, 0.33114405308363532],
[-0.338243, 0.38481919033970186, 0.33758224773572593],
[-0.34954521158781249, 0.38893673270978957, 0.34406857345706121],
[-0.360595, 0.39303141192522423, 0.35060113785132169],
[-0.37135838317133318, 0.39710265559866176, 0.35717797829706543],
[-0.381798, 0.40114990929637445, 0.36379706333568435],
[-0.39187868153355310, 0.40517263797216468, 0.37045629420948067],
[-0.40156251714303143, 0.40917032739217379, 0.37715350655259416],
[-0.41081200027603648, 0.41314248554659660, 0.38388647223695682],
[-0.41958876384575455, 0.41708864404418750, 0.39065290137485847],
[-0.427854, 0.42100835948531845, 0.39745044447908279],
[-0.43556798985946316, 0.42490121480925819, 0.40427669478093176],
[-0.44269120892462210, 0.42876682061126120, 0.411129],
[-0.44918333641116115, 0.43260481642499687, 0.41800541850520428],
[-0.45500383997901744, 0.43641487196581696, 0.42490281504375094],
[-0.46011193273608297, 0.44019668833034237, 0.43181877073824460],
[-0.46446663667372628, 0.44394999914786737, 0.43875063264614961],
[-0.46802684745703582, 0.44767457167911767, 0.44569570769930750],
[-0.47075140038671470, 0.45137020785795518, 0.452651],
[-0.47259913734142522, 0.45503674527172017, 0.459615],
[-0.47352897450217379, 0.45867405807601819, 0.46658275096965490],
[-0.47349997065395005, 0.46228205783988935, 0.47355306631618571],
[-0.47247139585461678, 0.46586069431749005, 0.48052265029635261],
[-0.47040280025685582, 0.46940995614259767, 0.487489],
[-0.46725408286580145, 0.47292987144247872, 0.49444817648267497],
[-0.46298556001324409, 0.476421, 0.50139836428342299],
[-0.45755803332838962, 0.47988197553641204, 0.50833632033019882],
[-0.45093285698591917, 0.48331442238607819, 0.51525915593292138],
[-0.44307200401348362, 0.48671803943763564, 0.52216398562700339],
[-0.43393813144416193, 0.49009305846281309, 0.52904793159810792],
[-0.42349464410315513, 0.49343975255735767, 0.53590812814181021],
[-0.411706, 0.49675843611747977, 0.54274172614608440],
[-0.39853655489408424, 0.50004946471886302, 0.54954589758425909],
[-0.38395305254303996, 0.50331323489779844, 0.55631784000584916],
[-0.36792224928457440, 0.50655018383440620, 0.56305478101252160],
[-0.35041218394640600, 0.50976078893832066, 0.56975398270633271],
[-0.33139198622249783, 0.51294556733766050, 0.57641274609735138],
[-0.31083192559857781, 0.51610507527250460, 0.58302841545780393],
[-0.28870345751289361, 0.51923990739453252, 0.58959838260996556],
[-0.26497926662746779, 0.522351, 0.59612],
[-0.23963330709821820, 0.52543811002287522, 0.60259104049169643],
[-0.21264083974687400, 0.52850285431797850, 0.60900879002896047],
[-0.18397846605163073, 0.53154566835913497, 0.61537096288704773],
[-0.15362415888838510, 0.534567, 0.62167524976944810],
[-0.121557, 0.53756863041423408, 0.62791941257859041],
[-0.087758653938722120, 0.54055042047605473, 0.63410128790366682],
[-0.052210489106750899, 0.54351356175892296, 0.64021879035097973],
[-0.014896494804709044, 0.54645894895901359, 0.64626991570766568],
[0.024198154625816634, 0.54938750366756073, 0.65225274393028720],
[0.061372, 0.55230017285777400, 0.65816544195052251],
[0.088588440701310334, 0.55519792732610662, 0.66400626629089132],
[0.11083460403103476, 0.55808176009355481, 0.66977356548425493],
[0.13024350538300958, 0.56095268477280336, 0.67546578229160925],
[0.14778406439909464, 0.56381173390709027, 0.68108145571350687],
[0.16398836770997294, 0.56665995728672902, 0.68661922279127619],
[0.17918339030935121, 0.56949842024922615, 0.69207782019506403],
[0.19358574373889231, 0.57232820196891054, 0.69745608559653727],
[0.20734688008091257, 0.57515039374192911, 0.70275295882496180],
[0.22057708478767773, 0.57796609727237558, 0.70796748280618838],
[0.23335925364888604, 0.58077642296519139, 0.713099],
[0.24575729871036644, 0.58358248823132008, 0.71814617433141437],
[0.25782153122589446, 0.58638541581041914, 0.72310894863464536],
[0.26959224766647716, 0.58918633211621208, 0.72798658758457269],
[0.28110219855820157, 0.59198636560933526, 0.73277865614707205],
[0.29237833619015358, 0.59478664520227165, 0.73748482353564670],
[0.30344308173853646, 0.597588, 0.74210486268478881],
[0.31431526319004066, 0.60039245128515961, 0.74663864953044890],
[0.32501082230201667, 0.60320022403709772, 0.75108616210367807],
[0.33554335607878927, 0.60601273251207466, 0.75544747944404511],
[0.34592453745042978, 0.608831, 0.75972278033992302],
[0.35616444629558303, 0.61165638302126624, 0.76391234190319857],
[0.36627183292082044, 0.61448971642171468, 0.76801653798635294],
[0.37625432996460589, 0.617332, 0.77203583745021276],
[0.38611862443397549, 0.62018479954370087, 0.77597080229098503],
[0.39587059857837004, 0.62304867309333056, 0.77982208563542232],
[0.40551544615439394, 0.62592482792499249, 0.78359042961319469],
[0.415058, 0.62881429057992300, 0.78727666311566480],
[0.42450165827678887, 0.63171807176304839, 0.79088169945041598],
[0.43385076182327798, 0.63463716550340410, 0.79440653390090143],
[0.44310834254015297, 0.63757254837723343, 0.79785224120062548],
[0.452277, 0.64052517879332094, 0.80121997293123604],
[0.46136034791942998, 0.64349599633981636, 0.80451095485384139],
[0.47035977933251688, 0.64648592119161230, 0.80772648418275295],
[0.47927776856136256, 0.64949585357708450, 0.81086792681072706],
[0.48811626270862612, 0.65252667330284309, 0.81393671449459293],
[0.49687703215044426, 0.655579, 0.81693434200995108],
[0.50556169094767089, 0.65865438943471599, 0.81986236428340276],
[0.51417171470196332, 0.66175293984781414, 0.82272239351047993],
[0.52270845622263584, 0.66487568504374639, 0.825516],
[0.53117315931055553, 0.66802339750458617, 0.82824519062290591],
[0.53956697091671535, 0.67119682756024846, 0.83091144326144961],
[0.54789095189319081, 0.67439670326825785, 0.83351666661805890],
[0.55614608652109898, 0.67762373033572154, 0.83606271603809512],
[0.56433329097291007, 0.68087859208119683, 0.83855148696418225],
[0.57245342084355055, 0.68416194943412945, 0.84098491215751148],
[0.58050727786576117, 0.68747444096953991, 0.84336495895884211],
[0.58849561590909027, 0.69081668297562127, 0.84569362659434588],
[0.59641914634835358, 0.69418926955196381, 0.84797294353106589],
[0.60427854287605320, 0.69759277273611942, 0.85020496488640596],
[0.61207444582341097, 0.70102774265627799, 0.852392],
[0.61980746604647063, 0.70449470770786027, 0.85453545944143083],
[0.62747818842658820, 0.70799417475190129, 0.85663815364783780],
[0.63508717502858147, 0.71152662933313726, 0.85870198954324184],
[0.64263496795455755, 0.71509253591579480, 0.86072911879344838],
[0.65012209192693893, 0.718692, 0.86272170550818550],
[0.65754905663034502, 0.72232645906278414, 0.86468192412278189],
[0.66491635883850864, 0.72599530148434221, 0.86661195735685692],
[0.67222448434959070, 0.72969924818702214, 0.86851399425154130],
[0.67947390975060162, 0.73343866225615872, 0.87039022828651669],
[0.68666510402948910, 0.73721388737867921, 0.87224285557792169],
[0.69379853005143410, 0.74102524815209680, 0.87407407315797436],
[0.70087464591426363, 0.74487305039753748, 0.87588607733699098],
[0.70789390619635551, 0.74875758147537652, 0.87768106214831010],
[0.71485676310913648, 0.752679, 0.87946121787650355],
[0.721764, 0.75663788916716457, 0.88122872966916455],
[0.72861507017167060, 0.76063415104825183, 0.882986],
[0.73541142215887156, 0.76466811292419534, 0.88473452861073487],
[0.742153, 0.76873997458378385, 0.88647714904998132],
[0.74884078748913352, 0.77284991922955015, 0.88821578994594907],
[0.755475, 0.77699811377518702, 0.88995259287658923],
[0.762055, 0.78118470913536053, 0.89168968771956247],
[0.76858336536380700, 0.78540984050662999, 0.89342919185526959],
[0.77505902851443498, 0.78967362763813576, 0.89517320945620671],
[0.78148288494935803, 0.79397617509066221, 0.89692383086375827],
[0.78785541896531064, 0.79831757248256552, 0.89868313205388928],
[0.79417712210675351, 0.80269789472095099, 0.90045317419371040],
[0.800448, 0.80711720221633687, 0.90223600329143072],
[0.80667004214014404, 0.811576, 0.90403364994296287],
[0.81284228432226457, 0.81607294329366265, 0.90584812917929136],
[0.81896574758076324, 0.82060942687349847, 0.90768144041977938],
[0.82504096978603036, 0.82518499598484862, 0.90953556753788389],
[0.83106850022038015, 0.82979964104515391, 0.911412],
[0.837049, 0.83445333878682437, 0.913314],
[0.842983, 0.83914605228376315, 0.91524245453870101],
[0.84887062188359730, 0.84387773093507956, 0.917199],
[0.85471313512034486, 0.848648, 0.919187],
[0.86051090384803664, 0.85345771247460789, 0.92120667773049336],
[0.86626456457641621, 0.85830584490681738, 0.92326083353450683],
[0.87197477223409359, 0.86319260112932328, 0.92535117010429546],
[0.87764220159512674, 0.86811785990609436, 0.92747955893910405],
[0.88326754887910741, 0.873081, 0.929648],
[0.88885153356002267, 0.87808332393279309, 0.93185795459179432],
[0.89439490042771896, 0.88312320853934523, 0.93411168798821365],
[0.89989842195717329, 0.88820095273452515, 0.93641093377707940],
[0.90536290105589390, 0.89331635199700588, 0.93875756822997625],
[0.91078917428015005, 0.89846918178460156, 0.94115348201948623],
[0.91617811563869134, 0.90365919571578746, 0.94360058719395623],
[0.92153064114130578, 0.90888612328716623, 0.94610082584350497],
[0.92684771430458002, 0.91414966699032152, 0.94865618098129245],
[0.93213035290634771, 0.91944949863889158, 0.95126869037408646],
[0.93737963739716035, 0.92478525463849270, 0.95394046437085767],
[0.942597, 0.93015652981294117, 0.95667370926182349],
[0.94778284623559716, 0.93556286921341258, 0.95947075846537200],
[0.95293935754402248, 0.941004, 0.962334],
[0.95806773143013080, 0.94647860125020788, 0.96526651155033127],
[0.96316960807890883, 0.95198671168912463, 0.96827099566513264],
[0.96824684178471643, 0.95752726759086559, 0.97135105979884473],
[0.97330157671434103, 0.96309926738325313, 0.97451084372764052],
[0.97833636896562248, 0.96870144627063037, 0.97775547282537800],
[0.98335439912161993, 0.97433213010368303, 0.98109166785463386],
[0.98835988485288928, 0.97998894651948654, 0.98452897186808330],
[0.99335902520489638, 0.98566815136581509, 0.98808266530596611],
[0.99836289313967719, 0.99136252323019425, 0.99178306655215309],
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
