from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[1., 1., 0.85098],
[0.996078, 1., 0.847059],
[0.996078, 1., 0.839216],
[0.992157, 0.996078, 0.835294],
[0.992157, 0.996078, 0.831373],
[0.988235, 0.996078, 0.827451],
[0.988235, 0.996078, 0.819608],
[0.984314, 0.992157, 0.815686],
[0.980392, 0.992157, 0.811765],
[0.980392, 0.992157, 0.803922],
[0.976471, 0.992157, 0.8],
[0.976471, 0.992157, 0.796078],
[0.972549, 0.988235, 0.792157],
[0.968627, 0.988235, 0.784314],
[0.968627, 0.988235, 0.780392],
[0.964706, 0.988235, 0.776471],
[0.964706, 0.984314, 0.768627],
[0.960784, 0.984314, 0.764706],
[0.960784, 0.984314, 0.760784],
[0.956863, 0.984314, 0.752941],
[0.952941, 0.980392, 0.74902],
[0.952941, 0.980392, 0.745098],
[0.94902, 0.980392, 0.741176],
[0.94902, 0.980392, 0.733333],
[0.945098, 0.980392, 0.729412],
[0.941176, 0.976471, 0.72549],
[0.941176, 0.976471, 0.717647],
[0.937255, 0.976471, 0.713725],
[0.937255, 0.976471, 0.709804],
[0.933333, 0.972549, 0.705882],
[0.933333, 0.972549, 0.698039],
[0.929412, 0.972549, 0.694118],
[0.92549, 0.972549, 0.694118],
[0.921569, 0.968627, 0.694118],
[0.913725, 0.968627, 0.694118],
[0.909804, 0.964706, 0.694118],
[0.905882, 0.964706, 0.694118],
[0.901961, 0.960784, 0.698039],
[0.898039, 0.960784, 0.698039],
[0.894118, 0.956863, 0.698039],
[0.886275, 0.956863, 0.698039],
[0.882353, 0.952941, 0.698039],
[0.878431, 0.952941, 0.698039],
[0.87451, 0.94902, 0.698039],
[0.870588, 0.94902, 0.698039],
[0.862745, 0.945098, 0.698039],
[0.858824, 0.945098, 0.698039],
[0.854902, 0.945098, 0.701961],
[0.85098, 0.941176, 0.701961],
[0.847059, 0.941176, 0.701961],
[0.839216, 0.937255, 0.701961],
[0.835294, 0.937255, 0.701961],
[0.831373, 0.933333, 0.701961],
[0.827451, 0.933333, 0.701961],
[0.823529, 0.929412, 0.701961],
[0.819608, 0.929412, 0.701961],
[0.811765, 0.92549, 0.701961],
[0.807843, 0.92549, 0.701961],
[0.803922, 0.921569, 0.705882],
[0.8, 0.921569, 0.705882],
[0.796078, 0.917647, 0.705882],
[0.788235, 0.917647, 0.705882],
[0.784314, 0.913725, 0.705882],
[0.780392, 0.913725, 0.705882],
[0.772549, 0.909804, 0.705882],
[0.764706, 0.905882, 0.705882],
[0.752941, 0.901961, 0.709804],
[0.745098, 0.901961, 0.709804],
[0.737255, 0.898039, 0.709804],
[0.729412, 0.894118, 0.709804],
[0.717647, 0.890196, 0.713725],
[0.709804, 0.886275, 0.713725],
[0.701961, 0.882353, 0.713725],
[0.694118, 0.878431, 0.713725],
[0.682353, 0.87451, 0.713725],
[0.67451, 0.87451, 0.717647],
[0.666667, 0.870588, 0.717647],
[0.658824, 0.866667, 0.717647],
[0.647059, 0.862745, 0.717647],
[0.639216, 0.858824, 0.721569],
[0.631373, 0.854902, 0.721569],
[0.623529, 0.85098, 0.721569],
[0.611765, 0.847059, 0.721569],
[0.603922, 0.847059, 0.721569],
[0.596078, 0.843137, 0.72549],
[0.588235, 0.839216, 0.72549],
[0.576471, 0.835294, 0.72549],
[0.568627, 0.831373, 0.72549],
[0.560784, 0.827451, 0.72549],
[0.552941, 0.823529, 0.729412],
[0.541176, 0.819608, 0.729412],
[0.533333, 0.819608, 0.729412],
[0.52549, 0.815686, 0.729412],
[0.517647, 0.811765, 0.733333],
[0.505882, 0.807843, 0.733333],
[0.498039, 0.803922, 0.733333],
[0.490196, 0.8, 0.733333],
[0.482353, 0.8, 0.737255],
[0.47451, 0.796078, 0.737255],
[0.466667, 0.792157, 0.737255],
[0.458824, 0.788235, 0.737255],
[0.45098, 0.788235, 0.741176],
[0.443137, 0.784314, 0.741176],
[0.439216, 0.780392, 0.741176],
[0.431373, 0.780392, 0.745098],
[0.423529, 0.776471, 0.745098],
[0.415686, 0.772549, 0.745098],
[0.407843, 0.768627, 0.745098],
[0.4, 0.768627, 0.74902],
[0.392157, 0.764706, 0.74902],
[0.384314, 0.760784, 0.74902],
[0.376471, 0.760784, 0.752941],
[0.368627, 0.756863, 0.752941],
[0.360784, 0.752941, 0.752941],
[0.352941, 0.74902, 0.752941],
[0.345098, 0.74902, 0.756863],
[0.337255, 0.745098, 0.756863],
[0.329412, 0.741176, 0.756863],
[0.321569, 0.737255, 0.756863],
[0.317647, 0.737255, 0.760784],
[0.309804, 0.733333, 0.760784],
[0.301961, 0.729412, 0.760784],
[0.294118, 0.729412, 0.764706],
[0.286275, 0.72549, 0.764706],
[0.278431, 0.721569, 0.764706],
[0.270588, 0.717647, 0.764706],
[0.262745, 0.717647, 0.768627],
[0.254902, 0.713725, 0.768627],
[0.25098, 0.709804, 0.768627],
[0.247059, 0.705882, 0.768627],
[0.243137, 0.701961, 0.768627],
[0.239216, 0.694118, 0.768627],
[0.231373, 0.690196, 0.764706],
[0.227451, 0.686275, 0.764706],
[0.223529, 0.682353, 0.764706],
[0.219608, 0.678431, 0.764706],
[0.215686, 0.67451, 0.764706],
[0.211765, 0.666667, 0.764706],
[0.207843, 0.662745, 0.764706],
[0.203922, 0.658824, 0.764706],
[0.196078, 0.654902, 0.760784],
[0.192157, 0.65098, 0.760784],
[0.188235, 0.647059, 0.760784],
[0.184314, 0.643137, 0.760784],
[0.180392, 0.635294, 0.760784],
[0.176471, 0.631373, 0.760784],
[0.172549, 0.627451, 0.760784],
[0.168627, 0.623529, 0.760784],
[0.160784, 0.619608, 0.756863],
[0.156863, 0.615686, 0.756863],
[0.152941, 0.607843, 0.756863],
[0.14902, 0.603922, 0.756863],
[0.145098, 0.6, 0.756863],
[0.141176, 0.596078, 0.756863],
[0.137255, 0.592157, 0.756863],
[0.133333, 0.588235, 0.756863],
[0.12549, 0.580392, 0.752941],
[0.121569, 0.576471, 0.752941],
[0.117647, 0.572549, 0.752941],
[0.113725, 0.568627, 0.752941],
[0.113725, 0.560784, 0.74902],
[0.113725, 0.556863, 0.74902],
[0.113725, 0.54902, 0.745098],
[0.117647, 0.545098, 0.741176],
[0.117647, 0.537255, 0.737255],
[0.117647, 0.529412, 0.737255],
[0.117647, 0.52549, 0.733333],
[0.117647, 0.517647, 0.729412],
[0.117647, 0.513725, 0.72549],
[0.121569, 0.505882, 0.72549],
[0.121569, 0.498039, 0.721569],
[0.121569, 0.494118, 0.717647],
[0.121569, 0.486275, 0.713725],
[0.121569, 0.482353, 0.713725],
[0.121569, 0.47451, 0.709804],
[0.12549, 0.470588, 0.705882],
[0.12549, 0.462745, 0.701961],
[0.12549, 0.454902, 0.701961],
[0.12549, 0.45098, 0.698039],
[0.12549, 0.443137, 0.694118],
[0.12549, 0.439216, 0.690196],
[0.12549, 0.431373, 0.690196],
[0.129412, 0.423529, 0.686275],
[0.129412, 0.419608, 0.682353],
[0.129412, 0.411765, 0.678431],
[0.129412, 0.407843, 0.678431],
[0.129412, 0.4, 0.67451],
[0.129412, 0.392157, 0.670588],
[0.133333, 0.388235, 0.666667],
[0.133333, 0.380392, 0.666667],
[0.133333, 0.376471, 0.662745],
[0.133333, 0.368627, 0.658824],
[0.133333, 0.364706, 0.654902],
[0.133333, 0.356863, 0.654902],
[0.133333, 0.352941, 0.65098],
[0.133333, 0.34902, 0.65098],
[0.133333, 0.341176, 0.647059],
[0.137255, 0.337255, 0.643137],
[0.137255, 0.333333, 0.643137],
[0.137255, 0.329412, 0.639216],
[0.137255, 0.321569, 0.635294],
[0.137255, 0.317647, 0.635294],
[0.137255, 0.313725, 0.631373],
[0.137255, 0.305882, 0.631373],
[0.137255, 0.301961, 0.627451],
[0.137255, 0.298039, 0.623529],
[0.137255, 0.290196, 0.623529],
[0.141176, 0.286275, 0.619608],
[0.141176, 0.282353, 0.615686],
[0.141176, 0.27451, 0.615686],
[0.141176, 0.270588, 0.611765],
[0.141176, 0.266667, 0.611765],
[0.141176, 0.258824, 0.607843],
[0.141176, 0.254902, 0.603922],
[0.141176, 0.25098, 0.603922],
[0.141176, 0.247059, 0.6],
[0.141176, 0.239216, 0.596078],
[0.141176, 0.235294, 0.596078],
[0.145098, 0.231373, 0.592157],
[0.145098, 0.223529, 0.592157],
[0.145098, 0.219608, 0.588235],
[0.145098, 0.215686, 0.584314],
[0.145098, 0.207843, 0.584314],
[0.145098, 0.203922, 0.580392],
[0.141176, 0.2, 0.572549],
[0.137255, 0.2, 0.564706],
[0.133333, 0.196078, 0.556863],
[0.129412, 0.192157, 0.552941],
[0.12549, 0.188235, 0.545098],
[0.12549, 0.188235, 0.537255],
[0.121569, 0.184314, 0.529412],
[0.117647, 0.180392, 0.521569],
[0.113725, 0.180392, 0.513725],
[0.109804, 0.176471, 0.505882],
[0.105882, 0.172549, 0.498039],
[0.101961, 0.168627, 0.494118],
[0.0980392, 0.168627, 0.486275],
[0.0941176, 0.164706, 0.478431],
[0.0901961, 0.160784, 0.470588],
[0.0901961, 0.160784, 0.462745],
[0.0862745, 0.156863, 0.454902],
[0.0823529, 0.152941, 0.447059],
[0.0784314, 0.14902, 0.439216],
[0.0745098, 0.14902, 0.435294],
[0.0705882, 0.145098, 0.427451],
[0.0666667, 0.141176, 0.419608],
[0.0627451, 0.137255, 0.411765],
[0.0588235, 0.137255, 0.403922],
[0.054902, 0.133333, 0.396078],
[0.0509804, 0.129412, 0.388235],
[0.0509804, 0.129412, 0.380392],
[0.0470588, 0.12549, 0.376471],
[0.0431373, 0.121569, 0.368627],
[0.0392157, 0.117647, 0.360784],
[0.0352941, 0.117647, 0.352941],
[0.0313725, 0.113725, 0.345098]]

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
