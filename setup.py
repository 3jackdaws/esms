from setuptools import setup

try:
    long_description = open("README.md").read()
except:
    long_description = ""

setup(
    name='esms',
    version='0.0.1',
    description='Send SMS via carrier specific email gateways',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/3jackdaws/esms',
    author='Ian Murphy',
    author_email='3jackdaws@gmail.com',
    license='MIT',
    packages=['esms'],
    python_requires='>=3.5',
    install_requires=[],
    test_suite='pytest',
    tests_require=['pytest', 'pytest-asyncio'],
)