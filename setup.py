from setuptools import setup, find_packages

setup(
    name='stringtr',
    version='0.1.0',
    author='Hasan Çağrı Güngör',
    author_email='iletisim@cagrigungor.com',
    packages=find_packages(),
    description='Türkçe karakter destekli string işleme kütüphanesi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/stringtr',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)