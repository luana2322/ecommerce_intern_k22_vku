from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.service import admin_role_service
from app.schema.adminrole_schema import  AdminRoleCreate, AdminRoleOut

router = APIRouter(prefix="/admin_roles", tags=["AdminRole"])

@router.post("/", response_model=AdminRoleOut)
def create_admin_role(admin_role: AdminRoleCreate, db: Session = Depends(get_db)):
    return admin_role_service.create_admin_role(db, admin_role)

@router.get("/", response_model=list[AdminRoleOut])
def list_admin_roles(db: Session = Depends(get_db)):
    return admin_role_service.get_all_admin_roles(db)

@router.get("/{admin_role_id}", response_model=AdminRoleOut)
def get_admin_role(admin_role_id: int, db: Session = Depends(get_db)):
    result = admin_role_service.get_admin_role_by_id(db, admin_role_id)
    if not result:
        raise HTTPException(status_code=404, detail="AdminRole not found")
    return result

@router.delete("/{admin_role_id}", response_model=AdminRoleOut)
def delete_admin_role(admin_role_id: int, db: Session = Depends(get_db)):
    result = admin_role_service.delete_admin_role(db, admin_role_id)
    if not result:
        raise HTTPException(status_code=404, detail="AdminRole not found")
    return result