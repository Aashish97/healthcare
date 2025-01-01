from fastapi import FastAPI

from apps.organization.routers import router as organization_router
from apps.user.routers import router as user_router
from apps.report.routers import router as report_router


app = FastAPI()

# Include routers
app.include_router(organization_router, prefix="/organizations", tags=["organizations"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(report_router, prefix="/reports", tags=["reports"])
