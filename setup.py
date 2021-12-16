from setuptools import setup

setup(
    name = "basic_stats",
    version = "0.0.1",
    packages = ['mean','sd','norm','is_norm','is_skew', 'graph','stats'],
    install_requires = ['matplotlib.pyplot','numpy'],
)