from setuptools import setup


setup(
    name='fake_account',
    version='0.0.1',
    description='Package that generates fields for registration account',
    url='https://github.com/smnenko/fake_account',
    author='Stanislav Semenenko',
    author_email='stanichgame@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='account information registration creator',
    project_urls={
        'Source': 'https://github.com/smnenko/fake_account',
        'Issues': 'https://github.com/smnenko/fake_account/issues'
    },
    py_modules=['fake_account'],
    install_requires=['faker'],
    python_requires='>=3.8'
)
