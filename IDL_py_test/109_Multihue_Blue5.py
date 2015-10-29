from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.000019872508023912684, 0.000019586801788918958, 0.000019529289536969018],
[0.000382175, 0.000322318, 0.00036822895103079211],
[0.0011303579711904603, 0.00090586136251075535, 0.0010874119005089922],
[0.0022375102519527888, 0.0017286942214234824, 0.0021559395146994302],
[0.0036921901250302801, 0.0027685170287674288, 0.00356976],
[0.0054878075541255856, 0.0040103841748266441, 0.0053311],
[0.00761994, 0.0054433019223908011, 0.0074455948938531172],
[0.0100853, 0.0070587562606725073, 0.0099211321683072787],
[0.012881, 0.0088499425817890141, 0.012767242695708277],
[0.016004709078559307, 0.010811313358363999, 0.015994759728775190],
[0.019453953788375024, 0.012938290929315805, 0.019615604107294252],
[0.023226338377868305, 0.015227074491369093, 0.0236426],
[0.027319353344989097, 0.017674504729487634, 0.028089576236787924],
[0.031730334805815018, 0.020277965672705432, 0.032970885496207546],
[0.036456423196814851, 0.023035311654831907, 0.038301751772313035],
[0.041469332669352203, 0.025944811818389830, 0.043946636470633828],
[0.046466315330026674, 0.029005107248419471, 0.049589203266613584],
[0.051398611854077354, 0.0322152, 0.055236833009249024],
[0.056269189930206555, 0.035574313763111542, 0.060893854940572097],
[0.061080514548072402, 0.039082098452642544, 0.066564032684859192],
[0.065834632625158457, 0.042663878715898086, 0.072250651786933157],
[0.0705332, 0.046196826577785809, 0.077956588585913866],
[0.075177732402262915, 0.049693834583369144, 0.083684365042872189],
[0.079769252317340555, 0.053158079455018138, 0.089436192842646867],
[0.084308719625184964, 0.056592493703017770, 0.095214009197266691],
[0.088796862235072466, 0.059999799401728844, 0.10101950615291677],
[0.093234239339791941, 0.063382536297171388, 0.10685415475676299],
[0.097621261180068558, 0.066743085366265831, 0.11271922511760435],
[0.10195820567094990, 0.070083688691958468, 0.11861580315789783],
[0.10624523248489995, 0.073406466327798486, 0.12454480467906828],
[0.110482, 0.076713430681913136, 0.13050698723001347],
[0.11466965089105122, 0.0800065, 0.13650296016842819],
[0.11880687043426080, 0.083287503170381333, 0.14253319322760991],
[0.12289384480409918, 0.086558200462443086, 0.14859802384180562],
[0.12693029251425802, 0.089820279851504176, 0.15469766343659094],
[0.13091586538478850, 0.093075369676771463, 0.16083220285410074],
[0.13485015375684625, 0.096325043439809910, 0.16700161705382072],
[0.13873269112064360, 0.099570824978889472, 0.173206],
[0.14256295824601908, 0.102814, 0.17944441427918437],
[0.14634038689054271, 0.10605658477926006, 0.185717],
[0.15006436314833416, 0.10929939991723103, 0.19202368065012102],
[0.15373423049315588, 0.11254400285571248, 0.19836329760806037],
[0.15734929256145097, 0.11579172555696429, 0.204735],
[0.16090881571448726, 0.11904386957897534, 0.21113925377612314],
[0.16441203141336474, 0.12230170785358704, 0.21757400987416758],
[0.167858, 0.12556648616074084, 0.22403874198918050],
[0.17124630496261856, 0.12883942432641876, 0.23053243031387294],
[0.17457567054902121, 0.13212171716831367, 0.23705396679529561],
[0.17784534801244595, 0.13541453521035862, 0.24360215675957886],
[0.18105442524233822, 0.13871902518482893, 0.25017572052271681],
[0.18420196695464194, 0.14203631033875338, 0.25677329500701179],
[0.18728701640250717, 0.14536749055974293, 0.26339343538078574],
[0.19030859705609782, 0.148714, 0.27003461673720436],
[0.19326571426284900, 0.15207581855641850, 0.276695],
[0.19615735689852948, 0.15545504818308684, 0.28337361285405294],
[0.19898249901857495, 0.15885233577333552, 0.29006799335682620],
[0.20174010151843175, 0.162269, 0.29677655016668941],
[0.20442911381099482, 0.16570497743239032, 0.303497],
[0.20704847552869116, 0.16916221277695381, 0.31022853298039377],
[0.20959711825727473, 0.172641, 0.31696796020216483],
[0.21207396730800388, 0.17614301162628373, 0.32371357084000207],
[0.214478, 0.17966828909946381, 0.33046320731020740],
[0.21680796520063356, 0.18321791117728398, 0.33721465338733980],
[0.21906294990434255, 0.18679265803137104, 0.34396563697942428],
[0.22124181656456582, 0.19039327700282049, 0.35071383303532461],
[0.22334348747523836, 0.19402, 0.35745686658557074],
[0.22536689043269065, 0.19767494913049621, 0.36419231591701384],
[0.22731096094150460, 0.20135732167911813, 0.37091771588081329],
[0.22917464450421660, 0.20506820260472164, 0.37763056133236994],
[0.230957, 0.20880815640252448, 0.38432831070095253],
[0.23265669715972448, 0.21257770723937375, 0.39100838968591151],
[0.23427302913727371, 0.21637733773890838, 0.39766819507552215],
[0.235805, 0.22020748780211352, 0.40430509868366993],
[0.23725135848240109, 0.22406855347249405, 0.41091645139878030],
[0.23861144797239164, 0.22796088585487284, 0.4175],
[0.23988426147293523, 0.23188479009654733, 0.424052],
[0.24106891880861209, 0.23584052443920062, 0.43057048712149165],
[0.24216457512762935, 0.23982829934960503, 0.437053],
[0.24317042436004799, 0.24384827673673287, 0.44349629939243079],
[0.244086, 0.24790056926240866, 0.44989807882813032],
[0.24490969305869759, 0.25198523975214437, 0.45625553805881908],
[0.24564172768832843, 0.25610230071222195, 0.46256601734890163],
[0.24628119367329560, 0.26025171395851748, 0.46882687623454416],
[0.24682753661727264, 0.26443339036190633, 0.47503549822743402],
[0.24728026535117481, 0.26864718971445967, 0.48118929552398820],
[0.24763895674099135, 0.27289292071992283, 0.48728571370731794],
[0.24790326074671137, 0.27717034111129563, 0.49332223642898570],
[0.24807290575157770, 0.28147915789758954, 0.49929639005741139],
[0.24814770418282822, 0.28581902774110796, 0.50520574827964349],
[0.24812755844715684, 0.29018955746587644, 0.511048],
[0.24801246720647813, 0.29459030469709491, 0.51682063702449421],
[0.24780253202199909, 0.29902077863076981, 0.52252159201112247],
[0.24749796439724137, 0.30348044093196180, 0.52814860918411821],
[0.24709909325346341, 0.307969, 0.53369956528817097],
[0.24660637287382869, 0.312485, 0.53917241027677731],
[0.24602039135574588, 0.31702848410422096, 0.54456517122032999],
[0.245342, 0.32159860433464377, 0.54987595606539808],
[0.24457172097913171, 0.32619454839525114, 0.555103],
[0.24371096144333437, 0.33081551846388524, 0.56024445505200859],
[0.24276082059930232, 0.33546067880535407, 0.56529882099727235],
[0.24172270333222862, 0.34012915756449452, 0.57026452075703671],
[0.24059821231751710, 0.34482004864598176, 0.57514011708709090],
[0.23938916138297500, 0.349532, 0.57992427246412459],
[0.238098, 0.35426528402342722, 0.58461575152445466],
[0.23672577751460389, 0.35901766291790232, 0.58921342328288018],
[0.23527626151173792, 0.36378852758201752, 0.593716],
[0.23375185313113123, 0.36857683144461684, 0.598123],
[0.23215565660806159, 0.373382, 0.60243389082704279],
[0.230491, 0.37820146499515434, 0.60664717602589458],
[0.22876189967564137, 0.38303560290898342, 0.61076262634533218],
[0.22697219500607629, 0.38788280109175732, 0.61477977079499113],
[0.22512645880083187, 0.39274192818050679, 0.61869825180433158],
[0.22322957783900360, 0.39761184280828754, 0.62251782556689217],
[0.22128686672404357, 0.40249139592438438, 0.62623836214954653],
[0.21930409377049642, 0.40737943310017583, 0.62986],
[0.21728750740624397, 0.41227479681344331, 0.63338237244348727],
[0.21524386275680363, 0.41717632870419447, 0.63680615341131785],
[0.21318044797538288, 0.42208287179537546, 0.64013151034292049],
[0.21110510976168212, 0.42699327267218501, 0.64335887633097522],
[0.20902627737306367, 0.43190638361406264, 0.64648879427812878],
[0.20695298427435271, 0.43682106467379073, 0.649522],
[0.20489488639865921, 0.441736, 0.65245899804908258],
[0.20286227580548088, 0.44665062828825058, 0.65530090507659910],
[0.20086608833020003, 0.45156328768655224, 0.65804860272673449],
[0.19891790363118050, 0.45647307460108882, 0.66070315808697833],
[0.19702993587058171, 0.46137891694897310, 0.66326573689554846],
[0.19521501313155976, 0.46628, 0.66573760111872082],
[0.19348654360033457, 0.47117457558836390, 0.66812],
[0.19185846655420430, 0.47606234837005784, 0.67041469934629538],
[0.19034518632571576, 0.48094209249188385, 0.67262291479718195],
[0.18896148768971566, 0.48581284530295127, 0.67474637286180217],
[0.18772243157114824, 0.49067367012830437, 0.67678677595998293],
[0.186643, 0.49552365743051457, 0.67874590574249727],
[0.18573910502128219, 0.500362, 0.68062561994612225],
[0.18502512002322039, 0.50518762336063772, 0.68242784918735133],
[0.18451600767597595, 0.50999992783169912, 0.68415459370489962],
[0.18422597673782074, 0.51479804817920827, 0.68580792006091829],
[0.18416851577302565, 0.51958122492541226, 0.68739],
[0.18435619564607184, 0.52434873087710576, 0.688903],
[0.18480047842036804, 0.52909987168791173, 0.69034898054738869],
[0.18551154010615670, 0.53383398634011536, 0.69173050937850888],
[0.18649811464312124, 0.53855, 0.69304983055415481],
[0.18776736589723655, 0.54324866208548117, 0.69430933816811602],
[0.18932479330507127, 0.54792807103870900, 0.69551146916080098],
[0.19117417518415431, 0.55258814998906058, 0.69665870000966612],
[0.19331755177896356, 0.55722840912632798, 0.69775354345248108],
[0.19575524800630212, 0.561848, 0.69879854524957419],
[0.19848593379962776, 0.56644768198731577, 0.69979628099075442],
[0.20150671811685578, 0.57102588925200626, 0.70074935295213736],
[0.20481327122503423, 0.57558266357863652, 0.70166038700763700],
[0.20839996890524309, 0.58011768770370886, 0.702532],
[0.21226005176967538, 0.58463067837575333, 0.70336694477127004],
[0.21638579292524957, 0.58912138607111197, 0.70416781126796102],
[0.22076866768221792, 0.59358959466514216, 0.70493731970412754],
[0.22539951978873979, 0.59803512106189993, 0.70567816980464704],
[0.230269, 0.60245781478535065, 0.706393],
[0.23536631111821194, 0.60685755753510218, 0.70708472341115547],
[0.24068214431630547, 0.61123426270961068, 0.70775584812658887],
[0.24620599332215354, 0.615588, 0.70840915193704312],
[0.25192765791930966, 0.61991836935551736, 0.70904734136406777],
[0.257837, 0.62422575142876247, 0.70967311708144421],
[0.263924, 0.62851005599433973, 0.71028917169659522],
[0.27017963267553746, 0.63277134685252667, 0.71089818761072454],
[0.27659377725113626, 0.63700971611499724, 0.711503],
[0.28315763340328515, 0.64122528357681319, 0.71210576961722527],
[0.28986247873673099, 0.64541819607668083, 0.71270963131245901],
[0.29669994696347657, 0.64958862684765462, 0.71331704177238731],
[0.30366203593944607, 0.65373677486035942, 0.71393060297614097],
[0.31074110992099591, 0.65786286416068462, 0.71455289546666534],
[0.31792989714950604, 0.66196714320382388, 0.71518647673582103],
[0.32522148373914878, 0.66604988418639410, 0.71583387967865708],
[0.33260930471100403, 0.67011138237828793, 0.71649761111503041],
[0.340087, 0.67415195545580287, 0.71718015037667682],
[0.34764906627800735, 0.67817194283747639, 0.71788394795776733],
[0.35528951436965739, 0.68217170502396973, 0.71861142422695745],
[0.36300318387142622, 0.68615162294323850, 0.71936496819889917],
[0.37078506409787870, 0.69011209730213197, 0.72014693636318139],
[0.37863041233641304, 0.69405354794546237, 0.72095965156865904],
[0.38653473937138688, 0.69797641322351711, 0.72180540196115228],
[0.39449379532264822, 0.70188114936886681, 0.72268643997251147],
[0.40250355591207049, 0.70576822988327748, 0.723605],
[0.41056020923924880, 0.70963814493542055, 0.72456320428768095],
[0.41866014312113731, 0.71349140077001882, 0.725563],
[0.4268, 0.71732851912898621, 0.726607],
[0.43497633064238456, 0.72115003668506228, 0.72769716221752734],
[0.44318625301637105, 0.72495650448835858, 0.72883511170250981],
[0.45142677236952938, 0.72874848742619280, 0.73002304082020286],
[0.45969510646605266, 0.73252656369652480, 0.73126288543453921],
[0.467989, 0.73629132429525035, 0.73255653860058123],
[0.47630476402599237, 0.74004337251756580, 0.733906],
[0.48464117220282227, 0.74378332347358567, 0.73531262521531970],
[0.49299554917129068, 0.74751180361833214, 0.736779],
[0.50136571569081911, 0.75122945029619859, 0.73830556705493056],
[0.50974959171606204, 0.754937, 0.73989512051150008],
[0.51814519031645478, 0.75863484444428841, 0.74154891065792372],
[0.52655061199352971, 0.76232391715407233, 0.74326851591713761],
[0.53496403937004888, 0.76600480606703780, 0.74505546797284461],
[0.543384, 0.76967819665117743, 0.74691125139917325],
[0.55180802285917330, 0.77334478283664820, 0.74883730331327902],
[0.560235, 0.77700526666220804, 0.75083501304968592],
[0.56866406347256915, 0.78066035793616995, 0.75290572185517579],
[0.57709280295609733, 0.78431077391182824, 0.75505072260296258],
[0.58552011186362995, 0.78795723897736747, 0.75727125952485619],
[0.59394462528749781, 0.7916, 0.75956852796003471],
[0.60236502861405605, 0.79524124784611050, 0.76194367411897779],
[0.61078005458593621, 0.79888027351223523, 0.76439779486098569],
[0.61918848054103270, 0.802518, 0.76693193748361321],
[0.62758912581464965, 0.80615611765626105, 0.76954709952219014],
[0.63598084929200305, 0.80979445355442514, 0.77224422855743458],
[0.64436254709907403, 0.81343408604454082, 0.77502422202899268],
[0.65273315042049063, 0.81707578718367679, 0.77788792705250043],
[0.66109162343368266, 0.82072033403645506, 0.78083614023753234],
[0.66943696134910880, 0.82436850851645915, 0.78386960750350609],
[0.67776818854678456, 0.828021, 0.786989],
[0.68608435679964974, 0.83167889142708984, 0.79019503335995889],
[0.69438454357465229, 0.83534268674846457, 0.793488],
[0.70266785040246960, 0.83901328329006364, 0.796869],
[0.71093340130697424, 0.84269148546615435, 0.80033828915490501],
[0.71918034128532105, 0.84637810198495678, 0.80389608122158163],
[0.72740783482947646, 0.850074, 0.807543],
[0.73561506447954872, 0.85378, 0.811279],
[0.74380122939876003, 0.85749658899492842, 0.81510496494062645],
[0.75196554395918080, 0.86122503596458178, 0.81902069196097038],
[0.76010723632622024, 0.86496600578004623, 0.82302646587346995],
[0.76822554702866330, 0.86872033371049051, 0.82712240329763698],
[0.77631972749917466, 0.87248885993162850, 0.83130856535927644],
[0.78438903856807163, 0.87627242979356101, 0.83558495684358225],
[0.79243274889022341, 0.88007189415485720, 0.83995152520737570],
[0.80045013328134484, 0.88388810979395327, 0.84440815942464587],
[0.80844047093528082, 0.88772193991148773, 0.84895468863434331],
[0.81640304348779524, 0.89157425474041763, 0.85359088055278831],
[0.82433713288466315, 0.89544593228488090, 0.85831643960471615],
[0.83224201900170092, 0.89933785921406673, 0.86313100471629556],
[0.840117, 0.90325093194429307, 0.868034],
[0.84796127399033805, 0.90718605795160212, 0.873025],
[0.85577416592799871, 0.91114415736931564, 0.87810408467572198],
[0.86355489288543641, 0.91512616494134824, 0.88327],
[0.87130267423361152, 0.91913303242444633, 0.88852132304483056],
[0.879017, 0.92316573156348636, 0.89385827118260319],
[0.88669613563458327, 0.92722525780766318, 0.89927956429857570],
[0.89434008802320719, 0.93131263499804040, 0.90478416210909529],
[0.90194761820542324, 0.93542892134864364, 0.91037090201240911],
[0.90951771379010105, 0.93957521718051473, 0.91603848296471224],
[0.91704927139096370, 0.94375267507883798, 0.92178544464232803],
[0.92454106985878304, 0.94796251347599425, 0.92761014002730458],
[0.93199173366877597, 0.95220603520672575, 0.933511],
[0.93939968149519104, 0.95648465350324596, 0.93948497548745935],
[0.94676305168178698, 0.96079992953373983, 0.94553047969820170],
[0.95407959007193666, 0.96515362865142495, 0.95164426787263257],
[0.96134647312864108, 0.96954780865052592, 0.95782278103474583],
[0.96856001195632369, 0.97398496664174072, 0.96406157764109024],
[0.97571511657383370, 0.97846830335323542, 0.97035486220748879],
[0.98280421388952244, 0.98300225367877137, 0.97669455727413557],
[0.989815, 0.987594, 0.98306814814968890],
[0.99672050617126062, 0.99225619228717832, 0.98945197482812974],
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
