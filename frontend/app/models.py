from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Complaint(db.Model):
    __tablename__ = "stg_complaints"

    # We currently don't have a primary key but SQLAlchemy requires one
    record_num = db.Column("record_num", db.VARCHAR, primary_key=True)
    record_type = db.Column("record_type", db.VARCHAR)
    record_type_mapped = db.Column("record_type_mapped", db.VARCHAR)
    record_type_desc = db.Column("record_type_desc", db.VARCHAR)
    description = db.Column("description", db.VARCHAR)
    open_date = db.Column("open_date", db.VARCHAR)
    last_insp_date = db.Column("last_insp_date", db.VARCHAR)
    last_insp_result = db.Column("last_insp_result", db.VARCHAR)
    status_current = db.Column("status_current", db.VARCHAR)
    original_address1 = db.Column("original_address1", db.VARCHAR)
    original_city = db.Column("original_city", db.VARCHAR)
    original_state = db.Column("original_state", db.VARCHAR)
    original_zip = db.Column("original_zip", db.VARCHAR)
    link = db.Column("link", db.VARCHAR)
    latitude = db.Column("latitude", db.VARCHAR)
    longitude = db.Column("longitude", db.VARCHAR)
    location1 = db.Column("location1", db.VARCHAR)


class RealPropertyAccount(db.Model):
    __tablename__ = "stg_real_property_account"

    # We currently don't have a primary key but SQLAlchemy requires one
    acct_nbr = db.Column("acct_nbr", db.VARCHAR, primary_key=True)
    major_minor = db.Column("major_minor", db.String)
    major = db.Column("major", db.VARCHAR)
    minor = db.Column("minor", db.VARCHAR)
    taxpayer_name = db.Column("taxpayer_name", db.VARCHAR)
    attn_line = db.Column("attn_line", db.VARCHAR)
    addr_line = db.Column("addr_line", db.VARCHAR)
    city_state = db.Column("city_state", db.VARCHAR)
    zip_code = db.Column("zip_code", db.VARCHAR)
    levy_code = db.Column("levy_code", db.VARCHAR)
    tax_stat = db.Column("tax_stat", db.VARCHAR)
    bill_yr = db.Column("bill_yr", db.VARCHAR)
    new_construction_flag = db.Column("new_construction_flag", db.VARCHAR)
    tax_val_reason = db.Column("tax_val_reason", db.VARCHAR)
    appr_land_val = db.Column("appr_land_val", db.VARCHAR)
    appr_imps_val = db.Column("appr_imps_val", db.VARCHAR)
    taxable_land_val = db.Column("taxable_land_val", db.VARCHAR)
    taxable_imps_val = db.Column("taxable_imps_val", db.VARCHAR)
    address_normalized = db.Column("address_normalized", db.VARCHAR)


class ApartmentComplex(db.Model):
    __tablename__ = "stg_apartment_complex"

    major_minor = db.Column("major_minor", db.String)
    major = db.Column("major", db.VARCHAR)
    minor = db.Column("minor", db.VARCHAR)
    complex_descr = db.Column("complex_descr", db.VARCHAR)
    nbr_bldgs = db.Column("nbr_bldgs", db.VARCHAR)
    nbr_stories = db.Column("nbr_stories", db.VARCHAR)
    nbr_units = db.Column("nbr_units", db.VARCHAR)
    avg_unit_size = db.Column("avg_unit_size", db.VARCHAR)
    project_location = db.Column("project_location", db.VARCHAR)
    project_appeal = db.Column("project_appeal", db.VARCHAR)
    pcnt_with_view = db.Column("pcnt_with_view", db.VARCHAR)
    constr_class = db.Column("constr_class", db.VARCHAR)
    bldg_quality = db.Column("bldg_quality", db.VARCHAR)
    condition = db.Column("condition", db.VARCHAR)
    yr_built = db.Column("yr_built", db.VARCHAR)
    eff_yr = db.Column("eff_yr", db.VARCHAR)
    pcnt_complete = db.Column("pcnt_complete", db.VARCHAR)
    elevators = db.Column("elevators", db.VARCHAR)
    secty_system = db.Column("secty_system", db.VARCHAR)
    fireplace = db.Column("fireplace", db.VARCHAR)
    laundry = db.Column("laundry", db.VARCHAR)
    # We currently don't have a primary key but SQLAlchemy requires one
    address = db.Column("address", db.VARCHAR, primary_key=True)
    address_normalized = db.Column("address_normalized", db.VARCHAR)

    @classmethod
    def for_major_minors(cls, major_minors: list[str]):
        return (
            cls.query.filter(cls.major_minor.in_(major_minors))
            .order_by(cls.major_minor)
            .all()
        )

    @classmethod
    def for_taxpayer_name(cls, taxpayer_name: str):
        accounts = RealPropertyAccount.query.filter_by(
            taxpayer_name=taxpayer_name
        ).all()
        major_minors = [account.major_minor for account in accounts]
        return cls.for_major_minors(major_minors)

    @classmethod
    def for_taxpayer_address(cls, taxpayer_address: str):
        accounts = RealPropertyAccount.query.filter_by(
            address_normalized=taxpayer_address
        ).all()
        major_minors = [account.major_minor for account in accounts]
        return cls.for_major_minors(major_minors)
