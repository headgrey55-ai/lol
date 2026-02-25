## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import search_tool, FinancialDocumentTool

## Creating a task to analyze user's financial document query
analyze_financial_document = Task(
    description=(
        "Analyze the financial document related to the user's query: {query}\n"
        "Provide a comprehensive analysis that includes:\n"
        "1. Key financial metrics and ratios\n"
        "2. Financial health assessment\n"
        "3. Trends and patterns in the financial data\n"
        "4. Relevant market context\n"
        "Use the document content to support all claims and recommendations."
    ),
    
    expected_output=(
        "A detailed financial analysis including:\n"
        "- Summary of key findings\n"
        "- Financial metrics with sources\n"
        "- Risk factors identified\n"
        "- Opportunities based on the document\n"
        "- Actionable insights for the user"
    ),
    
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description=(
        "Based on the financial document analysis for: {query}\n"
        "Provide evidence-based investment recommendations:\n"
        "1. Analyze financial ratios and their investment implications\n"
        "2. Identify investment opportunities aligned with the financial data\n"
        "3. Consider sector trends and market conditions\n"
        "4. Assess suitability for different investor profiles\n"
        "All recommendations must be supported by financial analysis."
    ),
    
    expected_output=(
        "Investment analysis report with:\n"
        "- Data-driven investment recommendations\n"
        "- Analysis of 3-5 relevant investment options\n"
        "- Risk-return profiles\n"
        "- Alignment with financial document findings\n"
        "- Recommended portfolio allocation strategies"
    ),
    
    agent=investment_advisor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description=(
        "Conduct a thorough risk assessment based on the financial document: {query}\n"
        "Analyze:\n"
        "1. Market risks relevant to the financial data\n"
        "2. Operational risks indicated by financial metrics\n"
        "3. Industry-specific risks\n"
        "4. Regulatory and compliance risks\n"
        "Provide practical risk mitigation strategies."
    ),
    
    expected_output=(
        "Comprehensive risk assessment including:\n"
        "- Identified risk factors with severity ratings\n"
        "- Risk mitigation strategies\n"
        "- Stress test scenarios\n"
        "- Risk monitoring recommendations\n"
        "- Regulatory compliance considerations"
    ),
    
    agent=risk_assessor,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a document verification task
verification = Task(
    description=(
        "Verify that the uploaded document is a legitimate financial document: {query}\n"
        "Assess:\n"
        "1. Document authenticity and legitimacy\n"
        "2. Whether it contains financial information\n"
        "3. Document completeness and quality\n"
        "4. Compliance with financial reporting standards\n"
        "Provide a clear verification report."
    ),
    
    expected_output=(
        "Verification report including:\n"
        "- Document authenticity assessment\n"
        "- Financial data quality rating\n"
        "- Completeness assessment\n"
        "- Regulatory compliance status\n"
        "- Recommendation for further analysis"
    ),
    
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)
