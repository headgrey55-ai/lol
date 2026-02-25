## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.agents import Agent
from crewai.llm.llm import LLM
from tools import search_tool, FinancialDocumentTool

# Loading LLM - Fixed: Properly initialize the LLM
try:
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
except ImportError:
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)
    except ImportError:
        raise ValueError("Please install either 'openai' or 'google-generativeai'")

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide data-driven insights for {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a professional financial analyst with expertise in corporate finance, "
        "market analysis, and investment strategies. You provide sound financial advice "
        "based on careful analysis of financial statements and market data. "
        "You adhere to SEC regulations and financial best practices. "
        "Your recommendations are always backed by thorough research and legitimate analysis."
    ),
    tools=[FinancialDocumentTool.read_data_tool],  # Fixed: Changed 'tool' to 'tools'
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify that uploaded documents are legitimate financial documents and assess their validity",
    verbose=True,
    memory=True,
    backstory=(
        "You are a compliance officer with experience in financial document validation. "
        "You carefully review documents to ensure they are legitimate financial reports. "
        "You maintain high standards for accuracy and regulatory compliance. "
        "You provide clear feedback on document authenticity and financial relevance."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=True
)

# Creating an investment advisor agent
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide evidence-based investment recommendations based on financial analysis of {query}",
    verbose=True,
    backstory=(
        "You are a certified investment advisor with a track record of providing sound recommendations. "
        "You analyze financial data carefully and provide recommendations aligned with client goals. "
        "You understand risk management, portfolio diversification, and market fundamentals. "
        "You always disclose relevant risks and follow fiduciary principles."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)

# Creating a risk assessor agent
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Conduct thorough risk assessments based on financial documents for {query}",
    verbose=True,
    backstory=(
        "You are a risk management expert with deep knowledge of financial markets and risk models. "
        "You conduct comprehensive risk assessments using established financial frameworks. "
        "You understand market dynamics, regulatory requirements, and portfolio risk metrics. "
        "Your assessments are practical, evidence-based, and aligned with industry standards."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)
