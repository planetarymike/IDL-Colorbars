from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000198725080239126838, 0.0000195868017889189583, 0.0000195292895369690181],
[0.000356230672136303073, 0.000340176783340015172, 0.000294765337669803090],
[0.00103169290696975371, 0.000974297031188886380, 0.000803134962426855386],
[0.00201336795183252714, 0.00188556167448519362, 0.00149683982615946378],
[0.00328599153630430461, 0.00305560061787074405, 0.00234856613605040473],
[0.00484059571251699468, 0.00447263533734827776, 0.00333910590283806406],
[0.00667144346529655301, 0.00612831588430390751, 0.00445365497908330014],
[0.00877474530998151488, 0.00801637854221003837, 0.00568017725363984417],
[0.0111480049119082932, 0.0101319536640855044, 0.00700853467372470739],
[0.0137896430521591441, 0.0124711639246606037, 0.00842996916154532296],
[0.0166987631641264192, 0.0150308714926698558, 0.00993676927279692375],
[0.0198749961518939790, 0.0178085092189398421, 0.0115220432265871163],
[0.0233183928825970027, 0.0208019626906267643, 0.0131795575125232441],
[0.0270293469674516076, 0.0240094848086885825, 0.0149036181175501662],
[0.0310085376500880867, 0.0274296320860405833, 0.0166889806441315944],
[0.0352568865317783795, 0.0310612159780854560, 0.0185307807000539664],
[0.0397755241085776048, 0.0349032649306790649, 0.0204244789263893362],
[0.0443825894840866111, 0.0389549942641320146, 0.0223658168561078445],
[0.0489401093590453237, 0.0431169565643512928, 0.0243507809553809018],
[0.0534599061550685081, 0.0472239647001322441, 0.0263755729601612941],
[0.0579453169959294259, 0.0512883673318510133, 0.0284365851335849039],
[0.0623993069597481645, 0.0553132193606406600, 0.0305303794242593012],
[0.0668245264872271427, 0.0593012511273798212, 0.0326536697558397204],
[0.0712233577820007013, 0.0632549159237029701, 0.0348033068584743810],
[0.0755979526935555146, 0.0671764288205028148, 0.0369762651846149426],
[0.0799502639307211049, 0.0710677986916421200, 0.0391696315497671241],
[0.0842820709957960434, 0.0749308548464584501, 0.0413588743024270525],
[0.0885950018979956011, 0.0787672693485029496, 0.0434855479897108058],
[0.0928905514617330286, 0.0825785758511265455, 0.0455609939385679466],
[0.0971700968645401453, 0.0863661855969528880, 0.0475867595105053456],
[0.101434910903543812, 0.0901314010901517193, 0.0495642618394307524],
[0.105686173386136090, 0.0938754278453658997, 0.0514948011773174383],
[0.109924980961176033, 0.0975993845364311330, 0.0533795724359924437],
[0.114152355645620512, 0.101304311805439723, 0.0552196752142110545],
[0.118369252253445051, 0.104991179943749818, 0.0570161225453371181],
[0.122576564895874068, 0.108660895617940373, 0.0587698485584055921],
[0.126775132691882786, 0.112314307783047657, 0.0604817152114566700],
[0.130965744803911988, 0.115952212900879592, 0.0621525182288653541],
[0.135149144894379403, 0.119575359561445938, 0.0637829923524537434],
[0.139326035082916549, 0.123184452589513910, 0.0653738159983561218],
[0.143497079471476052, 0.126780156705247116, 0.0669256153970425316],
[0.147662907294004164, 0.130363099797166121, 0.0684389682819388223],
[0.151824115738736082, 0.133933875856849238, 0.0699144071821901913],
[0.155981272484052025, 0.137493047617470832, 0.0713524223669034507],
[0.160134917982875130, 0.141041148932197796, 0.0727534644813414011],
[0.164285567525648407, 0.144578686923359651, 0.0741179469097967281],
[0.168433713107746824, 0.148106143929048417, 0.0754462478950250759],
[0.172579825123681557, 0.151623979270189557, 0.0767387124400168430],
[0.176724353907472903, 0.155132630858079462, 0.0779956540144000898],
[0.180867731136059806, 0.158632516659790057, 0.0792173560847909963],
[0.185010371110447630, 0.162124036036631614, 0.0804040734858546269],
[0.189152671927473259, 0.165607570968969581, 0.0815560336466406577],
[0.193295016553474697, 0.169083487179076092, 0.0826734376848546060],
[0.197437773809806982, 0.172552135162285986, 0.0837564613800722280],
[0.201581299278961790, 0.176013851135531113, 0.0848052560354576324],
[0.205725936139045662, 0.179468957911271293, 0.0858199492362786420],
[0.209872015933479483, 0.182917765703936780, 0.0868006455123889187],
[0.214019859282019165, 0.186360572875203051, 0.0877474269108548255],
[0.218169776538529647, 0.189797666623729183, 0.0886603534840067209],
[0.222322068400355122, 0.193229323624382249, 0.0895394636974002345],
[0.226477026473615617, 0.196655810621443328, 0.0903847747614361097],
[0.230634933798306518, 0.200077384979821471, 0.0911962828897209810],
[0.234796065336684234, 0.203494295197889585, 0.0919739634866349742],
[0.238960688428060786, 0.206906781385195526, 0.0927177712659867648],
[0.243129063212833951, 0.210315075707973032, 0.0934276403020949664],
[0.247301443028281942, 0.213719402805103154, 0.0941034840141020956],
[0.251478074778428373, 0.217119980176909200, 0.0947451950838208989],
[0.255659199280055427, 0.220517018548951393, 0.0953526453069092617],
[0.259845051586741760, 0.223910722212786018, 0.0959256853766661810],
[0.264035861292642560, 0.227301289345466895, 0.0964641445992355240],
[0.268231852817565564, 0.230688912309412186, 0.0969678305384817640],
[0.272433245674754132, 0.234073777934112159, 0.0974365285882649035],
[0.276640254722672785, 0.237456067781025126, 0.0978700014692685805],
[0.280853090401969929, 0.240835958392889682, 0.0982679886469363661],
[0.285071958958696026, 0.244213621528579061, 0.0986302056664229987],
[0.289297062654764403, 0.247589224384525186, 0.0989563433997631137],
[0.293528599966552950, 0.250962929803658086, 0.0992460671996961696],
[0.297766765772480013, 0.254334896472725946, 0.0994990159537408880],
[0.302011751530312011, 0.257705279108791874, 0.0997148010311816879],
[0.306263745444906033, 0.261074228635637673, 0.0998930051145829334],
[0.310522932627030790, 0.264441892350751329, 0.100033180906283159],
[0.314789495243851858, 0.267808414083520907, 0.100134849699005657],
[0.319063612661645735, 0.271173934345200818, 0.100197499798236694],
[0.323345461581226512, 0.274538590471192279, 0.100220584782327232],
[0.327635216166577481, 0.277902516756114826, 0.100203521584353583],
[0.331933048167091627, 0.281265844582134772, 0.100145688377557995],
[0.336239127033853780, 0.284628702540960010, 0.100046422243660699],
[0.340553620030304538, 0.287991216549898787, 0.0999050166003967455],
[0.344876692337654556, 0.291353509962339441, 0.0997207183612573988],
[0.349208507155355396, 0.294715703672988827, 0.0994927247964663974],
[0.353549225796928657, 0.298077916218181083, 0.0992201800596439198],
[0.357899007781434797, 0.301440263871548153, 0.0989021713392297108],
[0.362258010920827100, 0.304802860735321313, 0.0985377245874433649],
[0.366626391403446661, 0.308165818827519145, 0.0981257997721130537],
[0.371004303873868235, 0.311529248165252237, 0.0976652855879134307],
[0.375391901509311621, 0.314893256844368863, 0.0971549935530887643],
[0.379789336092821839, 0.318257951115645532, 0.0965936514052667117],
[0.384196758083377443, 0.321623435457713769, 0.0959798956950005389],
[0.388614316683134009, 0.324989812646900078, 0.0953122634576736016],
[0.393042159901917765, 0.328357183824155852, 0.0945891828226063380],
[0.397480434619160161, 0.331725648559222319, 0.0938089623917031379],
[0.401929286643389283, 0.335095304912189806, 0.0929697791875856716],
[0.406388860769413884, 0.338466249492581417, 0.0920696649313335336],
[0.410859300833331997, 0.341838577516096698, 0.0911064903607106402],
[0.415340749765468253, 0.345212382859133415, 0.0900779472384835023],
[0.419833349641360598, 0.348587758111204737, 0.0889815276236893271],
[0.424337241730887271, 0.351964794625361066, 0.0878144998819212763],
[0.428852566545641134, 0.355343582566713334, 0.0865738807876893501],
[0.433379463884634331, 0.358724210959158296, 0.0852564029143662583],
[0.437918072878426157, 0.362106767730394297, 0.0838584763037190373],
[0.442468532031745798, 0.365491339755311784, 0.0823761431417281143],
[0.447030979264694317, 0.368878012897840502, 0.0808050238182007330],
[0.451605551952595940, 0.372266872051326747, 0.0791402522831606003],
[0.456192386964562602, 0.375658001177516521, 0.0773763979880582598],
[0.460791620700837623, 0.379051483344206297, 0.0755073708486704576],
[0.465403389128986433, 0.382447400761629641, 0.0735263044916960595],
[0.470027827818978505, 0.385845834817640620, 0.0714254114015994146],
[0.474665071977228681, 0.389246866111745637, 0.0691958012426757974],
[0.479315256479632523, 0.392650574488047521, 0.0668272502400738544],
[0.483978515903672635, 0.396057039067141181, 0.0643079044957497736],
[0.488654984559600936, 0.399466338277021882, 0.0616238925590872275],
[0.493344796520786721, 0.402878549883041892, 0.0587588108911512516],
[0.498048085653233274, 0.406293751016966687, 0.0556930273061168393],
[0.502764985644329143, 0.409712018205168838, 0.0524027170699104053],
[0.507495630030859291, 0.413133427395998232, 0.0488584947172853098],
[0.512240152226307699, 0.416558053986370691, 0.0450234133228238284],
[0.516998685547504611, 0.419985972847605360, 0.0408499333662795741],
[0.521771363240629005, 0.423417258350547554, 0.0363331047409600136],
[0.525710569878150791, 0.427127685801644286, 0.0415455695650425935],
[0.528806586197773432, 0.431117079795327263, 0.0553119417416409950],
[0.531904124472414308, 0.435109723532685511, 0.0675563251323586245],
[0.535003453032917853, 0.439105685243752542, 0.0787784824679858831],
[0.538104837525155810, 0.443105035185969443, 0.0892642978692957945],
[0.541208540953261430, 0.447107845598941733, 0.0991942230383712209],
[0.544314823721931851, 0.451114190660979963, 0.108690130818504566],
[0.547423943677882940, 0.455124146447308864, 0.117838508813934290],
[0.550536156150564948, 0.459137790889831920, 0.126703101598124091],
[0.553651713992186156, 0.463155203738369769, 0.135332317574997335],
[0.556770867617148890, 0.467176466523268219, 0.143763819996257425],
[0.559893865040941852, 0.471201662519313447, 0.152027504394718543],
[0.563020951918563384, 0.475230876710872330, 0.160147502773624495],
[0.566152371582529734, 0.479264195758199507, 0.168143575390791750],
[0.569288365080517167, 0.483301707964848559, 0.176032103219925823],
[0.572429171212692878, 0.487343503246136567, 0.183826811993151706],
[0.575575026568773795, 0.491389673098613755, 0.191539311014020081],
[0.578726165564861561, 0.495440310570490594, 0.199179501182471186],
[0.581882820480082663, 0.499495510232985718, 0.206755888787401643],
[0.585045221493081247, 0.503555368152556526, 0.214275830176237303],
[0.588213596718388354, 0.507619981863976277, 0.221745724900592800],
[0.591388172242699239, 0.511689450344235075, 0.229171169898368332],
[0.594569172161099502, 0.515763873987223342, 0.236557083823884240],
[0.597756818613240260, 0.519843354579185957, 0.243907808234204493],
[0.600951331819523094, 0.523927995274913405, 0.251227190637174969],
[0.604152930117286657, 0.528017900574655807, 0.258518653182440550],
[0.607361829997026259, 0.532113176301733604, 0.265785249884266217],
[0.610578246138678504, 0.536213929580832693, 0.273029714606245644],
[0.613802391447975881, 0.540320268816961269, 0.280254501546061130],
[0.617034477092891831, 0.544432303675061235, 0.287461819587160383],
[0.620274712540200390, 0.548550145060250904, 0.294653661601167127],
[0.623523305592152854, 0.552673905098697071, 0.301831829567059118],
[0.626780462423307982, 0.556803697119092167, 0.308997956204124846],
[0.630046387617505421, 0.560939635634737810, 0.316153523683480653],
[0.633321284205021651, 0.565081836326218223, 0.323299879878682084],
[0.636605353699900234, 0.569230416024653296, 0.330438252533203303],
[0.639898796137481574, 0.573385492695531629, 0.337569761656409839],
[0.643201810112151939, 0.577547185423104237, 0.344695430406450898],
[0.646514592815307876, 0.581715614395341807, 0.351816194675437954],
[0.649837340073559977, 0.585890900889445843, 0.358932911557269918],
[0.653170246387194786, 0.590073167257902931, 0.366046366849785532],
[0.656513504968891049, 0.594262536915090234, 0.373157281719393774],
[0.659867307782731283, 0.598459134324411002, 0.380266318636849343],
[0.663231845583484025, 0.602663084985968323, 0.387374086676695706],
[0.666607307956220696, 0.606874515424769889, 0.394481146259439697],
[0.669993883356240882, 0.611093553179452687, 0.401588013404235555],
[0.673391759149340241, 0.615320326791543248, 0.408695163550407359],
[0.676801121652442439, 0.619554965795228951, 0.415803034998124654],
[0.680222156174614567, 0.623797600707649225, 0.422912032011798389],
[0.683655047058457588, 0.628048363019712896, 0.430022527624011164],
[0.687099977721952304, 0.632307385187415361, 0.437134866172890324],
[0.690557130700708344, 0.636574800623687653, 0.444249365601646573],
[0.694026687690713628, 0.640850743690742020, 0.451366319545405348],
[0.697508829591556689, 0.645135349692942284, 0.458485999227353613],
[0.701003736550182444, 0.649428754870179481, 0.465608655183563702],
[0.704511588005203748, 0.653731096391760969, 0.472734518833535178],
[0.708032562731790938, 0.658042512350814124, 0.479863803911487807],
[0.711566838887205844, 0.662363141759200080, 0.486996707771695736],
[0.715114594056984743, 0.666693124542943383, 0.494133412579612463],
[0.718676005301847276, 0.671032601538176010, 0.501274086399217555],
[0.722251249205361878, 0.675381714487596541, 0.508418884185823372],
[0.725840501922416559, 0.679740606037453121, 0.515567948692554845],
[0.729443939228570093, 0.684109419735044466, 0.522721411297810468],
[0.733061736570345568, 0.688488300026741551, 0.529879392760175150],
[0.736694069116499595, 0.692877392256549651, 0.537042003906568866],
[0.740341111810416175, 0.697276842665183194, 0.544209346258749283],
[0.744003039423628332, 0.701686798389696276, 0.551381512602714841],
[0.747680026610619830, 0.706107407463640424, 0.558558587505046611],
[0.751372247964983697, 0.710538818817776141, 0.565740647779741090],
[0.755079878077058342, 0.714981182281331007, 0.572927762908671756],
[0.758803091593149737, 0.719434648583832659, 0.580119995418423518],
[0.762542063276511972, 0.723899369357490996, 0.587317401215878054],
[0.766296968070205531, 0.728375497140171690, 0.594520029884595735],
[0.770067981162013027, 0.732863185378955118, 0.601727924943732950],
[0.773855278051613693, 0.737362588434290034, 0.608941124070911832],
[0.777659034620212353, 0.741873861584761762, 0.616159659290201223],
[0.781479427202858124, 0.746397161032489431, 0.623383557126066523],
[0.785316632663731196, 0.750932643909156483, 0.630612838723875302],
[0.789170828474653252, 0.755480468282711426, 0.637847519937278507],
[0.793042192797206114, 0.760040793164736383, 0.645087611382494042],
[0.796930904568765031, 0.764613778518527854, 0.652333118459239025],
[0.800837143592914358, 0.769199585267894892, 0.659584041337747840],
[0.804761090634687148, 0.773798375306716690, 0.666840374910995681],
[0.808702927521158466, 0.778410311509286967, 0.674102108710890824],
[0.812662837248020020, 0.783035557741474819, 0.681369226786827653],
[0.816641004092778289, 0.787674278872758760, 0.688641707544555781],
[0.820637613735417881, 0.792326640789151715, 0.695919523542867568],
[0.824652853387359386, 0.796992810407106678, 0.703202641245047055],
[0.828686911929790271, 0.801672955688425559, 0.710491020721430555],
[0.832739980062520591, 0.806367245656267828, 0.717784615298709849],
[0.836812250464752827, 0.811075850412313115, 0.725083371150798572],
[0.840903917969313075, 0.815798941155194468, 0.732387226825107263],
[0.845015179752242385, 0.820536690200274532, 0.739696112696959118],
[0.849146235539848249, 0.825289271000914537, 0.747009950343512030],
[0.853297287835781404, 0.830056858171350997, 0.754328651826956631],
[0.857468542171096693, 0.834839627511361537, 0.761652118874821427],
[0.861660207380846144, 0.839637756032900251, 0.768980241942872178],
[0.865872495911397810, 0.844451421988933637, 0.776312899143239421],
[0.870105624163498459, 0.849280804904738340, 0.783649955016899713],
[0.874359812877163356, 0.854126085611988661, 0.790991259125309876],
[0.878635287565667999, 0.858987446286011758, 0.798336644430603926],
[0.882932279007650700, 0.863865070486660724, 0.805685925427010452],
[0.887251023808181549, 0.868759143203386097, 0.813038895977584164],
[0.891591765042413664, 0.873669850905174017, 0.820395326799486790],
[0.895954752998662340, 0.878597381596196048, 0.827754962526999871],
[0.900340246042079406, 0.883541924878229468, 0.835117518263264524],
[0.904748511625849572, 0.888503672021148660, 0.842482675507816081],
[0.909179827484302594, 0.893482816043167372, 0.849850077315220109],
[0.913634483052528812, 0.898479551802957577, 0.857219322497403624],
[0.918112781170971060, 0.903494076106411970, 0.864589958624071952],
[0.922615040152556354, 0.908526587831674948, 0.871961473495075690],
[0.927141596316903405, 0.913577288077284555, 0.879333284645416824],
[0.931692807134732681, 0.918646380339950719, 0.886704726281572375],
[0.936269055181893961, 0.923734070730976575, 0.894075032811272319],
[0.940870753186585640, 0.928840568243964659, 0.901443317775609043],
[0.945498350582209990, 0.933966085091965437, 0.908808546451403965],
[0.950152342181465381, 0.939110837140851973, 0.916169499539063903],
[0.954833279918349542, 0.944275044479553238, 0.923524723962130922],
[0.959541789165203940, 0.949458932191041272, 0.930872464453362025],
[0.964278592124780398, 0.954662731428648326, 0.938210565438116206],
[0.969044542653376806, 0.959886680977551587, 0.945536324942384376],
[0.973840680577567786, 0.965131029629761161, 0.952846266713174406],
[0.978668321604878488, 0.970396040019342432, 0.960135763046599755],
[0.983529218325624677, 0.975681995323712692, 0.967398359528782614],
[0.988425881939344664, 0.980989212329763771, 0.974624426062195126],
[0.993362341461640042, 0.986318071505226990, 0.981797974664938011],
[0.998346548939382461, 0.991669109780818458, 0.988886582067263542],
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