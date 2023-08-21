import pandas as pd
from gooey import Gooey, GooeyParser
import datetime
import sys
from function import read_text_from_file,get_summary
from function_wordcloud import wordcloud_generator

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()  # Flush the stream after writing

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()  # Flush the stream after writing

    def __getattr__(self, attr):
        return getattr(self.stream, attr)  # Delegate other attributes to the underlying stream


sys.stdout = Unbuffered(sys.stdout)

@Gooey(advanced= True,
       program_name= "Summarization",
       program_description= "Settings",
       default_size=(600,800),
       navigation="TABBED",
       tabbed_groups= True,
       required_cols=1,
       optional_cols=1,
       description="Run summary",
       column_layout = True,
       header_bg_color = "#27bdea"
)
def parse_args():
    parser = GooeyParser()

    output_settings = parser.add_argument_group("Run Summary")
    output_settings.add_argument('output_file_dir', metavar= "Output Folder Location",
                                 help="Output File Folder Location" , widget="DirChooser")
    output_settings.add_argument('output_fname', metavar="Output Filename",
                                 help= "Enter Output File Name")
    pre_input_details_group = output_settings.add_argument_group("Main file location to summarize")
    pre_input_details_group.add_argument("analytics_raw_filename", metavar= "Main File Location",
                                 help="File to summarize" , widget="FileChooser", default = 'n/a')
    
    options_settings = parser.add_argument_group("Options")
    options_settings.add_argument("options_bool",
                                  metavar= "Select [Summarizer] for summarizing or [Word Cloud] for Frequent Words",
                                  choices = ['Summarizer','Word Cloud'],
                                  default = 'Summarizer')
    
    args_return = parser.parse_args()
    return args_return



if __name__ =='__main__':
    print("")
    print("----- Let's begin------")
    print("")
    print(sys.path)
    init = True
    args = parse_args()
    output_file_dir = args.output_file_dir
    output_file_name = args.output_fname
    output_file_name = output_file_dir + '\\' + output_file_name + '.docx'
    
    options_bool = args.options_bool
    input_file = args.analytics_raw_filename

    current_date = datetime.datetime.now()
    text_read = read_text_from_file(input_file)
    print(options_bool)
    if options_bool == 'Summarizer':
        get_summary(text_read,output_file_name)
    else:
        wordcloud_generator(text_read,output_file_name)

    
