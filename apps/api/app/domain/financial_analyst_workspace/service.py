from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.financial_analyst_workspace.models import AgenticFinancialAnalystWorkspaceSession, AgenticFinancialAnalystWorkspaceItem
from app.domain.financial_analyst_workspace.schemas import AgenticFinancialAnalystWorkspaceSessionCreate, AgenticFinancialAnalystWorkspaceItemCreate

class AgenticFinancialAnalystWorkspaceService:
    @staticmethod
    def create_session(db: Session, data: AgenticFinancialAnalystWorkspaceSessionCreate) -> AgenticFinancialAnalystWorkspaceSession:
        db_obj = AgenticFinancialAnalystWorkspaceSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticFinancialAnalystWorkspaceSession:
        return db.query(AgenticFinancialAnalystWorkspaceSession).filter(AgenticFinancialAnalystWorkspaceSession.id == session_id).first()
