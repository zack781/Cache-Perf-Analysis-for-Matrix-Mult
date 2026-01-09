from m5.objects import Cache
from m5.proxy import *
from m5.objects import RandomRP
from m5.objects import NMRURP
from m5.objects import TreePLRURP

class L1Cache(Cache):
    assoc = 2
    data_latency = 2
    tag_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20

    def __init__(self, options=None):
        super(L1Cache, self).__init__()
        pass

class L1ICache(L1Cache):
    size = '16kB'

    def __init__(self, options=None):
        super(L1ICache, self).__init__()
        if not options or not options.l1i_size or not options.policy:
            return
        self.size = options.l1i_size
        self.data_latency = int(options.latency)
        self.tag_latency = int(options.latency)
        self.response_latency = int(options.latency)
        self.assoc = int(options.assoc)
        print('setting policy', options.policy)
        if (options.policy == '0'):
            print('TreePLRURP')
            self.replacement_policy = TreePLRURP()
        elif (options.policy == '1'):
            print('NMRU')
            self.replacement_policy = NMRURP()
        elif (options.policy == '2'):
            print('Random')
            self.replacement_policy = RandomRP()

class L1DCache(L1Cache):
    size = '64kB'

    def __init__(self, options=None):
        super(L1DCache, self).__init__()
        if not options or not options.l1d_size or not options.policy:
            return
        self.size = options.l1d_size
        self.data_latency = int(options.latency)
        self.tag_latency = int(options.latency)
        self.response_latency = int(options.latency)
        self.assoc = int(options.assoc)
        print('setting policy', options.policy)
        if (options.policy == '0'):
            print('TreePLRURP')
            self.replacement_policy = TreePLRURP()
        elif (options.policy == '1'):
            print('NMRU')
            self.replacement_policy = NMRURP()
        elif (options.policy == '2'):
            print('Random')
            self.replacement_policy = RandomRP()

class L2Cache(Cache):
    size = '256kB'
    assoc = 16
    # hit_latency = 20
    data_latency = 20
    tag_latency = 20
    response_latency = 20
    mshrs = 20
    tgts_per_mshr = 12

    def __init__(self, options=None):
        super(L2Cache, self).__init__()
        if not options or not options.l2_size:
            return
        self.size = options.l2_size
