from setuptools import setup, find_packages


setup(
    name='essentia-bridges-api',
    version='0.0.1',
    author='Essentia.one developers',
    author_email='dev@essentia.one',
    url='https://github.com/essentiaone/essentia-bridges-api',
    description='Essentia bridges API wrapper written in Python',
    download_url='https://github.com/essentiaone/essentia-bridges-api/archive/master.zip',
    license='MIT',
    keywords='essentia bridges api',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.18.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ]
)
