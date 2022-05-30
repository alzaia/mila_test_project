from setuptools import setup, find_packages


setup(
    name='mila_test_project',
    version='0.0.1',
    packages=find_packages(include=['mila_test_project', 'mila_test_project.*']),
    python_requires='>=3.8',
    install_requires=[
        'flake8',
        'flake8-docstrings',
        'gitpython',
        'tqdm',
        'jupyter',
        'mlflow==1.15.0',
        'orion>=0.1.14',
        'pyyaml>=5.3',
        'pytest>=4.6',
        'protobuf==3.19.0',
        'pytest-cov',
        'sphinx',
        'sphinx-autoapi',
        'sphinx-rtd-theme',
        'sphinxcontrib-napoleon',
        'sphinxcontrib-katex',
        'recommonmark',
        'torch==1.9.0', 'pytorch_lightning==1.2.7'],
    entry_points={
        'console_scripts': [
            'main=mila_test_project.main:main'
        ],
    }
)
