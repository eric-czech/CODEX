from setuptools import setup
import os

if os.getenv('TF_GPU', 'false') == 'true':
    requires = ['tensorflow-gpu>=1.7.0']
else:
    requires = ['tensorflow>=1.7.0']

with open('requirements.txt', 'r') as fd:
    requires += [l.strip() for l in fd.readlines()]

if __name__ == '__main__':
    setup(
        name='codex',
        version='0.0.1',
        description="CODEX Data Processing Pipeline",
        author="Eric Czech",
        author_email="eric@hammerlab.org",
        url="",
        license="http://www.apache.org/licenses/LICENSE-2.0.html",
        classifiers=[
            'Environment :: Console',
            'Operating System :: OS Independent',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
        install_requires=requires,
        packages=['codex', 'codex.cli', 'codex.exec', 'codex.miq', 'codex.ops', 'codex.utils'],
        package_data={
            'codex': ['configs/*/examples/*/*', 'configs/*/schema/*']
        },
        include_package_data=True
    )
