from setuptools import setup, find_packages


install_requires = ['simple-crypt']

setup(
    name='passworry',
    version='0.1',
    author='Somesh Chaturvedi',
    author_email='somesh.08.96@gmail.com',
    description='Password saving cli tool',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        passworry=PassWorry.main:main
    ''',
    license='MIT',
    keywords=['passwords'],
    zip_safe=False
)
