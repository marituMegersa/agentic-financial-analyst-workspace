from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.financial_analyst_workspace.schemas import AgenticFinancialAnalystWorkspaceSessionCreate, AgenticFinancialAnalystWorkspaceSessionResponse
from app.domain.financial_analyst_workspace.service import AgenticFinancialAnalystWorkspaceService

router = APIRouter(prefix="/api/v1/financial_analyst_workspace", tags=["Agentic Financial Analyst Workspace Domain"])

@router.post("/sessions", response_model=AgenticFinancialAnalystWorkspaceSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticFinancialAnalystWorkspaceSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Financial Analyst Workspace.
    """
    return AgenticFinancialAnalystWorkspaceService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticFinancialAnalystWorkspaceSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticFinancialAnalystWorkspaceService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
