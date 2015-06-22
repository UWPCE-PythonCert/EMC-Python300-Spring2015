"""Install the sample extension."""

from setuptools import setup, Extension

setup(
    name = "Whirlwind",
    ext_modules = [ 
        Extension("ext1", sources=["ext1.c"]), 
        Extension("ext2", sources=["ext2.c"]), 
        Extension("ext3", sources=["ext3.c"]), 
        Extension("ext4", sources=["ext4.c"]), 
    ],
)
