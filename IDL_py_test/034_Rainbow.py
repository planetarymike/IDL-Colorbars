from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.486275, 0., 1.],
[0.486275, 0., 1.],
[0.470588, 0., 1.],
[0.45098, 0., 1.],
[0.435294, 0., 1.],
[0.415686, 0., 1.],
[0.4, 0., 1.],
[0.380392, 0., 1.],
[0.364706, 0., 1.],
[0.345098, 0., 1.],
[0.329412, 0., 1.],
[0.309804, 0., 1.],
[0.294118, 0., 1.],
[0.27451, 0., 1.],
[0.258824, 0., 1.],
[0.239216, 0., 1.],
[0.223529, 0., 1.],
[0.203922, 0., 1.],
[0.188235, 0., 1.],
[0.168627, 0., 1.],
[0.152941, 0., 1.],
[0.133333, 0., 1.],
[0.117647, 0., 1.],
[0.0980392, 0., 1.],
[0.0823529, 0., 1.],
[0.0627451, 0., 1.],
[0.0470588, 0., 1.],
[0.027451, 0., 1.],
[0.0117647, 0., 1.],
[0., 0.00784314, 1.],
[0., 0.0235294, 1.],
[0., 0.0431373, 1.],
[0., 0.0588235, 1.],
[0., 0.0784314, 1.],
[0., 0.0941176, 1.],
[0., 0.113725, 1.],
[0., 0.129412, 1.],
[0., 0.14902, 1.],
[0., 0.164706, 1.],
[0., 0.184314, 1.],
[0., 0.2, 1.],
[0., 0.219608, 1.],
[0., 0.235294, 1.],
[0., 0.254902, 1.],
[0., 0.270588, 1.],
[0., 0.290196, 1.],
[0., 0.305882, 1.],
[0., 0.32549, 1.],
[0., 0.341176, 1.],
[0., 0.360784, 1.],
[0., 0.376471, 1.],
[0., 0.396078, 1.],
[0., 0.411765, 1.],
[0., 0.431373, 1.],
[0., 0.447059, 1.],
[0., 0.466667, 1.],
[0., 0.482353, 1.],
[0., 0.501961, 1.],
[0., 0.517647, 1.],
[0., 0.537255, 1.],
[0., 0.552941, 1.],
[0., 0.572549, 1.],
[0., 0.588235, 1.],
[0., 0.607843, 1.],
[0., 0.623529, 1.],
[0., 0.643137, 1.],
[0., 0.658824, 1.],
[0., 0.678431, 1.],
[0., 0.694118, 1.],
[0., 0.713725, 1.],
[0., 0.729412, 1.],
[0., 0.74902, 1.],
[0., 0.764706, 1.],
[0., 0.784314, 1.],
[0., 0.8, 1.],
[0., 0.819608, 1.],
[0., 0.835294, 1.],
[0., 0.854902, 1.],
[0., 0.870588, 1.],
[0., 0.890196, 1.],
[0., 0.905882, 1.],
[0., 0.92549, 1.],
[0., 0.945098, 1.],
[0., 0.960784, 1.],
[0., 0.980392, 1.],
[0., 0.996078, 1.],
[0., 1., 0.984314],
[0., 1., 0.968627],
[0., 1., 0.94902],
[0., 1., 0.933333],
[0., 1., 0.913725],
[0., 1., 0.898039],
[0., 1., 0.878431],
[0., 1., 0.862745],
[0., 1., 0.843137],
[0., 1., 0.827451],
[0., 1., 0.807843],
[0., 1., 0.792157],
[0., 1., 0.772549],
[0., 1., 0.756863],
[0., 1., 0.737255],
[0., 1., 0.721569],
[0., 1., 0.701961],
[0., 1., 0.686275],
[0., 1., 0.666667],
[0., 1., 0.65098],
[0., 1., 0.631373],
[0., 1., 0.615686],
[0., 1., 0.596078],
[0., 1., 0.580392],
[0., 1., 0.560784],
[0., 1., 0.545098],
[0., 1., 0.52549],
[0., 1., 0.509804],
[0., 1., 0.490196],
[0., 1., 0.47451],
[0., 1., 0.454902],
[0., 1., 0.439216],
[0., 1., 0.419608],
[0., 1., 0.403922],
[0., 1., 0.384314],
[0., 1., 0.368627],
[0., 1., 0.34902],
[0., 1., 0.333333],
[0., 1., 0.313725],
[0., 1., 0.298039],
[0., 1., 0.278431],
[0., 1., 0.262745],
[0., 1., 0.243137],
[0., 1., 0.227451],
[0., 1., 0.207843],
[0., 1., 0.192157],
[0., 1., 0.172549],
[0., 1., 0.156863],
[0., 1., 0.137255],
[0., 1., 0.121569],
[0., 1., 0.101961],
[0., 1., 0.0862745],
[0., 1., 0.0666667],
[0., 1., 0.0509804],
[0., 1., 0.0313725],
[0., 1., 0.0156863],
[0.00392157, 1., 0.],
[0.0196078, 1., 0.],
[0.0509804, 1., 0.],
[0.054902, 1., 0.],
[0.0745098, 1., 0.],
[0.0901961, 1., 0.],
[0.109804, 1., 0.],
[0.12549, 1., 0.],
[0.145098, 1., 0.],
[0.160784, 1., 0.],
[0.180392, 1., 0.],
[0.196078, 1., 0.],
[0.215686, 1., 0.],
[0.231373, 1., 0.],
[0.25098, 1., 0.],
[0.266667, 1., 0.],
[0.286275, 1., 0.],
[0.301961, 1., 0.],
[0.321569, 1., 0.],
[0.337255, 1., 0.],
[0.356863, 1., 0.],
[0.372549, 1., 0.],
[0.392157, 1., 0.],
[0.407843, 1., 0.],
[0.427451, 1., 0.],
[0.443137, 1., 0.],
[0.462745, 1., 0.],
[0.482353, 1., 0.],
[0.498039, 1., 0.],
[0.517647, 1., 0.],
[0.533333, 1., 0.],
[0.552941, 1., 0.],
[0.568627, 1., 0.],
[0.588235, 1., 0.],
[0.603922, 1., 0.],
[0.623529, 1., 0.],
[0.639216, 1., 0.],
[0.658824, 1., 0.],
[0.67451, 1., 0.],
[0.694118, 1., 0.],
[0.709804, 1., 0.],
[0.729412, 1., 0.],
[0.745098, 1., 0.],
[0.764706, 1., 0.],
[0.780392, 1., 0.],
[0.8, 1., 0.],
[0.815686, 1., 0.],
[0.835294, 1., 0.],
[0.85098, 1., 0.],
[0.870588, 1., 0.],
[0.886275, 1., 0.],
[0.905882, 1., 0.],
[0.921569, 1., 0.],
[0.941176, 1., 0.],
[0.956863, 1., 0.],
[0.976471, 1., 0.],
[0.992157, 1., 0.],
[1., 0.988235, 0.],
[1., 0.972549, 0.],
[1., 0.952941, 0.],
[1., 0.937255, 0.],
[1., 0.917647, 0.],
[1., 0.901961, 0.],
[1., 0.882353, 0.],
[1., 0.866667, 0.],
[1., 0.847059, 0.],
[1., 0.831373, 0.],
[1., 0.811765, 0.],
[1., 0.796078, 0.],
[1., 0.776471, 0.],
[1., 0.760784, 0.],
[1., 0.741176, 0.],
[1., 0.72549, 0.],
[1., 0.705882, 0.],
[1., 0.690196, 0.],
[1., 0.670588, 0.],
[1., 0.654902, 0.],
[1., 0.635294, 0.],
[1., 0.619608, 0.],
[1., 0.6, 0.],
[1., 0.584314, 0.],
[1., 0.564706, 0.],
[1., 0.54902, 0.],
[1., 0.529412, 0.],
[1., 0.513725, 0.],
[1., 0.494118, 0.],
[1., 0.478431, 0.],
[1., 0.458824, 0.],
[1., 0.443137, 0.],
[1., 0.423529, 0.],
[1., 0.407843, 0.],
[1., 0.388235, 0.],
[1., 0.372549, 0.],
[1., 0.352941, 0.],
[1., 0.337255, 0.],
[1., 0.317647, 0.],
[1., 0.301961, 0.],
[1., 0.282353, 0.],
[1., 0.266667, 0.],
[1., 0.247059, 0.],
[1., 0.231373, 0.],
[1., 0.211765, 0.],
[1., 0.196078, 0.],
[1., 0.176471, 0.],
[1., 0.160784, 0.],
[1., 0.141176, 0.],
[1., 0.12549, 0.],
[1., 0.105882, 0.],
[1., 0.0901961, 0.],
[1., 0.0705882, 0.],
[1., 0.054902, 0.],
[1., 0.0352941, 0.],
[1., 0.0196078, 0.],
[1., 0.0196078, 0.]]

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
