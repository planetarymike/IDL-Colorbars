from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.403922, 0., 0.121569],
[0.415686, 0.00392157, 0.121569],
[0.427451, 0.00784314, 0.12549],
[0.439216, 0.0117647, 0.12549],
[0.45098, 0.0156863, 0.129412],
[0.462745, 0.0196078, 0.129412],
[0.47451, 0.0235294, 0.133333],
[0.486275, 0.027451, 0.133333],
[0.498039, 0.0313725, 0.137255],
[0.509804, 0.0352941, 0.137255],
[0.521569, 0.0392157, 0.141176],
[0.533333, 0.0431373, 0.141176],
[0.545098, 0.0470588, 0.145098],
[0.556863, 0.0470588, 0.145098],
[0.568627, 0.0509804, 0.14902],
[0.580392, 0.054902, 0.14902],
[0.592157, 0.0588235, 0.152941],
[0.603922, 0.0627451, 0.152941],
[0.615686, 0.0666667, 0.156863],
[0.627451, 0.0705882, 0.156863],
[0.639216, 0.0745098, 0.160784],
[0.65098, 0.0784314, 0.160784],
[0.662745, 0.0823529, 0.164706],
[0.67451, 0.0862745, 0.164706],
[0.686275, 0.0901961, 0.168627],
[0.698039, 0.0941176, 0.168627],
[0.701961, 0.105882, 0.172549],
[0.709804, 0.117647, 0.180392],
[0.713725, 0.12549, 0.184314],
[0.721569, 0.137255, 0.188235],
[0.72549, 0.14902, 0.196078],
[0.729412, 0.160784, 0.2],
[0.737255, 0.168627, 0.203922],
[0.741176, 0.180392, 0.207843],
[0.745098, 0.192157, 0.215686],
[0.752941, 0.203922, 0.219608],
[0.756863, 0.211765, 0.223529],
[0.764706, 0.223529, 0.231373],
[0.768627, 0.235294, 0.235294],
[0.772549, 0.247059, 0.239216],
[0.780392, 0.258824, 0.247059],
[0.784314, 0.266667, 0.25098],
[0.792157, 0.278431, 0.254902],
[0.796078, 0.290196, 0.262745],
[0.8, 0.301961, 0.266667],
[0.807843, 0.309804, 0.270588],
[0.811765, 0.321569, 0.27451],
[0.815686, 0.333333, 0.282353],
[0.823529, 0.345098, 0.286275],
[0.827451, 0.352941, 0.290196],
[0.835294, 0.364706, 0.298039],
[0.839216, 0.376471, 0.301961],
[0.843137, 0.388235, 0.309804],
[0.847059, 0.4, 0.317647],
[0.854902, 0.407843, 0.32549],
[0.858824, 0.419608, 0.333333],
[0.862745, 0.431373, 0.345098],
[0.866667, 0.443137, 0.352941],
[0.870588, 0.45098, 0.360784],
[0.878431, 0.462745, 0.368627],
[0.882353, 0.47451, 0.376471],
[0.886275, 0.486275, 0.384314],
[0.890196, 0.494118, 0.392157],
[0.894118, 0.505882, 0.4],
[0.901961, 0.517647, 0.411765],
[0.905882, 0.529412, 0.419608],
[0.909804, 0.537255, 0.427451],
[0.913725, 0.54902, 0.435294],
[0.917647, 0.560784, 0.443137],
[0.92549, 0.572549, 0.45098],
[0.929412, 0.580392, 0.458824],
[0.933333, 0.592157, 0.466667],
[0.937255, 0.603922, 0.478431],
[0.941176, 0.615686, 0.486275],
[0.94902, 0.623529, 0.494118],
[0.952941, 0.635294, 0.501961],
[0.956863, 0.647059, 0.509804],
[0.956863, 0.654902, 0.521569],
[0.960784, 0.662745, 0.529412],
[0.960784, 0.670588, 0.541176],
[0.960784, 0.678431, 0.552941],
[0.964706, 0.686275, 0.560784],
[0.964706, 0.694118, 0.572549],
[0.964706, 0.705882, 0.584314],
[0.968627, 0.713725, 0.592157],
[0.968627, 0.721569, 0.603922],
[0.968627, 0.729412, 0.615686],
[0.972549, 0.737255, 0.623529],
[0.972549, 0.745098, 0.635294],
[0.976471, 0.752941, 0.647059],
[0.976471, 0.760784, 0.654902],
[0.976471, 0.768627, 0.666667],
[0.980392, 0.776471, 0.67451],
[0.980392, 0.784314, 0.686275],
[0.980392, 0.792157, 0.698039],
[0.984314, 0.8, 0.705882],
[0.984314, 0.811765, 0.717647],
[0.984314, 0.819608, 0.729412],
[0.988235, 0.827451, 0.737255],
[0.988235, 0.835294, 0.74902],
[0.988235, 0.843137, 0.760784],
[0.992157, 0.85098, 0.768627],
[0.992157, 0.858824, 0.780392],
[0.992157, 0.862745, 0.788235],
[0.992157, 0.870588, 0.796078],
[0.992157, 0.87451, 0.807843],
[0.992157, 0.882353, 0.815686],
[0.992157, 0.886275, 0.823529],
[0.992157, 0.894118, 0.831373],
[0.996078, 0.898039, 0.843137],
[0.996078, 0.905882, 0.85098],
[0.996078, 0.909804, 0.858824],
[0.996078, 0.913725, 0.866667],
[0.996078, 0.921569, 0.878431],
[0.996078, 0.92549, 0.886275],
[0.996078, 0.933333, 0.894118],
[0.996078, 0.937255, 0.901961],
[0.996078, 0.945098, 0.913725],
[0.996078, 0.94902, 0.921569],
[0.996078, 0.952941, 0.929412],
[0.996078, 0.960784, 0.937255],
[1., 0.964706, 0.94902],
[1., 0.972549, 0.956863],
[1., 0.976471, 0.964706],
[1., 0.984314, 0.972549],
[1., 0.988235, 0.984314],
[1., 0.996078, 0.992157],
[1., 1., 1.],
[0.996078, 0.996078, 0.996078],
[0.992157, 0.992157, 0.992157],
[0.984314, 0.984314, 0.984314],
[0.980392, 0.980392, 0.980392],
[0.976471, 0.976471, 0.976471],
[0.972549, 0.972549, 0.972549],
[0.968627, 0.968627, 0.968627],
[0.960784, 0.960784, 0.960784],
[0.956863, 0.956863, 0.956863],
[0.952941, 0.952941, 0.952941],
[0.94902, 0.94902, 0.94902],
[0.945098, 0.945098, 0.945098],
[0.941176, 0.941176, 0.941176],
[0.933333, 0.933333, 0.933333],
[0.929412, 0.929412, 0.929412],
[0.92549, 0.92549, 0.92549],
[0.921569, 0.921569, 0.921569],
[0.917647, 0.917647, 0.917647],
[0.909804, 0.909804, 0.909804],
[0.905882, 0.905882, 0.905882],
[0.901961, 0.901961, 0.901961],
[0.898039, 0.898039, 0.898039],
[0.894118, 0.894118, 0.894118],
[0.886275, 0.886275, 0.886275],
[0.882353, 0.882353, 0.882353],
[0.878431, 0.878431, 0.878431],
[0.870588, 0.870588, 0.870588],
[0.866667, 0.866667, 0.866667],
[0.858824, 0.858824, 0.858824],
[0.854902, 0.854902, 0.854902],
[0.847059, 0.847059, 0.847059],
[0.843137, 0.843137, 0.843137],
[0.835294, 0.835294, 0.835294],
[0.831373, 0.831373, 0.831373],
[0.823529, 0.823529, 0.823529],
[0.819608, 0.819608, 0.819608],
[0.811765, 0.811765, 0.811765],
[0.807843, 0.807843, 0.807843],
[0.8, 0.8, 0.8],
[0.796078, 0.796078, 0.796078],
[0.788235, 0.788235, 0.788235],
[0.784314, 0.784314, 0.784314],
[0.776471, 0.776471, 0.776471],
[0.772549, 0.772549, 0.772549],
[0.764706, 0.764706, 0.764706],
[0.760784, 0.760784, 0.760784],
[0.752941, 0.752941, 0.752941],
[0.74902, 0.74902, 0.74902],
[0.741176, 0.741176, 0.741176],
[0.737255, 0.737255, 0.737255],
[0.729412, 0.729412, 0.729412],
[0.721569, 0.721569, 0.721569],
[0.713725, 0.713725, 0.713725],
[0.705882, 0.705882, 0.705882],
[0.698039, 0.698039, 0.698039],
[0.690196, 0.690196, 0.690196],
[0.682353, 0.682353, 0.682353],
[0.67451, 0.67451, 0.67451],
[0.666667, 0.666667, 0.666667],
[0.658824, 0.658824, 0.658824],
[0.65098, 0.65098, 0.65098],
[0.643137, 0.643137, 0.643137],
[0.635294, 0.635294, 0.635294],
[0.631373, 0.631373, 0.631373],
[0.623529, 0.623529, 0.623529],
[0.615686, 0.615686, 0.615686],
[0.607843, 0.607843, 0.607843],
[0.6, 0.6, 0.6],
[0.592157, 0.592157, 0.592157],
[0.584314, 0.584314, 0.584314],
[0.576471, 0.576471, 0.576471],
[0.568627, 0.568627, 0.568627],
[0.560784, 0.560784, 0.560784],
[0.552941, 0.552941, 0.552941],
[0.545098, 0.545098, 0.545098],
[0.537255, 0.537255, 0.537255],
[0.529412, 0.529412, 0.529412],
[0.521569, 0.521569, 0.521569],
[0.509804, 0.509804, 0.509804],
[0.501961, 0.501961, 0.501961],
[0.494118, 0.494118, 0.494118],
[0.482353, 0.482353, 0.482353],
[0.47451, 0.47451, 0.47451],
[0.466667, 0.466667, 0.466667],
[0.454902, 0.454902, 0.454902],
[0.447059, 0.447059, 0.447059],
[0.439216, 0.439216, 0.439216],
[0.427451, 0.427451, 0.427451],
[0.419608, 0.419608, 0.419608],
[0.411765, 0.411765, 0.411765],
[0.403922, 0.403922, 0.403922],
[0.392157, 0.392157, 0.392157],
[0.384314, 0.384314, 0.384314],
[0.376471, 0.376471, 0.376471],
[0.364706, 0.364706, 0.364706],
[0.356863, 0.356863, 0.356863],
[0.34902, 0.34902, 0.34902],
[0.337255, 0.337255, 0.337255],
[0.329412, 0.329412, 0.329412],
[0.321569, 0.321569, 0.321569],
[0.309804, 0.309804, 0.309804],
[0.301961, 0.301961, 0.301961],
[0.294118, 0.294118, 0.294118],
[0.286275, 0.286275, 0.286275],
[0.278431, 0.278431, 0.278431],
[0.270588, 0.270588, 0.270588],
[0.262745, 0.262745, 0.262745],
[0.254902, 0.254902, 0.254902],
[0.247059, 0.247059, 0.247059],
[0.239216, 0.239216, 0.239216],
[0.231373, 0.231373, 0.231373],
[0.223529, 0.223529, 0.223529],
[0.215686, 0.215686, 0.215686],
[0.207843, 0.207843, 0.207843],
[0.203922, 0.203922, 0.203922],
[0.196078, 0.196078, 0.196078],
[0.188235, 0.188235, 0.188235],
[0.180392, 0.180392, 0.180392],
[0.172549, 0.172549, 0.172549],
[0.164706, 0.164706, 0.164706],
[0.156863, 0.156863, 0.156863],
[0.14902, 0.14902, 0.14902],
[0.141176, 0.141176, 0.141176],
[0.133333, 0.133333, 0.133333],
[0.12549, 0.12549, 0.12549],
[0.117647, 0.117647, 0.117647],
[0.109804, 0.109804, 0.109804],
[0.101961, 0.101961, 0.101961]]

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