from setuptools import setup, find_packages
import re
import os.path

versionString = '8.0.1'

if __name__ == '__main__':
    setup(name='lucem_illud',
        version = versionString,
        author="James Evans, Reid McIlroy-Young",
        author_email = "reidmcy@uchicago.edu",
        license = 'GPL',
        url="https://github.com/Computational-Content-Analysis-2018/lucem-illud",
        packages = find_packages(),
        install_requires = [
                'numpy',
                'requests',
                'pandas',
                'python-docx',
                'pillow',
                'pdfminer2',
                'GitPython',
                'wordcloud',
                'scipy',
                'seaborn',
                'scikit-learn==0.19.1',
                'nltk',
                'gensim==3.2.0',
                'matplotlib',
                'pyanno3',
                'beautifulsoup4',
                'graphviz',
                'boto3',
                'networkx==2.1',
                'pydub',
                'speechrecognition',
                'pysoundfile',
                'scikit-image==0.13.1',
                'Pillow==6.2.0',
        ],
        classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Sociology',
        'Topic :: Text Processing',
        ],
        entry_points={'console_scripts': [
                  'cta2018-setup-user = lucem_illud._backend:makeUser',
              ]},
    )
