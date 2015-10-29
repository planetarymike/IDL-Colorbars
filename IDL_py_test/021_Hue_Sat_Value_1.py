from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[1., 0., 0.0117647],
[1., 0., 0.0117647],
[1., 0.00392157, 0.0509804],
[1., 0.00784314, 0.0666667],
[1., 0.0117647, 0.0901961],
[1., 0.0156863, 0.117647],
[1., 0.0196078, 0.145098],
[1., 0.0235294, 0.172549],
[1., 0.027451, 0.196078],
[1., 0.0313725, 0.223529],
[1., 0.0352941, 0.247059],
[1., 0.0509804, 0.27451],
[1., 0.0431373, 0.298039],
[1., 0.0470588, 0.321569],
[1., 0.0509804, 0.34902],
[1., 0.054902, 0.372549],
[1., 0.0588235, 0.396078],
[1., 0.0627451, 0.419608],
[1., 0.0666667, 0.447059],
[1., 0.0705882, 0.470588],
[1., 0.0745098, 0.494118],
[1., 0.0784314, 0.517647],
[1., 0.0823529, 0.541176],
[1., 0.0862745, 0.564706],
[1., 0.0901961, 0.584314],
[1., 0.0941176, 0.607843],
[1., 0.0980392, 0.631373],
[1., 0.101961, 0.654902],
[1., 0.105882, 0.67451],
[1., 0.109804, 0.698039],
[1., 0.113725, 0.721569],
[1., 0.117647, 0.741176],
[1., 0.121569, 0.764706],
[1., 0.12549, 0.784314],
[1., 0.129412, 0.803922],
[1., 0.133333, 0.827451],
[1., 0.137255, 0.847059],
[1., 0.141176, 0.866667],
[1., 0.145098, 0.890196],
[1., 0.14902, 0.909804],
[1., 0.152941, 0.929412],
[1., 0.156863, 0.94902],
[1., 0.160784, 0.968627],
[1., 0.164706, 0.988235],
[0.988235, 0.168627, 1.],
[0.968627, 0.172549, 1.],
[0.94902, 0.176471, 1.],
[0.929412, 0.180392, 1.],
[0.913725, 0.184314, 1.],
[0.894118, 0.188235, 1.],
[0.87451, 0.192157, 1.],
[0.858824, 0.196078, 1.],
[0.839216, 0.2, 1.],
[0.823529, 0.203922, 1.],
[0.803922, 0.207843, 1.],
[0.788235, 0.211765, 1.],
[0.768627, 0.215686, 1.],
[0.752941, 0.219608, 1.],
[0.737255, 0.223529, 1.],
[0.721569, 0.227451, 1.],
[0.701961, 0.231373, 1.],
[0.686275, 0.235294, 1.],
[0.670588, 0.239216, 1.],
[0.654902, 0.243137, 1.],
[0.639216, 0.247059, 1.],
[0.623529, 0.25098, 1.],
[0.607843, 0.25098, 1.],
[0.592157, 0.254902, 1.],
[0.576471, 0.258824, 1.],
[0.564706, 0.262745, 1.],
[0.54902, 0.266667, 1.],
[0.533333, 0.270588, 1.],
[0.521569, 0.27451, 1.],
[0.505882, 0.278431, 1.],
[0.490196, 0.282353, 1.],
[0.478431, 0.286275, 1.],
[0.462745, 0.290196, 1.],
[0.45098, 0.294118, 1.],
[0.439216, 0.298039, 1.],
[0.423529, 0.301961, 1.],
[0.411765, 0.305882, 1.],
[0.4, 0.309804, 1.],
[0.388235, 0.313725, 1.],
[0.372549, 0.317647, 1.],
[0.360784, 0.321569, 1.],
[0.34902, 0.32549, 1.],
[0.337255, 0.329412, 1.],
[0.333333, 0.341176, 1.],
[0.337255, 0.360784, 1.],
[0.341176, 0.380392, 1.],
[0.345098, 0.4, 1.],
[0.34902, 0.419608, 1.],
[0.352941, 0.435294, 1.],
[0.356863, 0.454902, 1.],
[0.360784, 0.47451, 1.],
[0.364706, 0.490196, 1.],
[0.368627, 0.509804, 1.],
[0.372549, 0.52549, 1.],
[0.376471, 0.545098, 1.],
[0.380392, 0.560784, 1.],
[0.384314, 0.576471, 1.],
[0.388235, 0.596078, 1.],
[0.392157, 0.611765, 1.],
[0.396078, 0.627451, 1.],
[0.4, 0.643137, 1.],
[0.403922, 0.658824, 1.],
[0.407843, 0.67451, 1.],
[0.411765, 0.690196, 1.],
[0.415686, 0.705882, 1.],
[0.419608, 0.721569, 1.],
[0.423529, 0.737255, 1.],
[0.427451, 0.752941, 1.],
[0.431373, 0.768627, 1.],
[0.435294, 0.780392, 1.],
[0.439216, 0.796078, 1.],
[0.443137, 0.811765, 1.],
[0.447059, 0.823529, 1.],
[0.45098, 0.839216, 1.],
[0.454902, 0.85098, 1.],
[0.458824, 0.866667, 1.],
[0.462745, 0.878431, 1.],
[0.466667, 0.894118, 1.],
[0.470588, 0.905882, 1.],
[0.47451, 0.917647, 1.],
[0.478431, 0.933333, 1.],
[0.482353, 0.945098, 1.],
[0.486275, 0.956863, 1.],
[0.490196, 0.968627, 1.],
[0.494118, 0.980392, 1.],
[0.498039, 0.992157, 1.],
[0.501961, 1., 0.992157],
[0.505882, 1., 0.980392],
[0.509804, 1., 0.968627],
[0.513725, 1., 0.956863],
[0.517647, 1., 0.94902],
[0.521569, 1., 0.937255],
[0.52549, 1., 0.92549],
[0.529412, 1., 0.917647],
[0.533333, 1., 0.905882],
[0.537255, 1., 0.898039],
[0.541176, 1., 0.886275],
[0.545098, 1., 0.878431],
[0.54902, 1., 0.866667],
[0.552941, 1., 0.858824],
[0.556863, 1., 0.85098],
[0.560784, 1., 0.839216],
[0.564706, 1., 0.831373],
[0.568627, 1., 0.823529],
[0.572549, 1., 0.815686],
[0.576471, 1., 0.807843],
[0.580392, 1., 0.8],
[0.584314, 1., 0.792157],
[0.588235, 1., 0.784314],
[0.592157, 1., 0.776471],
[0.596078, 1., 0.768627],
[0.6, 1., 0.760784],
[0.603922, 1., 0.752941],
[0.607843, 1., 0.74902],
[0.611765, 1., 0.741176],
[0.615686, 1., 0.733333],
[0.619608, 1., 0.729412],
[0.623529, 1., 0.721569],
[0.627451, 1., 0.717647],
[0.631373, 1., 0.709804],
[0.635294, 1., 0.705882],
[0.639216, 1., 0.701961],
[0.643137, 1., 0.694118],
[0.647059, 1., 0.690196],
[0.65098, 1., 0.686275],
[0.654902, 1., 0.682353],
[0.658824, 1., 0.678431],
[0.662745, 1., 0.67451],
[0.666667, 1., 0.670588],
[0.67451, 1., 0.670588],
[0.686275, 1., 0.67451],
[0.694118, 1., 0.678431],
[0.705882, 1., 0.682353],
[0.717647, 1., 0.686275],
[0.729412, 1., 0.690196],
[0.737255, 1., 0.694118],
[0.74902, 1., 0.698039],
[0.760784, 1., 0.701961],
[0.768627, 1., 0.705882],
[0.780392, 1., 0.709804],
[0.788235, 1., 0.713725],
[0.796078, 1., 0.717647],
[0.807843, 1., 0.721569],
[0.815686, 1., 0.72549],
[0.823529, 1., 0.729412],
[0.835294, 1., 0.733333],
[0.843137, 1., 0.737255],
[0.85098, 1., 0.741176],
[0.858824, 1., 0.745098],
[0.866667, 1., 0.74902],
[0.87451, 1., 0.74902],
[0.882353, 1., 0.752941],
[0.890196, 1., 0.756863],
[0.898039, 1., 0.760784],
[0.901961, 1., 0.764706],
[0.909804, 1., 0.768627],
[0.917647, 1., 0.772549],
[0.92549, 1., 0.776471],
[0.929412, 1., 0.780392],
[0.937255, 1., 0.784314],
[0.941176, 1., 0.788235],
[0.94902, 1., 0.792157],
[0.952941, 1., 0.796078],
[0.960784, 1., 0.8],
[0.964706, 1., 0.803922],
[0.968627, 1., 0.807843],
[0.972549, 1., 0.811765],
[0.980392, 1., 0.815686],
[0.984314, 1., 0.819608],
[0.988235, 1., 0.823529],
[0.992157, 1., 0.827451],
[0.996078, 1., 0.831373],
[1., 0.996078, 0.835294],
[1., 0.992157, 0.839216],
[1., 0.988235, 0.843137],
[1., 0.984314, 0.847059],
[1., 0.984314, 0.85098],
[1., 0.980392, 0.854902],
[1., 0.976471, 0.858824],
[1., 0.976471, 0.862745],
[1., 0.972549, 0.866667],
[1., 0.968627, 0.870588],
[1., 0.968627, 0.87451],
[1., 0.964706, 0.878431],
[1., 0.964706, 0.882353],
[1., 0.964706, 0.886275],
[1., 0.960784, 0.890196],
[1., 0.960784, 0.894118],
[1., 0.960784, 0.898039],
[1., 0.960784, 0.901961],
[1., 0.956863, 0.905882],
[1., 0.956863, 0.909804],
[1., 0.956863, 0.913725],
[1., 0.956863, 0.917647],
[1., 0.956863, 0.921569],
[1., 0.956863, 0.92549],
[1., 0.960784, 0.929412],
[1., 0.960784, 0.933333],
[1., 0.960784, 0.937255],
[1., 0.960784, 0.941176],
[1., 0.964706, 0.945098],
[1., 0.964706, 0.94902],
[1., 0.964706, 0.952941],
[1., 0.968627, 0.956863],
[1., 0.968627, 0.960784],
[1., 0.972549, 0.964706],
[1., 0.976471, 0.968627],
[1., 0.976471, 0.972549],
[1., 0.980392, 0.976471],
[1., 0.984314, 0.980392],
[1., 0.984314, 0.984314],
[1., 0.984314, 0.984314]]

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
