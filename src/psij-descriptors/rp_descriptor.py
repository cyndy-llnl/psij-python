from distutils.version import StrictVersion

from psij._descriptor import _Descriptor


__PSI_J_EXECUTORS__ = [_Descriptor(name='rp', version=StrictVersion('0.0.1'),
                                   cls='psij.executors.rp.RPJobExecutor')]