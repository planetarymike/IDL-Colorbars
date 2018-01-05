from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.0000208612, 0.0000200049, 0.0000198463],
[0.000296857, 0.000372831, 0.00034412],
[0.000795939, 0.00108947, 0.000981978],
[0.0014639, 0.00213956, 0.00189161],
[0.00226767, 0.00351049, 0.0030487],
[0.003183, 0.00519576, 0.00443492],
[0.00419057, 0.00719197, 0.00603483],
[0.00527439, 0.00949747, 0.00783455],
[0.00642081, 0.0121118, 0.00982114],
[0.00761806, 0.0150351, 0.0119822],
[0.00885585, 0.0182682, 0.0143057],
[0.0101252, 0.0218123, 0.0167798],
[0.0114183, 0.0256688, 0.0193928],
[0.0127283, 0.0298391, 0.0221331],
[0.0140494, 0.034325, 0.0249889],
[0.0153765, 0.0391281, 0.0279488],
[0.0167056, 0.0440887, 0.0310013],
[0.0180334, 0.0489957, 0.0341346],
[0.0193573, 0.0538622, 0.0373374],
[0.0206758, 0.0586913, 0.0405956],
[0.0219879, 0.0634856, 0.0437665],
[0.0232934, 0.0682474, 0.0468326],
[0.024593, 0.0729785, 0.0497954],
[0.0258881, 0.0776805, 0.052656],
[0.0271808, 0.0823549, 0.0554155],
[0.028474, 0.0870028, 0.0580747],
[0.0297714, 0.0916251, 0.0606346],
[0.0310775, 0.0962229, 0.0630956],
[0.0323975, 0.100797, 0.0654584],
[0.0337373, 0.105347, 0.0677235],
[0.0351037, 0.109874, 0.0698913],
[0.0365042, 0.114379, 0.0719623],
[0.037947, 0.118862, 0.0739367],
[0.0394412, 0.123322, 0.075815],
[0.0409851, 0.12776, 0.0775975],
[0.0425543, 0.132177, 0.0792845],
[0.0441661, 0.136571, 0.0808762],
[0.0458286, 0.140943, 0.0823731],
[0.0475493, 0.145294, 0.0837754],
[0.0493357, 0.149622, 0.0850833],
[0.0511949, 0.153928, 0.0862974],
[0.0531337, 0.158211, 0.0874178],
[0.0551584, 0.162471, 0.0884449],
[0.0572749, 0.166708, 0.0893791],
[0.0594886, 0.170922, 0.0902207],
[0.0618045, 0.175113, 0.0909702],
[0.0642269, 0.179279, 0.0916279],
[0.0667595, 0.183422, 0.0921943],
[0.0694057, 0.187539, 0.0926698],
[0.072168, 0.191632, 0.0930547],
[0.0750487, 0.1957, 0.0933497],
[0.0780493, 0.199742, 0.0935551],
[0.0811708, 0.203758, 0.0936714],
[0.084414, 0.207748, 0.0936992],
[0.087779, 0.211712, 0.0936389],
[0.0912655, 0.215648, 0.093491],
[0.0948729, 0.219557, 0.093256],
[0.0986004, 0.223439, 0.0929344],
[0.102447, 0.227292, 0.0925267],
[0.10641, 0.231118, 0.0920334],
[0.110489, 0.234915, 0.091455],
[0.114682, 0.238683, 0.0907918],
[0.118986, 0.242422, 0.0900444],
[0.1234, 0.246131, 0.0892132],
[0.127921, 0.249811, 0.0882985],
[0.132546, 0.253461, 0.0873006],
[0.137274, 0.257081, 0.0862199],
[0.142102, 0.260671, 0.0850567],
[0.147026, 0.264229, 0.083811],
[0.152046, 0.267758, 0.0824831],
[0.157157, 0.271255, 0.0810729],
[0.162358, 0.274722, 0.0795804],
[0.167646, 0.278157, 0.0780056],
[0.173018, 0.281561, 0.076348],
[0.178473, 0.284933, 0.0746074],
[0.184007, 0.288275, 0.0727832],
[0.189617, 0.291584, 0.0708747],
[0.195303, 0.294862, 0.0688811],
[0.20106, 0.298109, 0.0668011],
[0.206888, 0.301324, 0.0646335],
[0.212783, 0.304508, 0.0623766],
[0.218743, 0.307661, 0.0600284],
[0.224766, 0.310782, 0.0575865],
[0.23085, 0.313872, 0.0550481],
[0.236993, 0.316931, 0.0524097],
[0.243192, 0.319959, 0.0496672],
[0.249445, 0.322956, 0.0468157],
[0.255751, 0.325923, 0.0438493],
[0.262107, 0.328859, 0.0407608],
[0.268511, 0.331765, 0.0375547],
[0.274961, 0.334642, 0.0343642],
[0.281456, 0.337489, 0.0312019],
[0.287993, 0.340307, 0.0280746],
[0.294571, 0.343095, 0.0249891],
[0.301187, 0.345856, 0.021952],
[0.30784, 0.348588, 0.0189702],
[0.314528, 0.351293, 0.0160506],
[0.32125, 0.353971, 0.0132001],
[0.328002, 0.356622, 0.0104257],
[0.334785, 0.359246, 0.00773459],
[0.341595, 0.361845, 0.00513392],
[0.348431, 0.364419, 0.00263108],
[0.355292, 0.366968, 0.000233571],
[0.362176, 0.369493, 0.],
[0.369081, 0.371995, 0.],
[0.376005, 0.374474, 0.],
[0.382948, 0.376931, 0.],
[0.389906, 0.379367, 0.],
[0.396879, 0.381782, 0.],
[0.403865, 0.384177, 0.],
[0.410862, 0.386553, 0.],
[0.417869, 0.388911, 0.],
[0.424884, 0.391251, 0.],
[0.431906, 0.393575, 0.],
[0.438933, 0.395883, 0.],
[0.445964, 0.398177, 0.],
[0.452996, 0.400456, 0.],
[0.460029, 0.402723, 0.],
[0.46706, 0.404978, 0.],
[0.474089, 0.407222, 0.],
[0.481114, 0.409456, 0.],
[0.488133, 0.411681, 0.],
[0.495144, 0.413899, 0.],
[0.502147, 0.41611, 0.],
[0.50914, 0.418316, 0.],
[0.51612, 0.420517, 0.],
[0.523087, 0.422716, 0.],
[0.53004, 0.424912, 0.00231759],
[0.536976, 0.427108, 0.00636217],
[0.543894, 0.429304, 0.0108654],
[0.550793, 0.431502, 0.0158503],
[0.55767, 0.433704, 0.0213408],
[0.564526, 0.435909, 0.0273619],
[0.571357, 0.438121, 0.0339398],
[0.578163, 0.440339, 0.0410878],
[0.584942, 0.442566, 0.0482801],
[0.591693, 0.444802, 0.0553487],
[0.598414, 0.447049, 0.0623311],
[0.605103, 0.449309, 0.0692556],
[0.61176, 0.451583, 0.0761443],
[0.618382, 0.453872, 0.0830145],
[0.624969, 0.456178, 0.0898804],
[0.631518, 0.458502, 0.0967534],
[0.638029, 0.460845, 0.103643],
[0.644499, 0.463209, 0.110558],
[0.650928, 0.465595, 0.117505],
[0.657314, 0.468005, 0.124489],
[0.663656, 0.470441, 0.131516],
[0.669951, 0.472902, 0.138591],
[0.676199, 0.475392, 0.145716],
[0.682399, 0.47791, 0.152896],
[0.688548, 0.48046, 0.160134],
[0.694646, 0.483041, 0.167431],
[0.700691, 0.485656, 0.17479],
[0.706682, 0.488305, 0.182214],
[0.712618, 0.49099, 0.189702],
[0.718496, 0.493713, 0.197258],
[0.724317, 0.496474, 0.204882],
[0.730078, 0.499274, 0.212574],
[0.735779, 0.502116, 0.220335],
[0.741418, 0.505, 0.228167],
[0.746994, 0.507927, 0.236068],
[0.752506, 0.510899, 0.244039],
[0.757952, 0.513916, 0.252081],
[0.763332, 0.51698, 0.260191],
[0.768645, 0.520091, 0.268371],
[0.773889, 0.523251, 0.276619],
[0.779064, 0.526461, 0.284935],
[0.784168, 0.529721, 0.293317],
[0.7892, 0.533032, 0.301764],
[0.79416, 0.536395, 0.310276],
[0.799047, 0.539812, 0.31885],
[0.80386, 0.543281, 0.327485],
[0.808598, 0.546806, 0.336179],
[0.81326, 0.550385, 0.34493],
[0.817846, 0.554019, 0.353737],
[0.822356, 0.55771, 0.362597],
[0.826787, 0.561458, 0.371508],
[0.831141, 0.565262, 0.380468],
[0.835417, 0.569123, 0.389473],
[0.839614, 0.573043, 0.398522],
[0.843731, 0.57702, 0.407612],
[0.847769, 0.581056, 0.416739],
[0.851728, 0.58515, 0.425902],
[0.855607, 0.589302, 0.435097],
[0.859406, 0.593513, 0.44432],
[0.863124, 0.597783, 0.453569],
[0.866764, 0.602111, 0.462841],
[0.870323, 0.606498, 0.472131],
[0.873803, 0.610943, 0.481438],
[0.877204, 0.615447, 0.490757],
[0.880526, 0.620008, 0.500085],
[0.883769, 0.624627, 0.509419],
[0.886935, 0.629304, 0.518754],
[0.890024, 0.634037, 0.528088],
[0.893035, 0.638827, 0.537416],
[0.895971, 0.643673, 0.546736],
[0.898833, 0.648575, 0.556044],
[0.90162, 0.653532, 0.565335],
[0.904334, 0.658543, 0.574608],
[0.906976, 0.663608, 0.583857],
[0.909548, 0.668726, 0.59308],
[0.912051, 0.673896, 0.602272],
[0.914485, 0.679118, 0.611432],
[0.916854, 0.68439, 0.620555],
[0.919157, 0.689712, 0.629637],
[0.921398, 0.695084, 0.638677],
[0.923577, 0.700503, 0.647669],
[0.925696, 0.70597, 0.656613],
[0.927758, 0.711483, 0.665503],
[0.929765, 0.71704, 0.674338],
[0.931718, 0.722642, 0.683115],
[0.93362, 0.728287, 0.69183],
[0.935474, 0.733974, 0.700481],
[0.937281, 0.739702, 0.709067],
[0.939044, 0.74547, 0.717583],
[0.940765, 0.751276, 0.726028],
[0.942449, 0.757119, 0.7344],
[0.944096, 0.762999, 0.742697],
[0.94571, 0.768913, 0.750916],
[0.947295, 0.774861, 0.759057],
[0.948852, 0.780842, 0.767116],
[0.950385, 0.786854, 0.775094],
[0.951897, 0.792896, 0.782987],
[0.953392, 0.798967, 0.790796],
[0.954872, 0.805066, 0.798519],
[0.956341, 0.81119, 0.806155],
[0.957803, 0.81734, 0.813703],
[0.95926, 0.823513, 0.821163],
[0.960717, 0.829708, 0.828534],
[0.962177, 0.835925, 0.835815],
[0.963644, 0.842162, 0.843006],
[0.965121, 0.848417, 0.850108],
[0.966612, 0.85469, 0.85712],
[0.968122, 0.860978, 0.864043],
[0.969653, 0.867282, 0.870876],
[0.97121, 0.873598, 0.877621],
[0.972798, 0.879927, 0.884277],
[0.974419, 0.886267, 0.890846],
[0.976078, 0.892617, 0.897328],
[0.97778, 0.898975, 0.903725],
[0.979528, 0.905339, 0.910037],
[0.981328, 0.91171, 0.916266],
[0.983184, 0.918084, 0.922413],
[0.9851, 0.924461, 0.92848],
[0.987082, 0.93084, 0.934468],
[0.989135, 0.937217, 0.94038],
[0.991265, 0.943592, 0.946217],
[0.993479, 0.949963, 0.951981],
[0.995783, 0.956327, 0.957675],
[0.998187, 0.96268, 0.963301],
[1., 0.96902, 0.968862],
[1., 0.975339, 0.974362],
[1., 0.981631, 0.979803],
[1., 0.987876, 0.98519],
[1., 0.994001, 0.990529]]

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
