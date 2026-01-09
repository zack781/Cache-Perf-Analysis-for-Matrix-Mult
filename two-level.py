import m5
from m5.objects import *
from caches import *
from optparse import OptionParser
from m5.params import *

parser = OptionParser()
parser.add_option('--l1i_size', help="L1 instruction cache size")
parser.add_option('--l1d_size', help="L1 data cache size")
parser.add_option('--l2_size', help="Unified L2 cache size")
parser.add_option('--policy', help="Choose replacement policy (0: lru, 1: nmru, 2: random)")
parser.add_option('--latency', help="Set latency for data, tag, and response")
parser.add_option('--assoc', help="Set associativity")

(options, args) = parser.parse_args()

system = System()

system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2.3GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# use timing mode for memory simulation

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('2GB')]

# system.cpu = X86TimingSimpleCPU()
system.cpu = X86O3CPU()

system.cpu.icache = L1ICache(options)
system.cpu.dcache = L1DCache(options)

system.l2bus = L2XBar()

system.l2cache = L2Cache(options)

system.cpu.icache_port = system.cpu.icache.cpu_side
system.cpu.dcache_port = system.cpu.dcache.cpu_side

system.cpu.icache.mem_side = system.l2bus.cpu_side_ports
system.cpu.dcache.mem_side = system.l2bus.cpu_side_ports

system.l2bus.mem_side_ports = system.l2cache.cpu_side

system.membus = SystemXBar()
system.l2cache.mem_side = system.membus.cpu_side_ports

system.cpu.createInterruptController()

# connect a special port in the system up to the membus for read/write memory (specific to ISA)

system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

# create a DDR3 memory controller and connect it to the membus

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

# executing in syscall simulation mode (SE mode), pointing the CPU at the compiled executable

process = Process()
# process.cmd = ['/home/zack/gem5/tests/test-progs/hello/bin/x86/linux/hello']

process.cmd = ['/home/zack/matrix-mult/blocked_mm', 128, 32]
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)

# gem5 requires an explicit SEWorkload object to manage the address space and entry point for the X86 binary

system.workload = SEWorkload.init_compatible(process.cmd[0])

m5.instantiate() # goes through all the SimObjects and creates the c++ equivalents

# begin simulation

print("Beginning simulations!")
exit_event = m5.simulate()

print("Exiting @ ticks %i because %s" % (m5.curTick(), exit_event.getCause()))
