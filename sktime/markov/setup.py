import os


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('markov', parent_package, top_path)

    config.add_extension('_markov_bindings',
                         sources=['_bindings/src/markov_module.cpp'],
                         include_dirs=['_bindings/include', os.path.join(top_path, 'sktime', 'src', 'include')],
                         language='c++',
                         )

    config.add_subpackage('msm')
    config.add_subpackage('hmm')

    return config
