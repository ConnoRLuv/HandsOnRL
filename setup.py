import setuptools 

setuptools.setup(
    name='rlutils',
    version='1.0',
    description='utils for RL learning from Hands On Reinforcement Learning',
    author='ConnoRLuv',
    packages=setuptools.find_namespace_packages(exclude=["*.tests", "*.tests.*", "tests"]),
)