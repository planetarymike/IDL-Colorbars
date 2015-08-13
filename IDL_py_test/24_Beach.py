from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0., 0.984314, 0.],
[0., 0.984314, 0.],
[0., 0.976471, 0.],
[0., 0.968627, 0.],
[0., 0.960784, 0.],
[0., 0.952941, 0.],
[0., 0.945098, 0.],
[0., 0.933333, 0.],
[0., 0.92549, 0.],
[0., 0.917647, 0.],
[0., 0.909804, 0.],
[0., 0.901961, 0.],
[0., 0.894118, 0.],
[0., 0.886275, 0.],
[0., 0.878431, 0.],
[0., 0.866667, 0.],
[0., 0.858824, 0.],
[0., 0.85098, 0.],
[0., 0.843137, 0.],
[0., 0.835294, 0.],
[0., 0.827451, 0.],
[0., 0.819608, 0.],
[0., 0.807843, 0.],
[0., 0.8, 0.],
[0., 0.792157, 0.],
[0., 0.784314, 0.],
[0., 0.776471, 0.],
[0., 0.768627, 0.],
[0., 0.760784, 0.],
[0., 0.752941, 0.],
[0., 0.741176, 0.],
[0., 0.733333, 0.],
[0., 0.72549, 0.],
[0., 0.717647, 0.],
[0., 0.709804, 0.],
[0., 0.701961, 0.],
[0., 0.694118, 0.],
[0., 0.682353, 0.],
[0., 0.67451, 0.],
[0., 0.666667, 0.],
[0., 0.658824, 0.],
[0., 0.65098, 0.],
[0., 0.643137, 0.],
[0., 0.635294, 0.],
[0., 0.627451, 0.],
[0., 0.615686, 0.],
[0., 0.607843, 0.],
[0., 0.6, 0.],
[0., 0.592157, 0.],
[0., 0.584314, 0.],
[0., 0.576471, 0.],
[0., 0.568627, 0.],
[0., 0.556863, 0.],
[0., 0.54902, 0.],
[0., 0.541176, 0.],
[0., 0.533333, 0.],
[0., 0.52549, 0.],
[0., 0.517647, 0.],
[0., 0.509804, 0.],
[0., 0.501961, 0.],
[0., 0.501961, 0.0156863],
[0., 0.505882, 0.0313725],
[0., 0.513725, 0.0470588],
[0., 0.521569, 0.0666667],
[0., 0.52549, 0.0823529],
[0., 0.533333, 0.0980392],
[0., 0.541176, 0.113725],
[0., 0.545098, 0.133333],
[0., 0.552941, 0.14902],
[0., 0.560784, 0.164706],
[0., 0.568627, 0.180392],
[0., 0.572549, 0.2],
[0., 0.580392, 0.215686],
[0., 0.588235, 0.231373],
[0., 0.592157, 0.25098],
[0., 0.6, 0.266667],
[0., 0.607843, 0.282353],
[0., 0.615686, 0.298039],
[0., 0.619608, 0.317647],
[0., 0.627451, 0.333333],
[0., 0.635294, 0.34902],
[0., 0.639216, 0.364706],
[0., 0.647059, 0.384314],
[0., 0.654902, 0.4],
[0., 0.658824, 0.415686],
[0., 0.666667, 0.431373],
[0., 0.67451, 0.45098],
[0., 0.682353, 0.466667],
[0., 0.686275, 0.482353],
[0., 0.694118, 0.501961],
[0., 0.701961, 0.517647],
[0., 0.705882, 0.533333],
[0., 0.713725, 0.533333],
[0., 0.713725, 0.533333],
[0.0156863, 0.694118, 0.533333],
[0.0313725, 0.670588, 0.533333],
[0.0470588, 0.647059, 0.533333],
[0.0666667, 0.627451, 0.533333],
[0.0823529, 0.603922, 0.533333],
[0.0980392, 0.584314, 0.533333],
[0.113725, 0.560784, 0.533333],
[0.133333, 0.541176, 0.533333],
[0.14902, 0.517647, 0.533333],
[0.164706, 0.494118, 0.533333],
[0.180392, 0.47451, 0.533333],
[0.2, 0.45098, 0.533333],
[0.215686, 0.431373, 0.533333],
[0.231373, 0.407843, 0.533333],
[0.25098, 0.388235, 0.533333],
[0.266667, 0.364706, 0.533333],
[0.282353, 0.345098, 0.533333],
[0.298039, 0.321569, 0.533333],
[0.317647, 0.298039, 0.533333],
[0.333333, 0.278431, 0.533333],
[0.34902, 0.254902, 0.533333],
[0.364706, 0.235294, 0.533333],
[0.384314, 0.211765, 0.533333],
[0.4, 0.192157, 0.533333],
[0.415686, 0.168627, 0.533333],
[0.431373, 0.145098, 0.533333],
[0.45098, 0.12549, 0.533333],
[0.466667, 0.101961, 0.533333],
[0.482353, 0.0823529, 0.533333],
[0.501961, 0.0588235, 0.533333],
[0.517647, 0.0509804, 0.533333],
[0.533333, 0.0156863, 0.298039],
[0.54902, 0., 0.298039],
[0.298039, 0., 0.298039],
[0.298039, 0., 0.282353],
[0.298039, 0.0156863, 0.266667],
[0.317647, 0.0313725, 0.25098],
[0.333333, 0.0470588, 0.235294],
[0.34902, 0.0666667, 0.219608],
[0.364706, 0.0823529, 0.203922],
[0.384314, 0.0980392, 0.188235],
[0.4, 0.113725, 0.172549],
[0.415686, 0.133333, 0.156863],
[0.431373, 0.14902, 0.141176],
[0.45098, 0.164706, 0.12549],
[0.466667, 0.180392, 0.109804],
[0.482353, 0.2, 0.0901961],
[0.501961, 0.215686, 0.0745098],
[0.517647, 0.231373, 0.0588235],
[0.533333, 0.25098, 0.0431373],
[0.54902, 0.266667, 0.027451],
[0.568627, 0.282353, 0.0117647],
[0.584314, 0.298039, 0.],
[0.6, 0.317647, 0.],
[0.615686, 0.317647, 0.],
[0.615686, 0.333333, 0.],
[0.631373, 0.34902, 0.],
[0.643137, 0.364706, 0.],
[0.654902, 0.384314, 0.],
[0.666667, 0.4, 0.],
[0.678431, 0.415686, 0.],
[0.694118, 0.431373, 0.],
[0.705882, 0.45098, 0.],
[0.717647, 0.466667, 0.],
[0.729412, 0.482353, 0.],
[0.741176, 0.501961, 0.],
[0.756863, 0.517647, 0.],
[0.768627, 0.533333, 0.],
[0.780392, 0.54902, 0.],
[0.792157, 0.568627, 0.],
[0.803922, 0.584314, 0.],
[0.819608, 0.6, 0.],
[0.831373, 0.615686, 0.],
[0.843137, 0.635294, 0.],
[0.854902, 0.635294, 0.],
[0.854902, 0.65098, 0.],
[0.858824, 0.666667, 0.],
[0.862745, 0.682353, 0.],
[0.870588, 0.701961, 0.],
[0.87451, 0.717647, 0.],
[0.878431, 0.733333, 0.],
[0.882353, 0.752941, 0.],
[0.886275, 0.768627, 0.],
[0.890196, 0.784314, 0.],
[0.898039, 0.8, 0.],
[0.901961, 0.819608, 0.],
[0.905882, 0.835294, 0.],
[0.909804, 0.85098, 0.],
[0.913725, 0.866667, 0.],
[0.917647, 0.886275, 0.],
[0.92549, 0.901961, 0.],
[0.929412, 0.917647, 0.],
[0.933333, 0.933333, 0.],
[0.937255, 0.952941, 0.],
[0.941176, 0., 0.0156863],
[0., 0., 0.0313725],
[0., 0., 0.0470588],
[0., 0., 0.0666667],
[0., 0., 0.0823529],
[0., 0., 0.0980392],
[0., 0., 0.113725],
[0., 0., 0.133333],
[0., 0., 0.14902],
[0., 0., 0.164706],
[0., 0., 0.180392],
[0., 0., 0.2],
[0., 0., 0.215686],
[0., 0., 0.231373],
[0., 0., 0.25098],
[0., 0., 0.266667],
[0., 0., 0.282353],
[0., 0., 0.298039],
[0., 0., 0.317647],
[0., 0., 0.317647],
[0., 0., 0.329412],
[0., 0., 0.345098],
[0., 0., 0.356863],
[0., 0., 0.372549],
[0., 0., 0.384314],
[0., 0., 0.4],
[0., 0., 0.411765],
[0., 0., 0.427451],
[0., 0., 0.443137],
[0., 0., 0.454902],
[0., 0., 0.470588],
[0., 0., 0.482353],
[0., 0., 0.498039],
[0., 0., 0.509804],
[0., 0., 0.52549],
[0., 0., 0.537255],
[0., 0., 0.552941],
[0., 0., 0.568627],
[0., 0., 0.580392],
[0., 0., 0.596078],
[0., 0., 0.607843],
[0., 0., 0.623529],
[0., 0., 0.623529],
[0., 0., 0.635294],
[0., 0., 0.65098],
[0., 0., 0.666667],
[0., 0., 0.678431],
[0., 0., 0.694118],
[0., 0., 0.709804],
[0., 0., 0.721569],
[0., 0., 0.737255],
[0., 0., 0.752941],
[0., 0., 0.764706],
[0., 0., 0.780392],
[0., 0., 0.796078],
[0., 0., 0.807843],
[0., 0., 0.823529],
[0., 0., 0.839216],
[0., 0., 0.85098],
[0., 0., 0.866667],
[0., 0., 0.882353],
[0., 0., 0.894118],
[0., 0., 0.909804],
[0., 0., 0.92549],
[0., 0., 0.937255],
[0., 0., 0.],
[0., 0., 0.],
[0., 0., 0.]]

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