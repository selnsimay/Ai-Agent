from crewai import Task

class BiologicalAnalysisTask():
    def research(self, agent, genes):
        return Task(
            description = f"Research the '{genes}' and make a hypothesis based on biological evidence",
            agent = agent,
            expected_output = "1000 word count of biological information based on the genes",
        )

    def summary(self, agent, genes): 
        return Task(
            description = f"write a summary that explains the gene's relationship and function to each other based on the research '{genes}'",
            agent = agent,
            expected_output = "500 words",
        )

    def review_summary(self, agent, genes):
        return Task(
            description = f"review, edit, and fact-check the summary that explains the gene's relationship and function to each other based on the research '{genes}'. structure the summary in an efficient way. make sure there is enough context for biologists of all backgrounds. include author and date for the information gathered",
            agent = agent,
            expected_output = "300 words",
        )
    
    def interpreter_cell(self, agent, genes):
        return Task(
            description = f"your mission is to conduct biological analysis of the '{genes}' to get specific insights on their functions, enrichments, and any other biological data to help create an interepration of these genes within your respective fields. Write a paragraph length description for each gene and how they may interact as a whole. Give the author, date, and other references for where the information is given.",
            agent = agent,
            expected_output = "a couple of paragraphs",
        )
