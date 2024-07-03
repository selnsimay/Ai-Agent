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

    def hypothesize(self, agent, genes):
        return Task(
            description = f"your mission is to conduct biological analysis of the '{genes}' based on the information given to create a hypothesis of these genes' functions, significance, and context within your respective fields. Write a description for each gene and then in general how they may interact as a whole. Make sure to have a reliable biological mechanism of these genes.",
            agent = agent,
            expected_output = "a couple of paragraphs",
        )
    
    def info_dump(self, agent, genes):
        return Task(
            description = f"your mission is to gather all the biological, enrichment, context dependent information on the '{genes}' that can be found. Give the author, date, and other references for where the information is given. Even if there is no information on the gene, keep exploring and note the limited information.",
            agent = agent,
            expected_output = "500 words",
        )
    
    def compare_findings(self, agent, genes):
        return Task(
            description = f"your mission is to ocnduct a comparison analysis on each agent's conclusion of the genes. Give a report on how different and similar the findings are, make sure to include the specific agents and make lists of those that have the same repetitive information. Also note how the information is given, if it is in the same style, manner, etc. ",
            agent = agent,
            expected_output = "a couple of paragraphs",
        )