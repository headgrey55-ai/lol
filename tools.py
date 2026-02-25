## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tool
from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool:
    @staticmethod  # Fixed: Added @staticmethod decorator
    def read_data_tool(path='data/sample.pdf'):
        """Tool to read data from a pdf file from a path

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file content
        """
        
        try:
            # Fixed: Use proper PDF loader from langchain
            loader = PDFPlumberLoader(file_path=path)
            docs = loader.load()
            
            full_report = ""
            for doc in docs:
                # Clean and format the financial document data
                content = doc.page_content
                
                # Remove extra whitespaces and format properly
                while "\n\n" in content:
                    content = content.replace("\n\n", "\n")
                    
                full_report += content + "\n"
                
            return full_report if full_report.strip() else "Error: PDF file is empty or could not be read"
        
        except FileNotFoundError:
            return f"Error: File not found at path {path}"
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod  # Fixed: Added @staticmethod decorator
    def analyze_investment_tool(financial_document_data):
        """Analyze investment opportunities from financial document data
        
        Args:
            financial_document_data (str): Financial document content
            
        Returns:
            dict: Analysis results with key metrics
        """
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
        
        # TODO: Implement comprehensive investment analysis logic
        # This should include:
        # - Financial ratio analysis
        # - Trend analysis
        # - Valuation metrics
        # - Investment recommendations
        
        return {
            "status": "Analysis in progress",
            "processed_length": len(processed_data),
            "message": "Investment analysis logic to be implemented"
        }

## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod  # Fixed: Added @staticmethod decorator
    def create_risk_assessment_tool(financial_document_data):
        """Create comprehensive risk assessment from financial data
        
        Args:
            financial_document_data (str): Financial document content
            
        Returns:
            dict: Risk assessment results
        """
        # TODO: Implement comprehensive risk assessment logic
        # This should include:
        # - Market risk analysis
        # - Credit risk assessment
        # - Operational risk evaluation
        # - Risk mitigation strategies
        
        return {
            "status": "Assessment in progress",
            "message": "Risk assessment logic to be implemented"
        }
