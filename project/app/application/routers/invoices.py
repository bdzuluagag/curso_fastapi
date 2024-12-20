
from fastapi import APIRouter
from domain.models import Invoice
from services.invoices_service import create_invoice_service

router = APIRouter(tags=['invoices'])


@router.post("/invoices")
async def create_invoice_endpoint(invoice: Invoice):
    return create_invoice_service(invoice)