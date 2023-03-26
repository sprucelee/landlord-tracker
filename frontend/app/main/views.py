from flask import flash, redirect, render_template, url_for

from . import main
from ..utils import normalize_address
from ..models import ApartmentComplex, Complaint, RealPropertyAccount
from .forms import AddressLookupForm


@main.get("/")
def index():
    form = AddressLookupForm()
    return render_template("index.html", form=form, report_url=url_for("main.report"))


@main.post("/report")
def report():
    form = AddressLookupForm()
    if form.validate_on_submit():
        # Look up address
        address = form.data["address"]
        apartment = ApartmentComplex.query.filter(
            ApartmentComplex.address.ilike(address)
        ).first()

        # Try to normalize address if not found at first
        if not apartment:
            address = normalize_address(address)
            apartment = ApartmentComplex.query.filter(
                ApartmentComplex.address.ilike(address)
            ).first()

        if not apartment:
            flash("address not found")
            return redirect(url_for("main.index"))

        accounts = RealPropertyAccount.query.filter_by(
            major=apartment.major, minor=apartment.minor
        ).all()

        # Find apartments associated with taxpayer name and address
        taxpayer_names = {account.taxpayer_name for account in accounts}
        taxpayer_addresses = {account.address_normalized for account in accounts}

        taxpayer_name_apts = {
            taxpayer_name: ApartmentComplex.for_taxpayer_name(taxpayer_name)
            for taxpayer_name in taxpayer_names
        }

        taxpayer_address_apts = {
            taxpayer_address: ApartmentComplex.for_taxpayer_address(taxpayer_address)
            for taxpayer_address in taxpayer_addresses
        }

        complaints = Complaint.query.filter_by(
            original_address1=apartment.address
        ).all()

        return render_template(
            "report.html",
            address=apartment.address_normalized,
            apartment=apartment,
            complaints=complaints,
            taxpayer_name_apts=taxpayer_name_apts,
            taxpayer_address_apts=taxpayer_address_apts,
        )

    return redirect(url_for("main.index"))
