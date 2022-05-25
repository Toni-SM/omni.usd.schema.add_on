import os
import sys
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

# OV python (kit\python\include)
if sys.platform == 'win32':
    python_library_dir = os.path.join(os.path.dirname(sys.executable), "include")
elif sys.platform == 'linux':
    python_library_dir = os.path.join(os.path.dirname(sys.executable), "..", "include")

if not os.path.exists(python_library_dir):
    raise Exception("OV Python library directory not found: {}".format(python_library_dir))

ext_modules = [
    Extension("_rosBridgeSchema",
              [os.path.join("semu", "usd", "schemas", "RosBridgeSchema", "rosBridgeSchema.py")],
              library_dirs=[python_library_dir]),
    Extension("_rosControlBridgeSchema",
              [os.path.join("semu", "usd", "schemas", "RosControlBridgeSchema", "rosControlBridgeSchema.py")],
              library_dirs=[python_library_dir]),
]

setup(
    name = 'semu.usd.schemas',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
