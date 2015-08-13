from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.25098, 0.137255, 0.454902],
[0.25098, 0.137255, 0.454902],
[0.235294, 0.156863, 0.411765],
[0.223529, 0.172549, 0.368627],
[0.211765, 0.192157, 0.329412],
[0.2, 0.211765, 0.290196],
[0.188235, 0.227451, 0.25098],
[0.176471, 0.247059, 0.215686],
[0.164706, 0.262745, 0.180392],
[0.156863, 0.282353, 0.14902],
[0.145098, 0.298039, 0.117647],
[0.137255, 0.313725, 0.0941176],
[0.12549, 0.329412, 0.0705882],
[0.117647, 0.34902, 0.0470588],
[0.109804, 0.364706, 0.0313725],
[0.101961, 0.376471, 0.0196078],
[0.0941176, 0.392157, 0.00784314],
[0.0862745, 0.407843, 0.],
[0.0784314, 0.423529, 0.],
[0.0745098, 0.435294, 0.],
[0.0666667, 0.45098, 0.00392157],
[0.0627451, 0.462745, 0.0117647],
[0.054902, 0.47451, 0.0235294],
[0.0509804, 0.486275, 0.0509804],
[0.0470588, 0.498039, 0.054902],
[0.0431373, 0.509804, 0.0784314],
[0.0509804, 0.521569, 0.101961],
[0.0352941, 0.529412, 0.129412],
[0.0352941, 0.537255, 0.160784],
[0.0313725, 0.54902, 0.196078],
[0.027451, 0.556863, 0.231373],
[0.027451, 0.564706, 0.266667],
[0.027451, 0.568627, 0.305882],
[0.027451, 0.576471, 0.345098],
[0.027451, 0.580392, 0.388235],
[0.027451, 0.588235, 0.427451],
[0.027451, 0.592157, 0.470588],
[0.027451, 0.596078, 0.513725],
[0.027451, 0.596078, 0.556863],
[0.0313725, 0.6, 0.6],
[0.0313725, 0.6, 0.639216],
[0.0352941, 0.6, 0.682353],
[0.0509804, 0.6, 0.721569],
[0.0431373, 0.6, 0.756863],
[0.0470588, 0.6, 0.792157],
[0.0509804, 0.6, 0.827451],
[0.054902, 0.596078, 0.854902],
[0.0588235, 0.592157, 0.886275],
[0.0666667, 0.588235, 0.909804],
[0.0705882, 0.584314, 0.933333],
[0.0784314, 0.580392, 0.952941],
[0.0862745, 0.572549, 0.968627],
[0.0901961, 0.568627, 0.980392],
[0.0980392, 0.560784, 0.988235],
[0.105882, 0.552941, 0.992157],
[0.117647, 0.545098, 0.992157],
[0.12549, 0.537255, 0.992157],
[0.133333, 0.52549, 0.984314],
[0.145098, 0.517647, 0.976471],
[0.152941, 0.505882, 0.964706],
[0.164706, 0.494118, 0.945098],
[0.172549, 0.482353, 0.92549],
[0.184314, 0.470588, 0.901961],
[0.196078, 0.458824, 0.878431],
[0.207843, 0.443137, 0.847059],
[0.219608, 0.431373, 0.815686],
[0.231373, 0.415686, 0.784314],
[0.247059, 0.403922, 0.745098],
[0.258824, 0.388235, 0.709804],
[0.27451, 0.372549, 0.670588],
[0.286275, 0.356863, 0.627451],
[0.301961, 0.341176, 0.588235],
[0.313725, 0.32549, 0.545098],
[0.329412, 0.309804, 0.501961],
[0.345098, 0.290196, 0.458824],
[0.360784, 0.27451, 0.415686],
[0.376471, 0.258824, 0.376471],
[0.392157, 0.239216, 0.333333],
[0.407843, 0.223529, 0.294118],
[0.427451, 0.203922, 0.254902],
[0.443137, 0.184314, 0.219608],
[0.458824, 0.168627, 0.184314],
[0.478431, 0.14902, 0.152941],
[0.494118, 0.129412, 0.121569],
[0.513725, 0.113725, 0.0941176],
[0.533333, 0.0941176, 0.0705882],
[0.54902, 0.0745098, 0.0509804],
[0.568627, 0.0588235, 0.0352941],
[0.588235, 0.0509804, 0.0196078],
[0.607843, 0.0196078, 0.00784314],
[0.627451, 0.00392157, 0.],
[0.647059, 0.0117647, 0.],
[0.666667, 0.027451, 0.],
[0.686275, 0.0470588, 0.00392157],
[0.705882, 0.0627451, 0.0117647],
[0.729412, 0.0784314, 0.0196078],
[0.74902, 0.0980392, 0.0352941],
[0.768627, 0.113725, 0.054902],
[0.788235, 0.129412, 0.0745098],
[0.811765, 0.145098, 0.0980392],
[0.831373, 0.160784, 0.12549],
[0.854902, 0.176471, 0.156863],
[0.87451, 0.192157, 0.188235],
[0.898039, 0.207843, 0.223529],
[0.917647, 0.219608, 0.262745],
[0.941176, 0.235294, 0.298039],
[0.964706, 0.247059, 0.341176],
[0.984314, 0.258824, 0.380392],
[0.992157, 0.270588, 0.423529],
[0.968627, 0.282353, 0.466667],
[0.945098, 0.294118, 0.509804],
[0.92549, 0.305882, 0.54902],
[0.901961, 0.313725, 0.592157],
[0.878431, 0.32549, 0.635294],
[0.854902, 0.333333, 0.67451],
[0.835294, 0.341176, 0.713725],
[0.811765, 0.34902, 0.752941],
[0.788235, 0.356863, 0.788235],
[0.764706, 0.360784, 0.819608],
[0.741176, 0.368627, 0.85098],
[0.717647, 0.372549, 0.882353],
[0.698039, 0.376471, 0.905882],
[0.67451, 0.380392, 0.929412],
[0.65098, 0.384314, 0.94902],
[0.627451, 0.388235, 0.964706],
[0.603922, 0.388235, 0.976471],
[0.580392, 0.388235, 0.988235],
[0.560784, 0.388235, 0.992157],
[0.537255, 0.388235, 0.996078],
[0.513725, 0.388235, 0.992157],
[0.490196, 0.388235, 0.988235],
[0.470588, 0.384314, 0.976471],
[0.447059, 0.380392, 0.964706],
[0.423529, 0.380392, 0.94902],
[0.403922, 0.372549, 0.929412],
[0.380392, 0.368627, 0.905882],
[0.360784, 0.364706, 0.882353],
[0.337255, 0.356863, 0.85098],
[0.313725, 0.34902, 0.819608],
[0.294118, 0.345098, 0.788235],
[0.27451, 0.337255, 0.752941],
[0.25098, 0.32549, 0.713725],
[0.231373, 0.317647, 0.67451],
[0.207843, 0.305882, 0.635294],
[0.188235, 0.298039, 0.592157],
[0.168627, 0.286275, 0.54902],
[0.14902, 0.27451, 0.509804],
[0.129412, 0.262745, 0.466667],
[0.109804, 0.25098, 0.423529],
[0.0901961, 0.239216, 0.380392],
[0.0705882, 0.223529, 0.341176],
[0.0509804, 0.211765, 0.298039],
[0.0313725, 0.196078, 0.262745],
[0.0117647, 0.180392, 0.223529],
[0.00392157, 0.164706, 0.188235],
[0.0196078, 0.14902, 0.156863],
[0.0509804, 0.133333, 0.12549],
[0.0588235, 0.117647, 0.0980392],
[0.0745098, 0.101961, 0.0745098],
[0.0901961, 0.0862745, 0.054902],
[0.109804, 0.0666667, 0.0352941],
[0.12549, 0.0509804, 0.0196078],
[0.141176, 0.0352941, 0.0117647],
[0.156863, 0.0156863, 0.00392157],
[0.172549, 0., 0.],
[0.188235, 0.0156863, 0.],
[0.203922, 0.0352941, 0.],
[0.219608, 0.0509804, 0.00784314],
[0.235294, 0.0705882, 0.0196078],
[0.247059, 0.0901961, 0.0352941],
[0.262745, 0.105882, 0.0509804],
[0.27451, 0.12549, 0.0705882],
[0.286275, 0.145098, 0.0941176],
[0.301961, 0.160784, 0.121569],
[0.313725, 0.180392, 0.152941],
[0.32549, 0.2, 0.184314],
[0.337255, 0.215686, 0.219608],
[0.34902, 0.235294, 0.254902],
[0.360784, 0.25098, 0.294118],
[0.368627, 0.270588, 0.333333],
[0.380392, 0.286275, 0.376471],
[0.392157, 0.301961, 0.415686],
[0.4, 0.321569, 0.458824],
[0.407843, 0.337255, 0.501961],
[0.419608, 0.352941, 0.545098],
[0.427451, 0.368627, 0.588235],
[0.435294, 0.384314, 0.627451],
[0.443137, 0.4, 0.670588],
[0.447059, 0.411765, 0.709804],
[0.454902, 0.427451, 0.745098],
[0.462745, 0.439216, 0.784314],
[0.466667, 0.454902, 0.815686],
[0.47451, 0.466667, 0.847059],
[0.478431, 0.478431, 0.878431],
[0.482353, 0.490196, 0.901961],
[0.486275, 0.501961, 0.92549],
[0.490196, 0.513725, 0.945098],
[0.494118, 0.521569, 0.964706],
[0.498039, 0.533333, 0.976471],
[0.501961, 0.541176, 0.984314],
[0.501961, 0.54902, 0.992157],
[0.505882, 0.556863, 0.992157],
[0.505882, 0.564706, 0.992157],
[0.505882, 0.572549, 0.988235],
[0.505882, 0.576471, 0.980392],
[0.505882, 0.584314, 0.968627],
[0.505882, 0.588235, 0.952941],
[0.505882, 0.592157, 0.933333],
[0.505882, 0.596078, 0.909804],
[0.505882, 0.596078, 0.886275],
[0.501961, 0.6, 0.854902],
[0.498039, 0.6, 0.827451],
[0.498039, 0.6, 0.792157],
[0.494118, 0.6, 0.756863],
[0.490196, 0.6, 0.721569],
[0.486275, 0.6, 0.682353],
[0.482353, 0.596078, 0.639216],
[0.478431, 0.596078, 0.6],
[0.470588, 0.592157, 0.556863],
[0.466667, 0.588235, 0.513725],
[0.458824, 0.584314, 0.470588],
[0.454902, 0.576471, 0.427451],
[0.447059, 0.572549, 0.388235],
[0.439216, 0.564706, 0.345098],
[0.431373, 0.556863, 0.305882],
[0.423529, 0.54902, 0.266667],
[0.415686, 0.541176, 0.231373],
[0.403922, 0.533333, 0.196078],
[0.396078, 0.521569, 0.160784],
[0.388235, 0.513725, 0.129412],
[0.376471, 0.501961, 0.101961],
[0.364706, 0.490196, 0.0784314],
[0.356863, 0.478431, 0.054902],
[0.345098, 0.466667, 0.0509804],
[0.333333, 0.454902, 0.0235294],
[0.321569, 0.439216, 0.0117647],
[0.309804, 0.427451, 0.00392157],
[0.294118, 0.411765, 0.],
[0.282353, 0.396078, 0.],
[0.270588, 0.384314, 0.],
[0.254902, 0.368627, 0.00784314],
[0.243137, 0.352941, 0.0196078],
[0.227451, 0.337255, 0.0313725],
[0.211765, 0.317647, 0.0470588],
[0.196078, 0.301961, 0.0705882],
[0.184314, 0.286275, 0.0941176],
[0.168627, 0.266667, 0.117647],
[0.152941, 0.25098, 0.14902],
[0.133333, 0.235294, 0.180392],
[0.117647, 0.215686, 0.215686],
[0.101961, 0.196078, 0.25098],
[0.0862745, 0.180392, 0.290196],
[0.0666667, 0.160784, 0.329412],
[0.0509804, 0.145098, 0.368627],
[0.0313725, 0.12549, 0.411765],
[0.0313725, 0.12549, 0.411765]]

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