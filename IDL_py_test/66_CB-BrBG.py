from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.329412, 0.188235, 0.0196078],
[0.337255, 0.192157, 0.0196078],
[0.345098, 0.2, 0.0196078],
[0.356863, 0.203922, 0.0235294],
[0.364706, 0.207843, 0.0235294],
[0.372549, 0.215686, 0.0235294],
[0.380392, 0.219608, 0.0235294],
[0.392157, 0.223529, 0.0235294],
[0.4, 0.231373, 0.027451],
[0.407843, 0.235294, 0.027451],
[0.415686, 0.239216, 0.027451],
[0.427451, 0.247059, 0.027451],
[0.435294, 0.25098, 0.027451],
[0.443137, 0.254902, 0.0313725],
[0.45098, 0.258824, 0.0313725],
[0.462745, 0.266667, 0.0313725],
[0.470588, 0.270588, 0.0313725],
[0.478431, 0.27451, 0.0313725],
[0.486275, 0.282353, 0.0352941],
[0.498039, 0.286275, 0.0352941],
[0.505882, 0.290196, 0.0352941],
[0.513725, 0.298039, 0.0352941],
[0.521569, 0.301961, 0.0352941],
[0.533333, 0.305882, 0.0392157],
[0.541176, 0.313725, 0.0392157],
[0.54902, 0.317647, 0.0392157],
[0.556863, 0.32549, 0.0431373],
[0.564706, 0.333333, 0.0509804],
[0.572549, 0.341176, 0.054902],
[0.580392, 0.345098, 0.0588235],
[0.588235, 0.352941, 0.0666667],
[0.596078, 0.360784, 0.0705882],
[0.603922, 0.368627, 0.0745098],
[0.611765, 0.376471, 0.0823529],
[0.619608, 0.384314, 0.0862745],
[0.627451, 0.388235, 0.0901961],
[0.635294, 0.396078, 0.0980392],
[0.643137, 0.403922, 0.101961],
[0.65098, 0.411765, 0.109804],
[0.654902, 0.419608, 0.113725],
[0.662745, 0.427451, 0.117647],
[0.670588, 0.435294, 0.12549],
[0.678431, 0.439216, 0.129412],
[0.686275, 0.447059, 0.133333],
[0.694118, 0.454902, 0.141176],
[0.701961, 0.462745, 0.145098],
[0.709804, 0.470588, 0.14902],
[0.717647, 0.478431, 0.156863],
[0.72549, 0.482353, 0.160784],
[0.733333, 0.490196, 0.164706],
[0.741176, 0.498039, 0.172549],
[0.74902, 0.505882, 0.176471],
[0.752941, 0.517647, 0.188235],
[0.760784, 0.52549, 0.2],
[0.764706, 0.537255, 0.215686],
[0.768627, 0.545098, 0.227451],
[0.772549, 0.556863, 0.239216],
[0.780392, 0.568627, 0.25098],
[0.784314, 0.576471, 0.262745],
[0.788235, 0.588235, 0.278431],
[0.796078, 0.596078, 0.290196],
[0.8, 0.607843, 0.301961],
[0.803922, 0.619608, 0.313725],
[0.807843, 0.627451, 0.32549],
[0.815686, 0.639216, 0.341176],
[0.819608, 0.647059, 0.352941],
[0.823529, 0.658824, 0.364706],
[0.827451, 0.670588, 0.376471],
[0.835294, 0.678431, 0.388235],
[0.839216, 0.690196, 0.403922],
[0.843137, 0.698039, 0.415686],
[0.85098, 0.709804, 0.427451],
[0.854902, 0.721569, 0.439216],
[0.858824, 0.729412, 0.45098],
[0.862745, 0.741176, 0.466667],
[0.870588, 0.74902, 0.478431],
[0.87451, 0.760784, 0.490196],
[0.878431, 0.764706, 0.501961],
[0.882353, 0.772549, 0.509804],
[0.886275, 0.776471, 0.521569],
[0.890196, 0.784314, 0.533333],
[0.890196, 0.788235, 0.541176],
[0.894118, 0.796078, 0.552941],
[0.898039, 0.8, 0.564706],
[0.901961, 0.807843, 0.576471],
[0.905882, 0.811765, 0.584314],
[0.909804, 0.819608, 0.596078],
[0.913725, 0.823529, 0.607843],
[0.917647, 0.831373, 0.615686],
[0.921569, 0.835294, 0.627451],
[0.921569, 0.839216, 0.639216],
[0.92549, 0.847059, 0.647059],
[0.929412, 0.85098, 0.658824],
[0.933333, 0.858824, 0.670588],
[0.937255, 0.862745, 0.678431],
[0.941176, 0.870588, 0.690196],
[0.945098, 0.87451, 0.701961],
[0.94902, 0.882353, 0.713725],
[0.94902, 0.886275, 0.721569],
[0.952941, 0.894118, 0.733333],
[0.956863, 0.898039, 0.745098],
[0.960784, 0.905882, 0.752941],
[0.964706, 0.909804, 0.764706],
[0.964706, 0.913725, 0.772549],
[0.964706, 0.913725, 0.780392],
[0.964706, 0.917647, 0.788235],
[0.964706, 0.917647, 0.796078],
[0.964706, 0.921569, 0.803922],
[0.964706, 0.921569, 0.811765],
[0.964706, 0.92549, 0.819608],
[0.964706, 0.92549, 0.827451],
[0.964706, 0.929412, 0.835294],
[0.964706, 0.929412, 0.843137],
[0.964706, 0.933333, 0.85098],
[0.964706, 0.933333, 0.858824],
[0.960784, 0.937255, 0.866667],
[0.960784, 0.937255, 0.87451],
[0.960784, 0.941176, 0.882353],
[0.960784, 0.941176, 0.890196],
[0.960784, 0.945098, 0.898039],
[0.960784, 0.945098, 0.905882],
[0.960784, 0.94902, 0.913725],
[0.960784, 0.94902, 0.921569],
[0.960784, 0.952941, 0.929412],
[0.960784, 0.952941, 0.937255],
[0.960784, 0.956863, 0.945098],
[0.960784, 0.956863, 0.952941],
[0.960784, 0.960784, 0.960784],
[0.952941, 0.960784, 0.956863],
[0.945098, 0.956863, 0.956863],
[0.941176, 0.956863, 0.952941],
[0.933333, 0.952941, 0.952941],
[0.92549, 0.952941, 0.94902],
[0.917647, 0.94902, 0.945098],
[0.913725, 0.94902, 0.945098],
[0.905882, 0.94902, 0.941176],
[0.898039, 0.945098, 0.937255],
[0.890196, 0.945098, 0.937255],
[0.886275, 0.941176, 0.933333],
[0.878431, 0.941176, 0.933333],
[0.870588, 0.941176, 0.929412],
[0.862745, 0.937255, 0.92549],
[0.854902, 0.937255, 0.92549],
[0.85098, 0.933333, 0.921569],
[0.843137, 0.933333, 0.921569],
[0.835294, 0.929412, 0.917647],
[0.827451, 0.929412, 0.913725],
[0.823529, 0.929412, 0.913725],
[0.815686, 0.92549, 0.909804],
[0.807843, 0.92549, 0.905882],
[0.8, 0.921569, 0.905882],
[0.796078, 0.921569, 0.901961],
[0.788235, 0.917647, 0.901961],
[0.780392, 0.917647, 0.898039],
[0.768627, 0.913725, 0.894118],
[0.756863, 0.909804, 0.886275],
[0.745098, 0.905882, 0.882353],
[0.737255, 0.898039, 0.87451],
[0.72549, 0.894118, 0.870588],
[0.713725, 0.890196, 0.862745],
[0.701961, 0.886275, 0.858824],
[0.690196, 0.882353, 0.85098],
[0.678431, 0.878431, 0.847059],
[0.670588, 0.870588, 0.843137],
[0.658824, 0.866667, 0.835294],
[0.647059, 0.862745, 0.831373],
[0.635294, 0.858824, 0.823529],
[0.623529, 0.854902, 0.819608],
[0.611765, 0.85098, 0.811765],
[0.603922, 0.843137, 0.807843],
[0.592157, 0.839216, 0.803922],
[0.580392, 0.835294, 0.796078],
[0.568627, 0.831373, 0.792157],
[0.556863, 0.827451, 0.784314],
[0.545098, 0.823529, 0.780392],
[0.537255, 0.815686, 0.772549],
[0.52549, 0.811765, 0.768627],
[0.513725, 0.807843, 0.760784],
[0.501961, 0.803922, 0.756863],
[0.490196, 0.796078, 0.74902],
[0.478431, 0.788235, 0.741176],
[0.466667, 0.780392, 0.733333],
[0.454902, 0.772549, 0.72549],
[0.447059, 0.764706, 0.717647],
[0.435294, 0.756863, 0.709804],
[0.423529, 0.745098, 0.705882],
[0.411765, 0.737255, 0.698039],
[0.4, 0.729412, 0.690196],
[0.388235, 0.721569, 0.682353],
[0.376471, 0.713725, 0.67451],
[0.364706, 0.705882, 0.666667],
[0.356863, 0.698039, 0.658824],
[0.345098, 0.690196, 0.65098],
[0.333333, 0.682353, 0.643137],
[0.321569, 0.67451, 0.635294],
[0.309804, 0.666667, 0.627451],
[0.298039, 0.658824, 0.619608],
[0.286275, 0.65098, 0.611765],
[0.27451, 0.639216, 0.607843],
[0.262745, 0.631373, 0.6],
[0.254902, 0.623529, 0.592157],
[0.243137, 0.615686, 0.584314],
[0.231373, 0.607843, 0.576471],
[0.219608, 0.6, 0.568627],
[0.207843, 0.592157, 0.560784],
[0.2, 0.584314, 0.552941],
[0.192157, 0.576471, 0.545098],
[0.184314, 0.568627, 0.537255],
[0.176471, 0.560784, 0.529412],
[0.168627, 0.552941, 0.521569],
[0.160784, 0.545098, 0.513725],
[0.14902, 0.537255, 0.505882],
[0.141176, 0.529412, 0.498039],
[0.133333, 0.521569, 0.490196],
[0.12549, 0.513725, 0.482353],
[0.117647, 0.505882, 0.47451],
[0.109804, 0.498039, 0.466667],
[0.101961, 0.494118, 0.462745],
[0.0941176, 0.486275, 0.454902],
[0.0862745, 0.478431, 0.447059],
[0.0784314, 0.470588, 0.439216],
[0.0705882, 0.462745, 0.431373],
[0.0627451, 0.454902, 0.423529],
[0.0509804, 0.447059, 0.415686],
[0.0431373, 0.439216, 0.407843],
[0.0352941, 0.431373, 0.4],
[0.027451, 0.423529, 0.392157],
[0.0196078, 0.415686, 0.384314],
[0.0117647, 0.407843, 0.376471],
[0.00392157, 0.4, 0.368627],
[0.00392157, 0.392157, 0.360784],
[0.00392157, 0.388235, 0.352941],
[0.00392157, 0.380392, 0.34902],
[0.00392157, 0.376471, 0.341176],
[0.00392157, 0.368627, 0.333333],
[0.00392157, 0.360784, 0.32549],
[0.00392157, 0.356863, 0.321569],
[0.00392157, 0.34902, 0.313725],
[0.00392157, 0.341176, 0.305882],
[0.00392157, 0.337255, 0.298039],
[0.00392157, 0.329412, 0.294118],
[0.00392157, 0.32549, 0.286275],
[0.00392157, 0.317647, 0.278431],
[0., 0.309804, 0.270588],
[0., 0.305882, 0.262745],
[0., 0.298039, 0.258824],
[0., 0.294118, 0.25098],
[0., 0.286275, 0.243137],
[0., 0.278431, 0.235294],
[0., 0.27451, 0.231373],
[0., 0.266667, 0.223529],
[0., 0.258824, 0.215686],
[0., 0.254902, 0.207843],
[0., 0.247059, 0.203922],
[0., 0.243137, 0.196078],
[0., 0.235294, 0.188235]]

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