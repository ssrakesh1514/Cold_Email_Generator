import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

load_dotenv()


class Chain:

    def __init__(self):

        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.3-70b-versatile"
        )

        # In-memory cache
        self.cache = {}

    def extract_jobs(self, cleaned_text):

        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}

            ### INSTRUCTION:
            The scraped text is from the careers page of a website.

            Your job is to extract the job postings and return them in JSON format containing the following keys:
            `role`, `experience`, `skills`, and `description`.

            Only return valid JSON.

            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm

        res = chain_extract.invoke(
            input={"page_data": cleaned_text}
        )

        try:
            json_parser = JsonOutputParser()
            parsed_res = json_parser.parse(res.content)

        except OutputParserException:
            raise OutputParserException(
                "Context too big. Unable to parse jobs."
            )

        return parsed_res if isinstance(parsed_res, list) else [parsed_res]

    def write_mail(self, job, links):

        cache_key = f"{str(job)}_{str(links)}"

        # Return cached email if available
        if cache_key in self.cache:
             print("Returning email from cache...")
             print("Cache Size:", len(self.cache))
             return self.cache[cache_key]
        print("Calling Groq API...")

        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:

            You are Rakesh, a Business Development Executive at Jarvis.

            Jarvis is an AI & Software Consulting company dedicated to helping
            organizations automate and optimize their business processes.

            Over the years, Jarvis has helped multiple enterprises improve:
            - Scalability
            - Process efficiency
            - Cost optimization
            - Business automation

            Your task is to write a professional cold email to the client
            regarding the job opportunity above.

            Explain how Jarvis can help fulfill the requirements.

            Also include the most relevant portfolio links from:
            {link_list}

            Keep the email concise, professional, and personalized.

            Do not provide any preamble.

            ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm

        res = chain_email.invoke(
            {
                "job_description": str(job),
                "link_list": links
            }
        )
        # Save response in cache
        self.cache[cache_key] = res.content
        print("Email saved to cache.")
        print("Cache Size:", len(self.cache))
        return res.content


if __name__ == "__main__":

    print("API Key Loaded:",
          os.getenv("GROQ_API_KEY") is not None)

    chain = Chain()

    print("Chain initialized successfully.")
