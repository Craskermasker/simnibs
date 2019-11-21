''' Example of optimizaion maximizing intensity in the target

    Copyright (C) 2019 Guilherme B Saturnino
'''
import simnibs

opt = simnibs.opt_struct.TDCSoptimize()
opt.leadfield_hdf = 'leadfield/ernie_leadfield_EEG10-10_UI_Jurak_2007.hdf5'
opt.name = 'optimization/single_target'

opt.max_total_current = 2e-3
opt.max_individual_current = 1e-3
opt.max_active_electrodes = 8

target = opt.add_target()
target.positions = [-55.4, -20.7, 73.4]
# Set the intensity to a large value (e.g, 100)
target.intensity = 100

# Run optimization
simnibs.run_simnibs(opt)
