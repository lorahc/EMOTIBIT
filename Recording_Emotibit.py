#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Path to save data
path='/Users/laura/Documents/EMOTIBIT/Emotibit_data-script'


# In[18]:


import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainflow.data_filter import DataFilter


def main():
    BoardShim.enable_dev_board_logger()

    params = BrainFlowInputParams()
    board_id = BoardIds.EMOTIBIT_BOARD.value

    presets = BoardShim.get_board_presets(board_id)
    print (presets)
    
    board = BoardShim(board_id, params)
    board.prepare_session()
    board.start_stream()
    time.sleep(60) # defining the 
    data_default = board.get_board_data(preset=BrainFlowPresets.DEFAULT_PRESET)
    data_aux = board.get_board_data(preset=BrainFlowPresets.AUXILIARY_PRESET)
    data_anc = board.get_board_data(preset=BrainFlowPresets.ANCILLARY_PRESET)
    board.stop_stream()
    board.release_session()
    DataFilter.write_file(data_default, f'{path}_default.csv', 'w') # acceloremeter, gyroscope, magnetometer
    DataFilter.write_file(data_aux, f'{path}_ppg.csv', 'w') #PPg data
    DataFilter.write_file(data_anc, f'{path}_eda.csv', 'w') # EDA and Temperature
#filename=f'{path}/{Name}/{Date}/S{usernumber}R{session_number}_raw.csv'

if __name__ == "__main__":
    main()

