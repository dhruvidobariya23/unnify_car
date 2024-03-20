# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sequelizemeta(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'SequelizeMeta'


class AuthTokens(models.Model):
    id = models.UUIDField(primary_key=True)
    insurer_name = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=1800)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_tokens'


class Checkouts(models.Model):
    id = models.UUIDField(primary_key=True)
    quote = models.ForeignKey('FlowDetails', models.DO_NOTHING, blank=True, null=True)
    is_company = models.BooleanField()
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    gst_number = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.TextField()  # This field type is a guess.
    married = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField()
    pan_no = models.CharField(max_length=20)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    nominee_name = models.CharField(max_length=50)
    nominee_age = models.IntegerField()
    nominee_relationship = models.CharField(max_length=50)
    prev_od_policy_insurer = models.CharField(max_length=100, blank=True, null=True)
    prev_od_policy_number = models.CharField(max_length=20, blank=True, null=True)
    active_tp_policy_insurer = models.CharField(max_length=100, blank=True, null=True)
    active_tp_policy_number = models.CharField(max_length=20, blank=True, null=True)
    is_loan = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    prev_policy_insurer = models.CharField(max_length=100, blank=True, null=True)
    prev_policy_number = models.CharField(max_length=100, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    engine_no = models.CharField(max_length=50, blank=True, null=True)
    chassis_no = models.CharField(max_length=50, blank=True, null=True)
    financiar_name = models.CharField(max_length=200, blank=True, null=True)
    financiar_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkouts'


class Financier(models.Model):
    id = models.UUIDField(primary_key=True)
    financier_name = models.CharField(max_length=200)
    financier_code = models.CharField(max_length=20)
    financier_type = models.CharField(max_length=20)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financier'


class FlowDetails(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    policy_expired = models.BooleanField(blank=True, null=True)
    previous_year_claim = models.BooleanField(blank=True, null=True)
    make_name = models.CharField(max_length=200, blank=True, null=True)
    model_name = models.CharField(max_length=200, blank=True, null=True)
    variant_name = models.CharField(max_length=50, blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    rto_name = models.CharField(max_length=100, blank=True, null=True)
    flow_type = models.TextField()  # This field type is a guess.
    rc_no = models.CharField(max_length=20, blank=True, null=True)
    registration_year = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    quotedata = models.TextField(db_column='quoteData', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exp_ninety_days = models.BooleanField(blank=True, null=True)
    prevpoldeatils = models.TextField(db_column='prevPolDeatils', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    responsedata = models.TextField(db_column='responseData', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_updated = models.BooleanField(blank=True, null=True)
    vehicle_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_details'


class GetInTouches(models.Model):
    id = models.UUIDField(primary_key=True)
    contact = models.CharField(max_length=50)
    is_connected = models.BooleanField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'get_in_touches'


class GodigitVehicalMasters(models.Model):
    id = models.UUIDField(primary_key=True)
    vehicle_code = models.CharField(max_length=50)
    make_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    variant_name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=15)
    variant_id = models.UUIDField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    cubic_capacity = models.CharField(max_length=20, blank=True, null=True)
    vehicle_make_model = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'godigit_vehical_masters'


class InsuranceCompanies(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.TextField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insurance_companies'


class MainMaster(models.Model):
    id = models.UUIDField(primary_key=True)
    vehicle_code = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    cc = models.CharField(max_length=100)
    fule_type = models.CharField(max_length=100)
    seating_capacity = models.CharField(max_length=100)
    insurer_master = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    tata_variant_code = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_master'


class Makes(models.Model):
    id = models.UUIDField(primary_key=True)
    make_name = models.CharField(max_length=100)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'makes'


class Models(models.Model):
    id = models.UUIDField(primary_key=True)
    model_name = models.CharField(max_length=100)
    make = models.ForeignKey(Makes, models.DO_NOTHING, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'models'


class PincodeMasters(models.Model):
    id = models.UUIDField(primary_key=True)
    pincode = models.CharField(max_length=6)
    office_name = models.CharField(max_length=50, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pincode_masters'


class PreviousInsurerMasters(models.Model):
    id = models.UUIDField(primary_key=True)
    company_code = models.CharField(max_length=100)
    insurer_name = models.CharField(max_length=200)
    source = models.CharField(max_length=50)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    insurer_master = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'previous_insurer_masters'


class Proposals(models.Model):
    id = models.UUIDField(primary_key=True)
    quote = models.ForeignKey('Quotes', models.DO_NOTHING, blank=True, null=True)
    insurance_company = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50)
    proposal_responses = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proposals'


class QuoteResponseData(models.Model):
    id = models.UUIDField(primary_key=True)
    quoteid = models.ForeignKey(FlowDetails, models.DO_NOTHING, db_column='quoteId')  # Field name made lowercase.
    quoteresponseid = models.ForeignKey('QuoteResponses', models.DO_NOTHING, db_column='quoteResponseId')  # Field name made lowercase.
    response = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quote_response_data'


class QuoteResponses(models.Model):
    id = models.UUIDField(primary_key=True)
    insurer_name = models.CharField(max_length=100)
    quote_id = models.UUIDField(blank=True, null=True)
    quote_payload = models.TextField()  # This field type is a guess.
    quote_responses = models.TextField()  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    is_deleted = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_responses'


class Quotes(models.Model):
    id = models.UUIDField(primary_key=True)
    flow = models.ForeignKey(FlowDetails, models.DO_NOTHING, blank=True, null=True)
    policy_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    cover_idv = models.FloatField(blank=True, null=True)
    pa_cover = models.BooleanField(blank=True, null=True)
    engine_protection = models.BooleanField(blank=True, null=True)
    zero_dept = models.BooleanField(blank=True, null=True)
    invoice_cover = models.BooleanField(blank=True, null=True)
    rsa = models.BooleanField(blank=True, null=True)
    ncb_protecuion = models.BooleanField(blank=True, null=True)
    consumable = models.BooleanField(blank=True, null=True)
    key_lock_protection = models.BooleanField(blank=True, null=True)
    repair_of_glass = models.BooleanField(blank=True, null=True)
    driver_cover = models.BooleanField(blank=True, null=True)
    passanger_cover = models.FloatField(blank=True, null=True)
    accessories_non_electrical = models.FloatField(blank=True, null=True)
    accessories_electrical = models.FloatField(blank=True, null=True)
    previous_policy_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    expiry_prev_od = models.DateField(blank=True, null=True)
    expiry_active_tp = models.DateField(blank=True, null=True)
    exp_more_ninety = models.BooleanField(blank=True, null=True)
    clain_prev_policy = models.BooleanField(blank=True, null=True)
    ncb = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quotes'


class RtoMasters(models.Model):
    id = models.UUIDField(primary_key=True)
    rto_name = models.CharField(max_length=50)
    rto_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.
    insurer_master = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rto_masters'


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True)
    quoteid = models.ForeignKey(FlowDetails, models.DO_NOTHING, db_column='quoteId')  # Field name made lowercase.
    checkoutid = models.ForeignKey(Checkouts, models.DO_NOTHING, db_column='checkoutId')  # Field name made lowercase.
    payload = models.TextField()  # This field type is a guess.
    response = models.TextField()  # This field type is a guess.
    insurername = models.CharField(db_column='insurerName', max_length=255)  # Field name made lowercase.
    paymentdone = models.BooleanField(db_column='paymentDone')  # Field name made lowercase.
    kycdone = models.BooleanField(db_column='kycDone')  # Field name made lowercase.
    policypdfresponse = models.TextField(db_column='policyPdfResponse', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    kycresponse = models.TextField(db_column='kycResponse', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transactions'


class Variants(models.Model):
    id = models.UUIDField(primary_key=True)
    variant_name = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=10)
    model = models.ForeignKey(Models, models.DO_NOTHING, blank=True, null=True)
    vehicle_code = models.CharField(max_length=20)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variants'


class VehicalMasters(models.Model):
    id = models.UUIDField(primary_key=True)
    vehical_code = models.CharField(unique=True, max_length=20)
    vehical_make = models.CharField(max_length=100)
    vehical_model = models.CharField(max_length=100)
    vehical_variant = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=15)
    cubic_capacity = models.CharField(max_length=20, blank=True, null=True)
    sit_cap = models.CharField(max_length=20, blank=True, null=True)
    insurer_master = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehical_masters'


class ZoopMasters(models.Model):
    id = models.UUIDField(primary_key=True)
    car_no = models.CharField(max_length=15, blank=True, null=True)
    details = models.TextField(blank=True, null=True)  # This field type is a guess.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zoop_masters'
