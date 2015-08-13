from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0., 0., 0.],
[0.00392157, 0., 0.],
[0.00784314, 0., 0.],
[0.0156863, 0., 0.],
[0.0196078, 0., 0.],
[0.027451, 0., 0.],
[0.0313725, 0., 0.],
[0.0392157, 0., 0.],
[0.0431373, 0., 0.],
[0.0509804, 0., 0.],
[0.054902, 0., 0.],
[0.0588235, 0., 0.],
[0.0666667, 0., 0.],
[0.0705882, 0., 0.],
[0.0784314, 0., 0.],
[0.0823529, 0., 0.],
[0.0901961, 0., 0.],
[0.0941176, 0., 0.],
[0.101961, 0., 0.],
[0.105882, 0., 0.],
[0.109804, 0., 0.],
[0.117647, 0., 0.],
[0.121569, 0., 0.],
[0.129412, 0., 0.],
[0.133333, 0., 0.],
[0.141176, 0., 0.],
[0.145098, 0., 0.],
[0.152941, 0., 0.],
[0.156863, 0., 0.],
[0.164706, 0., 0.],
[0.168627, 0., 0.],
[0.172549, 0., 0.],
[0.180392, 0., 0.],
[0.184314, 0., 0.],
[0.192157, 0., 0.],
[0.196078, 0., 0.],
[0.203922, 0., 0.],
[0.207843, 0., 0.],
[0.215686, 0., 0.],
[0.219608, 0., 0.],
[0.223529, 0., 0.],
[0.231373, 0., 0.],
[0.235294, 0., 0.],
[0.243137, 0., 0.],
[0.247059, 0., 0.],
[0.254902, 0., 0.],
[0.258824, 0., 0.],
[0.266667, 0., 0.],
[0.270588, 0., 0.],
[0.27451, 0., 0.],
[0.282353, 0., 0.],
[0.286275, 0., 0.],
[0.294118, 0., 0.],
[0.298039, 0., 0.],
[0.305882, 0., 0.],
[0.309804, 0., 0.],
[0.317647, 0., 0.],
[0.321569, 0., 0.],
[0.329412, 0., 0.],
[0.333333, 0., 0.],
[0.337255, 0., 0.],
[0.345098, 0., 0.],
[0.34902, 0., 0.],
[0.356863, 0., 0.],
[0.360784, 0., 0.],
[0.368627, 0., 0.],
[0.372549, 0., 0.],
[0.380392, 0., 0.],
[0.384314, 0., 0.],
[0.388235, 0., 0.],
[0.396078, 0., 0.],
[0.4, 0., 0.],
[0.407843, 0., 0.],
[0.411765, 0., 0.],
[0.419608, 0., 0.],
[0.423529, 0., 0.],
[0.431373, 0., 0.],
[0.435294, 0., 0.],
[0.443137, 0., 0.],
[0.447059, 0., 0.],
[0.45098, 0., 0.],
[0.458824, 0., 0.],
[0.462745, 0., 0.],
[0.470588, 0., 0.],
[0.47451, 0., 0.],
[0.482353, 0., 0.],
[0.486275, 0., 0.],
[0.494118, 0., 0.],
[0.498039, 0., 0.],
[0.501961, 0., 0.],
[0.509804, 0., 0.],
[0.513725, 0., 0.],
[0.521569, 0., 0.],
[0.52549, 0., 0.],
[0.533333, 0., 0.],
[0.537255, 0., 0.],
[0.545098, 0., 0.],
[0.54902, 0., 0.],
[0.552941, 0., 0.],
[0.560784, 0., 0.],
[0.564706, 0., 0.],
[0.572549, 0., 0.],
[0.576471, 0., 0.],
[0.584314, 0., 0.],
[0.588235, 0., 0.],
[0.596078, 0., 0.],
[0.6, 0., 0.],
[0.607843, 0., 0.],
[0.611765, 0., 0.],
[0.615686, 0., 0.],
[0.623529, 0., 0.],
[0.627451, 0., 0.],
[0.635294, 0., 0.],
[0.639216, 0., 0.],
[0.647059, 0., 0.],
[0.65098, 0., 0.],
[0.658824, 0., 0.],
[0.662745, 0., 0.],
[0.666667, 0., 0.],
[0.67451, 0., 0.],
[0.678431, 0., 0.],
[0.686275, 0.00392157, 0.],
[0.690196, 0.0117647, 0.],
[0.698039, 0.0196078, 0.],
[0.701961, 0.027451, 0.],
[0.709804, 0.0352941, 0.],
[0.713725, 0.0431373, 0.],
[0.721569, 0.0509804, 0.],
[0.72549, 0.0588235, 0.],
[0.729412, 0.0666667, 0.],
[0.737255, 0.0705882, 0.],
[0.741176, 0.0784314, 0.],
[0.74902, 0.0862745, 0.],
[0.752941, 0.0941176, 0.],
[0.760784, 0.101961, 0.],
[0.764706, 0.109804, 0.],
[0.772549, 0.117647, 0.],
[0.776471, 0.12549, 0.],
[0.780392, 0.133333, 0.],
[0.788235, 0.137255, 0.],
[0.792157, 0.145098, 0.],
[0.8, 0.152941, 0.],
[0.803922, 0.160784, 0.],
[0.811765, 0.168627, 0.],
[0.815686, 0.176471, 0.],
[0.823529, 0.184314, 0.],
[0.827451, 0.192157, 0.],
[0.831373, 0.2, 0.],
[0.839216, 0.203922, 0.],
[0.843137, 0.211765, 0.],
[0.85098, 0.219608, 0.],
[0.854902, 0.227451, 0.],
[0.862745, 0.235294, 0.],
[0.866667, 0.243137, 0.],
[0.87451, 0.25098, 0.],
[0.878431, 0.258824, 0.],
[0.886275, 0.266667, 0.],
[0.890196, 0.270588, 0.],
[0.894118, 0.278431, 0.],
[0.901961, 0.286275, 0.],
[0.905882, 0.294118, 0.],
[0.913725, 0.301961, 0.],
[0.917647, 0.309804, 0.],
[0.92549, 0.317647, 0.],
[0.929412, 0.32549, 0.],
[0.937255, 0.333333, 0.],
[0.941176, 0.337255, 0.],
[0.945098, 0.345098, 0.],
[0.952941, 0.352941, 0.],
[0.956863, 0.360784, 0.],
[0.964706, 0.368627, 0.],
[0.968627, 0.376471, 0.],
[0.976471, 0.384314, 0.],
[0.980392, 0.392157, 0.],
[0.988235, 0.4, 0.],
[0.992157, 0.403922, 0.],
[1., 0.411765, 0.],
[1., 0.419608, 0.],
[1., 0.427451, 0.],
[1., 0.435294, 0.],
[1., 0.443137, 0.],
[1., 0.45098, 0.],
[1., 0.458824, 0.],
[1., 0.466667, 0.],
[1., 0.470588, 0.],
[1., 0.478431, 0.],
[1., 0.486275, 0.],
[1., 0.494118, 0.],
[1., 0.501961, 0.],
[1., 0.509804, 0.],
[1., 0.517647, 0.],
[1., 0.52549, 0.0117647],
[1., 0.533333, 0.027451],
[1., 0.537255, 0.0431373],
[1., 0.545098, 0.0588235],
[1., 0.552941, 0.0745098],
[1., 0.560784, 0.0901961],
[1., 0.568627, 0.105882],
[1., 0.576471, 0.121569],
[1., 0.584314, 0.137255],
[1., 0.592157, 0.152941],
[1., 0.6, 0.168627],
[1., 0.603922, 0.184314],
[1., 0.611765, 0.2],
[1., 0.619608, 0.211765],
[1., 0.627451, 0.227451],
[1., 0.635294, 0.243137],
[1., 0.643137, 0.258824],
[1., 0.65098, 0.27451],
[1., 0.658824, 0.290196],
[1., 0.666667, 0.305882],
[1., 0.670588, 0.321569],
[1., 0.678431, 0.337255],
[1., 0.686275, 0.352941],
[1., 0.694118, 0.368627],
[1., 0.701961, 0.384314],
[1., 0.709804, 0.4],
[1., 0.717647, 0.411765],
[1., 0.72549, 0.427451],
[1., 0.733333, 0.443137],
[1., 0.737255, 0.458824],
[1., 0.745098, 0.47451],
[1., 0.752941, 0.490196],
[1., 0.760784, 0.505882],
[1., 0.768627, 0.521569],
[1., 0.776471, 0.537255],
[1., 0.784314, 0.552941],
[1., 0.792157, 0.568627],
[1., 0.8, 0.584314],
[1., 0.803922, 0.6],
[1., 0.811765, 0.611765],
[1., 0.819608, 0.627451],
[1., 0.827451, 0.643137],
[1., 0.835294, 0.658824],
[1., 0.843137, 0.67451],
[1., 0.85098, 0.690196],
[1., 0.858824, 0.705882],
[1., 0.866667, 0.721569],
[1., 0.870588, 0.737255],
[1., 0.878431, 0.752941],
[1., 0.886275, 0.768627],
[1., 0.894118, 0.784314],
[1., 0.901961, 0.8],
[1., 0.909804, 0.811765],
[1., 0.917647, 0.827451],
[1., 0.92549, 0.843137],
[1., 0.933333, 0.858824],
[1., 0.937255, 0.87451],
[1., 0.945098, 0.890196],
[1., 0.952941, 0.905882],
[1., 0.960784, 0.921569],
[1., 0.968627, 0.937255],
[1., 0.976471, 0.952941],
[1., 0.984314, 0.968627],
[1., 0.992157, 0.984314],
[1., 1., 1.]]

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