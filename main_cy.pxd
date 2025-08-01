from calfews_src.model_cy cimport Model
from calfews_src.inputter_cy import Inputter

cdef class main_cy():
 
  cdef:
    public double progress
    public int running_sim, short_test, seed, total_sensitivity_factors
    public bint print_log, clean_output, save_full, parallel_mode
    public str scenario_name, model_mode, flow_input_type, flow_input_source, results_folder, output_list, runtime_file
    public dict objs
    public Model modelno, modelso, trinity, metropolitan

  cdef int initialize(self, str initial_condition) except -1

  #cdef void northern_initialization_routine(self, scenario, initial_condition)

  #cdef void southern_initialization_routine(self, scenario, initial_condition)

  cdef int run_sim(self, start_time) except -1

