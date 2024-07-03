import sys
from io import StringIO
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from agents import BiologicalAgents
from tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

# verbose_output = StringIO()
# sys.stdout = verbose_output

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'DLGAP5, DEPDC1, KIF20A, TROAP, KIF18B, KIF2C, RRM2, CDC25C, CCNB2, KIF14, CENPF, PRR11, UBE2C, PIMREG, PTTG1, NEK2, HMMR, PLK1, AURKA, MND1, LGALS4, DEFB1, OASL'

# Define your custom agents and tasks here
custom_agent_1 = agents.cellular_biologist()
custom_agent_2 = agents.computational_biologist()
custom_agent_3 = agents.cell_cyc()
custom_agent_4 = agents.drug_dev()
custom_agent_5 = agents.epigenetics_biologist()
custom_agent_6 = agents.genereg_expert()
custom_agent_7 = agents.molecular_biologist()
custom_agent_8 = agents.onco_res()
custom_agent_9 = agents.oncologist_physician()
custom_agent_10 = agents.systems_biologist()

# agents_dict = {
#     'custum_agent_1':agents.cellular_biologist(),
#     'custom_agent_2': agents.computational_biologist(),
#     'custom_agent_3': agents.cell_cyc(),
#     'custom_agent_4': agents.drug_dev(),
#     'custom_agent_5': agents.epigenetics_biologist(),
#     'custom_agent_6': agents.genereg_expert(),
#     'custom_agent_7': agents.molecular_biologist(),
#     'custom_agent_8': agents.onco_res(),
#     'custom_agent_9': agents.oncologist_physician(),
#     'custom_agent_10': agents.systems_biologist()
# }


# Custom tasks include agent name and variables as input
custom_task_1 = tasks.interpreter_cell(
    custom_agent_1, genes,
)
custom_task_2 = tasks.interpreter_cell(
    custom_agent_2, genes,
)
custom_task_3 = tasks.interpreter_cell(
    custom_agent_3, genes,
)
custom_task_4 = tasks.interpreter_cell(
    custom_agent_4, genes,
)
custom_task_5 = tasks.interpreter_cell(
    custom_agent_5, genes,
)
custom_task_6 = tasks.interpreter_cell(
    custom_agent_6, genes,
)
custom_task_7 = tasks.interpreter_cell(
    custom_agent_7, genes,
)
custom_task_8 = tasks.interpreter_cell(
    custom_agent_8, genes,
)
custom_task_9 = tasks.interpreter_cell(
    custom_agent_9, genes,
)
custom_task_10 = tasks.interpreter_cell(
    custom_agent_10, genes,
)



# Define your custom crew here
crew = Crew(
        agents=[custom_agent_1, custom_agent_2, custom_agent_3,custom_agent_3,custom_agent_5,custom_agent_6,custom_agent_7,custom_agent_8,custom_agent_9,custom_agent_10],
        tasks=[custom_task_1, custom_task_2,custom_task_3,custom_task_4,custom_task_5,custom_task_6, custom_task_7,custom_task_8,custom_task_9,custom_task_10],
        verbose=True,
        process = Process.sequential
)



result = crew.kickoff()
print(result)

# # automatically log
# sys.stdout = sys.__stdout__
# verbose_output.seek(0)
# verbose_output_content = verbose_output.read()
# print(verbose_output_content)
# with open('verbose.txt', 'a') as verbose_file:
#     verbose_file.write(verbose_output_content)