from setuptools import setup

setup(name='rand_tensor',
      version='1.0.0',
      description='This code package generate random tensors with user-specified marginal means and covariances from one of two optional distributions. The first is the maximum-entropy-distribution with the specified marginal means and covariances. The second is the tensor-normal-distribution with the specified means and covariances.',
      license='General Public License',
      packages=['rand_tensor'],
      install_requires=[
                        'numpy',
                        'scipy',
                        'itertools',
                        ],
      zip_safe=False)
