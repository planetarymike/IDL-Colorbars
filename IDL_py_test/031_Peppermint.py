from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[0., 0., 0.313725],
[0., 0., 0.313725],
[0., 0., 0.627451],
[0., 0., 0.941176],
[0.313725, 0., 0.],
[0.313725, 0., 0.313725],
[0.313725, 0., 0.627451],
[0.313725, 0., 0.941176],
[0.627451, 0., 0.],
[0.627451, 0., 0.313725],
[0.627451, 0., 0.627451],
[0.627451, 0., 0.941176],
[0.941176, 0., 0.],
[0.941176, 0., 0.313725],
[0.941176, 0., 0.627451],
[0.941176, 0., 0.941176],
[0., 0.0627451, 0.],
[0., 0.0627451, 0.313725],
[0., 0.0627451, 0.627451],
[0., 0.0627451, 0.941176],
[0.313725, 0.0627451, 0.],
[0.313725, 0.0627451, 0.313725],
[0.313725, 0.0627451, 0.627451],
[0.313725, 0.0627451, 0.941176],
[0.627451, 0.0627451, 0.],
[0.627451, 0.0627451, 0.313725],
[0.627451, 0.0627451, 0.627451],
[0.627451, 0.0627451, 0.941176],
[0.941176, 0.0627451, 0.],
[0.941176, 0.0627451, 0.313725],
[0.941176, 0.0627451, 0.627451],
[0.941176, 0.0627451, 0.941176],
[0., 0.12549, 0.],
[0., 0.12549, 0.313725],
[0., 0.12549, 0.627451],
[0., 0.12549, 0.941176],
[0.313725, 0.12549, 0.],
[0.313725, 0.12549, 0.313725],
[0.313725, 0.12549, 0.627451],
[0.313725, 0.12549, 0.941176],
[0.627451, 0.12549, 0.],
[0.627451, 0.12549, 0.313725],
[0.627451, 0.12549, 0.627451],
[0.627451, 0.12549, 0.941176],
[0.941176, 0.12549, 0.],
[0.941176, 0.12549, 0.313725],
[0.941176, 0.12549, 0.627451],
[0.941176, 0.12549, 0.941176],
[0., 0.188235, 0.],
[0., 0.188235, 0.313725],
[0., 0.188235, 0.627451],
[0., 0.188235, 0.941176],
[0.313725, 0.188235, 0.],
[0.313725, 0.188235, 0.313725],
[0.313725, 0.188235, 0.627451],
[0.313725, 0.188235, 0.941176],
[0.627451, 0.188235, 0.],
[0.627451, 0.188235, 0.313725],
[0.627451, 0.188235, 0.627451],
[0.627451, 0.188235, 0.941176],
[0.941176, 0.188235, 0.],
[0.941176, 0.188235, 0.313725],
[0.941176, 0.188235, 0.627451],
[0.941176, 0.188235, 0.941176],
[0., 0.25098, 0.],
[0., 0.25098, 0.313725],
[0., 0.25098, 0.627451],
[0., 0.25098, 0.941176],
[0.313725, 0.25098, 0.],
[0.313725, 0.25098, 0.313725],
[0.313725, 0.25098, 0.627451],
[0.313725, 0.25098, 0.941176],
[0.627451, 0.25098, 0.],
[0.627451, 0.25098, 0.313725],
[0.627451, 0.25098, 0.627451],
[0.627451, 0.25098, 0.941176],
[0.941176, 0.25098, 0.],
[0.941176, 0.25098, 0.313725],
[0.941176, 0.25098, 0.627451],
[0.941176, 0.25098, 0.941176],
[0., 0.313725, 0.],
[0., 0.313725, 0.313725],
[0., 0.313725, 0.627451],
[0., 0.313725, 0.941176],
[0.313725, 0.313725, 0.],
[0.313725, 0.313725, 0.313725],
[0.313725, 0.313725, 0.627451],
[0.313725, 0.313725, 0.941176],
[0.627451, 0.313725, 0.],
[0.627451, 0.313725, 0.313725],
[0.627451, 0.313725, 0.627451],
[0.627451, 0.313725, 0.941176],
[0.941176, 0.313725, 0.],
[0.941176, 0.313725, 0.313725],
[0.941176, 0.313725, 0.627451],
[0.941176, 0.313725, 0.941176],
[0., 0.376471, 0.],
[0., 0.376471, 0.313725],
[0., 0.376471, 0.627451],
[0., 0.376471, 0.941176],
[0.313725, 0.376471, 0.],
[0.313725, 0.376471, 0.313725],
[0.313725, 0.376471, 0.627451],
[0.313725, 0.376471, 0.941176],
[0.627451, 0.376471, 0.],
[0.627451, 0.376471, 0.313725],
[0.627451, 0.376471, 0.627451],
[0.627451, 0.376471, 0.941176],
[0.941176, 0.376471, 0.],
[0.941176, 0.376471, 0.313725],
[0.941176, 0.376471, 0.627451],
[0.941176, 0.376471, 0.941176],
[0., 0.439216, 0.],
[0., 0.439216, 0.313725],
[0., 0.439216, 0.627451],
[0., 0.439216, 0.941176],
[0.313725, 0.439216, 0.],
[0.313725, 0.439216, 0.313725],
[0.313725, 0.439216, 0.627451],
[0.313725, 0.439216, 0.941176],
[0.627451, 0.439216, 0.],
[0.627451, 0.439216, 0.313725],
[0.627451, 0.439216, 0.627451],
[0.627451, 0.439216, 0.941176],
[0.941176, 0.439216, 0.],
[0.941176, 0.439216, 0.313725],
[0.941176, 0.439216, 0.627451],
[0.941176, 0.439216, 0.941176],
[0., 0.501961, 0.],
[0., 0.501961, 0.313725],
[0., 0.501961, 0.627451],
[0., 0.501961, 0.941176],
[0.313725, 0.501961, 0.],
[0.313725, 0.501961, 0.313725],
[0.313725, 0.501961, 0.627451],
[0.313725, 0.501961, 0.941176],
[0.627451, 0.501961, 0.],
[0.627451, 0.501961, 0.313725],
[0.627451, 0.501961, 0.627451],
[0.627451, 0.501961, 0.941176],
[0.941176, 0.501961, 0.],
[0.941176, 0.501961, 0.313725],
[0.941176, 0.501961, 0.627451],
[0.941176, 0.501961, 0.941176],
[0., 0.564706, 0.],
[0., 0.564706, 0.313725],
[0., 0.564706, 0.627451],
[0., 0.564706, 0.941176],
[0.313725, 0.564706, 0.],
[0.313725, 0.564706, 0.313725],
[0.313725, 0.564706, 0.627451],
[0.313725, 0.564706, 0.941176],
[0.627451, 0.564706, 0.],
[0.627451, 0.564706, 0.313725],
[0.627451, 0.564706, 0.627451],
[0.627451, 0.564706, 0.941176],
[0.941176, 0.564706, 0.],
[0.941176, 0.564706, 0.313725],
[0.941176, 0.564706, 0.627451],
[0.941176, 0.564706, 0.941176],
[0., 0.627451, 0.],
[0., 0.627451, 0.313725],
[0., 0.627451, 0.627451],
[0., 0.627451, 0.941176],
[0.313725, 0.627451, 0.],
[0.313725, 0.627451, 0.313725],
[0.313725, 0.627451, 0.627451],
[0.313725, 0.627451, 0.941176],
[0.627451, 0.627451, 0.],
[0.627451, 0.627451, 0.313725],
[0.627451, 0.627451, 0.627451],
[0.627451, 0.627451, 0.941176],
[0.941176, 0.627451, 0.],
[0.941176, 0.627451, 0.313725],
[0.941176, 0.627451, 0.627451],
[0.941176, 0.627451, 0.941176],
[0., 0.690196, 0.],
[0., 0.690196, 0.313725],
[0., 0.690196, 0.627451],
[0., 0.690196, 0.941176],
[0.313725, 0.690196, 0.],
[0.313725, 0.690196, 0.313725],
[0.313725, 0.690196, 0.627451],
[0.313725, 0.690196, 0.941176],
[0.627451, 0.690196, 0.],
[0.627451, 0.690196, 0.313725],
[0.627451, 0.690196, 0.627451],
[0.627451, 0.690196, 0.941176],
[0.941176, 0.690196, 0.],
[0.941176, 0.690196, 0.313725],
[0.941176, 0.690196, 0.627451],
[0.941176, 0.690196, 0.941176],
[0., 0.752941, 0.],
[0., 0.752941, 0.313725],
[0., 0.752941, 0.627451],
[0., 0.752941, 0.941176],
[0.313725, 0.752941, 0.],
[0.313725, 0.752941, 0.313725],
[0.317647, 0.756863, 0.627451],
[0.313725, 0.752941, 0.941176],
[0.627451, 0.752941, 0.],
[0.627451, 0.752941, 0.313725],
[0.627451, 0.752941, 0.627451],
[0.627451, 0.752941, 0.941176],
[0.941176, 0.752941, 0.],
[0.941176, 0.752941, 0.313725],
[0.941176, 0.752941, 0.627451],
[0.941176, 0.752941, 0.941176],
[0., 0.815686, 0.],
[0., 0.815686, 0.313725],
[0., 0.815686, 0.627451],
[0., 0.815686, 0.941176],
[0.313725, 0.815686, 0.],
[0.313725, 0.815686, 0.313725],
[0.313725, 0.815686, 0.627451],
[0.313725, 0.815686, 0.941176],
[0.627451, 0.815686, 0.],
[0.627451, 0.815686, 0.313725],
[0.627451, 0.815686, 0.627451],
[0.627451, 0.815686, 0.941176],
[0.941176, 0.815686, 0.],
[0.941176, 0.815686, 0.313725],
[0.941176, 0.815686, 0.627451],
[0.941176, 0.815686, 0.941176],
[0., 0.878431, 0.],
[0., 0.878431, 0.313725],
[0., 0.878431, 0.627451],
[0., 0.878431, 0.941176],
[0.313725, 0.878431, 0.],
[0.313725, 0.878431, 0.313725],
[0.313725, 0.878431, 0.627451],
[0.313725, 0.878431, 0.941176],
[0.627451, 0.878431, 0.],
[0.627451, 0.878431, 0.313725],
[0.627451, 0.878431, 0.627451],
[0.627451, 0.878431, 0.941176],
[0.941176, 0.878431, 0.],
[0.941176, 0.878431, 0.313725],
[0.941176, 0.878431, 0.627451],
[0.941176, 0.878431, 0.941176],
[0., 0.941176, 0.],
[0., 0.941176, 0.313725],
[0., 0.941176, 0.627451],
[0., 0.941176, 0.941176],
[0.313725, 0.941176, 0.],
[0.313725, 0.941176, 0.313725],
[0.313725, 0.941176, 0.627451],
[0.313725, 0.941176, 0.941176],
[0.627451, 0.941176, 0.],
[0.627451, 0.941176, 0.313725],
[0.627451, 0.941176, 0.627451],
[0.627451, 0.941176, 0.941176],
[0.941176, 0.941176, 0.],
[0.941176, 0.941176, 0.313725],
[0.941176, 0.941176, 0.627451],
[0.941176, 0.941176, 0.627451]]

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