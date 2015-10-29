from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.25098, 0., 0.294118],
[0.258824, 0.00784314, 0.301961],
[0.266667, 0.0117647, 0.309804],
[0.27451, 0.0196078, 0.321569],
[0.286275, 0.027451, 0.329412],
[0.294118, 0.0313725, 0.337255],
[0.301961, 0.0392157, 0.345098],
[0.309804, 0.0470588, 0.356863],
[0.317647, 0.0509804, 0.364706],
[0.32549, 0.0588235, 0.372549],
[0.337255, 0.0666667, 0.380392],
[0.345098, 0.0705882, 0.392157],
[0.352941, 0.0784314, 0.4],
[0.360784, 0.0862745, 0.407843],
[0.368627, 0.0941176, 0.415686],
[0.376471, 0.0980392, 0.427451],
[0.388235, 0.105882, 0.435294],
[0.396078, 0.113725, 0.443137],
[0.403922, 0.117647, 0.45098],
[0.411765, 0.12549, 0.462745],
[0.419608, 0.133333, 0.470588],
[0.427451, 0.137255, 0.478431],
[0.439216, 0.145098, 0.486275],
[0.447059, 0.152941, 0.498039],
[0.454902, 0.156863, 0.505882],
[0.462745, 0.164706, 0.513725],
[0.466667, 0.176471, 0.521569],
[0.47451, 0.184314, 0.52549],
[0.478431, 0.196078, 0.533333],
[0.482353, 0.207843, 0.537255],
[0.490196, 0.215686, 0.545098],
[0.494118, 0.227451, 0.54902],
[0.498039, 0.239216, 0.556863],
[0.505882, 0.25098, 0.560784],
[0.509804, 0.258824, 0.568627],
[0.513725, 0.270588, 0.572549],
[0.521569, 0.282353, 0.580392],
[0.52549, 0.290196, 0.584314],
[0.533333, 0.301961, 0.592157],
[0.537255, 0.313725, 0.6],
[0.541176, 0.321569, 0.603922],
[0.54902, 0.333333, 0.611765],
[0.552941, 0.345098, 0.615686],
[0.556863, 0.352941, 0.623529],
[0.564706, 0.364706, 0.627451],
[0.568627, 0.376471, 0.635294],
[0.572549, 0.388235, 0.639216],
[0.580392, 0.396078, 0.647059],
[0.584314, 0.407843, 0.65098],
[0.588235, 0.419608, 0.658824],
[0.596078, 0.427451, 0.662745],
[0.6, 0.439216, 0.670588],
[0.607843, 0.447059, 0.67451],
[0.611765, 0.454902, 0.682353],
[0.619608, 0.462745, 0.686275],
[0.627451, 0.470588, 0.694118],
[0.631373, 0.482353, 0.698039],
[0.639216, 0.490196, 0.705882],
[0.643137, 0.498039, 0.709804],
[0.65098, 0.505882, 0.717647],
[0.658824, 0.513725, 0.721569],
[0.662745, 0.521569, 0.72549],
[0.670588, 0.529412, 0.733333],
[0.678431, 0.537255, 0.737255],
[0.682353, 0.54902, 0.745098],
[0.690196, 0.556863, 0.74902],
[0.698039, 0.564706, 0.756863],
[0.701961, 0.572549, 0.760784],
[0.709804, 0.580392, 0.764706],
[0.717647, 0.588235, 0.772549],
[0.721569, 0.596078, 0.776471],
[0.729412, 0.603922, 0.784314],
[0.733333, 0.615686, 0.788235],
[0.741176, 0.623529, 0.796078],
[0.74902, 0.631373, 0.8],
[0.752941, 0.639216, 0.807843],
[0.760784, 0.647059, 0.811765],
[0.764706, 0.654902, 0.815686],
[0.772549, 0.662745, 0.819608],
[0.776471, 0.666667, 0.823529],
[0.784314, 0.67451, 0.827451],
[0.788235, 0.682353, 0.831373],
[0.796078, 0.690196, 0.835294],
[0.8, 0.698039, 0.839216],
[0.803922, 0.701961, 0.843137],
[0.811765, 0.709804, 0.847059],
[0.815686, 0.717647, 0.85098],
[0.823529, 0.72549, 0.854902],
[0.827451, 0.733333, 0.858824],
[0.835294, 0.741176, 0.862745],
[0.839216, 0.745098, 0.862745],
[0.843137, 0.752941, 0.866667],
[0.85098, 0.760784, 0.870588],
[0.854902, 0.768627, 0.87451],
[0.862745, 0.776471, 0.878431],
[0.866667, 0.780392, 0.882353],
[0.870588, 0.788235, 0.886275],
[0.878431, 0.796078, 0.890196],
[0.882353, 0.803922, 0.894118],
[0.890196, 0.811765, 0.898039],
[0.894118, 0.815686, 0.901961],
[0.901961, 0.823529, 0.905882],
[0.905882, 0.831373, 0.909804],
[0.909804, 0.835294, 0.913725],
[0.909804, 0.843137, 0.913725],
[0.913725, 0.847059, 0.917647],
[0.917647, 0.854902, 0.917647],
[0.917647, 0.858824, 0.921569],
[0.921569, 0.862745, 0.92549],
[0.921569, 0.870588, 0.92549],
[0.92549, 0.87451, 0.929412],
[0.929412, 0.882353, 0.929412],
[0.929412, 0.886275, 0.933333],
[0.933333, 0.890196, 0.937255],
[0.937255, 0.898039, 0.937255],
[0.937255, 0.901961, 0.941176],
[0.941176, 0.909804, 0.941176],
[0.945098, 0.913725, 0.945098],
[0.945098, 0.917647, 0.94902],
[0.94902, 0.92549, 0.94902],
[0.952941, 0.929412, 0.952941],
[0.952941, 0.937255, 0.952941],
[0.956863, 0.941176, 0.956863],
[0.956863, 0.945098, 0.960784],
[0.960784, 0.952941, 0.960784],
[0.964706, 0.956863, 0.964706],
[0.964706, 0.964706, 0.964706],
[0.968627, 0.968627, 0.968627],
[0.964706, 0.968627, 0.964706],
[0.960784, 0.964706, 0.956863],
[0.956863, 0.964706, 0.952941],
[0.94902, 0.964706, 0.945098],
[0.945098, 0.964706, 0.941176],
[0.941176, 0.960784, 0.937255],
[0.937255, 0.960784, 0.929412],
[0.933333, 0.960784, 0.92549],
[0.929412, 0.960784, 0.921569],
[0.921569, 0.956863, 0.913725],
[0.917647, 0.956863, 0.909804],
[0.913725, 0.956863, 0.901961],
[0.909804, 0.956863, 0.898039],
[0.905882, 0.952941, 0.894118],
[0.901961, 0.952941, 0.886275],
[0.898039, 0.952941, 0.882353],
[0.890196, 0.94902, 0.87451],
[0.886275, 0.94902, 0.870588],
[0.882353, 0.94902, 0.866667],
[0.878431, 0.94902, 0.858824],
[0.87451, 0.945098, 0.854902],
[0.870588, 0.945098, 0.85098],
[0.862745, 0.945098, 0.843137],
[0.858824, 0.945098, 0.839216],
[0.854902, 0.941176, 0.831373],
[0.85098, 0.941176, 0.827451],
[0.843137, 0.937255, 0.819608],
[0.835294, 0.933333, 0.811765],
[0.827451, 0.929412, 0.803922],
[0.819608, 0.929412, 0.796078],
[0.811765, 0.92549, 0.788235],
[0.803922, 0.921569, 0.780392],
[0.796078, 0.917647, 0.772549],
[0.788235, 0.913725, 0.764706],
[0.780392, 0.909804, 0.756863],
[0.772549, 0.909804, 0.74902],
[0.764706, 0.905882, 0.741176],
[0.756863, 0.901961, 0.733333],
[0.745098, 0.898039, 0.721569],
[0.737255, 0.894118, 0.713725],
[0.729412, 0.890196, 0.705882],
[0.721569, 0.890196, 0.698039],
[0.713725, 0.886275, 0.690196],
[0.705882, 0.882353, 0.682353],
[0.698039, 0.878431, 0.67451],
[0.690196, 0.87451, 0.666667],
[0.682353, 0.870588, 0.658824],
[0.67451, 0.870588, 0.65098],
[0.666667, 0.866667, 0.643137],
[0.658824, 0.862745, 0.635294],
[0.65098, 0.858824, 0.627451],
[0.639216, 0.85098, 0.619608],
[0.627451, 0.847059, 0.607843],
[0.615686, 0.839216, 0.6],
[0.603922, 0.831373, 0.588235],
[0.592157, 0.823529, 0.580392],
[0.580392, 0.819608, 0.568627],
[0.572549, 0.811765, 0.560784],
[0.560784, 0.803922, 0.552941],
[0.54902, 0.796078, 0.541176],
[0.537255, 0.792157, 0.533333],
[0.52549, 0.784314, 0.521569],
[0.513725, 0.776471, 0.513725],
[0.501961, 0.772549, 0.505882],
[0.490196, 0.764706, 0.494118],
[0.478431, 0.756863, 0.486275],
[0.466667, 0.74902, 0.47451],
[0.454902, 0.745098, 0.466667],
[0.443137, 0.737255, 0.454902],
[0.431373, 0.729412, 0.447059],
[0.423529, 0.721569, 0.439216],
[0.411765, 0.717647, 0.427451],
[0.4, 0.709804, 0.419608],
[0.388235, 0.701961, 0.407843],
[0.376471, 0.694118, 0.4],
[0.364706, 0.690196, 0.388235],
[0.352941, 0.682353, 0.380392],
[0.341176, 0.67451, 0.372549],
[0.333333, 0.666667, 0.368627],
[0.321569, 0.658824, 0.360784],
[0.313725, 0.647059, 0.352941],
[0.301961, 0.639216, 0.34902],
[0.294118, 0.631373, 0.341176],
[0.282353, 0.623529, 0.333333],
[0.27451, 0.615686, 0.329412],
[0.262745, 0.607843, 0.321569],
[0.254902, 0.596078, 0.313725],
[0.243137, 0.588235, 0.309804],
[0.235294, 0.580392, 0.301961],
[0.223529, 0.572549, 0.294118],
[0.215686, 0.564706, 0.286275],
[0.203922, 0.556863, 0.282353],
[0.196078, 0.545098, 0.27451],
[0.184314, 0.537255, 0.266667],
[0.176471, 0.529412, 0.262745],
[0.164706, 0.521569, 0.254902],
[0.156863, 0.513725, 0.247059],
[0.145098, 0.505882, 0.243137],
[0.137255, 0.494118, 0.235294],
[0.12549, 0.486275, 0.227451],
[0.117647, 0.478431, 0.223529],
[0.105882, 0.470588, 0.215686],
[0.101961, 0.462745, 0.211765],
[0.0980392, 0.454902, 0.207843],
[0.0941176, 0.447059, 0.203922],
[0.0901961, 0.439216, 0.2],
[0.0862745, 0.431373, 0.196078],
[0.0823529, 0.423529, 0.192157],
[0.0784314, 0.415686, 0.184314],
[0.0745098, 0.407843, 0.180392],
[0.0705882, 0.4, 0.176471],
[0.0666667, 0.392157, 0.172549],
[0.0627451, 0.384314, 0.168627],
[0.0588235, 0.376471, 0.164706],
[0.054902, 0.368627, 0.160784],
[0.0470588, 0.360784, 0.156863],
[0.0431373, 0.352941, 0.152941],
[0.0392157, 0.345098, 0.14902],
[0.0352941, 0.337255, 0.145098],
[0.0313725, 0.329412, 0.141176],
[0.027451, 0.321569, 0.137255],
[0.0235294, 0.313725, 0.129412],
[0.0196078, 0.305882, 0.12549],
[0.0156863, 0.298039, 0.121569],
[0.0117647, 0.290196, 0.117647],
[0.00784314, 0.282353, 0.113725],
[0.00392157, 0.27451, 0.109804],
[0., 0.266667, 0.105882]]

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
