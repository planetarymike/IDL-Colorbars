from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0.984314, 0., 0.0117647],
[0.984314, 0., 0.0117647],
[0.984314, 0., 0.0352941],
[0.984314, 0.00392157, 0.0588235],
[0.988235, 0.00392157, 0.0862745],
[0.988235, 0.00784314, 0.109804],
[0.992157, 0.00784314, 0.133333],
[0.988235, 0.0156863, 0.160784],
[0.988235, 0.0196078, 0.188235],
[0.984314, 0.027451, 0.215686],
[0.984314, 0.0313725, 0.243137],
[0.980392, 0.027451, 0.258824],
[0.980392, 0.0352941, 0.286275],
[0.976471, 0.0509804, 0.317647],
[0.976471, 0.0313725, 0.329412],
[0.976471, 0.0588235, 0.368627],
[0.972549, 0.0666667, 0.392157],
[0.972549, 0.0705882, 0.415686],
[0.968627, 0.0784314, 0.439216],
[0.968627, 0.0823529, 0.462745],
[0.964706, 0.0901961, 0.486275],
[0.964706, 0.0941176, 0.509804],
[0.964706, 0.101961, 0.529412],
[0.960784, 0.105882, 0.552941],
[0.960784, 0.109804, 0.576471],
[0.956863, 0.117647, 0.596078],
[0.956863, 0.121569, 0.615686],
[0.952941, 0.129412, 0.635294],
[0.952941, 0.133333, 0.658824],
[0.952941, 0.137255, 0.678431],
[0.94902, 0.145098, 0.698039],
[0.94902, 0.14902, 0.717647],
[0.945098, 0.156863, 0.733333],
[0.945098, 0.160784, 0.752941],
[0.945098, 0.164706, 0.772549],
[0.941176, 0.172549, 0.788235],
[0.941176, 0.176471, 0.807843],
[0.941176, 0.180392, 0.823529],
[0.937255, 0.188235, 0.843137],
[0.937255, 0.192157, 0.858824],
[0.937255, 0.196078, 0.87451],
[0.933333, 0.203922, 0.890196],
[0.933333, 0.207843, 0.905882],
[0.929412, 0.215686, 0.921569],
[0.921569, 0.219608, 0.929412],
[0.901961, 0.223529, 0.929412],
[0.886275, 0.231373, 0.92549],
[0.870588, 0.235294, 0.92549],
[0.85098, 0.239216, 0.92549],
[0.835294, 0.247059, 0.921569],
[0.819608, 0.25098, 0.921569],
[0.803922, 0.254902, 0.921569],
[0.788235, 0.258824, 0.921569],
[0.772549, 0.266667, 0.917647],
[0.760784, 0.270588, 0.917647],
[0.745098, 0.27451, 0.917647],
[0.729412, 0.282353, 0.913725],
[0.717647, 0.286275, 0.913725],
[0.701961, 0.290196, 0.913725],
[0.690196, 0.298039, 0.909804],
[0.678431, 0.301961, 0.909804],
[0.662745, 0.305882, 0.909804],
[0.65098, 0.309804, 0.909804],
[0.639216, 0.317647, 0.905882],
[0.627451, 0.321569, 0.905882],
[0.615686, 0.32549, 0.905882],
[0.603922, 0.329412, 0.901961],
[0.592157, 0.333333, 0.901961],
[0.580392, 0.337255, 0.901961],
[0.568627, 0.341176, 0.901961],
[0.560784, 0.345098, 0.901961],
[0.54902, 0.352941, 0.898039],
[0.537255, 0.356863, 0.898039],
[0.529412, 0.360784, 0.898039],
[0.521569, 0.364706, 0.898039],
[0.509804, 0.372549, 0.894118],
[0.501961, 0.376471, 0.894118],
[0.494118, 0.380392, 0.894118],
[0.486275, 0.384314, 0.894118],
[0.478431, 0.388235, 0.894118],
[0.470588, 0.396078, 0.890196],
[0.462745, 0.4, 0.890196],
[0.454902, 0.403922, 0.890196],
[0.447059, 0.407843, 0.890196],
[0.439216, 0.411765, 0.890196],
[0.435294, 0.419608, 0.886275],
[0.427451, 0.423529, 0.886275],
[0.427451, 0.431373, 0.886275],
[0.431373, 0.447059, 0.886275],
[0.435294, 0.462745, 0.886275],
[0.443137, 0.478431, 0.882353],
[0.447059, 0.490196, 0.882353],
[0.45098, 0.505882, 0.882353],
[0.454902, 0.517647, 0.882353],
[0.458824, 0.533333, 0.882353],
[0.462745, 0.545098, 0.882353],
[0.466667, 0.560784, 0.882353],
[0.47451, 0.572549, 0.878431],
[0.478431, 0.584314, 0.878431],
[0.482353, 0.596078, 0.878431],
[0.490196, 0.611765, 0.878431],
[0.490196, 0.619608, 0.878431],
[0.494118, 0.631373, 0.878431],
[0.498039, 0.643137, 0.878431],
[0.501961, 0.654902, 0.878431],
[0.505882, 0.666667, 0.878431],
[0.513725, 0.678431, 0.87451],
[0.517647, 0.686275, 0.87451],
[0.521569, 0.698039, 0.87451],
[0.529412, 0.709804, 0.87451],
[0.533333, 0.721569, 0.87451],
[0.537255, 0.729412, 0.87451],
[0.541176, 0.737255, 0.87451],
[0.545098, 0.74902, 0.87451],
[0.54902, 0.756863, 0.87451],
[0.54902, 0.764706, 0.87451],
[0.552941, 0.772549, 0.87451],
[0.556863, 0.780392, 0.87451],
[0.564706, 0.788235, 0.870588],
[0.568627, 0.796078, 0.870588],
[0.572549, 0.803922, 0.870588],
[0.576471, 0.811765, 0.870588],
[0.580392, 0.819608, 0.870588],
[0.584314, 0.827451, 0.870588],
[0.588235, 0.835294, 0.870588],
[0.592157, 0.843137, 0.870588],
[0.596078, 0.847059, 0.870588],
[0.6, 0.854902, 0.870588],
[0.603922, 0.862745, 0.870588],
[0.607843, 0.866667, 0.870588],
[0.611765, 0.870588, 0.866667],
[0.615686, 0.870588, 0.862745],
[0.619608, 0.870588, 0.854902],
[0.623529, 0.870588, 0.85098],
[0.627451, 0.870588, 0.847059],
[0.631373, 0.870588, 0.839216],
[0.635294, 0.870588, 0.835294],
[0.639216, 0.870588, 0.831373],
[0.643137, 0.870588, 0.827451],
[0.647059, 0.870588, 0.823529],
[0.65098, 0.870588, 0.815686],
[0.654902, 0.870588, 0.811765],
[0.658824, 0.870588, 0.807843],
[0.662745, 0.870588, 0.807843],
[0.666667, 0.870588, 0.803922],
[0.670588, 0.870588, 0.8],
[0.670588, 0.87451, 0.796078],
[0.67451, 0.87451, 0.792157],
[0.682353, 0.87451, 0.792157],
[0.682353, 0.87451, 0.788235],
[0.686275, 0.87451, 0.784314],
[0.690196, 0.87451, 0.784314],
[0.694118, 0.87451, 0.780392],
[0.698039, 0.87451, 0.776471],
[0.701961, 0.87451, 0.776471],
[0.705882, 0.87451, 0.772549],
[0.709804, 0.87451, 0.772549],
[0.713725, 0.87451, 0.772549],
[0.717647, 0.87451, 0.768627],
[0.721569, 0.878431, 0.772549],
[0.72549, 0.878431, 0.768627],
[0.72549, 0.878431, 0.768627],
[0.729412, 0.878431, 0.764706],
[0.733333, 0.878431, 0.764706],
[0.737255, 0.878431, 0.764706],
[0.741176, 0.878431, 0.764706],
[0.745098, 0.878431, 0.764706],
[0.745098, 0.882353, 0.764706],
[0.74902, 0.882353, 0.764706],
[0.752941, 0.882353, 0.764706],
[0.756863, 0.882353, 0.764706],
[0.760784, 0.882353, 0.764706],
[0.764706, 0.882353, 0.764706],
[0.768627, 0.882353, 0.768627],
[0.772549, 0.886275, 0.768627],
[0.780392, 0.886275, 0.772549],
[0.784314, 0.886275, 0.776471],
[0.792157, 0.886275, 0.780392],
[0.796078, 0.886275, 0.784314],
[0.8, 0.886275, 0.788235],
[0.807843, 0.890196, 0.788235],
[0.811765, 0.890196, 0.792157],
[0.815686, 0.890196, 0.796078],
[0.823529, 0.890196, 0.8],
[0.827451, 0.890196, 0.803922],
[0.831373, 0.894118, 0.803922],
[0.835294, 0.894118, 0.807843],
[0.839216, 0.894118, 0.811765],
[0.843137, 0.894118, 0.815686],
[0.847059, 0.894118, 0.819608],
[0.85098, 0.898039, 0.819608],
[0.854902, 0.898039, 0.823529],
[0.858824, 0.898039, 0.827451],
[0.862745, 0.898039, 0.831373],
[0.862745, 0.898039, 0.831373],
[0.866667, 0.898039, 0.835294],
[0.870588, 0.901961, 0.835294],
[0.87451, 0.901961, 0.839216],
[0.878431, 0.901961, 0.843137],
[0.882353, 0.901961, 0.847059],
[0.886275, 0.905882, 0.847059],
[0.886275, 0.905882, 0.85098],
[0.890196, 0.909804, 0.854902],
[0.894118, 0.909804, 0.854902],
[0.894118, 0.909804, 0.858824],
[0.898039, 0.909804, 0.862745],
[0.901961, 0.909804, 0.866667],
[0.901961, 0.913725, 0.866667],
[0.905882, 0.913725, 0.870588],
[0.909804, 0.913725, 0.87451],
[0.909804, 0.917647, 0.87451],
[0.913725, 0.917647, 0.878431],
[0.913725, 0.917647, 0.882353],
[0.917647, 0.917647, 0.886275],
[0.921569, 0.921569, 0.886275],
[0.921569, 0.921569, 0.890196],
[0.921569, 0.921569, 0.894118],
[0.92549, 0.92549, 0.894118],
[0.92549, 0.92549, 0.898039],
[0.92549, 0.92549, 0.901961],
[0.929412, 0.92549, 0.901961],
[0.929412, 0.92549, 0.905882],
[0.929412, 0.929412, 0.909804],
[0.933333, 0.929412, 0.909804],
[0.933333, 0.929412, 0.913725],
[0.937255, 0.929412, 0.913725],
[0.937255, 0.933333, 0.917647],
[0.937255, 0.933333, 0.921569],
[0.941176, 0.933333, 0.921569],
[0.941176, 0.937255, 0.92549],
[0.941176, 0.937255, 0.929412],
[0.945098, 0.937255, 0.929412],
[0.94902, 0.941176, 0.933333],
[0.94902, 0.941176, 0.933333],
[0.94902, 0.945098, 0.937255],
[0.94902, 0.945098, 0.941176],
[0.952941, 0.94902, 0.941176],
[0.952941, 0.94902, 0.945098],
[0.956863, 0.94902, 0.945098],
[0.956863, 0.952941, 0.94902],
[0.956863, 0.952941, 0.952941],
[0.960784, 0.956863, 0.952941],
[0.960784, 0.956863, 0.956863],
[0.964706, 0.960784, 0.956863],
[0.964706, 0.960784, 0.960784],
[0.964706, 0.964706, 0.964706],
[0.968627, 0.964706, 0.964706],
[0.968627, 0.968627, 0.968627],
[0.972549, 0.968627, 0.968627],
[0.972549, 0.972549, 0.972549],
[0.976471, 0.972549, 0.972549],
[0.976471, 0.976471, 0.976471],
[0.980392, 0.976471, 0.976471],
[0.980392, 0.980392, 0.980392],
[0.984314, 0.980392, 0.980392],
[0.984314, 0.980392, 0.980392]]

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