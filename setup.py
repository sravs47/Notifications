import setuptools

setuptools.setup(
    name='Notifications',
    version='0.0',
    author='sravani',
    description='A small greeting card website',
    packages = setuptools.find_packages(),
    include_package_data=True,
    install_requires=['flask'],
)